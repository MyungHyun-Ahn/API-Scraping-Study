# 한국환경공단 대기오염정보

# 한국환경공단_측정소정보
#(https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15073877)

import requests
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import pandas as pd

from xml.etree import ElementTree


# .gitignore 파일에 추가하여 내 컴퓨터에서만 볼수있음.
from secretkey import key

decode_key = requests.utils.unquote(key)

url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getNearbyMsrstnList'

params2 = '?' + 'ServiceKey=' + key + '&' + \
urlencode({ quote_plus('returnType') : 'xml',
            quote_plus('tmX') : '244148.546388',
            quote_plus('tmY') : '412423.75772',
            quote_plus('ver') : '1.0' })
print(url + params2)

request = Request(url + params2)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()

print(response_body)

root = ElementTree.fromstring(response_body)

df = pd.DataFrame()

for item in root.iter('item'):
    
    item_dict = {}
    item_dict['tm'] = item.find('tm').text
    item_dict['stationName'] = item.find('stationName').text
    item_dict['addr'] = item.find('addr').text

    df = df.append(item_dict, ignore_index=True)

print(df)
