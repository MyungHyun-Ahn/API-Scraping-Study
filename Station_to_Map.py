import folium
import Station_Information as si
import Search_Nearby_Station as ns

def si_to_map(df):
    x_sum = 0
    y_sum = 0

    for i in range(df.shape[0]):
        x_sum = x_sum + float(df.loc[i, 'dmX'])
        y_sum = y_sum + float(df.loc[i, 'dmY'])

    x = x_sum / df.shape[0]    
    y = y_sum / df.shape[0] 

    map = folium.Map(location=[x, y], zoom_start=13)
    
    for i in range(df.shape[0]):
        marker = folium.Marker([df.loc[i, 'dmX'], df.loc[i, 'dmY']], popup=df.loc[i, 'stationName']+' 측정소', icon=folium.Icon(color='red'))
        marker.add_to(map)

    map.save('html/map.html')


if __name__ == '__main__':
    X, Y = ns.select_TM()
    df = ns.search_station(X, Y)
    station_list = list(df['stationName'])
    si_df = si.station_info(station_list)
    print(si_df)
    si_to_map(si_df)
