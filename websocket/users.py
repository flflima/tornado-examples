import json
import tornado.web
from tornado.ioloop import IOLoop

users = [
    {
        "id": 1,
        "nome": u"João"
    },
    {
        "id": 2,
        "nome": "Maria"
    }
]


class ListUsers(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):

        self.write(json.dumps(users))


class FindUser(tornado.web.RequestHandler):
    def get(self, id):
        for user in users:
            print("user[\"id\"] = %s" % user["id"])
            print("id = %s" % id)
            if user["id"] == int(id):
                self.write(json.dumps(user))
                break
        else:
            self.write("{}")


class AddUser(tornado.web.RequestHandler):
    def put(self, nome):
        id = len(users) + 1
        person = {
            "id": id,
            "nome": nome
        }
        users.append(person)

        self.write(json.dumps(users))


application = tornado.web.Application([
    (r"/list/users", ListUsers),
    (r"/list/user/([0-9]+)", FindUser),
    (r"/list/user/nome/([AZaz]+)", AddUser)
])

if __name__ == "__main__":
    application.listen(8888)
    IOLoop.instance().start()