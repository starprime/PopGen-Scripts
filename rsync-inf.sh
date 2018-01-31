#!/bin/bash
DIRC_WEBAPP="/home/sumit/Desktop/Popgen-webapp-inbound"
DIRC_PROCESSING_IN="/home/sumit/Desktop/Popgen-processing/in"
### rsync copied some large while without wait for them to copy from the source hence adding a delay
sleep 55
rsync --remove-source-files -avz  -e "ssh -i /home/sumit/popgen.pem" ubuntu@ec2-35-170-7-225.compute-1.amazonaws.com:/home/ubuntu/inbound/ /home/sumit/Desktop/Popgen-webapp-inbound/

if [ "$(ls -A $DIRC_WEBAPP)" ]; then
    /home/sumit/Desktop/scripts/./python-prime.py
fi

if [ "$(ls -A $DIRC_PROCESSING_IN)" ]; then
    /home/sumit/Desktop/scripts/./preProc.py
fi


