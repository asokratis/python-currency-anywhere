from urllib.request import urlopen
from urllib.error import URLError
from configurations import currency_configurations
from configurations import retry_configurations
import datetime
import argparse
import time
import simplejson as json
from functools import wraps
import decimal
import csv, sqlite3

# Trying out a Retry decorator in Python = https://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry

def validate(date_text):
    try:
        date_converted = datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return date_converted
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

@retry(URLError, tries=retry_configurations.config["tries"], delay=retry_configurations.config["delay"], backoff=retry_configurations.config["backoff"])
def get_currency(reference_date):
    currency_base=args.basecurrency
    country_map = currency_configurations.currencymap
    search=args.currencynamelist
    usersymbol=args.symbollist
    access_key=args.apiaccesskey
    symbols=""
    url=""
    query=""
    inputvalues  = [item.lower() for item in search]
    inputsymbols = [item.lower() for item in usersymbol]
    cur.execute("SELECT COUNT(*) FROM currency WHERE date = '%s'" % reference_date + ";")
    if (cur.fetchall()[0])[0] == 0:
        if args.legacy_user:
            url = "https://data.fixer.io/api/" + reference_date + "?access_key=" + access_key + "&base=" + currency_base
        else:
            url = "http://data.fixer.io/api/" + reference_date + "?access_key=" + access_key + "&base=EUR" 
        if args.debug:
            print("Debug: Calling API to cache data from " + url)
        html = urlopen(url)
        handler = html.read()
        result = json.loads(handler)
        if result["success"] == False:
            print("ERROR " + str(result['error']['code']))
            print(result['error']['info'])
        else:
            to_db = [(key,reference_date,value) for key,value in result['rates'].items()]
            cur.executemany("INSERT INTO currency (symbol, date, rate) VALUES (?, ?, ?);", to_db)
            con.commit() 
    for key, value in currency_configurations.currencymap.items():
        if any(inputvalue in value.lower() for inputvalue in inputvalues) and any(inputsymbol==key.lower() for inputsymbol in inputsymbols):
            symbols+=(key + ",")
    if len(symbols) == 0:
        print("No currency name found. Please try again and check currency configuration for the list of available currency names.")
    elif not (any(currency_base==key for key in currency_configurations.currencymap.keys())):
        print("Currency base was not found. Please try again and check currency configuration for the list of currency.")
    else:
        if args.legacy_user:
            query = "select symbol, rate from currency where date = '%s'" % reference_date + " and upper(symbol) IN (%s) " % ','.join("'" + symbol + "'" for symbol in symbols[:-1].split(","))
        else:
            query = "select symbol, rate from currency where date = '%s'" % reference_date + " and upper(symbol) IN (%s "  % ','.join("'" + symbol + "'" for symbol in symbols[:-1].split(",")) + ",'%s')" % currency_base
        if args.debug:
            print("Debug: Running query: " + query)
        cur.execute(query)
        finalresult = dict(cur.fetchall())
        outputlist=[]
        denominator = 1
        if not args.legacy_user:
            denominator=decimal.Decimal(finalresult[currency_base])
        for symbol,rate in sorted(finalresult.items()):
            if symbol in symbols:
                amount=args.amount.quantize(decimal.Decimal("0.01"),decimal.ROUND_HALF_UP)
                rate=(decimal.Decimal(rate)/denominator)
                reciprocal_rate=(decimal.Decimal(1)/rate)*amount
                rate=rate*amount
                rate=rate.quantize(decimal.Decimal("0.0000000000000001"),decimal.ROUND_HALF_UP)
                reciprocal_rate=reciprocal_rate.quantize(decimal.Decimal("0.0000000000000001"),decimal.ROUND_HALF_UP)
                output=""
                output += str(currency_configurations.currencymap[symbol]) + "," + str(symbol) + "," + str(reference_date) + "," + "{0:.2f}".format(amount) + "," +  "{0:.14f}".format(rate) + "," + "{0:.14f}".format(reciprocal_rate)
                outputlist.append(str(output))
        return outputlist

now=datetime.datetime.now()
currentdate=now.strftime("%Y-%m-%d")
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "apiaccesskey",
  type=str
)
CLI.add_argument(
  "--currencynamelist",
  nargs="*",
  type=str,
  default=list(currency_configurations.currencymap.values())
)
CLI.add_argument(
  "--symbollist",
  nargs="*",
  type=str,
  default=list(currency_configurations.currencymap.keys())
)
CLI.add_argument(
  "--datelist",
  nargs="*",
  type=str,
  default=[currentdate]
)
CLI.add_argument(
  "--amount",
  type=decimal.Decimal,
  default=decimal.Decimal(1.00)
)
CLI.add_argument(
  "--basecurrency",
  type=str,
  default="EUR"
)
CLI.add_argument(
  "--daysinterval",
  type=int,
  default=0
)
CLI.add_argument(
   "--debug",
   action='store_true'
)
CLI.add_argument(
   "--visual",
   action='store_true'
)
CLI.add_argument(
   "--legacy_user",
   action='store_true'
)
CLI.add_argument(
   "--no_header",
   action='store_true'
)
CLI.add_argument(
   "--sort_by_symbol",
   action='store_true'
)
CLI.add_argument(
   "--output_fluctuation",
   action='store_true'
)
args = CLI.parse_args()
header=""
header1=""
header2=""
decimal.getcontext().prec = 50
if args.visual:
    header1= "Currency Name".ljust(40," ") + "Symbol".ljust(12," ") + "Date".rjust(10," ") + "Amount".rjust(12," ") + "Rate".rjust(32," ") + "Reciprocal Rate".rjust(32," ")
    header2= "=" * 140
    if args.output_fluctuation:
        header1+= "Perc. Diff.".rjust(16," ") + "Difference".rjust(32," ")
        header2+= "=" * 48
    header=header1+"\n"+header2
else:
    header="currency_name,symbol,date,amount,rate,reciprocal_rate"
    if args.output_fluctuation:
        header+=",perc_diff,difference"
rendereddatelist=[]
if args.daysinterval != 0 and len(args.datelist) != 1:
    print("Parameter --daysinterval cannot be used when parameter --datelist has more than one date.\nWhen parameter --daysinterval is in use, place only one date in parameter --datelist.")
else:
    if args.daysinterval != 0 and len(args.datelist) == 1:
        if args.daysinterval > 0:
            startdate=validate(args.datelist[0])
            enddate=validate(args.datelist[0]) + datetime.timedelta(days=args.daysinterval)
        elif args.daysinterval < 0:
            enddate=validate(args.datelist[0])
            startdate=validate(args.datelist[0]) + datetime.timedelta(days=args.daysinterval)
        rendereddatelist = [str((startdate + datetime.timedelta(days=x)).date()) for x in range((enddate-startdate).days + 1)]
    else:
        rendereddatelist = sorted(args.datelist)
    resultlist=[]
    fullresultlist=[]
    sqlite_file='data/currency_'
    if args.legacy_user:
        sqlite_file += args.basecurrency.lower() + '.sqlite'
    else:
        sqlite_file += "eur.sqlite" 
    con = sqlite3.connect(sqlite_file)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS currency (symbol, date, rate);")
    con.commit()
    for i in rendereddatelist:
        date_converted = validate(i)
        maximum = datetime.date.today()
        minimum = datetime.date(1999, 1, 1)
        if not (minimum <= date_converted.date() <= maximum):
            print("Date " + i + " is out of bounds. Date range must be between " + minimum.strftime("%Y-%m-%d") + " and " + maximum.strftime("%Y-%m-%d") + ".")
        elif not (args.amount >= 0.01 and args.amount <= 1000000):
            print("Amount " + str(args.amount) + " is out of bounds. Amount range must be between 0.01 and 1000000.00")
        else:
            resultlist.append(get_currency(i))
    if not args.no_header:
        print(header)
    for datelist in resultlist:
        for symbollist in datelist:
            fullresultlist.append(symbollist.split(","))
    if args.sort_by_symbol or args.output_fluctuation:
        fullresultlist = sorted(fullresultlist, key=lambda row:(row[1],row[2]), reverse=False)
    lastrate=decimal.Decimal(0)
    lastcurrencysymbol=""
    for columnlist in fullresultlist:
        fluctuationoutput=""
        if args.output_fluctuation:
            if lastcurrencysymbol == str(columnlist[1]) and lastrate != 0:
                perc_diff = (((decimal.Decimal(columnlist[4]) - lastrate) / lastrate)*100)
                difference = (decimal.Decimal(columnlist[4]) - lastrate)
            else:
                perc_diff  = decimal.Decimal(0.0)
                difference = decimal.Decimal(0.0)
                lastcurrencysymbol=str(columnlist[1])
            lastrate=decimal.Decimal(columnlist[4])
            difference=difference.quantize(decimal.Decimal("0.0000000000000001"),decimal.ROUND_HALF_UP)
            perc_diff=perc_diff.quantize(decimal.Decimal("0.0001"),decimal.ROUND_HALF_UP)
            if args.visual:
                fluctuationoutput="{0:.4f}".format(decimal.Decimal(perc_diff)).rjust(16," ")+"{0:.14f}".format(decimal.Decimal(difference)).rjust(32," ")
            else:
                fluctuationoutput=","+"{0:.4f}".format(decimal.Decimal(perc_diff))+","+"{0:.14f}".format(decimal.Decimal(difference))
        if args.visual:
            print(columnlist[0].ljust(40," ") + columnlist[1].ljust(12," ") + columnlist[2].ljust(10," ") + "{0:.2f}".format(decimal.Decimal(columnlist[3])).rjust(12," ") + "{0:.14f}".format(decimal.Decimal(columnlist[4])).rjust(32," ") +  "{0:.14f}".format(decimal.Decimal(columnlist[5])).rjust(32," ") + fluctuationoutput)
        else:
            print(columnlist[0]+","+columnlist[1]+","+columnlist[2]+","+columnlist[3]+","+columnlist[4]+","+columnlist[5]+fluctuationoutput)
    con.close()