import os
from wsgiref.simple_server import make_server

from lightrest import app


if __name__ == '__main__':
    wsgi_app = app.VersionSelectorApplication()
    server = make_server('0.0.0.0', 8080, wsgi_app)
    server.serve_forever()
