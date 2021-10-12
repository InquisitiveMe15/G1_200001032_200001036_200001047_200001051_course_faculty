# import the flask class
from flask import Flask, session, render_template, request,make_response,redirect,flash
from flaskext.mysql import MySQL

# instatiating flask class 
app=Flask(__name__)
mysql = MySQL()
 
# configuring MySQL for the web application
app.config['MYSQL_DATABASE_USER'] = 'root'    # default user of MySQL to be replaced with appropriate username
app.config['MYSQL_DATABASE_PASSWORD'] = '' # default passwrod of MySQL to be replaced with appropriate password
app.config['MYSQL_DATABASE_DB'] = 'database2'  # Database name to be replaced with appropriate database name
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # default database host of MySQL to be replaced with appropriate database host
#initialise mySQL
mysql.init_app(app)
#creating connection to access data
conn = mysql.connect()


#creating a cursor
cursor = conn.cursor()
cursor.execute('SELECT courseName FROM courses')
courselist = cursor.fetchall() 

cursor.execute('SELECT departmentName FROM department')
departmentlist = cursor.fetchall()

cursor.execute('SELECT name FROM faculty')
facultylist = cursor.fetchall()

@app.route('/') 
def index(): 
    return render_template("home.html", courselist=courselist, departmentlist=departmentlist, facultylist=facultylist)
    


# @app.route('/filter', methods=['GET','POST'])
# def filter():
#     if request.method == 'POST':
#         course=(request.form['course'])
#         department=request.form['department']
#         faculty=request.form['faculty']
#         startingyear=request.form['startingyear']
#         endingyear=request.form['endingyear']
#         #query1
#         #cursor.execute('SELECT departmentID )
#         cursor.execute('')
#         # print(course, department, startingyear,endingyear,faculty)
#         return("SUBMITTED SUCCESSFULLY ")

@app.route('/query1')
def query1():
    return render_template("query1.html", facultylist=facultylist, departmentlist=departmentlist)
@app.route('/query2')
def query2():
    return render_template("query2.html", facultylist=facultylist, departmentlist=departmentlist)
@app.route('/query3')
def query3():
    return render_template("query3.html")
@app.route('/query4')
def query4():
    return render_template("query4.html", courselist=courselist, departmentlist=departmentlist)
@app.route('/query5')
def query5():
    return render_template("query5.html")


@app.route('/executeQuery1', methods=['GET','POST'])
def executeQuery1():
    if request.method == 'POST':
        departmentName=request.form['department']
        # print(departmentName)
        query_string="SELECT departmentID FROM department WHERE departmentName='{}'".format(departmentName)
        cursor.execute(query_string)
        departmentID=list(cursor.fetchall())
        # print(type(departmentID), type(departmentID[0][0]),departmentID[0][0])
        query_string="SELECT facultyID FROM associated where departmentID='{}'".format(departmentID[0][0])
        cursor.execute(query_string)
        facultyIDs=cursor.fetchall()
        facultyname=request.form['faculty']
        # print(facultyname)
        facultyid=[]
        for ids in facultyIDs:
            query_string="SELECT facultyId FROM faculty WHERE name='{}' AND facultyID='{}'".format(facultyname,ids[0])
            cursor.execute(query_string)
            facultyid.append(cursor.fetchall()[0][0])
        courseid=[]
        for id in facultyid:
            query_string="SELECT courseID FROM istaughtby WHERE facultyID='{}'".format(id)
            cursor.execute(query_string)
            courseid.append(cursor.fetchall()[0][0])
        coursename=[]
        for Id in courseid:
            query_string="SELECT courseName FROM courses WHERE courseID='{}'".format(Id)
            cursor.execute(query_string)
            coursename.append(cursor.fetchall()[0][0])
        # resultlist=coursename
        print(type(courselist))
        # return("1")
        return render_template("filteredtable.html",resultlist=courselist, result="Courses")
    return("NOT SUBMITTED PROPERLY")


@app.route('/executeQuery2', methods=['GET','POST'])
def executeQuery2():
    if request.method == 'POST':
        return("EXECUTED SUCCESSFULLY")
    return("NOT SUBMITTED PROPERLY")


@app.route('/executeQuery3', methods=['GET','POST'])
def executeQuery3():
    if request.method == 'POST':
        return("EXECUTED SUCCESSFULLY")
    return("NOT SUBMITTED PROPERLY")


@app.route('/executeQuery4', methods=['GET','POST'])
def executeQuery4():
    if request.method == 'POST':
        return("EXECUTED SUCCESSFULLY")
    return("NOT SUBMITTED PROPERLY")


@app.route('/executeQuery5', methods=['GET','POST'])
def executeQuery5():
    if request.method == 'POST':
        return("EXECUTED SUCCESSFULLY")
    return("NOT SUBMITTED PROPERLY")



if __name__ == '__main__':
    app.run(debug=True)