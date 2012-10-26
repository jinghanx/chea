#! /usr/bin/env python

import redis
import xml.etree.ElementTree as ET
import os
import sys

from download_songs_from_xiami import decode

range1 = sys.argv[1]
range2 = sys.argv[2]
r = redis.Redis()
for file in os.listdir('/home/ubuntu/songs_xml'):
    index1 = file.find('_')
    index2 = file.find('.')
    index = int(file[index1+1:index2])
    if index >= int(range1) and index <= int(range2):
        print file
        tree = ET.parse('/home/ubuntu/songs_xml/'+file)
        root = tree.getroot()
        location_encoded = root[0][10].text
        location_decoded = decode(location_encoded)
        song_name = root[0][2].text.encode('utf-8')
        album_cover = root[0][6].text
        album_name = root[0][7].text.encode('utf-8')
        artist_name = root[0][9].text.encode('utf-8')

        if artist_name not in r.hvals('artists'):
            r.hset('artists', len(r.hkeys('artists')), artist_name)

        if album_name not in r.hvals(artist_name):
            r.hset(artist_name, len(r.hkeys(artist_name)), album_name)

        if song_name not in r.hvals(artist_name+':'+album_name):
            r.hset(artist_name+':'+album_name, len(r.hkeys(artist_name+':'+album_name)), song_name)

            r.hset(artist_name+':'+album_name+':'+song_name, 'play_times', 0)
            r.hset(artist_name+':'+album_name+':'+song_name, 'song_name', song_name)
            r.hset(artist_name+':'+album_name+':'+song_name, 'album_name', album_name)
            r.hset(artist_name+':'+album_name+':'+song_name, 'artist_name', artist_name)
            r.hset(artist_name+':'+album_name+':'+song_name, 'album_cover', album_cover)
            r.hset(artist_name+':'+album_name+':'+song_name, 'song_url', location_decoded)


