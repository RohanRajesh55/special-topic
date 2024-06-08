from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = ''  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'flask'  # Use the database name you created

mysql = MySQL(app)  # Initialize MySQL

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        user_name = request.form.get('user-name')
        user_address = request.form.get('user-address')
        user_email = request.form.get('user-email')
        user_password = request.form.get('user-password')
        user_confirm_password = request.form.get('user-confirm-password')

        if user_password != user_confirm_password:
            error = "Passwords don't match"
            return render_template('index.html', error=error)

        try:
            cur = mysql.connection.cursor()
            query = "INSERT INTO users (username, address, email, password) VALUES (%s, %s, %s, %s)"
            values = (user_name, user_address, user_email, user_password)
            cur.execute(query, values)
            mysql.connection.commit()  # Commit the changes to the database
            cur.close()

            return render_template('login.html', succ_msg='Registration Successful!')
        except Exception as e:
            print(f'Error - {e}')
            error_msg = f'Database error: {e}'
            return render_template('index.html', error=error_msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user_email = request.form.get('user-email')
        user_password = request.form.get('user-password')

        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (user_email, user_password))
            user_data = cur.fetchone()
            cur.close()

            if user_data:
                return render_template('login.html', succ_msg='Login Successful...')
            else:
                return render_template('login.html', err_msg='Invalid login details!')
        except Exception as e:
            print(f'Error - {e}')
            err_msg = f'Database error: {e}'
            return render_template('login.html', err_msg=err_msg)

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)