'''import os
import logging
import time

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

li = os.listdir(
    '/home/saifullah/Desktop/Automatic-Resume-QA/Model/stackexchange')

comm = "7z x -y stackexchange/"

for i in range(1, len(li)):
    name = li[i]
    print("[INFO: EXTRACTION OF FILE", i, "-", name, "UNDER PROGRESS]")

    newname = li[i][:-3]
    os.system("mkdir " + newname)
    commTemp = comm + name + " -o" + newname
    os.system("cd " + newname)
    os.system(commTemp)
    os.system("cd ..")
    print("")

print("EVERYTHING OK, SUCCESSFULLY EXTRACTED ALL THE FILES!")
'''
import os
import glob
from pyunpack import Archive

for i, f in enumerate(glob.glob(os.path.join("/home/saifullah/Desktop/Automatic-Resume-QA/Model/stackexchange", "*.7z"))):
    dir_path = "/home/saifullah/Desktop/Automatic-Resume-QA/stackexchange/dataset" + \
        str(i+1)
    os.mkdir(dir_path)
    Archive(f).extractall(dir_path)
