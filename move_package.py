#!/usr/bin/env python
import shutil
from subprocess import call
import os

def zip(path):
    print path
    
    file_name_st=str(path).split("/")
    file_name=file_name_st[len(file_name_st)-1]
    os.chdir(path)
    op_path='/home/sumit/Desktop/AWS/'+file_name
    shutil.make_archive(op_path, 'zip', path)

    cmnd = 'tar -cvzf '+op_path+'.tar.gz'+' .'
    print cmnd
    call(cmnd, shell=True)

#zip('/home/sumit/Dropbox/PopGen/file/sumit/Conneticut_Run')
