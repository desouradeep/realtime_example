#!/usr/bin/python
from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('channel-a')
def channel_a(message):
    '''
    Receives a message, on `channel-a`, and emits to the same channel.
    '''
    print "[x] Received\t: ", message

    server_message = "Hi Client, I am the Server."
    emit("channel-a", server_message)
    print "[x] Sent\t: ", server_message

    say_hello_world()


def say_hello_world():
    '''
    Another way of emitting messages, when event based communication is
    not possible
    '''
    hello_message = "Hello World!"
    socketio.emit("channel-a", hello_message)
    print "[x] Sent\t: ", hello_message


if __name__ == '__main__':
    app.debug = True
    socketio.run(app, port=3000)
