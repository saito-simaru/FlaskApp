# image_generator.py
import os
import time
from PIL import Image, ImageDraw

WAIT_FLAG_PATH = 'state/wait_flag.txt'

def update_loop():
    while True:
        # フラグファイルが存在するなら待機
        if os.path.exists(WAIT_FLAG_PATH):
            print("画像生成停止中：ボタンが押されるのを待っています")
            time.sleep(1)
            continue

        # 画像生成
        img = Image.new('RGB', (400, 300), color='black')
        current_time = time.strftime("%H:%M:%S")
        d = ImageDraw.Draw(img)
        d.text((10, 10), f"Now: {current_time}", fill='white')
        img.save('static/images/generated_image.jpg')
        print("画像更新:", current_time)

        # フラグファイルを作成して「停止」状態に
        with open(WAIT_FLAG_PATH, 'w') as f:
            f.write('wait')

        # ループは1秒ずつチェックしながら待つ
        time.sleep(1)

if __name__ == '__main__':
    update_loop()
