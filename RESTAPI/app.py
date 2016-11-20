from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test_py'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route("/")
def main():
    return "Welcome!"

@app.route("/user", methods=['GET'])
def user():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM tbl_user")
    rv = cursor.fetchall()
    print(rv)
    return str(rv)


if __name__ == "__main__":
    app.run()


    

