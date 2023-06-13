from flask import Flask, request, jsonify
import pickle
import numpy as np
import os
import mysql.connector

app = Flask(__name__)

# Load the pre-trained model using pickle
with open('ranfor.pkl', 'rb') as f:
    model = pickle.load(f)

# Configure MySQL connection
mysql_host = '34.101.152.159'
mysql_user = 'root'
mysql_password = 'plantcycopedianew'
mysql_db = 'plantcycopedia'

def create_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_db
        )
        return connection
    except mysql.connector.Error as error:
        print('Error while connecting to MySQL:', error)
        return None

def close_mysql_connection(connection):
    if connection:
        connection.close()

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Crop Yield Prediction</h1>
            <p>A prototype API for predicting crop yield using Random Forest.</p>'''

@app.route('/ranfors', methods=['POST'])
def predict():
    data = request.json

    # Validate input types
    if not all(isinstance(val, (int, float)) for val in data.values()):
        return jsonify({'error': 'Invalid input types. All input values should be numbers.'}), 400

    # Extract the input parameters from the request body
    N = float(data['N'])
    P = float(data['P'])
    K = float(data['K'])
    temperature = float(data['temperature'])
    humidity = float(data['humidity'])
    pH = float(data['ph'])
    rainfall = float(data['rainfall'])

    # Create an np.array from the input values
    input_array = np.array([[N, P, K, temperature, humidity, pH, rainfall]])

    # Make the prediction using the loaded model
    prediction = model.predict(input_array)
    pred_string = prediction[0].title()

    # Connect to the MySQL database
    connection = create_mysql_connection()
    if connection:
        try:
            cursor = connection.cursor()

            # Prepare and execute the SQL query to retrieve data based on the plant name
            query = "SELECT * FROM plant WHERE Plant = %s"
            cursor.execute(query, (pred_string,))

            # Fetch the result
            result = cursor.fetchall()

            # Close the cursor and connection
            cursor.close()
            close_mysql_connection(connection)

            # Check if any rows were returned
            if result:
                # Extract the column names from the cursor description
                column_names = [desc[0] for desc in cursor.description]

                # Create a dictionary to store the retrieved data
                data_dict = {}
                for i, column in enumerate(column_names):
                    data_dict[column] = result[0][i]

                # Return the data as a response
                return jsonify(data_dict)
            else:
                return jsonify({'message': 'No data found for the given plant name.'})

        except mysql.connector.Error as error:
            print('Error while executing MySQL query:', error)
            close_mysql_connection(connection)
            return jsonify({'error': 'Error while retrieving data from MySQL.'})

    return jsonify({'error': 'Unable to connect to MySQL.'})


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)
