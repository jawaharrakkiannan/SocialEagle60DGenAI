from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Social eagless! Welcome to the community!!"

if __name__ == "__main__":
    app.run(debug=True)


'''
inside Postman, set the request type to GET and the URL to:
http://localhost:5000/

nothing else is needed in the body for a GET request.


'''