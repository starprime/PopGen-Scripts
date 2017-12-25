#!/bin/bash

rsync -avz  -e "ssh -i /home/sumit/popgen.pem" ubuntu@ec2-54-198-81-249.compute-1.amazonaws.com:/home/ubuntu/inbound/ /home/sumit/Desktop/Popgen-webapp-inbound/

/home/sumit/Desktop/scripts/./python-prime.py 
##/home/sumit/Desktop/scripts/./Popgen-ghost.py



