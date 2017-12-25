#!/usr/bin/env python

import os
import shutil
import docker
rootdir = '/home/sumit/Desktop/Popgen-webapp-inbound'
processsDir='/home/sumit/Desktop/Popgen-processing/in'

##for dir in os.listdir(rootdir):
    ##print [os.curdir, os.pardir] + os.listdir(path)
print os.listdir(rootdir)

allFold=os.listdir(rootdir)
## !!! move fle from Popgen Processing to In Directory
for fold in allFold:
    print rootdir+'/'+fold
    chldDir=rootdir+'/'+fold
    ## copy all files from Popgen-webapp-inboundn to -->> Popgen-processing
    shutil.move(chldDir,processsDir)
    #print os.listdir(chldDir)

#for subdir, dirs, files in os.walk(rootdir):
    #for dirs in dirs:
        #print os.path.join(subdir, dirs)


'''
import os

for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        print(os.path.join(dirname, filename))

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')
'''