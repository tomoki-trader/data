import sqlite3
#接続
conn = sqlite3.connect('/home/tomoki/SQL/example2.db')
#カーソル取得
c = conn.cursor()

c.execute("CREATE TABLE articles (id int, title varchar(1024), body text, created datetime)")

c.execute("INSERT INTO articles VALUES (1, 'morning', 'fish', '2020-02-01 00:00:00')")
c.execute("INSERT INTO articles VALUES (2,'lunch','curry','2020-02-02 00:00:00')")
c.execute("INSERT INTO articles VALUES (3,'dinner','hunberger','2020-02-03 00:00:00')")
 
# コミット
conn.commit()
 
# コネクションをクローズ
conn.close()
