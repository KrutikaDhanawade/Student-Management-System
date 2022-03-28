from flask import Flask,render_template,request,redirect
import dbm

from dbm import Student



app=Flask(__name__)#creating the Flask application
'''
@app.route('/home')
def a():
    return "<h1>Hello all, from flask</h1>"

@app.route('/a')
def showLoginPage():
    return render_template('login.html')
'''
@app.route('/')
def showHome():
    return render_template('index.html')

@app.route('/allstudents')
def showall():
    data=dbm.showAllStudents()
    #sending values to html page
    #we use name=value format as below, and access these names in html
    return render_template('students.html',num=500,students=data)

@app.route('/addstudent')
def showAddStudent():
    return render_template('addstudent.html')

@app.route('/savestudent',methods=['post'])
def savestudent():
    n=request.form['sname']
    b=request.form['branch']
    p=request.form['perc']
    perc=float(p)
    s=Student(n,b,perc)
    dbm.addStudent(s)
    #return "<h1>Success</h1>"
    return redirect('/allstudents')

@app.route('/delete/<int:i>')
def deleteStudent(i):
    dbm.deleteStudentById(i)
    return redirect('/allstudents')

@app.route('/showstudent/<int:i>')
def showCurrentStudentObj(i):
    obj=dbm.showStudentById(i)
    return render_template('showstudent.html',student=obj)

@app.route('/updatestudent',methods=['post'])
def saveupdate():
    i=request.form['sid']
    sid=int(i)
    n=request.form['sname']
    b=request.form['branch']
    p=request.form['perc']
    perc=float(p)
    s=Student(n,b,perc,sid)
    dbm.updateStudent(s)
    #return "<h1>Success</h1>"
    return redirect('/allstudents')







if __name__=='__main__':
    app.run(debug=True)

