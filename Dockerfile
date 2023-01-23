FROM python:3.8

WORKDIR /docker_demo
 
ADD . .

RUN mkdir -p /root/.cache/torch/hub/checkpoints/

RUN mv /docker_demo/densenet121-a639ec97.pth /root/.cache/torch/hub/checkpoints/densenet121-a639ec97.pth

RUN pip install -i https://mirrors.bfsu.edu.cn/pypi/web/simple/ -r requirements.txt

CMD ["python", "app.py"]