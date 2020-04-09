import datetime
import json

from flask import Flask, jsonify, request
from marshmallow import Schema, fields, post_load, exceptions as mm_ex

from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongo')
db = client['hello-world']

const = {
    'host': '0.0.0.0',
    'port': 8080,
    'version': 'v0.1.0'
}

# this breaks replicasets
# echos = []

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
    def __init__(self, echo, **kwargs):
        self.echo = f'Hello there, {echo}!'
        self.echo_at = datetime.datetime.now()

class EchoSchema(Schema):
    _id = fields.Inferred()
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

@app.route('/echo')
def echo():
    schema = EchoSchema()
    mschema = EchoSchema(many=True)

    echos = []
    for echo in list(db.echos.find()):
        echos.append(schema.load(echo))
    return jsonify(mschema.dump(echos))

@app.route('/echo', methods=['POST'])
def add_echo():
    schema = EchoSchema()
    try:
        echo = schema.load(request.get_json())
        echos = db.echos
        echos.insert_one(schema.dump(echo))
    except mm_ex.ValidationError as e:
        return jsonify(e.messages), 400
    return jsonify(schema.dump(echo)), 201

def main():
    app.run(
        host=const['host'],
        port=const['port'],
        debug=True,
    )

if __name__ == '__main__':
    exit(main())
