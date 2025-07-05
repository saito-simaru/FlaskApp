from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "これはPCからの情報です"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
