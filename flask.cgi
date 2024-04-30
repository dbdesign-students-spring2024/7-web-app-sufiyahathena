#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/sufiyahathena/Desktop/7-web-app-sufiyahathena/.venv/lib/python3.11/site-packages')
from wsgiref.handlers import CGIHandler
from app import app
CGIHandler().run(app)

