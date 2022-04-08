# 읍면동명을 입력하여 TM 좌표를 검색

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import pandas as pd

from xml.etree import ElementTree

from secretkey import key

import warnings
warnings.filterwarnings("ignore")

url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getTMStdrCrdnt'

def search_TM():
    umdName = input('읍면동명을 입력하세요: ')
    params3 = '?' + 'ServiceKey=' + key + '&' + \
    urlencode({ quote_plus('returnType') : 'xml',
                quote_plus('umdName') : umdName,
                quote_plus('ver') : '1.0' })
    #print(url + params3)

    request = Request(url + params3)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    root = ElementTree.fromstring(response_body)

    tm_df = pd.DataFrame()

    for item in root.iter('item'):
        tm_dict = {}
        if item.find('umdName').text == umdName:
            tm_dict['sidoName'] = item.find('sidoName').text
            tm_dict['sggName'] = item.find('sggName').text
            tm_dict['umdName'] = item.find('umdName').text
            tm_dict['tmX'] = float(item.find('tmX').text)
            tm_dict['tmY'] = float(item.find('tmY').text)
        tm_df = tm_df.append(tm_dict, ignore_index=True)
    
    if tm_df.empty:
        return print('검색 결과가 없습니다.')

    return tm_df

if __name__ == '__main__':
    print(search_TM())
