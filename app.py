from flask import Flask, render_template, request
import db_helper
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pwd'
app.config['MYSQL_DB'] = 'authors'

mysql = MySQL(app)

@app.route("/")
def main():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT Author FROM author_cooccur")
    authors = cursor.fetchall()
    cursor.close()
    return render_template('index.html', authors=authors)

@app.route("/getCoauthors", methods=['POST'])
def getCoauthors():
    author = request.form['author_list']
    cursor = mysql.connection.cursor()
    cursor.execute("""SELECT Coauthor FROM author_cooccur WHERE Author = %s""", (author,))
    co_authors = cursor.fetchall()
    cursor.close()
    return render_template('results.html', co_authors=co_authors)

if __name__ == "__main__":
    app.run()