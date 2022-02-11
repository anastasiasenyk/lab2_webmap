"""web_map, folium"""
import folium
import pandas as pd
import argparse
import math
# python main.py 2017 49.83826 24.02324 'locations_coordinate.csv'


def distance(row):
    latitude1, longitude1 = row[3], row[4]
    latitude2 = float(args.latitude)
    longitude2 = float(args.longitude)
    pre_dist = (math.sin((latitude2-latitude1)/2))**2 +\
               ((math.sin((longitude2-longitude1))/2)**2)*math.cos(latitude2)*math.cos(latitude1)
    dist = 6371 * 2 * math.atan2(math.sqrt(pre_dist), math.sqrt(1 - pre_dist))
    row[3] = dist
    return row[:4]


def find_10_films():
    file_films = pd.read_csv(args.path_to_dataset)
    data_films = []
    for index, row in file_films.iterrows():
        if row[2] == str(args.year) or row[2] == int(args.year):
            data_films.append(list(row)[1:])

    series_film = pd.Series(data_films)
    series_film = series_film.apply(distance)
    series_film = sorted(series_film, key=lambda x: x[3])
    return series_film[:10]

# def top_5_films():
#


def map_create():
    map = folium.Map(location=[49.817545, 24.023932],
                      zoom_start=17)
    map.save('Map_web.html')

    map.add_child(folium.Marker(location=[49.817545, 24.023932],
                                popup="Хіба я тут!",
                                icon=folium.Icon()))


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('year', help='year of the film')
        parser.add_argument('latitude', help='latitude (coordinates)')
        parser.add_argument('longitude', help='longitude (coordinates)')
        parser.add_argument('path_to_dataset', help='path to data_file with films')
        args = parser.parse_args()
        print(find_10_films())
    except Exception as e:
        print(e)
