from flask import Flask, jsonify, render_template
import os
import json

app = Flask(__name__)
WAIT_FLAG_PATH = 'state/wait_flag.txt'
EXTERNAL_JSON_PATH = 'state/external_status.json'
IMAGE_PATH = 'static/images/generated_image.jpg'

#最初に呼ばれる関数
@app.route('/')
def index():
    # # 画像ファイル名を設定（必要に応じて変更）
    # image_filename = 'generated_image.jpg'
    # image_path = os.path.join('images', image_filename).replace('\\', '/')
    
    # print("image_path:", image_path)
    # return render_template('index.html', image_path=image_path)

    return render_template('index.html')

#画像生成を開始させる
@app.route('/button_clicked', methods=['POST'])
def button_clicked():
    print("buttonが押された")
    if os.path.exists(WAIT_FLAG_PATH):
        os.remove(WAIT_FLAG_PATH)
        return jsonify({'status': 'resumed'})
    return jsonify({'status': 'already_running'})

#画像生成を止めるふぃあるを作成
@app.route('/create_flag', methods=['POST'])
def create_flag():
    print("画像生成を止める")
    with open(WAIT_FLAG_PATH, 'w') as f:
        f.write('wait')
    return jsonify({'status': 'flag_created'})

#〇✖をjsonfileを読み込んで判定
@app.route('/system_status')
def system_status():
    print("jsonfileを読み取る")
    EXTERNAL_JSON_PATH = 'state/external_status.json'
    if os.path.exists(EXTERNAL_JSON_PATH):
        with open(EXTERNAL_JSON_PATH, 'r') as f:
            status = json.load(f)
        return jsonify(status)
    return jsonify({'status': False})  # デフォルトはFalse

#Javascriptから叩くと画像ファイルの更新日時を返す
@app.route('/image_status')
def image_status():
    print("画像の更新時間をreturn")
    IMAGE_PATH = 'static/images/generated_image.jpg'
    if os.path.exists(IMAGE_PATH):
        timestamp = os.path.getmtime(IMAGE_PATH)
        return jsonify({'last_updated': timestamp})
    return jsonify({'error': 'Image not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #デバッグモードにしておく
    # app.run(debug=True)