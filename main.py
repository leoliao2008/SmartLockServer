from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def run_test():
    return jsonify(data='hello wordl')


def run_app():
    app.run('172.16.0.4',80)


if __name__ == '__main__':
    print('hello world.')
    run_app()
