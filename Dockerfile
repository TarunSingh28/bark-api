FROM ubuntu:20.04
COPY ./bark /bark
RUN apt-get -y update && \
apt-get -y install git && \
apt-get install -y python3 && \
apt-get install -y python3-pip
WORKDIR /bark
COPY ./requirements.txt /bark/requirements.txt
RUN pip install . --no-cache-dir
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]