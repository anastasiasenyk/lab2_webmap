"""web_map, folium"""
import argparse
import math
import folium
import pandas as pd


def distance(row):
    """
    add to the list another element that will be equal
    to the distance between two pairs of coordinates
    use of the haversinus formula
    :param row: list
    :return: list
    >>> distance(['4Real',2007,'Peru',-6.8699697,-75.0458515])
    """
    latitude1, longitude1 = row[3] * math.pi/180, row[4] * math.pi / 180
    latitude2 = float(args.latitude) * math.pi/180
    longitude2 = float(args.longitude) * math.pi/180
    pre_dist = (math.sin((latitude2 - latitude1)/2)) ** 2 + \
               ((math.sin((longitude2 - longitude1))/2)**2)*math.cos(latitude2)*math.cos(latitude1)
    dist = 6371 * 2 * math.atan2(math.sqrt(pre_dist), math.sqrt(1 - pre_dist))
    row.append(dist)
    return row


def row_lenght(row):
    """
    return a list with an additional element equal to the
    fabs of the difference between the longitude coordinates
    :param row: list
    :return: list
    """
    longitude1 = float(row[4])
    short_dist = math.fabs(longitude1 - float(args.longitude))
    row.append(short_dist)
    return row


def find_10_films():
    """
    read from the movie database file and return the movies
    that were shot the specified year, which are closest to
    the coordinates
    :return: list
    """
    file_films = pd.read_csv(args.path_to_dataset)
    data_films = []
    for _, row in file_films.iterrows():
        if row[2] == str(args.year) or row[2] == int(args.year):
            data_films.append(list(row)[1:])

    series_film = pd.Series(data_films)
    series_film = series_film.apply(distance)
    series_film = sorted(series_film, key=lambda row: row[5])
    return series_film[:10]


def top_5_films():
    """
    the next 5 films to the given coordinates of all time
    :return: list
    """
    file_films = pd.read_csv(args.path_to_dataset)
    data_films = []
    for _, row in file_films.iterrows():
        data_films.append(list(row)[1:])
    series_film = pd.Series(data_films)
    series_film = series_film.apply(distance)
    series_film = sorted(series_film, key=lambda row: row[5])
    return series_film[:5]


def in_row():
    """
    top 10 films shot in later years than the specified year,
    and with the smallest deviation from the longitude
    of the specified coordinate
    :return: list
    """
    file_films = pd.read_csv(args.path_to_dataset)
    data_films = []
    for _, row in file_films.iterrows():
        if row[2] > int(args.year):
            data_films.append(list(row)[1:])
    series_film = pd.Series(data_films)
    series_film = series_film.apply(row_lenght)
    series_film = sorted(series_film, key=lambda row: row[5])
    return series_film[:10]


def map_create():
    """
    create a web map with four layers and
    different labels that correspond to the previous function
    :return: None
    """
    new_map = folium.Map(location=[args.latitude, args.longitude], zoom_start=3)

    folium.CircleMarker(location=[args.latitude, args.longitude], radius=4, popup='I am here!',
                        color='red', fill=True, fill_color='red').add_to(new_map)

    film_label = folium.FeatureGroup(name="top 10 for year")
    for film in find_10_films():
        film_label.add_child(folium.Marker(location=[film[3], film[4]], popup=film[0],
                                           icon=folium.Icon(color='orange', fill=True,
                                                            fill_color='orange')))

    film_near = folium.FeatureGroup(name="nearest 5 for all time")
    for film in top_5_films():
        film_near.add_child(folium.Marker(location=[film[3], film[4]], popup=film[0],
                                          icon=folium.Icon(color='purple', fill=True,
                                                           fill_color='purple')))

    film_row = folium.FeatureGroup(name="3 in row")
    for film in in_row():
        film_row.add_child(folium.Marker(location=[film[3], film[4]], popup=film[0],
                                         icon=folium.Icon(color='darkgreen', fill=True,
                                                          fill_color='darkgreen')))
    new_map.add_child(film_row)
    new_map.add_child(film_near)
    new_map.add_child(film_label)
    new_map.add_child(folium.LayerControl())
    new_map.save('Map_web.html')


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('year', help='year of the film')
        parser.add_argument('latitude', help='latitude (coordinates)')
        parser.add_argument('longitude', help='longitude (coordinates)')
        parser.add_argument('path_to_dataset', help='path to data_file with films')
        args = parser.parse_args()
        map_create()
    except PermissionError:
        print('error: Permission denied')
    except Exception as e:
        print(e)
