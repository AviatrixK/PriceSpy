from flask import Flask
from backend.webScraping import mainWebScraping

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/amzn')
def scrape():
    result = mainWebScraping()
    return result

if __name__ == '__main__':
    app.run(debug=True)