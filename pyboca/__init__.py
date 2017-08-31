import requests
from pyquery import PyQuery

def _get_ch2en(name):
    payload ={"Submit":"翻　譯"}
    col = ["mrid", "maid", "mtid"]
    for i, t in enumerate(name):
        payload.update({col[i]:t})
    obca_url = 'http://www.boca.gov.tw/sp.asp?xdURL=E2C/c2102-5.asp&CtNode=677&mp=1'
    res = requests.post(obca_url, data=payload)
    S = PyQuery(res.text)
    multi_pin = {}
    ens = PyQuery(S("#AutoNumber2")[1])("td").map(lambda i, e:{PyQuery(e)('span')[0].text[:-1]:
                                                               PyQuery(e)('span')[-1].text})[1:]
    for en in ens:
        multi_pin.update(en)
    return multi_pin

def ch2en(name, encode="威妥瑪(WG)拼音"):
    multi_pin = _get_ch2en(name)
    if encode in multi_pin:
        return multi_pin[encode]
    else:
        print("Only support %s." %str(list(multi_pin.keys())))