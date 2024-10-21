# Dockerfile

# ベースイメージとしてpython:3.11-slimを使用
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt update && apt -y upgrade && apt -y install \
  sudo \
  curl \
  git \
  vim \
  nano \
  build-essential \
  libpq-dev

# ソースコードをコピー
COPY . .

# pipとpoetryをインストール
RUN pip install --upgrade pip && \
  pip install --no-cache-dir -r requirements.txt
