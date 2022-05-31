from os import symlink
import numpy as np
from PIL import Image

import sys 

if len(sys.argv) > 1:
    s = Image.open(sys.argv[1])
    s = s.resize((256,256))
    s.save(sys.argv[1])
    print("Image saved")
else:
    print("Please provide the file path")
    exit(1)


