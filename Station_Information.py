from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

import json

from secretkey import key

import Search_TM as STM
import Search_Nearby_Station as SNS

def station_info(stationName_list):
    url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getMsrstnList'
    
    info_df = pd.DataFrame()

    for stationName in stationName_list:
        params3 = '?' + 'ServiceKey=' + key + '&' + \
        urlencode({ quote_plus('returnType') : 'json',
                    quote_plus('stationName') : stationName })
        #print(url + params3)

        request = Request(url + params3)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read()
    
        data = json.loads(response_body)
    
        si_df = pd.json_normalize(data['response']['body']['items'])

        info_df = info_df.append(si_df, ignore_index=True)

    info_df = info_df[['stationName', 'mangName', 'item', 'addr', 'year', 'dmX', 'dmY']]
    return info_df


if __name__ == '__main__':
    X, Y = SNS.select_TM()
    df = SNS.search_station(X, Y)
    station_list = list(df['stationName'])
    print(station_info(station_list))