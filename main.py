import datetime
import sqlite3
import sys
import urllib

import bottle


class WebApp(object):
  def __init__(self, app):
    self.app = app
    self.length_values = ['long', 'short']
    self.viewed_values = [1, 0]
    self.db_location = 'db/db.sqlite'
    self.pagination_limit = 10

  def get_index(self):
    return bottle.template('index.html.tpl')

  def get_static(self, filename):
    return bottle.static_file(filename, root='static/')

  def get_videos(self):
    limit = self.pagination_limit
    page = int(bottle.request.query.get('page') or 1)
    offset = page * limit - limit

    queries = {}
    query_keys = bottle.request.query.keys()
    for k in query_keys:
      print(k)
      if k.startswith('q_'):
        queries[k] = bottle.request.query.get(k)

    if len(queries.keys()) > 0:

      title = queries.get('q_title') or None
      url = queries.get('q_url') or None
      length = queries.get('q_length') or None
      viewed = queries.get('q_viewed') or None
      viewed =  int(viewed) if viewed != None else None
      timestamp = queries.get('q_timestamp') or None
      tags = queries.get('q_tags') or None
      add_date = queries.get('q_add_date') or None
      add_date =  int(add_date) if add_date != None else None
  
      a = []
      values = []
      if title:
        a.append('title LIKE ?')
        values.append('%{}%'.format(title))
      if url:
        a.append('url LIKE ?')
        values.append('%{}%'.format(url))
      if length and (length in self.length_values):
        a.append('length = ?')
        values.append(length)
      if viewed and (viewed in self.viewed_values):
        a.append('viewed = ?')
        values.append(viewed)
      if timestamp:
        a.append('timestamp LIKE ?')
        values.append('%{}%'.format(timestamp))
      if tags:
        a.append('tags LIKE ?')
        values.append('%{}%'.format(tags))
      if add_date:
        a.append('add_date = ?')
        values.append(add_date)
 
      s = 'SELECT * FROM video WHERE {} ORDER BY Id ASC LIMIT ? OFFSET ?'.format(
        ' AND '.join(a))
      count_s = 'SELECT COUNT(*) FROM video WHERE {}'.format(
        ' AND '.join(a))

      values += [limit, offset]

      conn = sqlite3.connect(self.db_location)
      c = conn.cursor()
      data = c.execute(s, values).fetchall()
      count = c.execute(count_s, values[:-2]).fetchone()[0]
      conn.commit()
      c.close()
      conn.close()

      query_string = urllib.urlencode(queries)

    else:

      conn = sqlite3.connect(self.db_location)
      c = conn.cursor()
      c.execute('SELECT * FROM video LIMIT ?, ?', (offset, limit))
      data = c.fetchall()
      count = c.execute('SELECT COUNT(*) FROM video').fetchone()[0]
      conn.commit()
      c.close()
      conn.close()

    videos = []
    date = None
    for row in data:
      date = datetime.datetime.fromtimestamp(row[7]).strftime(
        '%Y-%m-%d %H:%M:%S')
      videos.append(
        {
          'id': row[0],
          'title': row[1],
          'url': row[2],
          'length': row[3],
          'viewed': row[4],
          'timestamp': row[5],
          'tags': row[6],
          'add_date': date,
        }
      )

    query_string = urllib.urlencode(queries)

    meta = {'count': count, 'page': page, 'num_pages': count/limit,
            'limit': limit, 'query_string': query_string}
    return bottle.template("videos.html.tpl", videos=videos, meta=meta)

  def get_video(self, id):
    conn = sqlite3.connect(self.db_location)
    c = conn.cursor()
    c.execute('SELECT * FROM video WHERE Id = ?', [id])
    data = c.fetchall()[0]
    date = datetime.datetime.fromtimestamp(data[7]).strftime(
      '%Y-%m-%d %H:%M:%S')
    video = {
      'id': data[0],
      'title': data[1],
      'url': data[2],
      'length': data[3],
      'viewed': data[4],
      'timestamp': data[5],
      'tags': data[6],
      'add_date': date,
    }

    conn.commit()
    c.close()
    conn.close()

    return bottle.template('video.html.tpl', video=video)

  def get_video_new(self):
    return bottle.template('new_video.html.tpl')

  def post_video_new(self):
    title = bottle.request.forms.get('title')
    url = bottle.request.forms.get('url')
    length = bottle.request.forms.get('length')
    viewed = bottle.request.forms.get('viewed')
    timestamp = bottle.request.forms.get('timestamp')
    tags = bottle.request.forms.get('tags')
    add_date = datetime.datetime.now().strftime('%s')

    conn = sqlite3.connect(self.db_location)
    c = conn.cursor()
    c.execute("""INSERT INTO video
    (Title, Url, Length, Viewed, Timestamp, Tags, AddDate)
    VALUES (?, ?, ?, ?, ?, ?, ?)""",
              (title, url, length, viewed, timestamp, tags, add_date))
    conn.commit()
    id = c.lastrowid
    c.close()
    conn.close()
    bottle.redirect('/video/{}'.format(id))

  def post_video_delete(self):
    id = bottle.request.forms.get('id')
    conn = sqlite3.connect(self.db_location)
    c = conn.cursor()
    c.execute('DELETE FROM video WHERE Id = ?', [id])
    conn.commit()
    c.close()
    conn.close()
    bottle.redirect('/videos')

  def get_video_edit(self, id):
    conn = sqlite3.connect(self.db_location)
    c = conn.cursor()
    c.execute('SELECT * FROM video WHERE Id = ?', [id])
    data = c.fetchone()
    conn.commit()
    c.close()
    conn.close()
    video = {
      'id': data[0],
      'title': data[1],
      'url': data[2],
      'length': data[3],
      'viewed': data[4],
      'timestamp': data[5],
      'tags': data[6]
    }
    return bottle.template('edit_video.html.tpl', video=video)

  def post_video_edit(self):
    id = bottle.request.forms.get('id')
    title = bottle.request.forms.get('title')
    url = bottle.request.forms.get('url')
    length = bottle.request.forms.get('length')
    viewed = bottle.request.forms.get('viewed')
    timestamp = bottle.request.forms.get('timestamp')
    tags = bottle.request.forms.get('tags')

    conn = sqlite3.connect(self.db_location)
    c = conn.cursor()
    c.execute("""UPDATE video
    SET Title=?, Url=?, Length=?, Viewed=?, Timestamp=?, Tags=?)
    WHERE Id = ?""",
              (title, url, length, viewed, timestamp, tags, id))
    conn.commit()
    c.close()
    conn.close()
    bottle.redirect('/video/{}'.format(id))

  def post_video_search(self):
    title = bottle.request.forms.get('title') or None
    url = bottle.request.forms.get('url') or None
    length = bottle.request.forms.get('length') or None
    viewed = bottle.request.forms.get('viewed') or None
    viewed =  int(viewed) if viewed != None else None
    timestamp = bottle.request.forms.get('timestamp') or None
    tags = bottle.request.forms.get('tags') or None
    add_date = bottle.request.forms.get('add_date') or None
    add_date =  int(add_date) if add_date != None else None

    a = []
    query_pairs = {}
    if title:
      a.append('title LIKE ?')
      query_pairs['q_title'] = title
    if url:
      a.append('url LIKE ?')
      query_pairs['q_url'] = url
    if length and (length in self.length_values):
      a.append('length = ?')
      query_pairs['q_length'] = length
    if viewed and (viewed in self.viewed_values):
      a.append('viewed = ?')
      query_pairs['q_viewed'] = viewed
    if timestamp:
      a.append('timestamp LIKE ?')
      query_pairs['q_timestamp'] = timestamp
    if tags:
      a.append('tags LIKE ?')
      query_pairs['q_tags'] = tags
    if add_date:
      a.append('add_date = ?')
      query_pairs['q_add_date'] = add_date

    s = 'SELECT * FROM video WHERE {}'.format(' AND '.join(a))

    query_string = urllib.urlencode(query_pairs)

    bottle.redirect('/videos?{}'.format(query_string))

  def get_video_search(self):
    return bottle.template('search_videos.html.tpl')

  def get_exit(self):
    sys.stderr.close()

if __name__ == '__main__':
  app = bottle.default_app()
  web_app = WebApp(app)

  app.get('/static/<filename:path>',
          callback=web_app.get_static,
          name='get_static')

  app.get('/',
          callback=web_app.get_index,
          name='get_index')

  app.get(['/videos', '/videos/'],
          callback=web_app.get_videos,
          name='get_videos')

  app.get(['/video/<id:int>', '/video/<id:int>/'],
          callback=web_app.get_video,
          name='get_video')
  app.post(['/video', '/video/', ],
           callback=web_app.post_video_new,
           name='post_video_new')
  app.get(['/video/new', '/video/new/', ],
          callback=web_app.get_video_new,
          name='get_video_new')
  app.get(['/video/<id:int>/edit', '/video/<id:int>/edit/', ],
          callback=web_app.get_video_edit,
          name='get_video_edit')
  app.post(['/video/delete', '/video/delete/', ],
           callback=web_app.post_video_delete,
           name='post_video_delete')
  app.post(['/video/edit', '/video/edit/', ],
           callback=web_app.post_video_edit,
           name='post_video_edit')
  app.get(['/videos/search', '/videos/search/'],
          callback=web_app.get_video_search,
          name='get_video_search')
  app.post(['/videos/search', '/videos/search/'],
           callback=web_app.post_video_search,
           name='post_video_search')
  app.get(['/exit', '/exit'],
          callback=web_app.get_exit,
          name='get_exit')

  app.run(host='localhost', port=4321, debug=True, reloader=True)
