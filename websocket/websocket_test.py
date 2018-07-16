from datetime import date
import tornado.web


class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = {'version': '3.5.1',
                    'last_build': date.today().isoformat()}
        self.write(response)
        # self.render("template.html")


class GetGameByIdHandler(tornado.web.RequestHandler):
    def get(self, id):
        response = {'id': int(id),
                    'name': 'Crazy Game',
                    'release_date': date.today().isoformat()}
        self.write(response)


class MyPost(tornado.web.RequestHandler):
    def initialize(self):
        print("Initializing...")

    def post(self, id):
        response = {'post_id': int(id)}
        self.write(response)

    def put(self, id):
        response = {'pu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            t_id': int(id)}
        self.write(response)

    def delete(self, id):
        response = {'delete_id': int(id)}
        self.write(response)


application = tornado.web.Application([
    (r"/getgamebyid/([0-9]+)", GetGameByIdHandler),
    (r"/version", VersionHandler),
    (r"/posting/([0-9]+)", MyPost)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()