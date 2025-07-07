# image_generator.py
import os
import time
from PIL import Image, ImageDraw

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WAIT_FLAG_PATH = os.path.join(BASE_DIR, 'state', 'wait_flag.txt')

def update_loop():
    while True:
        if os.path.exists(WAIT_FLAG_PATH):
            print("画像生成停止中：ボタンが押されるのを待っています")
            time.sleep(1)
            continue

        # 画像生成
        img = Image.new('RGB', (400, 300), color='black')
        current_time = time.strftime("%H:%M:%S")
        d = ImageDraw.Draw(img)
        d.text((10, 10), f"Now: {current_time}", fill='white')
        img.save(os.path.join(BASE_DIR, 'static/images/generated_image.jpg'))
        print("画像更新:", current_time)

        # ✅ フラグは作らない！再びループで続行（Flask側で制御）
        time.sleep(10)

if __name__ == '__main__':
    update_loop()
