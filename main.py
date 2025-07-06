from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # 画像ファイル名を設定（必要に応じて変更）
    image_filename = 'generated_image.jpg'
    image_path = os.path.join('images', image_filename).replace('\\', '/')
    
    print("image_path:", image_path)
    
    return render_template('index.html', image_path=image_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
