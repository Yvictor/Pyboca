"""Pyboca
外交部中文名字轉拼音
"""

__version__ = "1.0"

import requests
from pyquery import PyQuery


def _get_ch2en(name):
    payload = {
        "SN": name,
        "sound": 2,
    }
    url = "https://crptransfer.moe.gov.tw/index.jsp"
    res = requests.get(url, params=payload)
    S = PyQuery(res.text)
    cols = [row.text for row in S(".result th")][2:]
    rows = [
        ",".join(r)
        for r in zip(
            [row.text.upper() for row in S(".result td span")][2::2],
            [row.text.upper().replace(" ", "-") for row in S(".result td span")][3::2],
        )
    ]
    multi_pin = {k: v for k, v in zip(cols, rows)}
    return multi_pin


def ch2en(name, encode="威妥瑪拼音"):
    multi_pin = _get_ch2en(name)
    if encode in multi_pin:
        return multi_pin[encode]
    else:
        print("Only support %s." % str(list(multi_pin.keys())))
