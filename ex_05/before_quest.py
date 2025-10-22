import os
import glob

folder_dir = os.path.join(os.path.dirname(__file__), "materials")

def createFile():
    for i in range(10):

        filename = os.path.join(folder_dir, "tmp_%04d.txt" % i)
        o = open(filename, "w")
        o.close

file_number = 0

def renameFile():
    global file_number

    for i in glob.glob(os.path.join(folder_dir, "tmp_*.txt")):
        os.rename(i, os.path.join(folder_dir, "t_%04d.dat" % file_number))
        file_number += 1


createFile()
input("Press Anything to Break Wiatting...")
renameFile()