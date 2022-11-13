from flask import Flask, render_template


# Create Flask Instance
app = Flask(__name__)

# create a route decorator
@app.route('/')

def index():
	first_name = "Brendan"
	favorite_pizza = ["Pep", "Cheese", "Shrooms", 41]
	return render_template("index.html", first_name=first_name,
		favorite_pizza=favorite_pizza)

#localhost:5000/user/Bream
@app.route('/user/<name>')

def user(name): 
	return render_template("user.html", username=name)
	
#create custom error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500