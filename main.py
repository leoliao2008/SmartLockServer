from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def run_test():
    return jsonify(data='hello wordl')


def run_app():
    app.run('193.112.61.174',8000)
    pass


if __name__ == '__main__':
    print('hello world.')
    run_app()
