from webapp import app, routes, socketio

if __name__ == "__main__":
    socketio.run(app)