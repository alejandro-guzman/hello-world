import datetime

from flask import Flask, jsonify, request
from marshmallow import Schema, fields, post_load, exceptions as mm_ex

app = Flask(__name__)

const = {
    'host': '0.0.0.0',
    'port': 8080,
    'version': 'v0.1.0'
}

class MessageResponse():
    def __init__(self, message=''):
        self.message = message

class MessageResponseSchema(Schema):
    message = fields.Str()

class HealthResponse():
    def __init__(self, message='', status=200):
        self.message = message
        self.status = status

class HealthResponseSchema(Schema):
    message = fields.Str()
    status = fields.Int()

class VersionResponse():
    def __init__(self, message='', version=''):
        self.message = message
        self.version = version

class VersionResponseSchema(Schema):
    message = fields.Str()
    version = fields.Str()

class Echo():
    def __init__(self, echo):
        self.echo = f'Hello there, {echo}!'
        self.echo_at = datetime.datetime.now()

class EchoSchema(Schema):
    echo = fields.Str(required=True)
    echo_at = fields.DateTime()

    @post_load
    def make_echo(self, data, **kwargs):
        return Echo(**data)

@app.route('/')
def index():
    schema = MessageResponseSchema()
    message = MessageResponse('Hello, World!')
    return jsonify(schema.dump(message))

@app.route('/health')
def health():
    schema = HealthResponseSchema()
    health = HealthResponse()
    return jsonify(schema.dump(health))

@app.route('/version')
def version():
    schema = VersionResponseSchema()
    version = VersionResponse(version=const['version'])
    return jsonify(schema.dump(version))

@app.route('/echo', methods=['POST'])
def echo():
    schema = EchoSchema()
    try:
        echo = schema.load(request.get_json())
    except mm_ex.ValidationError as e:
        return jsonify(e.messages), 400
    return jsonify(schema.dump(echo))

def main():
    app.run(
        host=const['host'],
        port=const['port'],
        debug=True,
    )

if __name__ == '__main__':
    exit(main())
