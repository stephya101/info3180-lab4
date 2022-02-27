import os

def get_uploaded_image():
    rootdir = os.getcwd()
    print (rootdir)
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            print (os.path.join(subdir, file))