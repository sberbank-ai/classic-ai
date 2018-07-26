from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/ready')
def ready():
    return 'OK'


@app.route('/generate/<poet_id>', methods=['POST'])
def generate(poet_id):
    request_data = request.get_json()
    seed = request_data['seed']
    generated_poem = 'Карл у Клары украл кораллы,\nКлара у Карла украла кларнет'
    return jsonify({'poem': generated_poem})


if __name__ == '__main__':
    app.run(port=8000)