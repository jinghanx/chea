#! /usr/bin/env python
import sys
import mechanize
import cookielib
import time
import os
import urllib
import math
import xml.etree.ElementTree as ET
from urllib import unquote

def decode(url_encoded):
    loc_2 = int(url_encoded[0])
    loc_3 = url_encoded[1:]
    loc_4 = int(math.floor(len(loc_3) / loc_2))
    loc_5 = len(loc_3) % loc_2
    loc_6 = dict()
    loc_7 = 0
    loc_8 = ''
    loc_9 = ''
    loc_10 = ''
    while loc_7 < loc_5:
        left = (loc_4+1)*loc_7
        right = left + loc_4+1
        loc_6[loc_7] = loc_3[left:right]
        loc_7 += 1
    loc_7 = loc_5
    while loc_7 < loc_2:
        left = loc_4 * (loc_7 - loc_5) + (loc_4 + 1) * loc_5
        right = left + loc_4
        loc_6[loc_7] = loc_3[left:right]
        loc_7 += 1
    loc_7 = 0
    while loc_7 < len(loc_6[0]):
        loc_10 = 0
        while loc_10 < len(loc_6):
            if not (loc_10 >= loc_5 and loc_7 == len(loc_6[0]) - 1):
                loc_8 += loc_6[loc_10][loc_7]
            loc_10 += 1
        loc_7 += 1
    loc_9 = unquote(loc_8).replace('^', str(0))
    return loc_9

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

for index in range(1600, 10000):
    if 'song_%d.xml' % index not in os.listdir('/home/ubuntu/songs_xml'):
        os.system('curl http://data.xiami.com/widget/xml-single/uid/0/sid/%d > /home/ubuntu/songs_xml/song_%d.xml' % (index, index))
    #try:
    #    tree = ET.parse('/home/ubuntu/songs_xml/song_%d.xml' % index)
    #    root = tree.getroot()
    #    location_encoded = root[0][10].text
    #    song_name = root[0][2].text
    #    album_name = root[0][7].text
    #    artist_name = root[0][9].text
    #    album_name = album_name.replace(' ', '_')
    #    artist_name = artist_name.replace(' ', '_')
    #    print 'url:', location_encoded, 'artist:', artist_name, 'album:', album_name, 'song:', song_name
    #    location_decoded = decode(location_encoded)
    #    print 'url_decoded: ', location_decoded
    #    if artist_name.encode('utf-8') not in os.listdir('/home/ubuntu/songs'):
    #        os.system(('mkdir /home/ubuntu/songs/%s' % artist_name).encode('utf-8'))
    #    if album_name.encode('utf-8') not in os.listdir(('/home/ubuntu/songs/%s' % artist_name).encode('utf-8')):
    #        os.system(('mkdir /home/ubuntu/songs/%s/%s' % (artist_name, album_name)).encode('utf-8'))
    #    #response = urllib.urlopen(location_decoded)
    #    response = br.open(location_decoded)
    #    html = response.read()
    #    song_file = open(('/home/ubuntu/songs/%s/%s/%s.mp3' % (artist_name, album_name, song_name)).encode('utf-8'), 'w')
    #    song_file.write(html)
    #    #os.system(('curl %s > /home/ubuntu/songs/%s/%s/%s.mp3' % (location_decoded, artist_name, album_name, song_name)).encode('utf-8'))
    #except:
    #    continue
