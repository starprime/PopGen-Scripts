
import shutil
import zipfile
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

def make_zip(inp,op):
    output_path = op
    folder_path = inp
    parent_folder = os.path.dirname(folder_path)
    # Retrieve the paths of the folder contents.
    os.chdir(folder_path)
    contents = os.walk(folder_path)

    if True:
        zip_file = zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED, allowZip64=True)
        for root, folders, files in contents:
            # Include all subfolders, including empty ones.
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder + '\\',
                                                      '')
                #print "Adding '%s' to archive." % absolute_path
                #zip_file.write(absolute_path, relative_path)
                zip_file.write(folder_name)

            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(parent_folder + '\\',
                                                      '')
                #print "Adding '%s' to archive." % absolute_path
                #zip_file.write(absolute_path, relative_path)
                zip_file.write(file_name)

        print "'%s' created successfully." % output_path