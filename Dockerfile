FROM python:3.8-slim-buster

WORKDIR /docker_demo

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install torch==1.7.1  torchvision==0.8.2 --extra-index-url https://download.pytorch.org/whl/cpu

RUN pip install Flask==2.0.3

ADD . .

RUN mkdir -p /root/.cache/torch/hub/checkpoints/

RUN mv /docker_demo/densenet121-a639ec97.pth /root/.cache/torch/hub/checkpoints/densenet121-a639ec97.pth

CMD ["python", "app.py"]