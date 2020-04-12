import datetime
import json
import os
import socket
import sys

from flask import Flask, jsonify, request
from marshmallow import Schema, fields, post_load, exceptions as mm_ex

app = Flask(__name__)

const = {
    'host': os.environ.get('HOST', '0.0.0.0'),
    'port': os.environ.get('PORT', 8080),
    'version': os.environ.get('VERSION') if os.environ.get('VERSION') else 'unknown'
}

class MessageResponse():
    def __init__(self, message=''):
        self.message = message

class MessageResponseSchema(Schema):
    message = fields.Str()

class HealthResponse():
    def __init__(self, message='', status=200, **kwargs):
        self.message = message
        self.status = status
        self.hostname = socket.gethostname()

class HealthResponseSchema(Schema):
    message = fields.Str()
    status = fields.Int()
    hostname = fields.Str()

class VersionResponse():
    def __init__(self, message='', version=''):
        self.message = message
        self.version = version

class VersionResponseSchema(Schema):
    message = fields.Str()
    version = fields.Str()

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

def main():
    app.run(
        host=const['host'],
        port=const['port'],
        debug=True,
    )

if __name__ == '__main__':
    sys.exit(main())
