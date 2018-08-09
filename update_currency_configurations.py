import argparse
from urllib.request import urlopen
import simplejson as json
import configparser

config = configparser.RawConfigParser()
config.read('settings.ini')

CLI=argparse.ArgumentParser()
CLI.add_argument(
  "serviceprovider",
  type=str
)
args = CLI.parse_args()

exchange_tree=config.get(args.serviceprovider,'exchange_tree')
variable_apikey=config.get(args.serviceprovider,'variable_apikey')
domain_name=config.get(args.serviceprovider,'domain_name')
value_apikey=config.get(args.serviceprovider,'value_apikey')
error_type=config.get(args.serviceprovider,'error_type')
get_currencylist=config.get(args.serviceprovider,'get_currencylist')
exchange_tree=config.get(args.serviceprovider,'exchange_tree')

url = domain_name + get_currencylist + "?" + variable_apikey + "=" + value_apikey
html = urlopen(url)
handler = html.read()
result = json.loads(handler)
if (error_type == "1" and not result["success"] == True) or (error_type == "2" and 'error' in result):
    if error_type == "1":
        print("ERROR " + str(result['error']['code']))
        print(result['error']['info'])
    elif error_type == "2":
        print("ERROR"  + str(result['status']))
        print(str(result['description']))
else:
    file = open('configurations/currency_configurations.py',mode='w',encoding='utf-8')
    file.write("# -*- coding: utf-8 -*-\n")
    file.write("currencymap = {\n")
    is_first = True
    if exchange_tree == "":
        dictresult = result
    else:
        dictresult = result[exchange_tree]
    for key,value in sorted(dictresult.items()):
        if is_first:
            file.write(" \"" + str(key) + "\": \"" + str(value) + "\"\n")
            is_first = False
        else:
            file.write(",\"" + str(key) + "\": \"" + str(value) + "\"\n")
    file.write("}\n")
    print("Updated currency_configurations")