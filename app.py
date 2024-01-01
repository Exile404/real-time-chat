from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

messages = []


@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@socketio.on('message')
def handle_message(data):
    username = data['username']
    message = data['message']
    file_data = data.get('file_data', None)
    file_name = data.get('file_name', '')
    file_type = data.get('file_type', '')

    if file_data:
        messages.append({
            'username': username,
            'message': message,
            'file_data': file_data,
            'file_name': file_name,
            'file_type': file_type
        })
    else:
        messages.append({'username': username, 'message': message})

    socketio.emit('update_messages', {'messages': messages})


# if __name__ == '__main__':
#     socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
