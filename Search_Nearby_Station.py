# 한국환경공단_근처_측정소_정보
#(https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15073877)

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import pandas as pd

import warnings

from xml.etree import ElementTree

import Search_TM as STM

warnings.filterwarnings("ignore")

# .gitignore 파일에 추가하여 내 컴퓨터에서만 볼수있음.
from secretkey import key

def select_TM():
    tm_df = STM.search_TM()

    print(tm_df)

    if len(tm_df.index) > 1:
        while True:
            sel = int(input('선택할 인덱스 번호를 입력해주세요 : '))
            if sel not in tm_df.index:
                print('잘못입력하셨습니다. 다시 입력해주세요.')
            else:
                tmX = tm_df.loc[sel, 'tmX']
                tmY = tm_df.loc[sel, 'tmY']
                break
        return tmX, tmY
    else:
        tmX = tm_df.loc[0, 'tmX']
        tmY = tm_df.loc[0, 'tmY']
        return tmX, tmY



def search_station(tmX, tmY):
    url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getNearbyMsrstnList'

    params2 = '?' + 'ServiceKey=' + key + '&' + \
    urlencode({ quote_plus('returnType') : 'xml',
                quote_plus('tmX') : tmX,
                quote_plus('tmY') : tmY })
    print(url + params2)

    request = Request(url + params2)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    root = ElementTree.fromstring(response_body)

    station_df = pd.DataFrame()

    for item in root.iter('item'):
    
        item_dict = {}
        item_dict['tm'] = item.find('tm').text
        item_dict['stationName'] = item.find('stationName').text
        item_dict['addr'] = item.find('addr').text

        station_df = station_df.append(item_dict, ignore_index=True)
    return station_df

if __name__ == '__main__':
    X, Y = select_TM()
    print(search_station(X, Y))