from flask import Flask, jsonify

app = Flask(__name__)

const = {
    'host': '0.0.0.0',
    'port': 8080,
    'version': 'v0.1.0'
}

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/health')
def health():
    return jsonify({'message': '', 'status': 200})

@app.route('/version')
def version():
    return jsonify({'message': '', 'vesion': const['version']})

def main():
    app.run(
        host=const['host'],
        port=const['port'],
        debug=True,
    )

if __name__ == '__main__':
    exit(main())
