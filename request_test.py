import argparse
import requests


def main(args):
    resp = requests.post(
        "http://localhost:5000/predict", files={"file": open(args.file, "rb")}
    )

    print(resp.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()
    main(args)
