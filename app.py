from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Haloooooooooooooooooo Assertible!"

@app.route("/hagemaru")
def hello():
	return "hai!"

if __name__ == "__main__":
	app.run()
