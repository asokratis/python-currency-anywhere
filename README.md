# python_currency_fixer
Get your currency with this python script via [fixer](https://fixer.io)

## configurations
To update existing [currency_configurations](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py), run [update_currency_configurations](https://github.com/asokratis/python_currency_fixer/blob/master/update_currency_configurations.py) while providing your fixer API Key as parameter. You can update the maximum number of failed attempts on requesting currency data at [retry_configurations](https://github.com/asokratis/python_currency_fixer/blob/master/retry_configurations.py). 

## get_currency
<br>By default, displays exchange rate for all currencies with EUR as base currency for today's date. 

### Required Parameters
* **apiaccesskey**: Register for an API Key at [fixer](https://fixer.io)

### Optional Parameters
* **datelist**: Date list where each date is in YYYY-MM-DD format. Used for retrieving exchange rate within the time points specified in date list. 
* **currencynamelist**: Currency name list where each currency name represents a wildcard for matching any currencies from currency dictionary found within [configuration](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py)
* **basecurrency**: Currency base for calculating the exchange rate represented as currency code.

### Flag Parameters
* **debug**: Prints helpful information for debugging.
* **visual**: Makes output human readable instead of csv format.

### Examples

`python get_currency.py "<access-key-id>" --visual --datelist 2018-03-01 2017-03-01 --currencynamelist mex aus eur`
```
Currency Name                 Abbreviation      Date       Exchange Rate
================================================================================
Mexican Peso                  MXN         2018-03-01           23.129746
Australian Dollar             AUD         2018-03-01            1.580825
Euro                          EUR         2018-03-01                   1
Mexican Peso                  MXN         2017-03-01           20.916698
Australian Dollar             AUD         2017-03-01            1.376369
Euro                          EUR         2017-03-01                   1
```

`python get_currency.py "<access-key-id>" --visual --currencynamelist dollar India --basecurrency USD`
```
Currency Name                 Abbreviation      Date       Exchange Rate
================================================================================
United States Dollar          USD         2018-03-18                   1
Zimbabwean Dollar             ZWL         2018-03-18          322.355011
Namibian Dollar               NAD         2018-03-18           11.969039
Fijian Dollar                 FJD         2018-03-18             2.01504
Belize Dollar                 BZD         2018-03-18            1.997804
Canadian Dollar               CAD         2018-03-18            1.309204
Guyanaese Dollar              GYD         2018-03-18          205.270004
New Taiwan Dollar             TWD         2018-03-18           29.111038
Bermudan Dollar               BMD         2018-03-18                   1
Cayman Islands Dollar         KYD         2018-03-18            0.820383
Bahamian Dollar               BSD         2018-03-18                   1
Singapore Dollar              SGD         2018-03-18             1.31673
Jamaican Dollar               JMD         2018-03-18          126.860001
Trinidad and Tobago Dollar    TTD         2018-03-18            6.723104
Australian Dollar             AUD         2018-03-18            1.295404
Surinamese Dollar             SRD         2018-03-18            7.410371
Barbadian Dollar              BBD         2018-03-18                   2
New Zealand Dollar            NZD         2018-03-18            1.385204
Brunei Dollar                 BND         2018-03-18            1.316104
Liberian Dollar               LRD         2018-03-18          130.960007
East Caribbean Dollar         XCD         2018-03-18            2.703606
Indian Rupee                  INR         2018-03-18           64.980003
Hong Kong Dollar              HKD         2018-03-18            7.841804
Solomon Islands Dollar        SBD         2018-03-18            7.731504
```

### Versions
**Current Version:** 0.02
#### Version 0.01
* Initial Draft
#### Version 0.02
* Updated Configurations
