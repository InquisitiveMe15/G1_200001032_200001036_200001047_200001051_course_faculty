# import the flask class
from flask import Flask, session, render_template, request, make_response, redirect, flash
from flaskext.mysql import MySQL
# ********************************************************
from flask_recaptcha import ReCaptcha


app = Flask(__name__)
# *********************************************************
app.secret_key = 'superSecretKey'
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lf4XtQcAAAAADTEkDEA0_AqdysjUvJxPuRf6hPs'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lf4XtQcAAAAAGuCw_oWxUh4_eqvNdP1GG0ahVWv'
recaptcha = ReCaptcha(app)
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}
# ***********************************************************

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Thds@19xcNh#20J'
app.config['MYSQL_DATABASE_DB'] = 'database2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()


cursor = conn.cursor()
cursor.execute('SELECT courseName FROM courses')
courselist = cursor.fetchall()

cursor.execute('SELECT departmentName FROM department')
departmentlist = cursor.fetchall()

cursor.execute('SELECT name FROM faculty')
facultylist = cursor.fetchall()


# @app.route('/', methods=['GET', 'POST'])
# def register():
#     message = '' # Create empty message
#     if request.method == 'POST': # Check to see if flask.request.method is POST
#             if recaptcha.verify(): # Use verify() method to see if ReCaptcha is filled out
#                 message = 'Thanks for filling out the form!' # Send success message
#                 if recaptcha.validate_on_submit():
#                     return render_template("home.html", courselist=courselist, departmentlist=departmentlist, facultylist=facultylist)
#             else:
#                 message = 'Please fill out the ReCaptcha!' # Send error message
#                 return render_template('form.html', message=message)
#     return render_template('form.html')


@app.route('/')
def index():
    return render_template("home.html", courselist=courselist, departmentlist=departmentlist, facultylist=facultylist)


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
            query_string = "SELECT courseName FROM courses WHERE courseID='{}' AND deapartmentID = '{}'".format(
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
            query_string = "SELECT courseName FROM courses WHERE courseID='{}' AND deapartmentID = '{}'".format(
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
        departmentName = request.form['department']
        # print(departmentName)                           ##extra

        query_string = "SELECT departmentID FROM department WHERE departmentName='{}'".format(
            departmentName)
        cursor.execute(query_string)
        departmentID = cursor.fetchall()
        CSEcoursesID = []
        query_string = "SELECT courseID FROM courses WHERE deapartmentID='{}'".format(
            departmentID[0][0])
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
        query_string = "SELECT courseID FROM courses WHERE deapartmentID='{}' AND courseName='{}'".format(
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
        # for id in cursorID:    #extra
        #     print(id)
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
        # for id in ValidCourseID:      #extra
        #     print(id)
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
        departmentID = []
        for id in ValidCourseID:
            query_string = "SELECT deapartmentID FROM courses WHERE courseID='{}'".format(
                id)
            cursor.execute(query_string)
            row = cursor.fetchone()
            if(row == None):
                print("No such course exists.")
            else:
                departmentID.append(row[0])
                row = cursor.fetchone()
                while(row != None):
                    departmentID.append(row[0])
                    row = cursor.fetchone()
        semester = []
        for id in ValidCourseID:
            query_string = "SELECT semester FROM courses WHERE courseID='{}'".format(
                id)
            cursor.execute(query_string)
            row = cursor.fetchone()
            if(row == None):
                print("No such course exists.")
            else:
                semester.append(row[0])
                row = cursor.fetchone()
                while(row != None):
                    semester.append(row[0])
                    row = cursor.fetchone()
        # for name in CourseName:  #extra
        #     print(name)
        result = []
        length = len(ValidCourseID)
        result.append(ValidCourseID)
        result.append(CourseName)
        result.append(departmentID)
        result.append(semester)
        # print(result)
        # print(type(result))
        return render_template("filteredtable_5.html", result=result, length=length)
        # return render_template("filteredtable_5.html", courseidlist=ValidCourseID, coursenamelist=CourseName, semesterlist=semester, departmentlist=departmentID)

    return("NOT SUBMITTED PROPERLY")

# *************************************************


@app.route('/executeCourses')
def executeCourses():
    cursor = conn.cursor()
    courseID = []
    courseName = []
    departmentID = []
    semester = []
    query_string = ("SELECT courseID FROM courses")
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        courseID.append(row[0])
        row = cursor.fetchone()
    print(courseID)

    for id in courseID:
        query_string = (
            "SELECT courseName FROM courses WHERE courseID='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            courseName.append(row[0])
            row = cursor.fetchone()
    print(courseName)

    query_string = ("SELECT deapartmentID FROM courses")
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        departmentID.append(row[0])
        row = cursor.fetchone()
    print(departmentID)

    for id in courseID:
        query_string = (
            "SELECT semester FROM courses WHERE courseID='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            semester.append(row[0])
            row = cursor.fetchone()
    print(semester)

    result = []
    length = len(courseID)
    result.append(courseID)
    result.append(courseName)
    result.append(departmentID)
    result.append(semester)
    return render_template("courses.html", result=result, length=length)


@app.route('/executeFaculty')
def executeFaculty():
    facultyId = []
    name = []
    emailID = []
    address = []
    query_string = ("SELECT facultyId FROM faculty")
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        facultyId.append(row[0])
        row = cursor.fetchone()
    print(facultyId)

    query_string = ("SELECT name FROM faculty")
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        name.append(row[0])
        row = cursor.fetchone()
    print(name)

    query_string = ("SELECT emailID FROM faculty")
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        emailID.append(row[0])
        row = cursor.fetchone()
    print(emailID)

    query_string = ("SELECT address FROM faculty")
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        address.append(row[0])
        row = cursor.fetchone()
    print(address)

    result = []
    length = len(facultyId)
    result.append(facultyId)
    result.append(name)
    result.append(emailID)
    result.append(address)
    return render_template("faculty.html", result=result, length=length)


@app.route('/completeinfo')
def completeinfo():
    courseID = []
    courseName = []
    facultyID = []
    facultyname = []
    departmentID = []
    departmentName = []
    semester = []
    roomNO = []
    day = []
    timing = []

    query_string = "SELECT courseID FROM courses"
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        courseID.append(row[0])
        row = cursor.fetchone()
    print(courseID)

    for id in courseID:
        query_string = (
            "SELECT courseName FROM courses WHERE courseID='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            courseName.append(row[0])
            row = cursor.fetchone()
    print(courseName)

    query_string = ("SELECT deapartmentID FROM courses")
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        departmentID.append(row[0])
        row = cursor.fetchone()
    print(departmentID)

    for id in courseID:
        query_string = (
            "SELECT semester FROM courses WHERE courseID='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            semester.append(row[0])
            row = cursor.fetchone()
    print(semester)

    for id in courseID:
        query_string = (
            "SELECT facultyID FROM istaughtby WHERE courseID='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        if(row == None):
            facultyID.append("NULL")
        else:
            facultyID.append(row[0])
    print(facultyID)

    for id in courseID:
        query_string = (
            "SELECT day FROM istaughtby WHERE courseID='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        if(row == None):
            day.append("NULL")
        else:
            day.append(row[0])
    print(day)

    for id in courseID:
        query_string = (
            "SELECT timing FROM istaughtby WHERE courseID='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        if(row == None):
            timing.append("NULL")
        else:
            timing.append(row[0])
    print(timing)

    for id in courseID:
        query_string = (
            "SELECT roomNO FROM istaughtby WHERE courseID='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        if(row == None):
            roomNO.append("NULL")
        else:
            roomNO.append(row[0])

    print(roomNO)

    for id in departmentID:
        query_string = (
            "SELECT departmentName FROM department WHERE departmentID='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        departmentName.append(row[0])
    print(departmentName)

    for id in facultyID:
        if id == "NULL":
            facultyname.append("NULL")
        else:
            query_string = (
                "SELECT name FROM faculty WHERE facultyId='{}'".format(id))
            cursor.execute(query_string)
            row = cursor.fetchone()
            facultyname.append(row[0])
    print(facultyname)

    result = []
    length = len(courseID)
    result.append(courseID)
    result.append(courseName)
    result.append(departmentID)
    result.append(departmentName)
    result.append(facultyID)
    result.append(facultyname)
    result.append(semester)
    result.append(day)
    result.append(timing)
    result.append(roomNO)
    return render_template("completeSummary.html", result=result, length=length)


@app.route('/addcoursePage')
def addcoursePage():
    return render_template("addcourse.html")


@app.route('/addfacultyPage')
def addfacultyPage():
    return render_template("addfaculty.html")


@app.route('/adddepartmentPage')
def adddepartmentPage():
    return render_template("adddepartment.html")


@app.route('/addcourse', methods=['GET', 'POST'])
def addcourse():
    warning = ''
    if request.method == 'POST' and 'courseID' in request.form and 'courseName' in request.form and 'departmentID' in request.form and 'semester' in request.form:
        courseID = request.form['courseID']
        courseName = request.form['courseName']
        departmentID = request.form['departmentID']
        semester = request.form['semester']
        cursor.execute(
            'SELECT * FROM courses WHERE courseID = % s', (courseID,))
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


@app.route('/addfaculty', methods=['GET', 'POST'])
def addfaculty():
    warning = ''
    if request.method == 'POST' and 'facultyId' in request.form and 'name' in request.form and 'emailID' in request.form and 'address' in request.form:
        facultyId = request.form['facultyId']
        name = request.form['name']
        emailID = request.form['emailID']
        address = request.form['address']
        cursor.execute(
            'SELECT * FROM faculty WHERE facultyId = % s', (facultyId,))
        faculty = cursor.fetchone()
        if faculty:
            warning = "faculty id already exists"
        elif not facultyId or not name or not emailID or not address:
            warning = 'Please fill all the required details first !'
        else:
            cursor.execute('INSERT INTO faculty VALUES (%s, % s, % s, % s)',
                           (facultyId, name, emailID, address))
            conn.commit()
            warning = 'added faculty '
    return render_template('addfaculty.html', warning=warning)


@app.route('/adddepartment', methods=['GET', 'POST'])
def adddepartment():
    warning = ''
    if request.method == 'POST' and 'departmentID' in request.form and 'departmentName' in request.form:
        departmentID = request.form['departmentID']
        departmentName = request.form['departmentName']
        cursor.execute(
            'SELECT * FROM department WHERE departmentID = % s', (departmentID,))
        department = cursor.fetchone()
        if department:
            warning = "department id already exists"
        elif not departmentID or not departmentName:
            warning = 'Please fill all the required details first !'
        else:
            cursor.execute('INSERT INTO department VALUES (%s, % s)',
                           (departmentID, departmentName))
            conn.commit()
            warning = 'added department '
    return render_template('adddepartment.html', warning=warning)


@app.route('/editcoursePage')
def editcoursePage():
    return render_template("editcourse.html")


@app.route('/editfacultyPage')
def editfacultyPage():
    return render_template("editfaculty.html")


@app.route('/editcourse', methods=['GET', 'POST'])
def editcourse():
    warning = ''
    if request.method == 'POST' and 'courseID' in request.form and 'courseName' in request.form and 'departmentID' in request.form and 'semester' in request.form:
        courseID = request.form['courseID']
        courseName = request.form['courseName']
        departmentID = request.form['departmentID']
        semester = request.form['semester']
        cursor.execute(
            'SELECT * FROM courses WHERE courseID = % s', (courseID,))
        course = cursor.fetchone()
        if course == None:
            warning = "course id doesn't exists"
        elif not courseID or not courseName or not departmentID or not semester:
            warning = 'Please fill all the required details first !'
        else:
            query_string = "UPDATE courses SET courseName='{}', deapartmentID='{}', semester='{}' WHERE courseID='{}'".format(
                courseName, departmentID, semester, courseID)
            cursor.execute(query_string)
            conn.commit()
            warning = 'Course editted'
    return render_template('editcourse.html', warning=warning)


@app.route('/editfaculty', methods=['GET', 'POST'])
def editfaculty():
    warning = ''
    if request.method == 'POST' and 'facultyId' in request.form and 'name' in request.form and 'emailID' in request.form and 'address' in request.form:
        facultyId = request.form['facultyId']
        name = request.form['name']
        emailID = request.form['emailID']
        address = request.form['address']
        cursor.execute(
            'SELECT * FROM faculty WHERE facultyId = % s', (facultyId,))
        faculty = cursor.fetchone()
        if faculty == None:
            warning = "faculty id doesn't exists"
        elif not facultyId or not name or not emailID or not address:
            warning = 'Please fill all the required details first !'
        else:
            query_string = "UPDATE faculty SET name='{}', emailID='{}', address='{}' WHERE facultyId='{}'".format(
                name, emailID, address, facultyId)
            cursor.execute(query_string)
            conn.commit()
            warning = 'Faculty editted'
    return render_template('editfaculty.html', warning=warning)


if __name__ == '__main__':
    app.run(debug=True)
