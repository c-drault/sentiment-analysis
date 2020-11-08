FROM python:3.6-slim

WORKDIR /project
ADD . project

RUN  pip install -r project/requirements.txt

ENV NAME World

CMD ["python", "project/main.py"]
