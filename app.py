from flask import Flask, render_template, jsonify
from utils.temperature_sensor import get_temperature

app = Flask(__name__)

@app.route('/')
def dashboard():
    temperature = get_temperature()
    return render_template('dashboard.html', temperature=temperature)

@app.route('/api/temperature')
def api_temperature():
    temperature = get_temperature()
    return jsonify({'temperature': temperature})

if __name__ == '__main__':
    # 例：localhostのポート8080で起動
    app.run(debug=True, host='localhost', port=8080)