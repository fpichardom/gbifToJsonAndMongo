#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May  13 2017
Takes the csv downloaded from gbif and formats it into geojson format
@author: fritz
"""

import json
import csv
import sys


# Set default encoding to utf-8

reload(sys)
sys.setdefaultencoding("utf-8")


#Load csv file
input_file = input('Enter file name/path: ')
output_file = input(' Enter output file name/path: ')
format = input('Pretty format y/n: ')
with open(input_file,'r') as inputfile, open(output_file,'w') as geojson:
    reader = csv.DictReader(inputfile,delimiter = '\t')
    #medio = list(reader)
    #termino =[]
    geojson.write('{ "type": "FeatureCollection", "features": [\n')
    first = True
    for i in reader:
        record = {'type':'Feature','properties':{},'geometry':{'type':'Point'}}
        
        for key,value in i.items():
            if key != '' and value != '':                
                if key == 'decimalLongitude':
                    lon = float(value)
                elif key == 'decimalLatitude':
                        lat = float(value)
                else:
                    record['properties'][key] = value
        record['geometry']['coordinates'] = [lon,lat]
        
        if format in ['y','yes','Y','Yes']:
            if first:
                geojson.write(json.dumps(record,indent=4,ensure_ascii=False))
                first = False
            else:
                geojson.write(',\n' + json.dumps(record,indent=4,ensure_ascii=False))  
        else:
            if first:
                geojson.write(json.dumps(record,ensure_ascii=False))
                first = False
            else:
                geojson.write(',\n' + json.dumps(record,ensure_ascii=False))        
       # out_json.write(json.dumps(record,ensure_ascii=False)+',\n')
    geojson.write(']}')           
    
    
    
# ,encoding="utf-8"
