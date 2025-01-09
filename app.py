app = Flask(_name_)

@app.route('/')
def home():
	return "Hello, Azure from Flask!"

if_name_== '_main_':
	app.run(debug=True)