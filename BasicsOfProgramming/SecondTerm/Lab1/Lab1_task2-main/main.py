import folium
import pandas
import argparse
import re
import csv
from haversine import *
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from operator import itemgetter
from geopy.exc import GeocoderUnavailable

def delete_multiple_element(list_object, indices):
    """
    Deletes from list multiple indexes which are in list
    >>> delete_multiple_element([51, 52, 53, 54, 55, 56, 57, 58, 59], [4, 2, 6])
    [51, 52, 54, 56, 58, 59]
    """
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)

def convert_list_to_csv(path_to_data_set: str, year: int, user_latitude, user_longitude):
    """
    Converts the file with format list into a scv of ten the nearest to user points
    """
    with open(path_to_data_set) as f:
        list_of_lines = f.readlines()
    normal_list = []
    header = ["name", "year", "location", "latitude", "longitude", "distance"]
    for line in list_of_lines[14:414]:
        regex = re.compile(r'[\n\r\t]')
        line = regex.sub(" ", line)
        line = re.sub(r' {[^}]*}', '', line)
        nline = [z for y in line.split("(") for z in y.split(")")]
        if len(nline) > 3:
            del nline[-2]
            del nline[-1]
        norm_name_text = nline[0].replace('"', "").strip()
        nline[0] = norm_name_text
        try:
            norm_loc_tex = nline[2].replace('"', "").strip()
            del nline[2]
            nline.append(norm_loc_tex)
            normal_list.append(nline)
        except IndexError:
            None
    bad_year_indexes = []
    for yearr in normal_list:
        try:
            if int(yearr[1]) != year:
                bad_year_indexes.append(normal_list.index(yearr))
        except ValueError:
            bad_year_indexes.append(normal_list.index(yearr))
    delete_multiple_element(normal_list, bad_year_indexes)
    for film in normal_list:
        try:
            geolocator = Nominatim(user_agent="GeoFinder")
            geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.5)
            location = geolocator.geocode(film[-1])
            if location == None:
                del film[-1]
            else:
                tupple = (location.latitude, location.longitude)
                film.append(tupple[0])
                film.append(tupple[1])
        except GeocoderUnavailable:
            del film[-1]
    bad_len_indexes = []
    for ellem in normal_list:
        if len(ellem) != 5:
            bad_len_indexes.append(normal_list.index(ellem))
    delete_multiple_element(normal_list, bad_len_indexes)
    coord_tuple = (user_latitude, user_longitude)
    for coords in normal_list:
        try:
            distance = haversine(coord_tuple, (float(coords[-2]), float(coords[-1])))
            coords.append(distance)
        except ValueError:
            normal_list.remove(coords)
    normal_list = sorted(normal_list, key=itemgetter(-1))
    with open('films.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(normal_list[0:10])
    with open('all_films.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(normal_list)


def main():
    """
    Parses the parameters and generates the map
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('year', type=int)
    parser.add_argument('user_latitude', type=float)
    parser.add_argument('user_longitude', type=float)
    parser.add_argument('path_to_file', type=str)

    args = parser.parse_args()

    convert_list_to_csv(args.path_to_file, args.year, args.user_latitude, args.user_longitude)
    data = pandas.read_csv("films.csv")
    latitudee = data["latitude"]
    longiitude = data["longitude"]
    film_name = data['name']
    dataal = pandas.read_csv("all_films.csv")
    latitudee_all = dataal["latitude"]
    longiitude_all = dataal["longitude"]
    film_name_all = dataal['name']
    mapy = folium.Map(location=[args.user_latitude, args.user_longitude], zoom_start=10)
    fg = folium.FeatureGroup(name="Films_map")
    for latit, longi, namme in zip(latitudee, longiitude, film_name):
        fg.add_child(folium.Marker(location=(latit, longi), radius=10, popup=str(args.year) + "\n" + namme,\
icon=folium.Icon(color="red", icon="info-sign")))
    fg_al = folium.FeatureGroup(name="Films_map")
    for latit, longi, namme in zip(latitudee_all, longiitude_all, film_name_all):
        fg_al.add_child(folium.Marker(location=(latit, longi), radius=10, popup=str(args.year) + "\n" + namme, \
                                   icon=folium.Icon(color="blue", icon="info-sign")))
    fg_pp = folium.FeatureGroup(name="Population")
    fg_pp.add_child(folium.GeoJson(data=open('world.json', 'r',
                                             encoding='utf-8-sig').read(),
                                   style_function=lambda x: {'fillColor':
                                                                 'blue' if x['properties']['POP2005'] < 10000000
                                                                 else 'orange' if 10000000 <= x['properties'][
                                                                     'POP2005'] < 20000000
                                                                 else 'yellow'}))
    mapy.add_child(fg_al)
    mapy.add_child(fg_pp)
    mapy.add_child(fg)
    mapy.add_child(folium.LayerControl())
    mapy.save('Great_map.html')


if __name__ == '__main__':
    main()
