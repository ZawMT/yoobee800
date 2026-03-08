'''
Testing Flask
'''
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    '''
    Just a simple hello world function to try out Flask
    '''
    return "<p>Hello, World!</p>"


@app.route("/admin")
def admin_page():
    '''
    Just another page
    '''
    return "<h1>This is Admin page</h1>"


@app.route("/bye")
def bye_page():
    '''
    Just another page
    '''
    return "<h1>Bye from Flask!</h1>"


@app.route("/welcome/<name>")
def welcome(name):
    '''
    A function that takes a parameter
    '''
    return f"<p>Welcome {name}!</p>"


@app.route("/welcomemember/<name>/<int:id>")
def welcomemember(name, id):
    '''
    A function that takes two parameters
    '''
    return f"<p>Welcome {name}. Your id is {id}!</p>"


@app.route("/info")
def info():
    '''
    A function that returns a string with some HTML tags
    '''

    url = "https://flask.palletsprojects.com/en/stable/quickstart/"

    html_str = f"""<html style=\"background-color:green\">
    <head>
    <title>Flask Info</title>
    <style>
        body {{
            color: red;
        }}
    </style>
    </head>
    <p>This is a page trying some HTML tags</p>

    To know more about flask, please visit and read:
    <a href="{url}">Flask Quickstart</a>

    <br><br>
    This is the logo of Flask
    <br><br>

    <img src="/static/flask.jpeg" alt="Flask Logo" width="200"></html>
    """

    return html_str


if __name__ == "__main__":
    app.run(debug=True)
