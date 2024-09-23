import glob
import os
import shutil

os.makedirs("dist/config", exist_ok=True)

files = glob.iglob(os.path.join("src/keymon", "*.kbd"))
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, "dist/config/")

shutil.copytree("src/keymon/themes", "dist/config/themes", dirs_exist_ok=True)
