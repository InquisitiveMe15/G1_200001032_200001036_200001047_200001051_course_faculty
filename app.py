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
#create connection to access data
conn = mysql.connect()


@app.route('/') 

def index(): 
    #create a cursor
    cursor = conn.cursor() 
    #execute select statement to fetch data to be displayed in combo/dropdown
    cursor.execute('SELECT courseID,courseName FROM courses') 
    #fetch all rows ans store as a set of tuples 
    courselist = cursor.fetchall() 

    cursor.execute('SELECT departmentID,departmentName FROM department')
    departmentlist = cursor.fetchall()

    cursor.execute('SELECT facultyID,name FROM faculty')
    facultylist = cursor.fetchall()
    #render template and send the set of tuples to the HTML file for displaying
    return render_template("home.html",courselist=courselist, departmentlist=departmentlist, facultylist=facultylist) 
   
