from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', 'Guest')
    return render_template('index.html', name=name)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template('thank_you.html', name=name, email=email)
    return render_template('contact.html')

@app.route('/thank_you')
def thank_you():
    return "Thank you for your submission!"

if __name__ == '__main__':
    app.run(debug=True)