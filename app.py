from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

messages = []

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('send_message')
def handle_message(message):
    messages.append(message)
    emit('message', message, broadcast=True)

    @socketio.on('clear_messages')
    def handle_clear_messages():
        messages.clear()
    emit('message', "Histórico limpo!", broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
