from tornado.web import Application,StaticFileHandler,RequestHandler
from pathlib import Path
from utils import songs
import os,json

class MainHandler(RequestHandler):
  def get(self):
    self.render('index.html')

class SongsHandler(RequestHandler):
  def get(self):
    playlistId = self.get_query_argument('playlist')
    arr = songs.getSonglist(playlistId)
    self.set_header('Content-Type','application/json;charset=utf-8')
    self.write(json.dumps(arr,ensure_ascii = False))

class MyApplication(Application):
  def __init__(self):
    site_path = Path(os.path.realpath(__file__)).parents[1]/'vue-mysite/dist'
    handlers = [
      (r"/", MainHandler),
      (r"/songs", SongsHandler),
      (r"/(.*)", StaticFileHandler, {'path': str(site_path)})
    ]
    settings = {
      'template_path' : str(site_path)
    }
    super().__init__(handlers, **settings)