# python_currency_fixer
Get your currency with this python script via [fixer](https://fixer.io)

## configurations
To update existing [currency_configurations](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py), run [update_currency_configurations](https://github.com/asokratis/python_currency_fixer/blob/master/update_currency_configurations.py) while providing your fixer API Key as parameter. You can update the maximum number of failed attempts on requesting currency data at [retry_configurations](https://github.com/asokratis/python_currency_fixer/blob/master/retry_configurations.py). 

## get_currency
By default, displays exchange rate for all currencies with EUR as base currency for today's date. 

### Required Parameters
* **apiaccesskey**: Register for an API Key at [fixer](https://fixer.io)

### Optional Parameters
* **datelist**: Date list where each date is in YYYY-MM-DD format. Used for retrieving exchange rate within the time points specified in date list. 
* **currencynamelist**: Currency name list where each currency name represents a wildcard for matching any currencies from currency dictionary found within [configuration](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py)
* **basecurrency**: Currency base for calculating the exchange rate represented as currency code.

### Flag Parameters
* **debug**: Prints helpful information for debugging.
* **visual**: Makes output human readable instead of csv format.
* **legacy_user**: For a limited time, [fixer currently offers additional features for free to legacy users](https://fixer.io/signup/legacy), such as the ability to use any currency as your base and SSL support. Please turn this flag on if you are a legacy user. If this flag is turned off, our script will do some workarounds to still be able to use any currency as your base.
* **no_header**: Output does not display header which can be useful when appending data to existing files.

### Output 
**1. currency_name** (Currency Name)<br>
**2. symbol** (Symbol)<br>
**3. date** (Date)<br>
**4. rate** (Rate)<br>
**5. reciprocal_rate** (Reciprocal Rate)<br>

**[1]** _parenthesis = column name when visual flag is turned on_

### Q&A

#### I am a free user in Fixer. Can I use any base currencies with this script?

> Yes. Currently, Fixer only allows EUR as their base currency for free users. Our script does some workarounds to closely resemble of fetching results with a different base currency. If you used the old Fixer without API key, for a limited time, you can use any base currency by registering a [legacy account](https://fixer.io/signup/legacy). Just do not forget to add the flag parameter **legacy_user** when using our script.

#### I am free user in Fixer. I do not have access to the Time-Series Endpoint. Can I use your script to do that?

> Yes. However, unlike running a Time-Series Endpoint will cost you one API call, our script will cost you one API call for each date you input in our optional parameter **datelist**. For instance, if you want to find the rates between 2018-03-01 and 2018-03-10, you will need to type `--datelist 2018-03-01 2018-03-02 2018-03-03 2018-03-04 2018-03-05 2018-03-06 2018-03-07 2018-03-08 2018-03-09 2018-03-10` which will cost you ten API calls. 

#### I am free user in Fixer. I do not have access to the Conversion Endpoint. Can I use your script to do that?

> Stay tuned on our next updates for including this feature :wink:

#### What do you output? What choices do I have for the output?

> Check the [list of columns we output](https://github.com/asokratis/python_currency_fixer#output) for more info.<br><br>We currently have two choices for output: CSV and human-readable. To see your output in a human-readable format, add the flag parameter **visual**. 

#### Do you have the option for saving my CSV output into a flatfile?

> We currently are not planning to add this feature in our next updates :neutral_face:<br><br>If you are in a linux environment, you have the ability to write the CSV output into a new flatfile by typing `python get_currency.py "<access-key-id>" > myflatfile.csv` or append to an existing flatfile by typing `python get_currency.py "<access-key-id>" --no_header >> myflatfile.csv` 

#### Do you have the option for getting only the columns I need?

> We currently are not planning to add this feature in our next updates :neutral_face:<br><br>If you are in a linux environment and already saved your CSV output into a flatfile (see previous question), then by checking the [list of columns we output](https://github.com/asokratis/python_currency_fixer#output), you can create a new flatfile by creating only the columns you need. For instance, if we want from `myflatfile.csv` only the `symbol` and `rate` in a new flatfile called `derivedflatfile.csv`, then we type `cut -d ',' -f 2,4 myflatfile.csv > derivedflatfile.csv` 

### Examples

`python get_currency.py "<access-key-id>" --visual --datelist 2018-03-01 2017-03-01 --currencynamelist mex aus eur`
```
Currency Name                           Symbol            Date                          Rate               Reciprocal Rate
==================================================================================================================================
Mexican Peso                            MXN         2018-03-01               23.129746000000                0.043234370148
Australian Dollar                       AUD         2018-03-01                1.580825000000                0.632581088988
Euro                                    EUR         2018-03-01                1.000000000000                1.000000000000
Mexican Peso                            MXN         2017-03-01               20.916698000000                0.047808693322
Australian Dollar                       AUD         2017-03-01                1.376369000000                0.726549348322
Euro                                    EUR         2017-03-01                1.000000000000                1.000000000000
```

`python get_currency.py "<access-key-id>" --visual --datelist 2018-03-18 --basecurrency BTC`
```
Currency Name                           Symbol            Date                          Rate               Reciprocal Rate
==================================================================================================================================
Algerian Dinar                          DZD         2018-03-18           933328.560000000007                0.000001071434
Namibian Dollar                         NAD         2018-03-18            98014.393333333342                0.000010202583
Ghanaian Cedi                           GHS         2018-03-18            36101.313333333337                0.000027699823
Egyptian Pound                          EGP         2018-03-18           143961.573333333337                0.000006946298
Bulgarian Lev                           BGN         2018-03-18            13022.053333333335                0.000076792805
Bermudan Dollar                         BMD         2018-03-18             8189.033333333335                0.000122114535
Panamanian Balboa                       PAB         2018-03-18             8189.033333333335                0.000122114535
Bolivian Boliviano                      BOB         2018-03-18            56175.233333333338                0.000017801439
Danish Krone                            DKK         2018-03-18            49667.126666666671                0.000020134042
Botswanan Pula                          BWP         2018-03-18            78397.706666666671                0.000012755475
Lebanese Pound                          LBP         2018-03-18         12365434.833333334783                0.000000080871
Tanzanian Shilling                      TZS         2018-03-18         18408944.420000002634                0.000000054321
Vietnamese Dong                         VND         2018-03-18        186406925.386666690691                0.000000005365
Angolan Kwanza                          AOA         2018-03-18          1753541.860000000044                0.000000570274
Cambodian Riel                          KHR         2018-03-18         32608725.473333333691                0.000000030667
Malaysian Ringgit                       MYR         2018-03-18            31994.666666666669                0.000031255209
Cayman Islands Dollar                   KYD         2018-03-18             6716.133333333334                0.000148895198
Libyan Dinar                            LYD         2018-03-18            10852.940000000002                0.000092140931
Ukrainian Hryvnia                       UAH         2018-03-18           216108.533333333355                0.000004627305
Jordanian Dinar                         JOD         2018-03-18             5793.766666666667                0.000172599288
Aruban Florin                           AWG         2018-03-18            14576.473333333335                0.000068603700
Saudi Riyal                             SAR         2018-03-18            30709.713333333335                0.000032562987
Euro                                    EUR         2018-03-18             6666.666666666667                0.000150000000
Hong Kong Dollar                        HKD         2018-03-18            64225.506666666666                0.000015570138
Swiss Franc                             CHF         2018-03-18             7802.586666666667                0.000128162626
Gibraltar Pound                         GIP         2018-03-18             5872.353333333334                0.000170289481
Belarusian Ruble                        BYR         2018-03-18        160505018.566666684631                0.000000006230
Gold (troy ounce)                       XAU         2018-03-18                6.233333333333                0.160427807487
New Belarusian Ruble                    BYN         2018-03-18            16050.453333333334                0.000062303536
Mauritanian Ouguiya                     MRO         2018-03-18          2874350.806666666989                0.000000347905
Croatian Kuna                           HRK         2018-03-18            49563.266666666673                0.000020176233
Djiboutian Franc                        DJF         2018-03-18          1448066.466666666783                0.000000690576
Thai Baht                               THB         2018-03-18           255579.666666666700                0.000003912674
CFA Franc BEAC                          XAF         2018-03-18          4369830.980000000413                0.000000228842
Brunei Dollar                           BND         2018-03-18            10777.606666666668                0.000092784978
Ethiopian Birr                          ETB         2018-03-18           222905.433333333340                0.000004486207
Uruguayan Peso                          UYU         2018-03-18           232160.253333333364                0.000004307370
Nicaraguan Córdoba                      NIO         2018-03-18           253699.573333333341                0.000003941670
Laotian Kip                             LAK         2018-03-18         67796990.773333339527                0.000000014750
Syrian Pound                            SYP         2018-03-18          4217187.306666666766                0.000000237125
Moroccan Dirham                         MAD         2018-03-18            75179.440000000006                0.000013301509
Mozambican Metical                      MZN         2018-03-18           513452.286666666706                0.000001947601
Philippine Peso                         PHP         2018-03-18           425010.753333333364                0.000002352882
South African Rand                      ZAR         2018-03-18            98068.600000000012                0.000010196944
Paraguayan Guarani                      PYG         2018-03-18         45203457.100000006013                0.000000022122
Zimbabwean Dollar                       ZWL         2018-03-18          2639775.360000000095                0.000000378820
Bhutanese Ngultrum                      BTN         2018-03-18           531058.680000000009                0.000001883031
Nigerian Naira                          NGN         2018-03-18          2923482.800000000329                0.000000342058
Costa Rican Colón                       CRC         2018-03-18          4607558.806666667149                0.000000217035
United Arab Emirates Dirham             AED         2018-03-18            30079.086666666669                0.000033245690
British Pound Sterling                  GBP         2018-03-18             5873.253333333334                0.000170263386
Malawian Kwacha                         MWK         2018-03-18          5842218.753333333761                0.000000171168
Sri Lankan Rupee                        LKR         2018-03-18          1277079.446666666739                0.000000783037
Pakistani Rupee                         PKR         2018-03-18           904642.326666666732                0.000001105409
Hungarian Forint                        HUF         2018-03-18          2072480.126666667001                0.000000482514
Romanian Leu                            RON         2018-03-18            31103.606666666670                0.000032150612
Lesotho Loti                            LSL         2018-03-18            98018.100000000005                0.000010202197
Mongolian Tugrik                        MNT         2018-03-18         19563595.180000000756                0.000000051115
Armenian Dram                           AMD         2018-03-18          3929424.873333333573                0.000000254490
Ugandan Shilling                        UGX         2018-03-18         29906344.566666669271                0.000000033438
Qatari Rial                             QAR         2018-03-18            29818.740000000003                0.000033535958
Special Drawing Rights                  XDR         2018-03-18             5636.780000000000                0.000177406250
Jamaican Dollar                         JMD         2018-03-18          1038860.553333333405                0.000000962593
Trinidad and Tobago Dollar              TTD         2018-03-18            55055.646666666675                0.000018163441
Saint Helena Pound                      SHP         2018-03-18             5872.313333333334                0.000170290641
Afghan Afghani                          AFN         2018-03-18           565043.786666666726                0.000001769774
Myanma Kyat                             MMK         2018-03-18         10956919.460000001638                0.000000091267
North Korean Won                        KPW         2018-03-18          7370128.906666667757                0.000000135683
Turkish Lira                            TRY         2018-03-18            32081.326666666667                0.000031170781
Bangladeshi Taka                        BDT         2018-03-18           678788.820000000103                0.000001473212
Yemeni Rial                             YER         2018-03-18          2046438.940000000257                0.000000488654
Cape Verdean Escudo                     CVE         2018-03-18           735375.060000000046                0.000001359850
Chinese Yuan                            CNY         2018-03-18            51835.733333333338                0.000019291711
Haitian Gourde                          HTG         2018-03-18           528847.673333333384                0.000001890904
CFA Franc BCEAO                         XOF         2018-03-18          4369830.980000000413                0.000000228842
Malagasy Ariary                         MGA         2018-03-18         25304109.673333334683                0.000000039519
Netherlands Antillean Guilder           ANG         2018-03-18            14574.093333333334                0.000068614903
Liberian Dollar                         LRD         2018-03-18          1072435.633333333365                0.000000932457
East Caribbean Dollar                   XCD         2018-03-18            22079.913333333334                0.000045290033
Norwegian Krone                         NOK         2018-03-18            63256.013333333343                0.000015808774
Macanese Pataca                         MOP         2018-03-18            66105.160000000011                0.000015127412
Indian Rupee                            INR         2018-03-18           532123.293333333388                0.000001879264
Mexican Peso                            MXN         2018-03-18           153057.106666666688                0.000006533509
Czech Republic Koruna                   CZK         2018-03-18           169386.040000000018                0.000005903674
Tajikistani Somoni                      TJS         2018-03-18            72279.693333333336                0.000013835144
New Taiwan Dollar                       TWD         2018-03-18           238390.526666666671                0.000004194798
Nepalese Rupee                          NPR         2018-03-18           851298.973333333397                0.000001174675
Colombian Peso                          COP         2018-03-18         23375590.586666669198                0.000000042780
Turkmenistani Manat                     TMT         2018-03-18            27842.706666666670                0.000035916048
Mauritian Rupee                         MUR         2018-03-18           270647.486666666713                0.000003694843
Indonesian Rupiah                       IDR         2018-03-18        112558238.786666683313                0.000000008884
Honduran Lempira                        HNL         2018-03-18           192769.813333333358                0.000005187534
Fijian Dollar                           FJD         2018-03-18            16501.013333333335                0.000060602339
Icelandic Króna                         ISK         2018-03-18           814791.740000000076                0.000001227307
Peruvian Nuevo Sol                      PEN         2018-03-18            26746.986666666669                0.000037387389
Belize Dollar                           BZD         2018-03-18            16360.080000000002                0.000061124395
Israeli New Sheqel                      ILS         2018-03-18            28259.526666666667                0.000035386297
Dominican Peso                          DOP         2018-03-18           404538.173333333368                0.000002471955
Guernsey Pound                          GGP         2018-03-18             5873.273333333334                0.000170262806
Moldovan Leu                            MDL         2018-03-18           134971.826666666684                0.000007408954
Bahamian Dollar                         BSD         2018-03-18             8189.033333333335                0.000122114535
Swedish Krona                           SEK         2018-03-18            67113.206666666674                0.000014900197
Zambian Kwacha (pre-2013)               ZMK         2018-03-18         73711104.866666677268                0.000000013566
Jersey Pound                            JEP         2018-03-18             5873.273333333334                0.000170262806
Australian Dollar                       AUD         2018-03-18            10612.186666666668                0.000094231286
Surinamese Dollar                       SRD         2018-03-18            60845.253333333335                0.000016435136
Cuban Peso                              CUP         2018-03-18           217009.333333333359                0.000004608097
Chilean Unit of Account (UF)            CLF         2018-03-18              182.700000000000                0.005473453749
Barbadian Dollar                        BBD         2018-03-18            16378.060000000002                0.000061057292
Comorian Franc                          KMF         2018-03-18          3269880.206666666995                0.000000305822
South Korean Won                        KRW         2018-03-18          8759724.686666667528                0.000000114159
Gambian Dalasi                          GMD         2018-03-18           383246.666666666713                0.000002609286
Venezuelan Bolívar Fuerte               VEF         2018-03-18        299374614.953333344149                0.000000003340
Guatemalan Quetzal                      GTQ         2018-03-18            60075.026666666667                0.000016645852
Cuban Convertible Peso                  CUC         2018-03-18             8189.033333333335                0.000122114535
Georgian Lari                           GEL         2018-03-18            19946.033333333335                0.000050135282
Chilean Peso                            CLP         2018-03-18          4980814.506666666887                0.000000200770
Zambian Kwacha                          ZMW         2018-03-18            78533.153333333340                0.000012733476
Lithuanian Litas                        LTL         2018-03-18            24965.893333333335                0.000040054645
Albanian Lek                            ALL         2018-03-18           871312.973333333389                0.000001147693
Rwandan Franc                           RWF         2018-03-18          6902780.313333333347                0.000000144869
Kazakhstani Tenge                       KZT         2018-03-18          2641044.653333333603                0.000000378638
Russian Ruble                           RUB         2018-03-18           470566.326666666672                0.000002125099
Silver (troy ounce)                     XAG         2018-03-18              502.006666666667                0.001992005418
Congolese Franc                         CDF         2018-03-18         12819889.113333334749                0.000000078004
Omani Rial                              OMR         2018-03-18             3151.940000000000                0.000317264923
Brazilian Real                          BRL         2018-03-18            26842.813333333337                0.000037253919
Solomon Islands Dollar                  SBD         2018-03-18            63313.506666666672                0.000015794418
Polish Zloty                            PLN         2018-03-18            28124.393333333334                0.000035556323
Kenyan Shilling                         KES         2018-03-18           827501.666666666700                0.000001208457
Salvadoran Colón                        SVC         2018-03-18            71652.913333333342                0.000013956167
Macedonian Denar                        MKD         2018-03-18           409205.913333333378                0.000002443757
Azerbaijani Manat                       AZN         2018-03-18            13917.246666666668                0.000071853293
Tongan Paʻanga                          TOP         2018-03-18            18386.013333333335                0.000054389170
Maldivian Rufiyaa                       MVR         2018-03-18           127503.173333333338                0.000007842942
Vanuatu Vatu                            VUV         2018-03-18           860339.640000000145                0.000001162332
Guinean Franc                           GNF         2018-03-18         73725846.520000008029                0.000000013564
Samoan Tala                             WST         2018-03-18            20758.326666666668                0.000048173440
Iraqi Dinar                             IQD         2018-03-18          9695813.366666667147                0.000000103137
Eritrean Nakfa                          ERN         2018-03-18           122754.146666666686                0.000008146364
Bosnia-Herzegovina Convertible Mark     BAM         2018-03-18            13059.073333333334                0.000076575112
Seychellois Rupee                       SCR         2018-03-18           109977.093333333339                0.000009092803
Canadian Dollar                         CAD         2018-03-18            10722.640000000001                0.000093260615
Guyanaese Dollar                        GYD         2018-03-18          1680962.540000000213                0.000000594897
Kuwaiti Dinar                           KWD         2018-03-18             2454.253333333334                0.000407455900
Burundian Franc                         BIF         2018-03-18         14338830.313333335696                0.000000069741
Papua New Guinean Kina                  PGK         2018-03-18            25877.413333333336                0.000038643739
Somali Shilling                         SOS         2018-03-18          4626800.580000000336                0.000000216132
Singapore Dollar                        SGD         2018-03-18            10790.680000000002                0.000092672566
Uzbekistan Som                          UZS         2018-03-18         66494933.793333335784                0.000000015039
São Tomé and Príncipe Dobra             STD         2018-03-18        163394115.293333345476                0.000000006120
Bitcoin                                 BTC         2018-03-18                1.000000000000                1.000000000000
Iranian Rial                            IRR         2018-03-18        308669168.433333376377                0.000000003240
CFP Franc                               XPF         2018-03-18           798450.520000000072                0.000001252426
Sierra Leonean Leone                    SLL         2018-03-18         62482311.413333342005                0.000000016005
Tunisian Dinar                          TND         2018-03-18            19891.006666666669                0.000050273976
New Zealand Dollar                      NZD         2018-03-18            11327.886666666668                0.000088277719
Falkland Islands Pound                  FKP         2018-03-18             5869.906666666667                0.000170360460
Latvian Lats                            LVL         2018-03-18             5081.706666666667                0.000196784282
United States Dollar                    USD         2018-03-18             8189.033333333335                0.000122114535
Kyrgystani Som                          KGS         2018-03-18           558897.273333333404                0.000001789238
Argentine Peso                          ARS         2018-03-18           165082.860000000021                0.000006057564
Swazi Lilangeni                         SZL         2018-03-18            98043.993333333346                0.000010199503
Manx pound                              IMP         2018-03-18             5873.273333333334                0.000170262806
Serbian Dinar                           RSD         2018-03-18           784675.433333333362                0.000001274412
Bahraini Dinar                          BHD         2018-03-18             3087.480000000000                0.000323888738
Japanese Yen                            JPY         2018-03-18           867742.513333333326                0.000001152416
Sudanese Pound                          SDG         2018-03-18           147821.853333333345                0.000006764900
```

### Versions
**Current Version:** 0.02
#### Version 0.01
* Initial Draft
#### Version 0.02
* Updated Configurations
#### Version 0.03
* The formatting of numerical figures is in decimal format. If output in API is found in scientific notation, it is converted to decimal format. To keep accuracy of calculations, we keep them in decimal format. After calculations, we round them up with a precision of 12 digits and show the output of all numerical figures with 12 digits.
* Fixed output issues on the use cases when it was not encoded to `utf-8` properly. 
* Renamed the names shown in header. Check [output](https://github.com/asokratis/python_currency_fixer#output) for more info.
* Added new column: **reciprocal_rate** which represents `1/rate`
* Added flag parameter **no_header** that allows to show output without the headers. Useful for appending data to existing files that contains the header already.
* Added flag parameter **legacy_user**. If user is not a legacy_user, API by default does not provide user to use any base currency except `EUR`. We did some workarounds in our code where free users can use any base currency in our script and get the same results as a legacy user. For instance, one Bitcoin is 308977626 Iranian Rial when running our script as a legacy user while one Bitcoin is 308669168 Iranian Rial when running our script as a free user with our workarounds. The difference between the two results is close to one Euro cent. If you are a legacy user, we recommend to add the flag `legacy_user` in your script to get the most accurate results.
* Added Q&A Section in our documentation for all existing and new features.