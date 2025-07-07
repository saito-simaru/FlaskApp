from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)
WAIT_FLAG_PATH = 'state/wait_flag.txt'

@app.route('/')
def index():
    # 画像ファイル名を設定（必要に応じて変更）
    image_filename = 'generated_image.jpg'
    image_path = os.path.join('images', image_filename).replace('\\', '/')
    
    print("image_path:", image_path)
    
    return render_template('index.html', image_path=image_path)

@app.route('/button_clicked', methods=['POST'])
def button_clicked():
    if os.path.exists(WAIT_FLAG_PATH):
        os.remove(WAIT_FLAG_PATH)  # フラグ削除で画像生成を再開
        return jsonify({'status': 'resumed'})
    return jsonify({'status': 'already_running'})

#Javascriptから叩くと画像ファイルの更新日時を返す
@app.route('/image_status')
def image_status():
    image_path = 'static/images/generated_image.jpg'
    if os.path.exists(image_path):
        timestamp = os.path.getmtime(image_path)
        return jsonify({'last_updated': timestamp})
    return jsonify({'error': 'Image not found'}), 404

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000)
    #デバッグモードにしておく
    app.run(debug=True)