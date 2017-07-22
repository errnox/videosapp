import sqlite3


if __name__ == '__main__':
  con = sqlite3.connect('db.sqlite')
  c = con.cursor()
  c.execute("""CREATE TABLE video
(
  Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  Title VARCHAR,
  Url VARCHAR,
  Length VARCHAR,
  Viewed BOOLEAN,
  Timestamp VARCHAR,
  Tags VARCHAR,
  AddDate DATETIME
);""")
  con.commit()
  c.close()
