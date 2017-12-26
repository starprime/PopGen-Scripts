
import shutil
import os

def make_arhvive(path):
    print '## moving to Archive, this file',path

    file_name_st = str(path).split("/")
    file_name = file_name_st[len(file_name_st) - 1]

    op_path = '/home/sumit/Desktop/Popgen-processing/archive/' + file_name
    shutil.make_archive(op_path, 'zip', path)

def delete_file(path):
    print '## delete the folder',path
    shutil.rmtree(path)