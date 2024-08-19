from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    send(message, broadcast=True)

@socketio.on('new_user')
def new_user(name):
    send(f'{name} entrou no chat.', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)