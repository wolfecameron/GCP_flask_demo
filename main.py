from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')

@app.route('/form')
def form():
	return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
	name = request.form['name']
	major = request.form['major']
	rating = request.form['rating']
	comments = request.form['comments']
	return render_template('submitted_form.html',
			name=name, major=major, rating=rating, comments=comments) 

# name major rating comments
if __name__ == '__main__':
	app.run(port='8080',debug=True)
