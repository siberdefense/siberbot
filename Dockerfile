FROM python:3.10.6

RUN apt-get update && apt-get install -y --no-install-recommends \
python3-setuptools \
python3-pip \
python3-dev \
python3-venv \
git \
libffi-dev \ 
libnacl-dev \
&& \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/bot/logs
WORKDIR /usr/src/bot

COPY requirements.txt /usr/src/bot/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENV DISCORD_BOT_TOKEN=REPLACE_ME

COPY siberbot.py /usr/src/bot/
COPY cogs/ /usr/src/bot/cogs/

CMD [ "python3", "siberbot.py" ]