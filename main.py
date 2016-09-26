import re
import requests
import json
from flask import Flask, render_template, make_response, jsonify

app = Flask(__name__)
app.config["DEBUG"]=True

def get_tweets():
	for _ in range(10):
		json_string = requests.get('http://totes-random.herokuapp.com/rand')
		if (json_string.text.find('widgets') != -1):
			return json_string.text
	return "{}"

@app.route('/', methods=['GET'])
def main():
	return render_template('index.html')

@app.route('/tweets', methods=['GET'])
def tweets():
	tweets = get_tweets()

if __name__ == "__main__":
	app.run()