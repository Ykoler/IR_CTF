from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route that requires a password in the URL parameters
@app.route('/resource', methods=['GET'])
def get_resource():
    # Get the password from the URL parameters
    password = request.args.get('password')

    # Check if the password is correct
    if password == 'your_secret_password':
        return jsonify({'message': 'Here is your resource!'})
    else:
        return jsonify({'message': 'Unauthorized access!'}), 401

if __name__ == '__main__':
    app.run(debug=True)
