from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def index():
    return render_template('index.html')

# Define the route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data
    name = request.form.get('name')
    age = request.form.get('age')
    
    # If name and age are provided, process them
    if name and age:
        return f"<h1>Hello {name}, you are {age} years old!</h1>"
    else:
        return "<h1>Please enter both your name and age.</h1>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
