#!/usr/bin/env python

import os
import time
processsDir='/home/sumit/Desktop/Popgen-processing'
tic=time.time()
fileName=processsDir+"/"+"test"+str(tic)
file_object  = open(fileName, 'w')
file_object.write(fileName)
file_object.close()