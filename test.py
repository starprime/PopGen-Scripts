#!/usr/bin/env python

import yaml
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
path=str('/home/sumit/Desktop/Popgen-processing/ready/Conneticut_SP')

uploadToS3.create_path(path)