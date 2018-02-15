#!/usr/bin/env python

import zipfile
import os,shutil
import PopgenRun as PopgenRun
import multiprocessing

## root dirc
dir="/home/sumit/Desktop/Popgen-processing"
## here i will find .zip file
inDir=dir+"/in"
print inDir
allFold=os.listdir(inDir)
## got all file in "in" folder
print allFold
i=0
k=1
jobs=[]
## i can spawn two process only for now

while(i<k):
    fold=allFold[i]
    print fold
    path=dir+"/in/"+fold
    ## for one of the file in the IN folder
    ## extract zip content to ready folder
    zip_ref=zipfile.ZipFile(path,'r')
    ## creating seprate folder for each zip file
    filePath=dir+"/ready/"+fold
    ## extracting data into dedicated unzipped folder of the file
    filePath = filePath[:len(filePath) - 4]

    zip_ref.extractall(filePath)
    print "filePath",filePath
    os.remove(path)

    zip_ref.close()


    p=multiprocessing.Process(target=PopgenRun.worker,args=(filePath,))
    jobs.append(p)

    #p.daemon=True
    p.start()
    #p.join()
    i += 1




#pp=Project("")
#pp.load_project()
#pp.run_scenarios()