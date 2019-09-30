from pyquery import PyQuery
from urllib.parse import urlparse,parse_qs
import urllib.request
import urllib.parse
import http.cookiejar

cookie_jar = http.cookiejar.CookieJar()
cookie_processor = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(cookie_processor)
opener.addheaders =[
  ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'),
  ('Referer','http://music.163.com/')
]

url_base = 'https://music.163.com/playlist?id={0}'
url_download = 'http://music.163.com/song/media/outer/url?id={0}.mp3'

def getSonglist(playlistId):
  f = opener.open(urllib.request.Request(url_base.format(playlistId)))
  html = f.read().decode('utf-8')
  doc = PyQuery(html)
  songs = doc('#song-list-pre-cache ul li a')
  song_arr = []
  for song in songs:
    el = PyQuery(song)
    parser = urlparse(el.attr('href'))
    id = parse_qs(parser.query).get('id')[0]
    song_arr.append({
      'url': url_download.format(id),
      'title': el.text()
    })
  return song_arr