from PIL import Image, ImageDraw
import time

def update_loop():
    while True:
        img = Image.new('RGB', (400, 300), color='black')
        d = ImageDraw.Draw(img)
        current_time = time.strftime("%H:%M:%S")
        d.text((10, 10), f"Now: {current_time}", fill='white')
        img.save('static/images/generated_image.jpg')
        print("画像更新:", current_time)
        time.sleep(10)  # 5秒おきに画像更新

if __name__ == '__main__':
    update_loop()
