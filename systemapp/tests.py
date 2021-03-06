from django.test import TestCase

# Create your tests here.

list1 = [{
                         "close":"69.12",
                        "open":"72.97",
                        "low":"69.06",
                        "high":"73.84",
                        "amount":"4877",
                        "balance":"34943799.00",
                        "turnover_rate":"0.0079%",
                        "timestamp":"1584460800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"67.02",
                        "open":"70.25",
                        "low":"65.05",
                        "high":"70.39",
                        "amount":"7216",
                        "balance":"48262481.00",
                        "turnover_rate":"0.0116%",
                        "timestamp":"1584547200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"68.24",
                        "open":"67.29",
                        "low":"66.82",
                        "high":"68.82",
                        "amount":"4167",
                        "balance":"28318726.00",
                        "turnover_rate":"0.0067%",
                        "timestamp":"1584633600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"65.09",
                        "open":"68.24",
                        "low":"64.39",
                        "high":"68.24",
                        "amount":"5955",
                        "balance":"38910658.00",
                        "turnover_rate":"0.0096%",
                        "timestamp":"1584892800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"65.90",
                        "open":"65.68",
                        "low":"64.32",
                        "high":"66.51",
                        "amount":"2613",
                        "balance":"17117675.00",
                        "turnover_rate":"0.0042%",
                        "timestamp":"1584979200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"68.07",
                        "open":"67.47",
                        "low":"67.47",
                        "high":"69.20",
                        "amount":"3186",
                        "balance":"21749958.00",
                        "turnover_rate":"0.0051%",
                        "timestamp":"1585065600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"70.31",
                        "open":"68.30",
                        "low":"67.30",
                        "high":"71.47",
                        "amount":"4487",
                        "balance":"31509542.00",
                        "turnover_rate":"0.0072%",
                        "timestamp":"1585152000",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"70.15",
                        "open":"70.91",
                        "low":"69.30",
                        "high":"71.90",
                        "amount":"4733",
                        "balance":"33298169.00",
                        "turnover_rate":"0.0076%",
                        "timestamp":"1585238400",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"66.98",
                        "open":"68.86",
                        "low":"66.12",
                        "high":"70.12",
                        "amount":"3459",
                        "balance":"23339049.00",
                        "turnover_rate":"0.0056%",
                        "timestamp":"1585497600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"64.99",
                        "open":"67.58",
                        "low":"64.52",
                        "high":"68.43",
                        "amount":"4670",
                        "balance":"30906364.00",
                        "turnover_rate":"0.0075%",
                        "timestamp":"1585584000",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"64.90",
                        "open":"64.80",
                        "low":"64.28",
                        "high":"66.76",
                        "amount":"3275",
                        "balance":"21470855.00",
                        "turnover_rate":"0.0053%",
                        "timestamp":"1585670400",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"66.70",
                        "open":"65.48",
                        "low":"64.68",
                        "high":"66.97",
                        "amount":"1828",
                        "balance":"12066404.00",
                        "turnover_rate":"0.0029%",
                        "timestamp":"1585756800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"67.59",
                        "open":"66.05",
                        "low":"66.05",
                        "high":"68.00",
                        "amount":"1685",
                        "balance":"11330930.00",
                        "turnover_rate":"0.0027%",
                        "timestamp":"1585843200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"68.30",
                        "open":"68.88",
                        "low":"67.00",
                        "high":"68.88",
                        "amount":"3602",
                        "balance":"24580534.00",
                        "turnover_rate":"0.0058%",
                        "timestamp":"1586188800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"67.90",
                        "open":"67.66",
                        "low":"67.66",
                        "high":"68.34",
                        "amount":"2395",
                        "balance":"16276019.00",
                        "turnover_rate":"0.0039%",
                        "timestamp":"1586275200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"70.97",
                        "open":"68.55",
                        "low":"67.77",
                        "high":"71.24",
                        "amount":"5201",
                        "balance":"36503728.00",
                        "turnover_rate":"0.0084%",
                        "timestamp":"1586361600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"69.85",
                        "open":"70.11",
                        "low":"69.09",
                        "high":"72.50",
                        "amount":"5268",
                        "balance":"37382019.00",
                        "turnover_rate":"0.0085%",
                        "timestamp":"1586448000",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"73.50",
                        "open":"69.80",
                        "low":"69.80",
                        "high":"73.92",
                        "amount":"6127",
                        "balance":"44597457.00",
                        "turnover_rate":"0.0099%",
                        "timestamp":"1586707200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"79.75",
                        "open":"73.51",
                        "low":"72.11",
                        "high":"79.75",
                        "amount":"8195",
                        "balance":"62696613.00",
                        "turnover_rate":"0.0132%",
                        "timestamp":"1586793600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"79.90",
                        "open":"78.97",
                        "low":"78.50",
                        "high":"81.36",
                        "amount":"5456",
                        "balance":"43592389.00",
                        "turnover_rate":"0.0088%",
                        "timestamp":"1586880000",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"79.87",
                        "open":"76.99",
                        "low":"76.99",
                        "high":"80.45",
                        "amount":"7000",
                        "balance":"55197999.00",
                        "turnover_rate":"0.0113%",
                        "timestamp":"1586966400",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"77.00",
                        "open":"80.30",
                        "low":"76.85",
                        "high":"81.47",
                        "amount":"5538",
                        "balance":"43596560.00",
                        "turnover_rate":"0.0089%",
                        "timestamp":"1587052800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"79.41",
                        "open":"77.85",
                        "low":"76.60",
                        "high":"82.57",
                        "amount":"5250",
                        "balance":"41742458.00",
                        "turnover_rate":"0.0085%",
                        "timestamp":"1587312000",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"77.78",
                        "open":"78.50",
                        "low":"74.52",
                        "high":"79.59",
                        "amount":"5979",
                        "balance":"46102164.00",
                        "turnover_rate":"0.0096%",
                        "timestamp":"1587398400",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"78.23",
                        "open":"77.20",
                        "low":"77.10",
                        "high":"78.50",
                        "amount":"3109",
                        "balance":"24230701.00",
                        "turnover_rate":"0.0050%",
                        "timestamp":"1587484800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"78.30",
                        "open":"78.26",
                        "low":"78.00",
                        "high":"81.10",
                        "amount":"6385",
                        "balance":"50915294.00",
                        "turnover_rate":"0.0103%",
                        "timestamp":"1587571200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"88.99",
                        "open":"80.80",
                        "low":"80.80",
                        "high":"89.60",
                        "amount":"19776",
                        "balance":"168805347.00",
                        "turnover_rate":"0.0319%",
                        "timestamp":"1587657600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"87.15",
                        "open":"88.01",
                        "low":"84.31",
                        "high":"88.45",
                        "amount":"10191",
                        "balance":"88615252.00",
                        "turnover_rate":"0.0164%",
                        "timestamp":"1587916800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"88.79",
                        "open":"87.10",
                        "low":"86.14",
                        "high":"91.88",
                        "amount":"10362",
                        "balance":"92328342.00",
                        "turnover_rate":"0.0167%",
                        "timestamp":"1588003200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"87.10",
                        "open":"88.02",
                        "low":"87.05",
                        "high":"89.88",
                        "amount":"6325",
                        "balance":"55759481.00",
                        "turnover_rate":"0.0102%",
                        "timestamp":"1588089600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"86.31",
                        "open":"88.16",
                        "low":"85.70",
                        "high":"88.30",
                        "amount":"6424",
                        "balance":"55753211.00",
                        "turnover_rate":"0.0104%",
                        "timestamp":"1588176000",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"89.88",
                        "open":"85.20",
                        "low":"84.03",
                        "high":"90.85",
                        "amount":"10413",
                        "balance":"89816623.00",
                        "turnover_rate":"0.0168%",
                        "timestamp":"1588694400",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"88.66",
                        "open":"89.00",
                        "low":"88.18",
                        "high":"92.22",
                        "amount":"7685",
                        "balance":"68755977.00",
                        "turnover_rate":"0.0124%",
                        "timestamp":"1588780800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"89.00",
                        "open":"89.33",
                        "low":"88.09",
                        "high":"89.89",
                        "amount":"4968",
                        "balance":"44153587.00",
                        "turnover_rate":"0.0080%",
                        "timestamp":"1588867200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"96.17",
                        "open":"89.32",
                        "low":"89.32",
                        "high":"96.47",
                        "amount":"11703",
                        "balance":"109356023.00",
                        "turnover_rate":"0.0189%",
                        "timestamp":"1589126400",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"100.36",
                        "open":"94.50",
                        "low":"94.25",
                        "high":"101.44",
                        "amount":"8769",
                        "balance":"86547405.00",
                        "turnover_rate":"0.0141%",
                        "timestamp":"1589212800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"102.35",
                        "open":"99.99",
                        "low":"98.60",
                        "high":"105.00",
                        "amount":"8038",
                        "balance":"81771132.00",
                        "turnover_rate":"0.0130%",
                        "timestamp":"1589299200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"103.00",
                        "open":"102.00",
                        "low":"100.80",
                        "high":"103.80",
                        "amount":"5294",
                        "balance":"54284011.00",
                        "turnover_rate":"0.0085%",
                        "timestamp":"1589385600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"100.36",
                        "open":"103.00",
                        "low":"99.73",
                        "high":"108.47",
                        "amount":"6547",
                        "balance":"67684014.00",
                        "turnover_rate":"0.0106%",
                        "timestamp":"1589472000",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"101.11",
                        "open":"99.80",
                        "low":"99.30",
                        "high":"103.80",
                        "amount":"5196",
                        "balance":"52819143.00",
                        "turnover_rate":"8380.6455%",
                        "timestamp":"1589731200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"105.51",
                        "open":"101.11",
                        "low":"100.75",
                        "high":"108.20",
                        "amount":"5534",
                        "balance":"57623785.00",
                        "turnover_rate":"8925.8066%",
                        "timestamp":"1589817600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"101.50",
                        "open":"105.52",
                        "low":"99.90",
                        "high":"109.78",
                        "amount":"7067",
                        "balance":"73828413.00",
                        "turnover_rate":"11398.3867%",
                        "timestamp":"1589904000",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"99.91",
                        "open":"101.95",
                        "low":"98.11",
                        "high":"103.79",
                        "amount":"8265",
                        "balance":"83080991.00",
                        "turnover_rate":"13330.6455%",
                        "timestamp":"1589990400",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"96.46",
                        "open":"99.53",
                        "low":"94.30",
                        "high":"100.57",
                        "amount":"7193",
                        "balance":"69746265.00",
                        "turnover_rate":"11601.6133%",
                        "timestamp":"1590076800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"99.30",
                        "open":"96.00",
                        "low":"94.68",
                        "high":"100.05",
                        "amount":"6393",
                        "balance":"62860563.00",
                        "turnover_rate":"0.0103%",
                        "timestamp":"1590336000",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"105.01",
                        "open":"100.00",
                        "low":"100.00",
                        "high":"105.45",
                        "amount":"6100",
                        "balance":"62622170.00",
                        "turnover_rate":"0.0098%",
                        "timestamp":"1590422400",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"103.83",
                        "open":"104.88",
                        "low":"102.60",
                        "high":"109.00",
                        "amount":"7504",
                        "balance":"79381908.00",
                        "turnover_rate":"0.0121%",
                        "timestamp":"1590508800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"104.42",
                        "open":"104.05",
                        "low":"101.41",
                        "high":"105.97",
                        "amount":"4114",
                        "balance":"42619130.00",
                        "turnover_rate":"0.0066%",
                        "timestamp":"1590595200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"115.27",
                        "open":"104.00",
                        "low":"104.00",
                        "high":"116.78",
                        "amount":"9270",
                        "balance":"103687634.00",
                        "turnover_rate":"0.0150%",
                        "timestamp":"1590681600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"116.51",
                        "open":"116.11",
                        "low":"115.00",
                        "high":"122.14",
                        "amount":"9165",
                        "balance":"107165392.00",
                        "turnover_rate":"0.0148%",
                        "timestamp":"1590940800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"117.67",
                        "open":"116.50",
                        "low":"114.17",
                        "high":"117.69",
                        "amount":"4886",
                        "balance":"56741146.00",
                        "turnover_rate":"0.0079%",
                        "timestamp":"1591027200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"124.29",
                        "open":"117.64",
                        "low":"116.02",
                        "high":"126.25",
                        "amount":"6924",
                        "balance":"84283737.00",
                        "turnover_rate":"0.0112%",
                        "timestamp":"1591113600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"124.90",
                        "open":"123.00",
                        "low":"121.97",
                        "high":"125.90",
                        "amount":"3775",
                        "balance":"46778707.00",
                        "turnover_rate":"0.0061%",
                        "timestamp":"1591200000",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"120.67",
                        "open":"125.38",
                        "low":"120.24",
                        "high":"133.32",
                        "amount":"8942",
                        "balance":"113022975.00",
                        "turnover_rate":"0.0144%",
                        "timestamp":"1591286400",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"110.70",
                        "open":"121.30",
                        "low":"110.11",
                        "high":"123.39",
                        "amount":"11118",
                        "balance":"129716202.00",
                        "turnover_rate":"0.0179%",
                        "timestamp":"1591545600",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"117.96",
                        "open":"111.20",
                        "low":"111.09",
                        "high":"118.41",
                        "amount":"9243",
                        "balance":"106725605.00",
                        "turnover_rate":"0.0149%",
                        "timestamp":"1591632000",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"118.19",
                        "open":"117.27",
                        "low":"115.22",
                        "high":"122.00",
                        "amount":"6923",
                        "balance":"81874204.00",
                        "turnover_rate":"0.0112%",
                        "timestamp":"1591718400",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"115.81",
                        "open":"118.97",
                        "low":"114.06",
                        "high":"118.98",
                        "amount":"5421",
                        "balance":"62902355.00",
                        "turnover_rate":"0.0087%",
                        "timestamp":"1591804800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"117.51",
                        "open":"113.69",
                        "low":"113.25",
                        "high":"120.86",
                        "amount":"6322",
                        "balance":"74454597.00",
                        "turnover_rate":"0.0102%",
                        "timestamp":"1591891200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"114.00",
                        "open":"118.72",
                        "low":"114.00",
                        "high":"119.58",
                        "amount":"8476",
                        "balance":"97661197.00",
                        "turnover_rate":"0.0137%",
                        "timestamp":"1592150400",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"119.40",
                        "open":"114.49",
                        "low":"113.68",
                        "high":"119.77",
                        "amount":"7145",
                        "balance":"83863332.00",
                        "turnover_rate":"0.0115%",
                        "timestamp":"1592236800",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    },
                    {
                        "close":"122.40",
                        "open":"119.21",
                        "low":"119.21",
                        "high":"123.87",
                        "amount":"5973",
                        "balance":"72549606.00",
                        "turnover_rate":"",
                        "timestamp":"1592323200",
                        "factor_a":"1.0000",
                        "factor_b":"0.000000"
                    }
            ]
close_list = []
zdf_list = []
for i in range(62):
    close_list.append(list1[i]['close'])


for b in close_list:
    zdf = ((float(b) / 69.12) - 1)*100
    zdf = round(zdf,2)

    zdf_list.append(zdf)

print(zdf_list)

