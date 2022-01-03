import os
from pathlib import Path

FILE = "data/images/i4SqIP.jpg"
OBJ_NAME = f"image/{Path(FILE).name}"

os.system(f"python upload_image.py --file {FILE}")
os.system(f"python request_test.py --obj_name {OBJ_NAME}")
