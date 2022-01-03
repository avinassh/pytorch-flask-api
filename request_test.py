import io
import boto3
import argparse
import requests
from PIL import Image

ACCESS_KEY = "AKIAS7N4PKPROQAGJSVS"
SECRET_ACCESS_KEY = "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"


def main(args):
    resp = requests.post("http://localhost:5000/predict", params=vars(args))
    print(resp.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--obj_name")
    args = parser.parse_args()
    main(args)
