from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    print("SERVER STARTED")
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print("SOCKET CONNECTED")

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: '+ str(json))

if __name__ == '__main__':
    socketio.run(app)