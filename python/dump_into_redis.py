#! /usr/bin/env python

import redis
import xml.etree.ElementTree as ET
import os

r = redis.Redis()
index = 0
for file in list('songs_xml'):
    index += 1
    tree = ET.parse(file)
    root = tree.getroot()
    location_encoded = root[0][10].text
    location_decoded = decode(location_encoded)
    song_name = root[0][2].text
    album_cover = root[0][6].text
    album_name = root[0][7].text
    artist_name = root[0][9].text

    if artist_name not in r.hvals('artists'):
        r.hset('artists', len(r.hkeys('artists'), artist_name)

    if album_name not in r.hvals(artist_name):
        r.hset(artist_name, len(r.hkeys(artist_name)), album_name)

    if song_name not in r.hvals(artist_name+':'+album_name):
        r.hset(artist_name+':'+album_name, len(r.hkeys(artist_name+':'+album_name), song_name)

        r.hset(artist_name+':'+album_name+':'+song_name, 'play_times', 0)
        r.hset(artist_name+':'+album_name+':'+song_name, 'song_name', song_name)
        r.hset(artist_name+':'+album_name+':'+song_name, 'album_name', album_name)
        r.hset(artist_name+':'+album_name+':'+song_name, 'artist_name', artist_name)
        r.hset(artist_name+':'+album_name+':'+song_name, 'album_cover', album_cover)
        r.hset(artist_name+':'+album_name+':'+song_name, 'song_url', location_decoded)
