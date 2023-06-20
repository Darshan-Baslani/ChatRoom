from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print("\nReceived message:", message)
    socketio.emit('message', message, namespace='/')

@socketio.on('connect')
def connect(connect):
    print("Connected to the Server.")

if __name__ == '__main__':
    socketio.run(app)
