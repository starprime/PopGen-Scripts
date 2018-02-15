#!/usr/bin/env python

import yaml
from subprocess import call

'''
data = dict(

    B = dict(
        C = 'c',
        D = 'd',
        E = 'e',
    ),
    A = 'a'
)

with open('data.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)

data="""\
 name: Vorlin Laruknuzum
 sex: Male
 class: Priest
 title: Acolyte
 hp: [32, 71]
 sp: [1, 13]
 gold: 423
 inventory:
 - a Holy Book of Prayers (Words of Wisdom)
 - an Azure Potion of Cure Light Wounds
 - a Silver Wand of Wonder
 """

j=0.00005
print type(j)
print yaml.dump({'name': "The Cloak 'Colluin'", 'depth': 0.05, 'rarity': 45,'weight': 10, 'cost': 50000, 'flags': ['INT', 'WIS', 'SPEED', 'STEALTH']})
'''
'''
import os

def get_config_file(path):
    for file in os.listdir(path):
        if file.endswith(".yaml"):
            print file
            return file

dir="/home/sumit/Desktop/Popgen-processing/ready/NewJersey/"
get_config_file(dir)


import ruamel.yaml
inp=open("configuration.yaml","r")
code = ruamel.yaml.load(inp, ruamel.yaml.RoundTripLoader)
print code
'''

'''
from popgen import Project
import os

#os.chdir('/home/sumit/Desktop/Popgen-Check-Run')
os.chdir('/')
#os.chdir('/home/sumit/Desktop/AWS/Connecticut/')
str="/home/sumit/Desktop/Popgen-processing/ready/NewJersey/#info.sumitkr@gmail.com#configuration_NewJersey.yaml"
#str="/home/sumit/Desktop/Popgen-Check-Run/NewJersey/#info.sumitkr@gmail.com#configuration_NewJersey.yaml"
#str="/home/sumit/Desktop/AWS/Connecticut/Connecticut/configuration_connecticut.yaml"
p=Project(str)
p.load_project()
p.run_scenarios()
'''

import time
import datetime
import fileDump,uploadToS3

#fileDump.make_zip('/home/sumit/Desktop/Popgen-processing/ready/Conneticut_SP','starMax')
#path=str('/home/sumit/Desktop/Popgen-processing/ready/Conneticut_SP')

#uploadToS3.create_path(path)

##file_name='#info.sumitkr@gmail.com#configuration_Conneticut_SP'
#email_id = str(file_name).split("#")
#email_id = email_id[1]
#print email_id
#import sendEmail

#sendEmail.send_success_Email('#info.sumitkr@gmail.com#configuration_Conneticut_SP.yaml-2017-12-25-21-26-15.zip','info.sumitkr@gmail.com')
import move_package
import ruamel.yaml
#fileOb = open('configuration.yaml', 'r')

#inp = file.read(fileOb)
#code = ruamel.yaml.load(inp, ruamel.yaml.RoundTripLoader)
#code['project']['synthesize'] = False
#print code['project']['synthesize']

import zipfile,os,sys

"""Zip the contents of an entire folder (with that folder included
in the archive). Empty subfolders will be included in the archive
as well.
"""

#file_name='/home/sumit/Desktop/Connecticut/file.zip'
#folder_path='/home/sumit/Desktop/Connecticut/2017-10-31 21-38-18 Connecticut TAZ Scenario'
import makeArchive

##makeArchive.make_zip(folder_path,output_path)

import boto3
import os
import sendEmail
# this method upload the file at given path to S3 bucket
import requests
import json

makeArchive.call_rest2(5,"Yaml-Error")
