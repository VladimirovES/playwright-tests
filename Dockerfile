FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y \
    wget \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxcb1 \
    libxkbcommon0 \
    libatspi2.0-0 \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /playwright-tests/
COPY ./ /playwright-tests/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install pip==22.1.2 && pip install wheel && pip install --upgrade wheel \
    && pip install --upgrade cython \
    && pip install coincurve  \
    && pip install --upgrade setuptools \
    && pip install -r requirements.txt

RUN playwright install
