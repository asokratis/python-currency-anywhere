# python_currency_fixer
Get your currency with this python script via [fixer](https://fixer.io)
<br>By default, displays exchange rate for all currencies with USD as base currency for today's date. 

### Required Parameters
* **apiaccesskey**: Register for an API Key at [fixer](https://fixer.io)

### Optional Parameters
* **datelist**: Date list where each date is in YYYY-MM-DD format. Used for retrieving exchange rate within the time points specified in date list. 
* **currencynamelist**: Currency name list where each currency name represents a wildcard for matching any currencies from currency dictionary found within [configuration](https://github.com/asokratis/python_currency_fixer/blob/master/xe_configurations.py)
* **basecurrency**: Currency base for calculating the exchange rate represented as currency code.

### Flag Parameters
* **debug**: Prints helpful information for debugging.
* **visual**: Makes output human readable instead of csv format.

### Examples

`python get_currency.py "<access-key-id>" --visual --datelist 2018-03-01 2017-03-01 --currencynamelist mex aus eur`
```
Currency Name                 Abbreviation      Date       Exchange Rate
================================================================================
Mexican Peso                  MXN         2018-03-01           18.843794
Australian Dollar             AUD         2018-03-01            1.287897
Euro                          EUR         2018-03-01              0.8147
Mexican Peso                  MXN         2017-03-01           19.845798
Australian Dollar             AUD         2017-03-01            1.305901
Euro                          EUR         2017-03-01            0.948802
```

`python get_currency.py "<access-key-id>" --visual --currencynamelist dollar India --basecurrency EUR`
```
Currency Name                 Abbreviation      Date       Exchange Rate
================================================================================
United States Dollar          USD         2018-03-17            1.229951
Zimbabwean Dollar             ZWL         2018-03-17          396.480999
Namibian Dollar               NAD         2018-03-17           14.710683
Fijian Dollar                 FJD         2018-03-17            2.478402
Belize Dollar                 BZD         2018-03-17            2.457202
Canadian Dollar               CAD         2018-03-17            1.610257
Guyanaese Dollar              GYD         2018-03-17           252.47213
New Taiwan Dollar             TWD         2018-03-17           35.805162
Bermudan Dollar               BMD         2018-03-17            1.229951
Cayman Islands Dollar         KYD         2018-03-17            1.009031
Bahamian Dollar               BSD         2018-03-17            1.229951
Singapore Dollar              SGD         2018-03-17            1.619514
Jamaican Dollar               JMD         2018-03-17          156.277623
Trinidad and Tobago Dollar    TTD         2018-03-17            8.269091
Australian Dollar             AUD         2018-03-17            1.593284
Surinamese Dollar             SRD         2018-03-17            9.114396
Barbadian Dollar              BBD         2018-03-17            2.459903
New Zealand Dollar            NZD         2018-03-17            1.703734
Brunei Dollar                 BND         2018-03-17            1.618744
Liberian Dollar               LRD         2018-03-17          161.074445
East Caribbean Dollar         XCD         2018-03-17            3.325304
Indian Rupee                  INR         2018-03-17           79.922246
Hong Kong Dollar              HKD         2018-03-17            9.645038
Solomon Islands Dollar        SBD         2018-03-17            9.509374
```

### Versions
**Current Version:** 0.01
#### Version 0.01
* Initial Draft
