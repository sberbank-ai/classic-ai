from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/ready')
def ready():
    return 'OK'


@app.route('/generate/<poet_id>', methods=['POST'])
def generate(poet_id):
    request_data = request.get_json()
    seed = request_data['seed']
    generated_poem = (
        'Ехал Грека через реку,\n'
        'Видит Грека - в реке рак.\n'
        'Сунул Грека руку в реку,\n'
        'Рак за руку Грека - цап!'
    )
    return jsonify({'poem': generated_poem})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)