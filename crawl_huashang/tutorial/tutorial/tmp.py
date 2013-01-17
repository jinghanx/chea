#! /usr/bin/env python
import os
file = 'huashang.csv'
with open(file, 'r') as f:
    for line in f:
        combo = line.split(',')
        city = combo[0]
        name_chinese = combo[1]
        name_english = combo[2]
        address = combo[3]
        number = combo[6]
        category_1 = combo[5].replace(' ', '_')
        category_2 = combo[4].replace(' ', '_')
        if category_1 not in os.listdir('huashang'):
            os.mkdir('huashang/'+category_1)
        with open('huashang/'+category_1+'/'+category_2+'.txt', 'a') as o:
            o.write(name_chinese+'\t'+name_english+'\t'+address+'\t'+city+'\t'+category_1+'\t'+category_2+'\n')
