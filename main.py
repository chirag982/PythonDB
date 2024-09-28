import sqlite3

connection = sqlite3.connect('student.db')
cursor = connection.cursor()

# course_table= """
#                 CREATE TABLE COURSE (
#                 courseID VARCHAR(10) PRIMARY KEY,
#                 Name VARCHAR(30)
#                 )
#                 """

# cursor.execute(course_table)

# teacher_table= """
#                 CREATE TABLE TEACHER (
#                 teacherID VARCHAR(10) PRIMARY KEY,
#                 name VARCHAR(50),
#                 courseID VARCHAR(10),
#                 FOREIGN KEY(courseID) REFERENCES COURSE(courseID)
#                 )
#                 """
# cursor.execute(teacher_table)


# cursor.execute(''' INSERT INTO TEACHER VALUES("T1", "Robert Downey Junior", "C1") ''')
# cursor.execute(''' INSERT INTO TEACHER VALUES("T2", "Mads Mikkeleson", "C2") ''')
# cursor.execute(''' INSERT INTO TEACHER VALUES("T3", "Cillian Murphy", "C3") ''')
# cursor.execute(''' INSERT INTO TEACHER VALUES("T4", "Keanu Reeves", "C4") ''')
# cursor.execute(''' INSERT INTO TEACHER VALUES("T5", "Al Pacino", "C5") ''')


data=cursor.execute('''SELECT * FROM TEACHER''') 
for row in data: 
    print(row)

# connection.commit()