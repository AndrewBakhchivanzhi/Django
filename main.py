from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_index(self):
        with open('bootstrap.html', 'r', encoding='UTF-8') as file:
            data = file.read()
        return data

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(self.__get_index(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    webServer.server_close()
    print("Server stopped.")
