from urllib2 import urlopen
from urllib2 import URLError
import xe_configurations
import datetime
import argparse
import time
import simplejson as json
from functools import wraps

# Trying out a Retry decorator in Python = https://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck, e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print msg
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

@retry(URLError, tries=xe_configurations.config["tries"], delay=xe_configurations.config["delay"], backoff=xe_configurations.config["backoff"])
def get_currency(reference_date):
    currency_base=args.basecurrency
    country_map = xe_configurations.currencymap
    search=args.currencynamelist
    access_key=args.apiaccesskey
    symbols=""
    inputvalues = [item.lower() for item in search]
    for key, value in xe_configurations.currencymap.iteritems():
        if any(inputvalue in value.lower() for inputvalue in inputvalues):
            symbols+=(key + ",")
    if len(symbols) == 0:
        print "No currency name found. Please try again and check configuration for the list of available currency names."
    elif not (any(currency_base==key for key in xe_configurations.currencymap.keys())):
        print "Currency base was not found. Please try again and check configuration for the list of currency."
    else:
        url = "http://data.fixer.io/api/" + reference_date + "?access_key=" + access_key + "&base=" + currency_base + "&date=" + reference_date + "&symbols=" + symbols[:-1]
        if args.debug:
            print "Debug: Running url..."
            print "Debug: " + url
        html = urlopen(url)
        handler = html.read()
        result = json.loads(handler)
        if result["success"] == False:
            print "ERROR " + str(result['error']['code'])
            print  result['error']['info']
        else:
            for symbol,rate in result['rates'].iteritems():
                if args.visual:
                    print str(xe_configurations.currencymap[symbol]).ljust(30," ") + str(symbol).ljust(12," ") + str(reference_date).ljust(10," ") + str(rate).rjust(20," ")
                else:
                    print str(xe_configurations.currencymap[symbol]) + "," + str(symbol) + "," + str(reference_date) + "," + str(rate)

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
  default=list(xe_configurations.currencymap.values())
)
CLI.add_argument(
  "--datelist",
  nargs="*",
  type=str,
  default=[currentdate]
)
CLI.add_argument(
  "--basecurrency",
  type=str,
  default="USD"
)
CLI.add_argument(
   "--debug",
   action='store_true'
)
CLI.add_argument(
   "--visual",
   action='store_true'
)
args = CLI.parse_args()
if args.visual:
    print "Currency Name".ljust(30," ") + "Abbreviation".rjust(12," ") + "Date".rjust(10," ") + "Exchange Rate".rjust(20," ")
    print "=" * 80
else:
    print "currency_name,abbreviation,date,exchange_rate"
for i in args.datelist:
    date_converted = validate(i)
    maximum = datetime.date.today()
    minimum = datetime.date(1999, 1, 1)
    if (minimum <= date_converted.date() <= maximum):
        get_currency(i)
    else:
        print("Date " + i + " is out of bounds. Date range must be between " + minimum.strftime("%Y-%m-%d") + " and " + maximum.strftime("%Y-%m-%d") + ".")
