import sqlite3

class_conn = sqlite3.connect("student/class_conn.db")
teacher_conn = sqlite3.connect("teacher/teacher.db")
conn = sqlite3.connect("sqlite.db")

teacher_conn.execute("drop table SAVE;")
# teacher_arr = conn.execute("select class, tur, fan, last_name, first_name, code from TEACHER;").fetchall()
#
# for i in teacher_arr:
#     fan = teacher_conn.execute("select number from FAN_CONN where name = (?);",(i[2],)).fetchall()
#     if not fan:
#         teacher_conn.execute("insert into FAN_CONN(name) values (?);",(i[2],))
#         fan = teacher_conn.execute("select number from FAN_CONN where name = (?);",(i[2],)).fetchall()
#
#     if i[0] is None:
#         teacher_conn.execute("insert into CONN(id,fan,code) values (1,?,?);",(fan[0][0],i[5]))
#         teacher = teacher_conn.execute("select number from CONN where fan = (?) and code = (?);",(fan[0][0],i[5])).fetchall()[0][0]
#     else:
#         class_id = class_conn.execute("select number from NUMBER where name = (?);",(int(i[0]),)).fetchall()[0][0]
#         print(class_id,i[1])
#         class_id = class_conn.execute("select number from NAME where id = (?) and name = (?);",(class_id,i[1].upper())).fetchall()[0][0]
#         teacher_conn.execute("insert into CONN(id,fan,class_id,code) values (1,?,?,?);",(fan[0][0],class_id,i[5]))
#         teacher = teacher_conn.execute("select number from CONN where class_id = (?);",(class_id,)).fetchall()[0][0]
#
#     teacher_conn.execute("insert into NAME(name,last_name,first_name) values (?,?,?);",(teacher,i[3],i[4]))
#
#
#

teacher_conn.commit()