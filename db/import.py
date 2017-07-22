import csv

import sqlite3 as sqlite


if __name__ == '__main__':
  data = csv.reader(open('import.csv', 'rb'), delimiter=',', quotechar='"')

  conn = sqlite.connect('db.sqlite')
  c = conn.cursor()

  i = 0
  for row in data:
    i += 1
    if i > 1:
      # print(row[1])
      c.execute("""INSERT INTO video
      (Title, Url, Length, Viewed, Timestamp, Tags, AddDate)
      VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (row[0].decode('utf-8'),
                 row[1].decode('utf-8'),
                 row[2].decode('utf-8'),
                 row[3].decode('utf-8'),
                 row[4].decode('utf-8'),
                 row[5].decode('utf-8'),

                 row[6]))

  conn.commit()
  c.close()
  conn.close()
