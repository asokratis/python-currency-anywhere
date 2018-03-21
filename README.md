# python_currency_fixer
Get your currency with this python script via [Fixer](https://fixer.io)

## configurations
To update existing [currency_configurations](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py), run [update_currency_configurations](https://github.com/asokratis/python_currency_fixer/blob/master/update_currency_configurations.py) while providing your Fixer API Key as parameter. You can update the maximum number of failed attempts on requesting currency data at [retry_configurations](https://github.com/asokratis/python_currency_fixer/blob/master/retry_configurations.py). 

## get_currency
By default, uses [Fixer](https://fixer.io) free and legacy accounts to display exchange rate for all currencies with EUR as base currency in the amounts of one unit for today's date. 

### Required Parameters
* **apiaccesskey**: Register for an API Key at [Fixer](https://fixer.io)

### Optional Parameters
* **datelist**: Date list where each date is in YYYY-MM-DD format. Used for retrieving exchange rate within the time points specified in date list. 
* **currencynamelist**: Currency name list where each currency name represents a wildcard for matching any currencies from currency dictionary found within [currency configurations](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py)
* **symbollist**: Currency symbol list where each currency symbol must match to any currency symbols from currency dictionary found within [currency configurations](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py) (case insensitive)
* **basecurrency**: Currency base for calculating the exchange rate represented as currency code.
* **amount**: The amount to be converted from the base currency. Amount can be between the values of one hundredth to one million and is rounded to the nearest hundredth.
* **daysinterval**: Determines the number of consecutive days from parameter datelist for retrieving exchange rate within those dates. In order for daysinterval to take effect, it must be a positive number while only one date is specified in datelist.

### Flag Parameters
* **debug**: Prints helpful information for debugging.
* **visual**: Makes output human readable instead of csv format.
* **legacy_user**: For a limited time, [Fixer currently offers additional features for free to legacy users](https://fixer.io/signup/legacy), such as the ability to use any currency as your base and SSL support. Please turn this flag on if you are a legacy user. If this flag is turned off, our script will do some workarounds to still be able to use any currency as your base.
* **no_header**: Output does not display header which can be useful when appending data to existing files.

### Output 
**1. currency_name** (Currency Name)<br>
**2. symbol** (Symbol)<br>
**3. date** (Date)<br>
**4. amount** (Amount)<br>
**5. rate** (Rate)<br>
**6. reciprocal_rate** (Reciprocal Rate)<br>

**[1]** _parenthesis = column name when visual flag is turned on_

### Q&A

#### How do I filter output to only the currencies I need?

> You can either use optional parameter **currencynamelist** for entering a list that is similar to the currency name list within our [currency configurations](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py) or use the optional parameter **symbollist** for entering a list of symbols that match with the symbols list found in our [currency configurations](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py) (case insensitive).  

#### I am a free user in Fixer. Can I use any base currencies with this script?

> Yes. Currently, Fixer only allows EUR as their base currency for free users. Our script does some workarounds to closely resemble of fetching results with a different base currency. If you used the old Fixer without API key, for a limited time, you can use any base currency by registering a [legacy account](https://fixer.io/signup/legacy). Just do not forget to add the flag parameter **legacy_user** when using our script.

#### I am a free user in Fixer. I do not have access to the Time-Series Endpoint. Can I use your script to do that?

> Yes. However, unlike running a Time-Series Endpoint will cost you one API call, our script will cost you one API call for each date you input in our optional parameter **datelist**. For instance, if you want to find the rates between 2018-03-01 and 2018-03-10, you will need to type `--datelist 2018-03-01 2018-03-02 2018-03-03 2018-03-04 2018-03-05 2018-03-06 2018-03-07 2018-03-08 2018-03-09 2018-03-10` which will cost you ten API calls. 

#### That is a lot to type. Is there a shortcut version for doing the same thing with your script?

> Yes. From the previous query, you can do the same thing by using the optional parameter **daysinterval** by typing `--datelist 2018-03-01 --daysinterval 9`. Make sure **daysinterval** is a positive number and no more than one date is entered in parameter **datelist**. Otherwise, it will not work.

#### I am a free user in Fixer. I do not have access to the Conversion Endpoint. Can I use your script to do that?

> Yes. You can get your desired conversion by using the optional parameter **amount** which will reflect on the rate and reciprocal rate columns. **amount** can take values between one hundredth to one million. 

#### What do you output? What choices do I have for the output?

> Check the [list of columns we output](https://github.com/asokratis/python_currency_fixer#output) for more info.<br><br>We currently have two choices for output: CSV and human-readable. To see your output in a human-readable format, add the flag parameter **visual**. 

#### Your currency configurations are out of date? Do I have to update your currency configurations manually?

> You can update your [currency configurations](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py) automatically by running the python script **update_currency_configurations** by typing `python update_currency_configurations.py "<access-key-id>"`. Each time you update will cost you one API call.

#### Do you have the option for saving my CSV output into a flatfile?

> We currently are not planning to add this feature in our next updates :neutral_face:<br><br>If you are in a linux environment, you have the ability to write the CSV output into a new flatfile by typing `python get_currency.py "<access-key-id>" > myflatfile.csv` or append to an existing flatfile by typing `python get_currency.py "<access-key-id>" --no_header >> myflatfile.csv` 

#### Do you have the option for getting only the columns I need?

> We currently are not planning to add this feature in our next updates :neutral_face:<br><br>If you are in a linux environment and already saved your CSV output into a flatfile (see previous question), then by checking the [list of columns we output](https://github.com/asokratis/python_currency_fixer#output), you can create a new flatfile by creating only the columns you need. For instance, if we want from `myflatfile.csv` only the `symbol` and `rate` in a new flatfile called `derivedflatfile.csv`, then we type `cut -d ',' -f 2,5 myflatfile.csv > derivedflatfile.csv` 

### Examples

`python get_currency.py "<access-key-id>" --visual --datelist 2018-03-01 2017-03-01 --currencynamelist mex aus eur`
```
Currency Name                           Symbol            Date      Amount                            Rate                 Reciprocal Rate
============================================================================================================================================
Mexican Peso                            MXN         2018-03-01        1.00               23.12974600000000                0.04323437014829
Australian Dollar                       AUD         2018-03-01        1.00                1.58082500000000                0.63258108898834
Euro                                    EUR         2018-03-01        1.00                1.00000000000000                1.00000000000000
Mexican Peso                            MXN         2017-03-01        1.00               20.91669800000000                0.04780869332244
Australian Dollar                       AUD         2017-03-01        1.00                1.37636900000000                0.72654934832156
Euro                                    EUR         2017-03-01        1.00                1.00000000000000                1.00000000000000
```

`python get_currency.py "<access-key-id>" --visual --datelist 2018-03-18 --basecurrency BTC --amount 12.5`
```
Currency Name                           Symbol            Date      Amount                            Rate                 Reciprocal Rate
============================================================================================================================================
Algerian Dinar                          DZD         2018-03-18       12.50         11666607.00000000008344                0.00000008571472
Namibian Dollar                         NAD         2018-03-18       12.50          1225179.91666666677213                0.00000081620665
Ghanaian Cedi                           GHS         2018-03-18       12.50           451266.41666666670939                0.00000221598586
Egyptian Pound                          EGP         2018-03-18       12.50          1799519.66666666671216                0.00000055570385
Bulgarian Lev                           BGN         2018-03-18       12.50           162775.66666666668461                0.00000614342439
Bermudan Dollar                         BMD         2018-03-18       12.50           102362.91666666668278                0.00000976916282
Panamanian Balboa                       PAB         2018-03-18       12.50           102362.91666666668278                0.00000976916282
Bolivian Boliviano                      BOB         2018-03-18       12.50           702190.41666666673027                0.00000142411514
Danish Krone                            DKK         2018-03-18       12.50           620839.08333333339208                0.00000161072334
Botswanan Pula                          BWP         2018-03-18       12.50           979971.33333333339125                0.00000102043801
Lebanese Pound                          LBP         2018-03-18       12.50        154567935.41666668478515                0.00000000646965
Tanzanian Shilling                      TZS         2018-03-18       12.50        230111805.25000003293034                0.00000000434571
Vietnamese Dong                         VND         2018-03-18       12.50       2330086567.33333363363561                0.00000000042917
Angolan Kwanza                          AOA         2018-03-18       12.50         21919273.25000000055566                0.00000004562195
Cambodian Riel                          KHR         2018-03-18       12.50        407609068.41666667114140                0.00000000245333
Malaysian Ringgit                       MYR         2018-03-18       12.50           399933.33333333336091                0.00000250041674
Cayman Islands Dollar                   KYD         2018-03-18       12.50            83951.66666666667253                0.00001191161581
Libyan Dinar                            LYD         2018-03-18       12.50           135661.75000000001875                0.00000737127451
Ukrainian Hryvnia                       UAH         2018-03-18       12.50          2701356.66666666693894                0.00000037018436
Jordanian Dinar                         JOD         2018-03-18       12.50            72422.08333333333771                0.00001380794302
Aruban Florin                           AWG         2018-03-18       12.50           182205.91666666668708                0.00000548829598
Saudi Riyal                             SAR         2018-03-18       12.50           383871.41666666668378                0.00000260503897
Euro                                    EUR         2018-03-18       12.50            83333.33333333334063                0.00001200000000
Hong Kong Dollar                        HKD         2018-03-18       12.50           802818.83333333332969                0.00000124561104
Swiss Franc                             CHF         2018-03-18       12.50            97532.33333333334054                0.00001025301011
Gibraltar Pound                         GIP         2018-03-18       12.50            73404.41666666667286                0.00001362315846
Belarusian Ruble                        BYR         2018-03-18       12.50       2006312732.08333355789084                0.00000000049843
Gold (troy ounce)                       XAU         2018-03-18       12.50               77.91666666666667                0.01283422459893
New Belarusian Ruble                    BYN         2018-03-18       12.50           200630.66666666667844                0.00000498428289
Mauritanian Ouguiya                     MRO         2018-03-18       12.50         35929385.08333333736036                0.00000002783237
Croatian Kuna                           HRK         2018-03-18       12.50           619540.83333333340968                0.00000161409861
Djiboutian Franc                        DJF         2018-03-18       12.50         18100830.83333333478867                0.00000005524608
Thai Baht                               THB         2018-03-18       12.50          3194745.83333333374963                0.00000031301395
CFA Franc BEAC                          XAF         2018-03-18       12.50         54622887.25000000515866                0.00000001830734
Brunei Dollar                           BND         2018-03-18       12.50           134720.08333333334469                0.00000742279826
Ethiopian Birr                          ETB         2018-03-18       12.50          2786317.91666666674951                0.00000035889659
Uruguayan Peso                          UYU         2018-03-18       12.50          2902003.16666666705444                0.00000034458956
Nicaraguan Córdoba                      NIO         2018-03-18       12.50          3171244.66666666676743                0.00000031533360
Laotian Kip                             LAK         2018-03-18       12.50        847462384.66666674408939                0.00000000117999
Syrian Pound                            SYP         2018-03-18       12.50         52714841.33333333457893                0.00000001896999
Moroccan Dirham                         MAD         2018-03-18       12.50           939743.00000000007732                0.00000106412072
Mozambican Metical                      MZN         2018-03-18       12.50          6418153.58333333382601                0.00000015580805
Philippine Peso                         PHP         2018-03-18       12.50          5312634.41666666704677                0.00000018823053
South African Rand                      ZAR         2018-03-18       12.50          1225857.50000000015173                0.00000081575550
Paraguayan Guarani                      PYG         2018-03-18       12.50        565043213.75000007515966                0.00000000176978
Zimbabwean Dollar                       ZWL         2018-03-18       12.50         32997192.00000000119264                0.00000003030561
Bhutanese Ngultrum                      BTN         2018-03-18       12.50          6638233.50000000010958                0.00000015064249
Nigerian Naira                          NGN         2018-03-18       12.50         36543535.00000000411690                0.00000002736462
Costa Rican Colón                       CRC         2018-03-18       12.50         57594485.08333333935682                0.00000001736277
United Arab Emirates Dirham             AED         2018-03-18       12.50           375988.58333333336268                0.00000265965522
British Pound Sterling                  GBP         2018-03-18       12.50            73415.66666666667254                0.00001362107089
Malawian Kwacha                         MWK         2018-03-18       12.50         73027734.41666667201157                0.00000001369343
Sri Lankan Rupee                        LKR         2018-03-18       12.50         15963493.08333333423218                0.00000006264293
Pakistani Rupee                         PKR         2018-03-18       12.50         11308029.08333333414782                0.00000008843274
Hungarian Forint                        HUF         2018-03-18       12.50         25906001.58333333751697                0.00000003860109
Romanian Leu                            RON         2018-03-18       12.50           388795.08333333338075                0.00000257204899
Lesotho Loti                            LSL         2018-03-18       12.50          1225226.25000000006854                0.00000081617579
Mongolian Tugrik                        MNT         2018-03-18       12.50        244544939.75000000945163                0.00000000408923
Armenian Dram                           AMD         2018-03-18       12.50         49117810.91666666966171                0.00000002035921
Ugandan Shilling                        UGX         2018-03-18       12.50        373829307.08333336588808                0.00000000267502
Qatari Rial                             QAR         2018-03-18       12.50           372734.25000000004035                0.00000268287661
Special Drawing Rights                  XDR         2018-03-18       12.50            70459.75000000000309                0.00001419249997
Jamaican Dollar                         JMD         2018-03-18       12.50         12985756.91666666756492                0.00000007700745
Trinidad and Tobago Dollar              TTD         2018-03-18       12.50           688195.58333333343932                0.00000145307529
Saint Helena Pound                      SHP         2018-03-18       12.50            73403.91666666667698                0.00001362325126
Afghan Afghani                          AFN         2018-03-18       12.50          7063047.33333333407388                0.00000014158195
Myanma Kyat                             MMK         2018-03-18       12.50        136961493.25000002047601                0.00000000730132
North Korean Won                        KPW         2018-03-18       12.50         92126611.33333334695672                0.00000001085463
Turkish Lira                            TRY         2018-03-18       12.50           401016.58333333334107                0.00000249366246
Bangladeshi Taka                        BDT         2018-03-18       12.50          8484860.25000000129105                0.00000011785698
Yemeni Rial                             YER         2018-03-18       12.50         25580486.75000000321744                0.00000003909230
Cape Verdean Escudo                     CVE         2018-03-18       12.50          9192188.25000000056963                0.00000010878802
Chinese Yuan                            CNY         2018-03-18       12.50           647946.66666666672753                0.00000154333690
Haitian Gourde                          HTG         2018-03-18       12.50          6610595.91666666729876                0.00000015127229
CFA Franc BCEAO                         XOF         2018-03-18       12.50         54622887.25000000515866                0.00000001830734
Malagasy Ariary                         MGA         2018-03-18       12.50        316301370.91666668353946                0.00000000316154
Netherlands Antillean Guilder           ANG         2018-03-18       12.50           182176.16666666667351                0.00000548919224
Liberian Dollar                         LRD         2018-03-18       12.50         13405445.41666666706644                0.00000007459655
East Caribbean Dollar                   XCD         2018-03-18       12.50           275998.91666666667353                0.00000362320263
Norwegian Krone                         NOK         2018-03-18       12.50           790700.16666666679168                0.00000126470190
Macanese Pataca                         MOP         2018-03-18       12.50           826314.50000000013523                0.00000121019297
Indian Rupee                            INR         2018-03-18       12.50          6651541.16666666734645                0.00000015034110
Mexican Peso                            MXN         2018-03-18       12.50          1913213.83333333359589                0.00000052268073
Czech Republic Koruna                   CZK         2018-03-18       12.50          2117325.50000000023098                0.00000047229394
Tajikistani Somoni                      TJS         2018-03-18       12.50           903496.16666666669791                0.00000110681156
New Taiwan Dollar                       TWD         2018-03-18       12.50          2979881.58333333338186                0.00000033558380
Nepalese Rupee                          NPR         2018-03-18       12.50         10641237.16666666745707                0.00000009397404
Colombian Peso                          COP         2018-03-18       12.50        292194882.33333336497211                0.00000000342237
Turkmenistani Manat                     TMT         2018-03-18       12.50           348033.83333333336905                0.00000287328387
Mauritian Rupee                         MUR         2018-03-18       12.50          3383093.58333333391313                0.00000029558745
Indonesian Rupiah                       IDR         2018-03-18       12.50       1406977984.83333354141754                0.00000000071074
Honduran Lempira                        HNL         2018-03-18       12.50          2409622.66666666697557                0.00000041500274
Fijian Dollar                           FJD         2018-03-18       12.50           206262.66666666668630                0.00000484818710
Icelandic Króna                         ISK         2018-03-18       12.50         10184896.75000000094635                0.00000009818460
Peruvian Nuevo Sol                      PEN         2018-03-18       12.50           334337.33333333336751                0.00000299099113
Belize Dollar                           BZD         2018-03-18       12.50           204501.00000000002476                0.00000488995164
Israeli New Sheqel                      ILS         2018-03-18       12.50           353244.08333333334136                0.00000283090375
Dominican Peso                          DOP         2018-03-18       12.50          5056727.16666666710484                0.00000019775637
Guernsey Pound                          GGP         2018-03-18       12.50            73415.91666666667048                0.00001362102451
Moldovan Leu                            MDL         2018-03-18       12.50          1687147.83333333354990                0.00000059271629
Bahamian Dollar                         BSD         2018-03-18       12.50           102362.91666666668278                0.00000976916282
Swedish Krona                           SEK         2018-03-18       12.50           838915.08333333342177                0.00000119201576
Zambian Kwacha (pre-2013)               ZMK         2018-03-18       12.50        921388810.83333346585507                0.00000000108532
Jersey Pound                            JEP         2018-03-18       12.50            73415.91666666667048                0.00001362102451
Australian Dollar                       AUD         2018-03-18       12.50           132652.33333333334668                0.00000753850290
Surinamese Dollar                       SRD         2018-03-18       12.50           760565.66666666668802                0.00000131481086
Cuban Peso                              CUP         2018-03-18       12.50          2712616.66666666698767                0.00000036864774
Chilean Unit of Account (UF)            CLF         2018-03-18       12.50             2283.75000000000010                0.00043787629995
Barbadian Dollar                        BBD         2018-03-18       12.50           204725.75000000002057                0.00000488458340
Comorian Franc                          KMF         2018-03-18       12.50         40873502.58333333744029                0.00000002446573
South Korean Won                        KRW         2018-03-18       12.50        109496558.58333334409826                0.00000000913271
Gambian Dalasi                          GMD         2018-03-18       12.50          4790583.33333333390932                0.00000020874285
Venezuelan Bolívar Fuerte               VEF         2018-03-18       12.50       3742182686.91666680186655                0.00000000026722
Guatemalan Quetzal                      GTQ         2018-03-18       12.50           750937.83333333333321                0.00000133166816
Cuban Convertible Peso                  CUC         2018-03-18       12.50           102362.91666666668278                0.00000976916282
Georgian Lari                           GEL         2018-03-18       12.50           249325.41666666669156                0.00000401082254
Chilean Peso                            CLP         2018-03-18       12.50         62260181.33333333609120                0.00000001606163
Zambian Kwacha                          ZMW         2018-03-18       12.50           981664.41666666675495                0.00000101867806
Lithuanian Litas                        LTL         2018-03-18       12.50           312073.66666666668397                0.00000320437162
Albanian Lek                            ALL         2018-03-18       12.50         10891412.16666666736720                0.00000009181546
Rwandan Franc                           RWF         2018-03-18       12.50         86284753.91666666683799                0.00000001158953
Kazakhstani Tenge                       KZT         2018-03-18       12.50         33013058.16666667004015                0.00000003029104
Russian Ruble                           RUB         2018-03-18       12.50          5882079.08333333339964                0.00000017000791
Silver (troy ounce)                     XAG         2018-03-18       12.50             6275.08333333333445                0.00015936043346
Congolese Franc                         CDF         2018-03-18       12.50        160248613.91666668435876                0.00000000624030
Omani Rial                              OMR         2018-03-18       12.50            39399.25000000000485                0.00002538119380
Brazilian Real                          BRL         2018-03-18       12.50           335535.16666666671003                0.00000298031354
Solomon Islands Dollar                  SBD         2018-03-18       12.50           791418.83333333339998                0.00000126355345
Polish Zloty                            PLN         2018-03-18       12.50           351554.91666666667369                0.00000284450580
Kenyan Shilling                         KES         2018-03-18       12.50         10343770.83333333374684                0.00000009667654
Salvadoran Colón                        SVC         2018-03-18       12.50           895661.41666666676980                0.00000111649333
Macedonian Denar                        MKD         2018-03-18       12.50          5115073.91666666722375                0.00000019550060
Azerbaijani Manat                       AZN         2018-03-18       12.50           173965.58333333335536                0.00000574826343
Tongan Paʻanga                          TOP         2018-03-18       12.50           229825.16666666669310                0.00000435113358
Maldivian Rufiyaa                       MVR         2018-03-18       12.50          1593789.66666666672568                0.00000062743536
Vanuatu Vatu                            VUV         2018-03-18       12.50         10754245.50000000180643                0.00000009298653
Guinean Franc                           GNF         2018-03-18       12.50        921573081.50000010036844                0.00000000108510
Samoan Tala                             WST         2018-03-18       12.50           259479.08333333334590                0.00000385387518
Iraqi Dinar                             IQD         2018-03-18       12.50        121197667.08333333933651                0.00000000825098
Eritrean Nakfa                          ERN         2018-03-18       12.50          1534426.83333333357788                0.00000065170915
Bosnia-Herzegovina Convertible Mark     BAM         2018-03-18       12.50           163238.41666666667791                0.00000612600894
Seychellois Rupee                       SCR         2018-03-18       12.50          1374713.66666666673203                0.00000072742421
Canadian Dollar                         CAD         2018-03-18       12.50           134033.00000000000648                0.00000746084919
Guyanaese Dollar                        GYD         2018-03-18       12.50         21012031.75000000266261                0.00000004759178
Kuwaiti Dinar                           KWD         2018-03-18       12.50            30678.16666666667109                0.00003259647198
Burundian Franc                         BIF         2018-03-18       12.50        179235378.91666669620234                0.00000000557926
Papua New Guinean Kina                  PGK         2018-03-18       12.50           323467.66666666670019                0.00000309149910
Somali Shilling                         SOS         2018-03-18       12.50         57835007.25000000419404                0.00000001729057
Singapore Dollar                        SGD         2018-03-18       12.50           134883.50000000001984                0.00000741380525
Uzbekistan Som                          UZS         2018-03-18       12.50        831186672.41666669730041                0.00000000120310
São Tomé and Príncipe Dobra             STD         2018-03-18       12.50       2042426441.16666681844627                0.00000000048961
Bitcoin                                 BTC         2018-03-18       12.50               12.50000000000000                0.08000000000000
Iranian Rial                            IRR         2018-03-18       12.50       3858364605.41666720471338                0.00000000025918
CFP Franc                               XPF         2018-03-18       12.50          9980631.50000000090064                0.00000010019406
Sierra Leonean Leone                    SLL         2018-03-18       12.50        781028892.66666677506652                0.00000000128036
Tunisian Dinar                          TND         2018-03-18       12.50           248637.58333333335954                0.00000402191811
New Zealand Dollar                      NZD         2018-03-18       12.50           141598.58333333335490                0.00000706221755
Falkland Islands Pound                  FKP         2018-03-18       12.50            73373.83333333333900                0.00001362883680
Latvian Lats                            LVL         2018-03-18       12.50            63521.33333333334262                0.00001574274260
United States Dollar                    USD         2018-03-18       12.50           102362.91666666668278                0.00000976916282
Kyrgystani Som                          KGS         2018-03-18       12.50          6986215.91666666754464                0.00000014313901
Argentine Peso                          ARS         2018-03-18       12.50          2063535.75000000025673                0.00000048460512
Swazi Lilangeni                         SZL         2018-03-18       12.50          1225549.91666666682763                0.00000081596024
Manx pound                              IMP         2018-03-18       12.50            73415.91666666667048                0.00001362102451
Serbian Dinar                           RSD         2018-03-18       12.50          9808442.91666666701888                0.00000010195298
Bahraini Dinar                          BHD         2018-03-18       12.50            38593.50000000000156                0.00002591109902
Japanese Yen                            JPY         2018-03-18       12.50         10846781.41666666657081                0.00000009219325
Sudanese Pound                          SDG         2018-03-18       12.50          1847773.16666666681363                0.00000054119197
```

### Versions
**Current Version:** 0.04
#### Version 0.01
* Initial Draft
#### Version 0.02
* Changed default base currency from USD to EUR
* Added script **update_currency_configurations** that allow you to update automatically [currency configurations](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py) with the use of Fixer Supported Symbols Endpoint.
* Added documentation for all existing configurations.
#### Version 0.03
* The formatting of numerical figures is in decimal format. If output in API is found in scientific notation, it is converted to decimal format. To keep accuracy of calculations, we keep them in decimal format. After calculations, we round them up with a precision of 12 digits and show the output of all numerical figures with 12 digits.
* Fixed output issues on the use cases when it was not encoded to `utf-8` properly. 
* Renamed the names shown in header. Check [output](https://github.com/asokratis/python_currency_fixer#output) for more info.
* Added new column: **reciprocal_rate** which represents `1/rate`
* Added flag parameter **no_header** that allows to show output without the headers. Useful for appending data to existing files that contains the header already.
* Added flag parameter **legacy_user**. If user is not a legacy_user, API by default does not provide user to use any base currency except `EUR`. We did some workarounds in our code where free users can use any base currency in our script and get the same results as a legacy user. For instance, one Bitcoin is 308977626 Iranian Rial when running our script as a legacy user while one Bitcoin is 308669168 Iranian Rial when running our script as a free user with our workarounds. The difference between the two results is close to one Euro cent. If you are a legacy user, we recommend to add the flag `legacy_user` in your script to get the most accurate results.
* Added Q&A Section in our documentation for all existing and new features.
#### Version 0.04
* Numerical figures extended from 12 digits to 14 digits and increased decimal precision.
* Added a new column and optional parameter **amount** which is used to multiply the `rate`. The optional parameter amount must be between the values of one hundredth and one million and is rounded to the nearest one hundredth.
* Added optional parameter **symbollist** that allows filtering output by only the list of symbols in the symbolllist that match with the symbols within the [currency configurations](https://github.com/asokratis/python_currency_fixer/blob/master/currency_configurations.py) (case insensitive).
* Added optional parameter **daysinterval** that represents the number of consecutive days from the parameter datelist for the use of retrieving exchange rate within those dates. Parameter daysinterval must be a positive number and can have only one date in parameter datelist. 
* Updated main documentation and Q&A section on existing and new features.
