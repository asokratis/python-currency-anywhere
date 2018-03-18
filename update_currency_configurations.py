import argparse
from urllib2 import urlopen
import simplejson as json

CLI=argparse.ArgumentParser()
CLI.add_argument(
  "apiaccesskey",
  type=str
)
args = CLI.parse_args()
url = "https://data.fixer.io/api/symbols?access_key=" + args.apiaccesskey
html = urlopen(url)
handler = html.read()
result = json.loads(handler)
if result["success"] == False:
    print "ERROR " + str(result['error']['code'])
    print  result['error']['info']
else:
    file = open('currency_configurations.py','w')
    file.write("# -*- coding: utf-8 -*-\n")
    file.write("currencymap = {\n")
    is_first = True
    for symbol,name in result['symbols'].iteritems():
        if is_first:
	    file.write(" \"" + symbol.encode('utf-8') + "\": \"" + name.encode('utf-8') + "\"\n")
	    is_first = False
	else:
            file.write(",\"" + symbol.encode('utf-8') + "\": \"" + name.encode('utf-8') + "\"\n")
    file.write("}\n")
    print("Updated currency_configurations")
