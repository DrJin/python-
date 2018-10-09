import sqlite3

def showrecord(table):
    for record in table:
        print("이름 : %s 전화 :%s 주소 : %s" %(record))

con = sqlite3.connect('addr.db')
cursor = con.cursor()

#sql 명령 실행
cursor.execute("DROP TABLE IF EXISTS tblAddr")
cursor.execute("""CREATE TABLE tblAddr
(name CHAR(16) PRIMARY KEY, phone CHAR(16), addr TEXT)""")

cursor.execute("INSERT INTO tblAddr VALUES ('진승현', '1234-5678', '서울')")
cursor.execute("INSERT INTO tblAddr VALUES ('진승원', '4321-5678', '성동')")
cursor.execute("INSERT INTO tblAddr VALUES ('고릴라', '2345-5458', '밀림')")

con.commit()

cursor.execute("SELECT * FROM tblAddr")
table  = cursor.fetchall() #레코드를 읽어 필드가 튜플로 저장된 리스트로 반환한다.
                           #fetchone은 하나씩 읽기
showrecord(table)

print()

cursor.execute("SELECT * FROM tblAddr WHERE name like '진%'")
table  = cursor.fetchall()

showrecord(table)

cursor.close()
con.close()
