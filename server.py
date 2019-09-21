#!/usr/bin/python3.7
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.web import Application,StaticFileHandler,RequestHandler
from tornado.routing import Rule,RuleRouter,PathMatches
from pathlib import Path
import os

class MainHandler(RequestHandler):
    def get(self):
        self.render('index.html')

def make_app():
    site_path = Path(os.path.realpath(__file__)).parents[1]/'vue-mysite/dist'
    return Application([
        (r"/", MainHandler),
        (r"/(.*)", StaticFileHandler, {'path': str(site_path)})
    ],template_path = str(site_path))

def main():
    IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    router = RuleRouter([
        Rule(PathMatches(r"/.*"),make_app())
    ])
    server = HTTPServer(router)
    server.listen(80)
    IOLoop.instance().start()

if __name__ == "__main__":
    main()
