import io
import json
import boto3

import requests
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request

# s3 = boto3.resource('s3', region_name='us-east-2')
# bucket = s3.Bucket('sentinel-s2-l1c')
# object = bucket.Object('tiles/10/S/DG/2015/12/7/0/B01.jp2')

# file_stream = io.StringIO()
# object.download_fileobj(file_stream)
# img = mpimg.imread(file_stream)
# # whatever you need to do

with open(".aws/access_keys.json") as f:
    json_loaded = json.load(f)
    ACCESS_KEY = json_loaded["access_key"]
    SECRET_ACCESS_KEY = json_loaded["secret_access_key"]


app = Flask(__name__)
imagenet_class_index = json.load(open("imagenet_class_index.json"))
model = models.densenet121(pretrained=True)
model.eval()

# s3 = boto3.resource("s3", region_name="ap-northeast-2")
# bucket = s3.Bucket("flaskapitest11111")


def read_image(bucket_name):
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_ACCESS_KEY,
    )
    s3 = session.resource("s3", region_name="ap-northeast-2")
    bucket = s3.Bucket("flaskapitest11111")
    object = bucket.Object(bucket_name)
    file_stream = io.BytesIO()
    object.download_fileobj(file_stream)

    return file_stream


def transform_image(image_bytes):
    my_transforms = transforms.Compose(
        [
            transforms.Resize(255),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )
    image = Image.open(image_bytes)
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        bucket_name = request.args.get("obj_name")
        file_stream = read_image(bucket_name)
        class_id, class_name = get_prediction(image_bytes=file_stream)
        return jsonify({"class_id": class_id, "class_name": class_name})


if __name__ == "__main__":
    app.run()
