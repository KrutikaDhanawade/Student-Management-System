import pymysql

class Student:
    def __init__(self,name,branch,perc,sid=0):
        self.sid=sid
        self.name=name
        self.branch=branch
        self.perc=perc

    def __str__(self):
        return 'Id:{},Name:{},Branch:{},Percentage:{}'.format(self.sid,self.name,self.branch.self.perc)
    

#performing database operations
#define the different methods for db operations
#1. ADding the student record
def addStudent(stu):
    connection=pymysql.connect(host="localhost",user="root",password="",db="flask1")
    cursor=connection.cursor()
    #cursor is the object which executes the database queries
    query="insert into student(name,branch,perc) values(%s,%s,%s)"
    cursor.execute(query,(stu.name,stu.branch,stu.perc))
    connection.commit()#save the data permenently in db
    cursor.close()
    connection.close()

#2.viewing all the student records
def showAllStudents():
    connection=pymysql.connect(host="localhost",user="root",password="",db="flask1")
    cursor=connection.cursor()
    query="select * from student"
    cursor.execute(query)
    #fetchone()
    #fetchmany()
    #fetchall()
    data=cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#3. viewing single record
def showStudentById(i):    
    connection=pymysql.connect(host="localhost",user="root",password="",db="flask1")
    cursor=connection.cursor()
    query='select * from student where sid=%s'
    cursor.execute(query,(i))
    data=cursor.fetchone()
    cursor.close()
    connection.close()
    return data

#4. deleting the record by id
def deleteStudentById(i):    
    connection=pymysql.connect(host="localhost",user="root",password="",db="flask1")
    cursor=connection.cursor()
    query='delete from student where sid=%s'
    cursor.execute(query,(i))
    connection.commit()
    cursor.close()
    connection.close()

#updating the record
def updateStudent(stu):
    connection=pymysql.connect(host="localhost",user="root",password="",db="flask1")
    cursor=connection.cursor()
    query="update student set name=%s,branch=%s,perc=%s where sid=%s"
    cursor.execute(query,(stu.name,stu.branch,stu.perc,stu.sid))
    connection.commit()#save the data permenently in db
    cursor.close()
    connection.close()
