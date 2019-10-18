#!/usr/bin/python3.7
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.routing import Rule,RuleRouter,PathMatches
from app import MyApplication
from pathlib import Path
import os

cert = Path(os.path.realpath(__file__)).parents[0]/'ssl/server.pem'
key = Path(os.path.realpath(__file__)).parents[0]/'ssl/server.key'

def main():
    IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    router = RuleRouter([
        Rule(PathMatches(r"/.*"),MyApplication())
    ])
    server = HTTPServer(router,ssl_options={
        "certfile": str(cert),
        "keyfile": str(key),
    })
    server.listen(443)
    IOLoop.instance().start()

if __name__ == "__main__":
    main()
