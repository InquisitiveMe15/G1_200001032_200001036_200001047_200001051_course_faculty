# import the flask class
from flask import Flask, session, render_template, request, make_response, redirect, flash
from flaskext.mysql import MySQL
#from flask_mysqldb import MySQL
#import MySQLdb.cursors

# instatiating flask class
app = Flask(__name__)
mysql = MySQL()

# configuring MySQL for the web application
# default user of MySQL to be replaced with appropriate username
app.config['MYSQL_DATABASE_USER'] = 'root'
# default passwrod of MySQL to be replaced with appropriate password
app.config['MYSQL_DATABASE_PASSWORD'] = 'kanchi123456@'
# Database name to be replaced with appropriate database name
app.config['MYSQL_DATABASE_DB'] = 'database2'
# default database host of MySQL to be replaced with appropriate database host
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# initialise mySQL
mysql.init_app(app)
# creating connection to access data
conn = mysql.connect()


# creating a cursor
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

# ************************************************************************************************


@app.route('/executeQuery1', methods=['GET', 'POST'])
def executeQuery1():
    if request.method == 'POST':
        departmentName = request.form['department']

        # print(departmentName)                           ##extra

        query_string = "SELECT departmentID FROM department WHERE departmentName='{}'".format(
            departmentName)
        cursor.execute(query_string)
        departmentID = cursor.fetchall()

        query_string = "SELECT facultyID FROM associated where departmentID='{}'".format(
            departmentID[0][0])
        cursor.execute(query_string)
        facultyIDs = cursor.fetchall()
        facultyname = request.form['faculty']

        # print(facultyname)      ##extra

        facultyid = []
        for ids in facultyIDs:
            print(ids[0])
            query_string = "SELECT facultyId FROM faculty WHERE name='{}' AND facultyID='{}'".format(
                facultyname, ids[0])
            cursor.execute(query_string)
            if(cursor.fetchone() == None):
                print("NO SUCH facultId EXISTS")
            else:
                facultyid.append(ids[0])
        if len(facultyid) == 0:
            return render_template("filteredtable.html", resultlist=['NO SUCH COURSE EXISTS'], result="Courses")

        # for i in facultyid:    ##extra
        #     print(i)

        courseid = []
        for id in facultyid:
            query_string = "SELECT courseID FROM istaughtby WHERE facultyID='{}' AND startingYear >= 2009 AND startingYear < 2021".format(
                id)
            cursor.execute(query_string)
            row = cursor.fetchone()
            if (row == None):
                print("No such course exists.")
            else:
                courseid.append(row[0])
                row = cursor.fetchone()
                while(row != None):
                    courseid.append(row[0])
                    row = cursor.fetchone()

        if len(courseid) == 0:
            return render_template("filteredtable.html", resultlist=['NO SUCH COURSE EXISTS'], result="Courses")

        for i in courseid:  # extra
            print(i)

        coursename = []
        for Id in courseid:
            query_string = "SELECT courseName FROM courses WHERE courseID='{}' AND'departmentID' = '{}'".format(
                Id, int(departmentID[0][0]))
            cursor.execute(query_string)
            row = cursor.fetchone()
            if(row == None):
                print("No such course exists.")
            else:
                coursename.append(row[0])
                row = cursor.fetchone()
                while(row != None):
                    coursename.append(row[0])
                    row = cursor.fetchone()
                # courselist = cursor.fetchall()
                # coursename.append(courselist[0][0])
        if len(coursename) == 0:
            return render_template("filteredtable.html", resultlist=['NO SUCH COURSE EXISTS'], result="Courses")

        for i in coursename:  # extra
            print(i)

        return render_template("filteredtable.html", resultlist=coursename, result="Courses")
    return("NOT SUBMITTED PROPERLY")

# *********************************************************************************************************


@app.route('/executeQuery2', methods=['GET', 'POST'])
def executeQuery2():
    if request.method == 'POST':
        departmentName = request.form['department']

        print(departmentName)  # extra

        query_string = "SELECT departmentID FROM department WHERE departmentName='{}'".format(
            departmentName)
        cursor.execute(query_string)
        departmentID = cursor.fetchall()

        # print(type(departmentID), type(departmentID[0][0]),departmentID[0][0])  ##extra

        query_string = "SELECT facultyID FROM associated where departmentID='{}'".format(
            departmentID[0][0])
        cursor.execute(query_string)
        facultyIDs = cursor.fetchall()
        facultyname = request.form['faculty']

        print(facultyname)  # extra

        facultyid = []
        for ids in facultyIDs:
            print(ids[0])
            query_string = "SELECT facultyId FROM faculty WHERE name='{}' AND facultyID='{}'".format(
                facultyname, ids[0])
            cursor.execute(query_string)
            if(cursor.fetchone() == None):
                print("NO SUCH facultId EXISTS")
            else:
                facultyid.append(ids[0])
        if len(facultyid) == 0:
            return render_template("filteredtable.html", resultlist=['NO SUCH COURSE EXISTS'], result="Courses")

        for i in facultyid:  # extra
            print(i)

        courseid = []
        for id in facultyid:
            query_string = "SELECT courseID FROM istaughtby WHERE facultyID='{}'".format(
                id)
            cursor.execute(query_string)
            row = cursor.fetchone()
            if (row == None):
                print("No such course exists.")
            else:
                courseid.append(row[0])
                row = cursor.fetchone()
                while(row != None):
                    courseid.append(row[0])
                    row = cursor.fetchone()

        if len(courseid) == 0:
            return render_template("filteredtable.html", resultlist=['NO SUCH COURSE EXISTS'], result="Courses")

        for i in courseid:  # extra
            print(i)

        coursename = []
        for Id in courseid:
            query_string = "SELECT courseName FROM courses WHERE courseID='{}' AND'departmentID' = '{}'".format(
                Id, int(departmentID[0][0]))
            cursor.execute(query_string)
            row = cursor.fetchone()
            if(row == None):
                print("No such course exists.")
            else:
                coursename.append(row[0])
                row = cursor.fetchone()
                while(row != None):
                    coursename.append(row[0])
                    row = cursor.fetchone()
                # courselist = cursor.fetchall()
                # coursename.append(courselist[0][0])
        if len(coursename) == 0:
            return render_template("filteredtable.html", resultlist=['NO SUCH COURSE EXISTS'], result="Courses")

        for i in coursename:  # extra
            print(i)

        return render_template("filteredtable.html", resultlist=coursename, result="Courses")
    return("NOT SUBMITTED PROPERLY")

# *****************************************************************************************************


@app.route('/executeQuery3', methods=['GET', 'POST'])
def executeQuery3():
    if request.method == 'POST':
        CSEcoursesID = []
        query_string = "SELECT courseID FROM courses WHERE'departmentID'=1"
        cursor.execute(query_string)
        row = cursor.fetchone()
        if(row == None):
            return render_template("filteredtable.html", resultlist=["NO COURSES OF CSE DEPARTMENT EXISTS"], result="Courses")
        else:
            CSEcoursesID.append(row[0])
            row = cursor.fetchone()
            while(row != None):
                CSEcoursesID.append(row[0])
                row = cursor.fetchone()

        for id in CSEcoursesID:
            print(id)

        ValidcourseID = []
        for id in CSEcoursesID:
            # AND (endYear=NULL OR endYear > 2011)
            print(id)
            query_string = "SELECT courseID FROM istaughtby WHERE courseID='{}' AND (startingYear<2020) AND (endYear IS NULL OR endYear > 2011)".format(
                id)
            cursor.execute(query_string)
            row = cursor.fetchone()
            if(row == None):
                print("Invalid")
            else:
                ValidcourseID.append(row[0])

        if len(ValidcourseID) == 0:
            return render_template("filteredtable.html", resultlist=['NO COURSES OF CSE DEPARTMENT EXISTS THAT WERE TAUGHT IN THE GIVEN DURATION'], result="Courses")
        for id in ValidcourseID:
            print(id)
        CSEcoursesName = []
        for id in ValidcourseID:
            query_string = "SELECT courseName FROM courses WHERE courseID='{}'".format(
                id)
            cursor.execute(query_string)
            row = cursor.fetchone()
            if(row == None):
                return render_template("filteredtable.html", resultlist=["NO COURSES OF CSE DEPARTMENT EXISTS"], result="Courses")
            else:
                CSEcoursesName.append(row[0])
                row = cursor.fetchone()
                while(row != None):
                    CSEcoursesName.append(row[0])
                    row = cursor.fetchone()
        return render_template("filteredtable.html", resultlist=CSEcoursesName, result="Courses")

    return("NOT SUBMITTED PROPERLY")

# *********************************************************************************************************


@app.route('/executeQuery4', methods=['GET', 'POST'])
def executeQuery4():
    if request.method == 'POST':
        departmentName = request.form['department']
        courseName = request.form['course']
        # print(departmentName)                           ##extra
        courseID = []
        query_string = "SELECT departmentID FROM department WHERE departmentName='{}'".format(
            departmentName)
        cursor.execute(query_string)
        departmentID = cursor.fetchall()
        query_string = "SELECT courseID FROM courses WHERE'departmentID'='{}' AND courseName='{}'".format(
            departmentID[0][0], courseName)
        cursor.execute(query_string)
        row = cursor.fetchone()
        if (row == None):
            print("No such course exists.")
            return render_template("filteredtable.html", resultlist=['NO SUCH COURSE EXISTS, SO NO PROFFESSOR TEACHES THIS COURSE.'], result="PROFFESSORS")
        else:
            courseID.append(row[0])
            row = cursor.fetchone()
            while(row != None):
                courseID.append(row[0])
                row = cursor.fetchone()

        # for id in courseID:       #extra
        #     print(id)

        facultyId = []
        for ID in courseID:
            query_string = "SELECT facultyId FROM istaughtby WHERE courseID='{}'".format(
                ID)
            cursor.execute(query_string)
            row = cursor.fetchone()
            if(row == None):
                print("No such faculty exists.")
            else:
                facultyId.append(row[0])
                row = cursor.fetchone()
                while(row != None):
                    facultyId.append(row[0])
                    row = cursor.fetchone()

        # for id in facultyId:        #extra
        #     print(id)
        facultyname = []
        for ID in facultyId:
            query_string = "SELECT name FROM faculty WHERE facultyId = '{}'".format(
                ID)
            name = cursor.execute(query_string)
            row = cursor.fetchone()
            facultyname.append(row[0])
            cursor.fetchall()

        # for name in facultyname:         #extra
        #     print(name)

        return render_template("filteredtable.html", resultlist=facultyname, result="PROFFESSORS")
    return("NOT SUBMITTED PROPERLY")

# *************************************************************************************************


@app.route('/executeQuery5', methods=['GET', 'POST'])
def executeQuery5():
    if request.method == 'POST':
        cursorID = []
        query_string = "SELECT courseID FROM courses WHERE (semester = 1 OR semester = 3 OR semester = 5 OR semester = 7)"
        cursor.execute(query_string)
        row = cursor.fetchone()
        if(row == None):
            print("No such course exists.")
        else:
            cursorID.append(row[0])
            row = cursor.fetchone()
            while(row != None):
                cursorID.append(row[0])
                row = cursor.fetchone()
        for id in cursorID:  # extra
            print(id)
        ValidCourseID = []
        for id in cursorID:
            query_string = "SELECT courseID from istaughtby WHERE courseID='{}' AND (startingYear<2020) AND (endYear IS NULL OR endYear > 2020)".format(
                id)
            cursor.execute(query_string)
            row = cursor.fetchone()
            if(row == None):
                print("No such course exists.")
            else:
                ValidCourseID.append(row[0])
                row = cursor.fetchone()
                while(row != None):
                    ValidCourseID.append(row[0])
                    row = cursor.fetchone()
        for id in ValidCourseID:  # extra
            print(id)
        CourseName = []
        for id in ValidCourseID:
            query_string = "SELECT courseName FROM courses WHERE courseID='{}'".format(
                id)
            cursor.execute(query_string)
            row = cursor.fetchone()
            if(row == None):
                print("No such course exists.")
            else:
                CourseName.append(row[0])
                row = cursor.fetchone()
                while(row != None):
                    CourseName.append(row[0])
                    row = cursor.fetchone()
        for name in CourseName:
            print(name)
        return render_template("filteredtable.html", resultlist=CourseName, result="Courses")

    return("NOT SUBMITTED PROPERLY")

# **************************************************************************************************


@app.route('/addcourse', methods=['GET', 'POST'])
def addcourse():
    warning = ''
    if request.method == 'POST' and 'courseID' in request.form and 'courseName' in request.form and 'departmentID' in request.form and 'semester' in request.form:
        courseID = request.form['courseID']
        courseName = request.form['courseName']
        departmentID = request.form['departmentID']
        semester = request.form['semester']
        cursor.execute('SELECT * FROM courses WHERE courseID = % s', (courseID,))
        course = cursor.fetchone()
        if course:
            warning = "course id already exists"
        elif not courseID or not courseName or not departmentID or not semester:
            warning = 'Please fill all the required details first !'
        else:
            cursor.execute('INSERT INTO courses VALUES (%s, % s, % s, % s)',
                       (courseID, courseName, departmentID, semester))
            conn.commit()
            warning = 'added course '
    return render_template('addcourse.html', warning=warning)

#**********************************************************************
@app.route('/addfaculty', methods=['GET', 'POST'])
def addfaculty():
    warning = ''
    if request.method == 'POST' and 'facultyId' in request.form and 'name' in request.form and 'emailID' in request.form and 'address' in request.form:
        facultyId = request.form['facultyId']
        name = request.form['name']
        emailID = request.form['emailID']
        address = request.form['address']
        cursor.execute('SELECT * FROM courses WHERE facultyId = % s', (facultyId,))
        course = cursor.fetchone()
        if course:
            warning = "course id already exists"
        elif not facultyId or not name or not emailID or not address:
            warning = 'Please fill all the required details first !'
        else:
            cursor.execute('INSERT INTO courses VALUES (%s, % s, % s, % s)',
                       (facultyId, name, emailID, address))
            conn.commit()
            warning = 'added faculty '
    return render_template('addfaculty.html', warning=warning)
#*****************************************************************
@app.route('/adddepartment', methods=['GET', 'POST'])
def adddepartment():
    warning = ''
    if request.method == 'POST' and 'departmentID' in request.form and 'name' in request.form :
        departmentID = request.form['departmentID']
        departmentName = request.form['departmentName']
        cursor.execute('SELECT * FROM courses WHERE facultyId = % s', (departmentID,))
        course = cursor.fetchone()
        if course:
            warning = "course id already exists"
        elif not departmentID or not departmentName :
            warning = 'Please fill all the required details first !'
        else:
            cursor.execute('INSERT INTO courses VALUES (%s, % s)',
                       (departmentID, departmentName))
            conn.commit()
            warning = 'added department '
    return render_template('adddepartment.html', warning=warning)

if __name__ == '__main__':
    app.run(debug=True)