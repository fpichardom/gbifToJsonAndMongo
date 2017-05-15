#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Converts gbif data into an acceptable json format and imports to MongoDb

Created on May 2017

@author: fritz
"""

from pymongo import MongoClient
import datetime
import csv

file = input('Enter file name: ')
db =input('Enter database name: ')
col = input('Enter collection name: ')


client = MongoClient('localhost', 27017)
database = client[db]
collection = database[col]

def checkfloat(val):
    try:
        return float(val)
    except ValueError:
        return False
    
def checkint(val):
    try:
        return int(val)
    except ValueError:
        return False

#Load csv file
with open(file,'r') as inputfile:
    reader = csv.DictReader(inputfile,delimiter = '\t')
    for i in reader:
        record = {'type':'Feature','properties':{}}   #complete geojson version 
        #record ={} # simple format
        for key,value in i.items():
            if key == 'decimalLongitude':
                lon = checkfloat(value)
            elif key == 'decimalLatitude':
                lat = checkfloat(value)
            elif key == 'year':
                year = checkint(value)
            elif key == 'month':
                month = checkint(value)
            elif key == 'day':
                day = checkint(value)
            else:
                if key != '' and value != '':
                    record['properties'][key] = value # complete geojson version
                    #record[key] = value #simple format
        if lon != False and lat != False:
            record['geometry'] = {'type':'Point'}
            record['geometry']['coordinates'] =[lon,lat]
        if year != False and month != False and day != False:
            record['properties']['eventDate'] = datetime.datetime(year,month,day) # complete geojson
            #record['eventDate'] = datetime.datetime(year,month,day) # simple format
        collection.insert_one(record)
