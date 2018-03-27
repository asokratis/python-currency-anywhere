
from urllib.request import urlopen
from urllib.error import URLError
import currency_configurations
import retry_configurations
import datetime
import argparse
import time
import simplejson as json
from functools import wraps
import decimal

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
    inputvalues  = [item.lower() for item in search]
    inputsymbols = [item.lower() for item in usersymbol]
    for key, value in currency_configurations.currencymap.items():
        if any(inputvalue in value.lower() for inputvalue in inputvalues) and any(inputsymbol==key.lower() for inputsymbol in inputsymbols):
            symbols+=(key + ",")
    if len(symbols) == 0:
        print("No currency name found. Please try again and check currency configuration for the list of available currency names.")
    elif not (any(currency_base==key for key in currency_configurations.currencymap.keys())):
        print("Currency base was not found. Please try again and check currency configuration for the list of currency.")
    else:
        if args.legacy_user:
            url = "https://data.fixer.io/api/" + reference_date + "?access_key=" + access_key + "&base=" + currency_base + "&date=" + reference_date + "&symbols=" + symbols[:-1]
        else:
            url = "http://data.fixer.io/api/" + reference_date + "?access_key=" + access_key + "&base=EUR" + "&date=" + reference_date + "&symbols=" + symbols[:-1] + "," + currency_base
        if args.debug:
            print("Debug: Running url...")
            print("Debug: " + url)
        html = urlopen(url)
        handler = html.read()
        result = json.loads(handler)
        if result["success"] == False:
            print("ERROR " + str(result['error']['code']))
            print(result['error']['info'])
        else:
            denominator = 1
            if not args.legacy_user:
                denominator=decimal.Decimal(result['rates'][currency_base])
            for symbol,rate in sorted(result['rates'].items()):
                if symbol in symbols:
                    amount=args.amount.quantize(decimal.Decimal("0.01"),decimal.ROUND_HALF_UP)
                    rate=(decimal.Decimal(rate)/denominator)*amount
                    reciprocal_rate=(decimal.Decimal(1)/rate)
                    rate=rate.quantize(decimal.Decimal("0.0000000000000001"),decimal.ROUND_HALF_UP)
                    reciprocal_rate=reciprocal_rate.quantize(decimal.Decimal("0.0000000000000001"),decimal.ROUND_HALF_UP)
                    output = ""
                    if args.visual:
                        output += str(currency_configurations.currencymap[symbol]).ljust(40," ") + str(symbol).ljust(12," ") + str(reference_date).ljust(10," ") + "{0:.2f}".format(amount).rjust(12," ") + "{0:.14f}".format(rate).rjust(32," ") +  "{0:.14f}".format(reciprocal_rate).rjust(32," ")
                    else:
                        output += str(currency_configurations.currencymap[symbol]) + "," + str(symbol) + "," + str(reference_date) + "," + "{0:.2f}".format(amount) + "," +  "{0:.14f}".format(rate) + "," + "{0:.14f}".format(reciprocal_rate)
                    print(str(output))

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
args = CLI.parse_args()
header=""
decimal.getcontext().prec = 50
if args.visual:
    header=  "Currency Name".ljust(40," ") + "Symbol".ljust(12," ") + "Date".rjust(10," ") + "Amount".rjust(12," ") + "Rate".rjust(32," ") + "Reciprocal Rate".rjust(32," ") + "\n"
    header+= "=" * 140
else:
    header="currency_name,symbol,date,amount,rate,reciprocal_rate"
if not args.no_header:
    print(header)
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
    for i in rendereddatelist:
        date_converted = validate(i)
        maximum = datetime.date.today()
        minimum = datetime.date(1999, 1, 1)
        if not (minimum <= date_converted.date() <= maximum):
            print("Date " + i + " is out of bounds. Date range must be between " + minimum.strftime("%Y-%m-%d") + " and " + maximum.strftime("%Y-%m-%d") + ".")
        elif not (args.amount >= 0.01 and args.amount <= 1000000):
            print("Amount " + str(args.amount) + " is out of bounds. Amount range must be between 0.01 and 1000000.00")
        else:
            get_currency(i)
