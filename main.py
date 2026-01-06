#!/usr/bin/env python3
"""
Minimalist Website - Flask Application
A simple, clean website with monospace fonts and minimalist design
"""

import os
import socket
from flask import Flask, render_template

app = Flask(__name__)


def find_free_port(start_port=5000, max_attempts=10):
    """Find a free port starting from start_port"""
    for i in range(max_attempts):
        port = start_port + i
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
    return start_port + max_attempts


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


if __name__ == '__main__':
    # Use PORT environment variable if set, otherwise find a free port
    port = int(os.environ.get('PORT', find_free_port(5000)))
    print(f"Starting server on port {port}")
    print(f"Open http://localhost:{port} in your browser")
    app.run(debug=True, host='0.0.0.0', port=port)

