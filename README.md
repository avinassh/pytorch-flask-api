# PyTorch Flask API

This repo contains a sample code to show how to create a Flask API server by deploying our PyTorch model. This is a sample code which goes with [tutorial](https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html).

If you'd like to learn how to deploy to Heroku, then check [this repo](https://github.com/avinassh/pytorch-flask-api-heroku).

## Deploy with Docker

Build image

    docker build --network=host -t pytorch_flask:v0 .

Run Docker

    docker run --name pytorch_flask -p 5000:5000 -d pytorch_flask:v0

send the image file in a request:

    curl -X POST -F file=@cat_pic.jpeg http://localhost:5000/predict


## Benchmarking with Apache Bench

Remove Docker:

    docker stop pytorch_flask
    docker rm pytorch_flask

Run Benchmark Code:

    docker run --name pytorch_flask -p 5000:5000 -d pytorch_flask:v0 python benchmark.py

Benchmarking:

    ab -n 100 -c 10  http://localhost:5000/predict

## License

The mighty MIT license. Please check `LICENSE` for more details.

