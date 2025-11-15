FROM nikolaik/python-nodejs:python3.10-nodejs19

COPY . /app/

WORKDIR /app/

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg git wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
RUN cp sample.env .env

CMD bash start
