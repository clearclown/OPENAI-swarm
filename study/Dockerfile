# ベースイメージを指定
FROM jupyter/datascience-notebook:latest

# 作業ディレクトリを設定
WORKDIR /home/jovyan/work

# requirements.txt をコンテナにコピー
COPY requirements.txt .
COPY .env .

COPY . .

# Python パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install git+https://github.com/openai/swarm.git

# 環境変数を設定
ENV JUPYTER_ENABLE_LAB yes

# Jupyter Notebook を起動
CMD ["start-notebook.sh"]
