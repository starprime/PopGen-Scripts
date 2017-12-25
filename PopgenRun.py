#!/usr/bin/env python

import sys
from popgen import Project
import os,glob
import fileDump
import datetime


dir="/home/sumit/Desktop/Popgen-processing/process_log"
def get_config_file(path):
    for file in os.listdir(path):
        if file.endswith(".yaml"):
            print file
            return file

def worker(path):
    ## first get the exact name of the .yaml file
    file_name=get_config_file(path)
    poc = path.split("/")

    print "starting processing for ::",poc[len(poc) - 1]
    ## get the absolute path of config file
    configPath=path+'/'+file_name
    print 'configPath ##',configPath

    try:
        ## change directory to the root as i have given the absolute path
        os.chdir('/')

        p=Project(configPath)
        p.load_project()
        p.run_scenarios()
        fileDump.make_zip(path,file_name)
        fileDump.dropbox_up(path)

    except(Exception) as error:
        print 'error - ',error
        stuff=str(sys.stdout.flush())+str(error)

        fmt = '%Y-%m-%d-%H-%M-%S'
        timestamp= datetime.datetime.now().strftime(fmt)

        name=poc[len(poc) - 1]+str(timestamp)
        name = dir+"/error" + "/" +name+".txt"
        fh=open(name,"w")
        fh.write(str(stuff))
        fh.close()

    print "ending processing for ::",poc[len(poc) - 1]

