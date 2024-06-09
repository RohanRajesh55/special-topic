from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = ''  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'flask'  # Use your database name

mysql = MySQL(app)

@app.route('/')
def index():
    # Fetch property data from the database (you'll need to create the table)
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM properties")
    properties = cur.fetchall()
    cur.close()
    return render_template('index.html', properties=properties)

@app.route('/add_property', methods=['POST'])
def add_property():
    property_name = request.form['property_name']
    num_rooms = request.form['num_rooms']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    pincode = request.form['pincode']
    country = request.form['country']
    price = request.form['price']

    # Handle image upload
    property_image = request.files['property_image']
    image_data = property_image.read()

    # Insert data into the database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO properties (property_name, num_rooms, address, city, state, pincode, country, price, property_image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (property_name, num_rooms, address, city, state, pincode, country, price, image_data))
    mysql.connection.commit()
    cur.close()
    return "Property added successfully!"

@app.route('/properties')
def properties():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM properties")
    properties = cur.fetchall()
    cur.close()
    return render_template('properties.html', properties=properties)

if __name__ == '__main__':
    app.run(debug=True)