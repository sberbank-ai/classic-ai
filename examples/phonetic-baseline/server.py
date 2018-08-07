from flask import Flask, request, jsonify, abort

# Загрузка этого модуля занимает продолжительное время
# т.к. в нем загружаются корпуса текстов и модели
import phonetic_poet

app = Flask(__name__)


@app.route('/ready')
def ready():
    return 'OK'


@app.route('/generate/<poet_id>', methods=['POST'])
def generate(poet_id):
    request_data = request.get_json()
    seed = request_data['seed']
    try:
        generated_poem = phonetic_poet.generate_poem(seed, poet_id)
        return jsonify({'poem': generated_poem})
    except KeyError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
