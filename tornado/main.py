import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

if __name__ == "__main__":
    static_path = os.getcwd() + '/static'
    js_static_path = os.getcwd() + '/js'
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
        (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': js_static_path})
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
