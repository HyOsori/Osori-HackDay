import tornado.web
import tornado.websocket


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return None


class DefaultHandler(BaseHandler):
    def get(self):
    	self.render("index_dev.html")


class ApiHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args, **kwargs):
        self.write('websocket is opened'.decode())
    
    def on_message(self, message):
        self.write('websocket send message OK'.decode())

    def on_close(self):
        pass


