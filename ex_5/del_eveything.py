import os
import glob

folder_dir = os.path.join(os.path.dirname(__file__), "materials")

for i in glob.glob(os.path.join(folder_dir, "*.dat")):
    os.remove(i)

for i in glob.glob(os.path.join(folder_dir, "*.txt")):
    os.remove(i)

print("All .txt & .dat files in the folder have been deleted.")