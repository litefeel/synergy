#!/usr/bin/python3
#

import sys
from urllib.request import urlretrieve
import zipfile
import shutil

CORE_DIRNAME = "synergy-core"
ZIP_NAME = CORE_DIRNAME + ".zip"

URL = "https://codeload.github.com/litefeel/synergy-core/zip/"

def download(name):
    url = URL + name
    urlretrieve(url, ZIP_NAME)

def unzip(name):
    "unzip to synergy-core"
    zf = zipfile.ZipFile(ZIP_NAME)
    zf.extractall(".")

    if name.startswith('v'):
        name = name[1:]
    name = CORE_DIRNAME + '-' + name
    shutil.move(name, CORE_DIRNAME)

#------------- main -----------
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("download.py <tagname>", file=sys.stderr)
        sys.exit(1)
    print(sys.argv)
    download(sys.argv[1])
    unzip(sys.argv[1])
