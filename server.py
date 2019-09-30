#!/usr/bin/python3.7
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.routing import Rule,RuleRouter,PathMatches
from app import MyApplication

def main():
    IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    router = RuleRouter([
        Rule(PathMatches(r"/.*"),MyApplication())
    ])
    server = HTTPServer(router)
    server.listen(80)
    IOLoop.instance().start()

if __name__ == "__main__":
    main()
