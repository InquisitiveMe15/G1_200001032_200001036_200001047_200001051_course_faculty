# import the flask class
from flask import Flask, session, render_template, request,make_response,redirect,flash
from flaskext.mysql import MySQL

# instatiating flask class 
app=Flask(__name__)
mysql = MySQL()
 
# configuring MySQL for the web application
app.config['MYSQL_DATABASE_USER'] = 'root'    # default user of MySQL to be replaced with appropriate username
app.config['MYSQL_DATABASE_PASSWORD'] = 'Thds@19xcNh#20J' # default passwrod of MySQL to be replaced with appropriate password
app.config['MYSQL_DATABASE_DB'] = 'database2'  # Database name to be replaced with appropriate database name
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # default database host of MySQL to be replaced with appropriate database host
#initialise mySQL
mysql.init_app(app)
#create connection to access data
conn = mysql.connect()


#create a cursor
cursor = conn.cursor() 
#execute select statement to fetch data to be displayed in combo/dropdown
cursor.execute('SELECT courseName FROM courses') 
#fetch all rows ans store as a set of tuples 
courselist = cursor.fetchall() 

cursor.execute('SELECT departmentName FROM department')
departmentlist = cursor.fetchall()

cursor.execute('SELECT name FROM faculty')
facultylist = cursor.fetchall()
@app.route('/') 

def index(): 

    #render template and send the set of tuples to the HTML file for displaying
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


if __name__ == '__main__':
    app.run(debug=True)