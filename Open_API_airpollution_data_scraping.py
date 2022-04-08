# 한국환경공단 대기오염정보

# 한국환경공단_측정소정보
#(https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15073877)

import requests
from secretkey import key

url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getMsrstnList'

params ={'serviceKey' : key, 'returnType' : 'xml', 'numOfRows' : '100', 'pageNo' : '1', 'addr' : '서울', 'stationName' : '종로구' }

response = requests.get(url, params=params)
print(url)
print(response.content)
