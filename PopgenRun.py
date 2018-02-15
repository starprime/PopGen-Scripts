#!/usr/bin/env python

import sys
from popgen import Project
import os,glob,shutil
import fileDump,uploadToS3,sendEmail,makeArchive
import datetime
from subprocess import call


dir="/home/sumit/Desktop/Popgen-processing/process_log"
def get_config_file(path):
    for file in os.listdir(path):
        if file.endswith(".yaml"):

            print file
            return file
####        ('Submitted', 'Submitted'),('Yaml-Error', 'Yaml-Error'), ('System-Error', 'System-Error'),('Completed', 'Completed'),('In-Progress', 'In-Progress'),)

def worker(path):
    ## first get the exact name of the .yaml file
    file_name=get_config_file(path)
    poc = path.split("/")

    file_arr = str(file_name).split("#")
    email_id = file_arr[1]
    jobid=file_arr[2]

    ## Calling REST API to update status
    makeArchive.call_rest2(jobid,'In-Progress')

    print "starting processing for ::",poc[len(poc) - 1]
    ## get the absolute path of config file
    configPath=path+'/'+file_name
    print 'configPath ##',configPath

    try:
        ## change directory to the root as i have given the absolute path
        os.chdir('/')

        p=Project(configPath)
        print ' ## Load Project'
        p.load_project()
        print ' ## Run Scenerios '
        p.run_scenarios()
        print '## make zip of the output folder'
        fileDump.make_archive(path,file_name)
        print '## uploading file to S3'
        uploaded_file=uploadToS3.create_path(path,email_id)
        print '## Sending Email'
        op_path = '/home/sumit/Desktop/Popgen-processing/archive/'+'{{ARCHIVE}}'+file_name+'.zip'
        print 'archive path',op_path
        makeArchive.make_zip(path,op_path)
        makeArchive.delete_file(path)

        makeArchive.call_rest3(jobid,'Completed',uploaded_file)


    except(Exception) as error:
        shutil.copy(configPath, dir+"/error/")

        makeArchive.call_rest2(jobid, 'Yaml-Error')

        print 'error - ',error
        stuff=str(sys.stdout.flush())+str(error)

        fmt = '%Y-%m-%d-%H-%M-%S'
        timestamp= datetime.datetime.now().strftime(fmt)

        name=poc[len(poc) - 1]+str(timestamp)
        name = dir+"/error" + "/" +name+".txt"
        fh=open(name,"w")
        fh.write(str(stuff))
        fh.close()
        sendEmail.send_Error_Email(name,email_id)
        makeArchive.delete_file(path)


    print "ending processing for ::",poc[len(poc) - 1]

