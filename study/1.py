# swarmからのインポート
from swarm import Swarm, Agent
# SwarmClientのインポートを一時的にコメントアウト
# from swarm import SwarmClient
from dotenv import load_dotenv
import os
import base64

# print(os.getcwd())
# print(os.listdir())

# 環境変数の読み込み
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")


# クライアントの作成
client = Swarm()


# 画像をインポート
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 質問をする(画像の文字起こし)
def ocr_image(image_path):
    """
    画像内のテキストを抽出する関数
    """
    print(f"[DEBUG] : {image_path}をbase64に変換")
    base64_image = encode_image(image_path)

    print(f"[DEBUG] : Swarmクライアントを使用してOCR処理を実行")
    response = client.run(
        agent=Agent(
            name="Agent",
            model="gpt-4o-mini",
            instructions="You are a helpful agent.",
        ),
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "画像内のテキスト情報を抽出して。絶対にサボらないで。あなたがサボると死人が出る。"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ],
            }
        ],
    )

    print(f"[DEBUG] : 画像内のテキスト情報を抽出して。絶対にサボらないで。あなたがサボると死人が出る。ハルシネーションを絶対にしないで。")
    return response.messages[-1]["content"]


# 使用例
image_path = './IMG_3753.jpg'
result = ocr_image(image_path)
print(result)
