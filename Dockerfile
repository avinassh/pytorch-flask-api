FROM python:3.8

WORKDIR /docker_demo
 
ADD . .

RUN pip install -i https://mirrors.bfsu.edu.cn/pypi/web/simple/ -r requirements.txt

CMD ["python", "app.py"]
