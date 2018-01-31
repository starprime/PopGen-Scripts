#!/usr/bin/env python

import dropbox ,sys,os
import dropbox.dropbox
import sys
import shutil
import datetime
import zipfile
import dropbox.auth
import makeArchive

access_token='cZ2_iMTY9dAAAAAAAAAAuBPJKocYhbgYAj7JIOpFwfyyMQ32qR_3MTGCXyRNiCNS'
APP_KEY='ru5yef94wjgc2k0'
APP_SECRET='wxdysx6enu1617e'
ACCESS_TYPE='Full'

'''

sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()
'''

rootDir="/home/sumit/Desktop/Popgen-processing"
proc_log=rootDir+"/process_log"
result=rootDir+"/results/Example_Input_Data"

'''    
    zipF=zipfile.ZipFile(zipPath+'.zip','w',zipfile.ZIP_DEFLATED)

    for files in os.listdir(zipPath):
        print files,'---'
        zipF.write(zipPath+"/"+files)
    zipF.close()
'''
uploaded_file=''

def make_archive(path,file_name):
    ## get all the folders only from the processing directory ...

    ### !! for this to work the file with job_name should be deleted
    fmt = '%Y-%m-%d-%H-%M-%S'
    timestamp = datetime.datetime.now().strftime(fmt)

    file_name=file_name.replace('.yaml','')

    file_name=file_name+'-'+str(timestamp)
    ## add time stamp to the file

    ## get the result directory folder
    resultDirec = [f for f in os.listdir(path) if not os.path.isfile(os.path.join(path, f))]

    ## get the actual path of the result directory
    resultDirec = str(resultDirec).split("/")
    actualPath = resultDirec[len(resultDirec) - 1]


    actualPath= path+'/'+actualPath.replace('[','').replace(']','').replace('\'','')
    newPath=path+'/'+file_name
    print 'actualPath',actualPath
    print 'newPath',newPath

    os.rename(actualPath,newPath)

    #shutil.make_archive(newPath, 'zip', newPath)
    op_file=path+'/'+file_name+'.zip'
    print 'op_file',op_file
    makeArchive.make_zip(newPath,op_file)
    shutil.rmtree(newPath)
    '''
    for f in os.listdir(newPath):
        zipPath = newPath + "/" + f
        print '##', zipPath
        shutil.make_archive(newPath, 'zip', newPath)
    '''

'''def dropbox_up(path):
    dbx=dropbox.Dropbox(access_token)
    print type(dbx)
    for file in os.listdir(path):
        if file.endswith(".zip"):
            dest_path = os.path.join('/SuperAwesomeResults', file)
            file_path = os.path.join(path, file)
            print file_path
            print dest_path

            try:
                with open(file_path,"rb") as  f:
                    urll=dbx.files_upload(f.read(),dest_path,mute=True)

                    print 'urll',type(urll)
            except Exception as err:
                print("Failed to upload %s\n%s" % (file, err))
'''