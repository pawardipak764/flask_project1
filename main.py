from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']

        # Print the data (you can store it in a database instead)
        print(f"Name: {name}, Email: {email}")

        return render_template('success.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
