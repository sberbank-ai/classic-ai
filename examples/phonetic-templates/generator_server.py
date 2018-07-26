from flask import Flask, request, jsonify

import model

app = Flask(__name__)


@app.route('/ready')
def ready():
    return 'OK'


@app.route('/generate/<poet_id>', methods=['POST'])
def generate(poet_id):
    request_data = request.get_json()
    seed = request_data['seed']
    generated_poem = model.generate_poem(poet_id, seed)
    return jsonify({'poem': generated_poem})


if __name__ == '__main__':
    app.run(port=8000)