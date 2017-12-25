#!/usr/bin/env python
import shutil

def zip(path):
    print path
    #resultDirec = [f for f in os.listdir(path) if not os.path.isfile(os.path.join(path, f))]
    #print 'resultDirec',resultDirec

    shutil.make_archive(path, 'zip', path)

zip('/home/sumit/Dropbox/PopGen/file/sumit/Conneticut_Run')