import socketio

sio = socketio.AsyncClient()

# @sio.event
# def connect():
#    print("connected")
# sio.emit("registrar_usuario", {"id":4})
# sio.connect("http://localhost:5000")
# sio.wait()  # noqa: F704


class Socket:
    def __init__(self, id):
        self.id = id

    async def connect_socket(self):
        """
        Establishes an asynchronous socket connection to the server.

        Attempts to:
        1. Connect to the socket server at http://127.0.0.1:5000
        2. Register the user with a predefined user ID
        3. Set up event listeners

        Handles connection exceptions silently.
        """

        try:
            # print("socket conectado")
            await sio.connect("http://127.0.0.1:5000", {"extraHeaders": {"id": self.id}})

            await sio.wait()
            await sio.on("enveto")

        except Exception:
            pass

    def start_socket(self):
        """
        Initializes the socket connection in a separate thread.

        Creates a daemon thread that runs the asynchronous socket connection method,
        preventing blocking of the main application thread.
        """
        from threading import Thread
        import asyncio

        def run():
            asyncio.run(self.connect_socket())
        Thread(target=run, daemon=True).start()


if __name__ == "__main__":
    socket = Socket(1)
    socket.start_socket()
