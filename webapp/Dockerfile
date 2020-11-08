FROM python:3.6-slim
COPY . /app
WORKDIR /app
RUN  pip install -r /app/requirements.txt && chmod a+x run.sh
CMD ["./run.sh"]
