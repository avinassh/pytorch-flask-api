import io
import json
import boto3
import argparse
import requests

from pathlib import Path
from PIL import Image


FILE = "data/images/ZR87WJ.jpeg"

with open(".aws/access_keys.json") as f:
    json_loaded = json.load(f)
    ACCESS_KEY = json_loaded["access_key"]
    SECRET_ACCESS_KEY = json_loaded["secret_access_key"]


def main(args):

    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_ACCESS_KEY,
    )
    client = session.client("s3", region_name="ap-northeast-2")
    client.upload_file(args.file, "flaskapitest11111", f"image/{Path(args.file).name}")
    print("Upload: ")
    print(f"{args.file} -> image/{Path(args.file).name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, default=FILE)
    args = parser.parse_args()
    main(args)
