import requests, json, os
from flask import Flask, render_template, make_response, jsonify

app = Flask(__name__)

def get_tweets():
    for _ in range(10):
        res = requests.get('http://totes-random.herokuapp.com/rand')
        # If there's an error on the Haskell server--which happens randomly, but with
        # decent regularity--it will return an error string in the response. So loop
        # 10 times, but if a valid response isn't returned by then, give up
        if (res.status_code == 200):
            return res.text
    return "{}"

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/tweets', methods=['GET'])
def tweets():
    tweets = get_tweets()
    return tweets

if __name__ == "__main__":
    if 'PORT' in os.environ:
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
    else:
        app.run()
