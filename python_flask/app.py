from flask import Flask
from uuid import UUID
app=Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"

@app.route("/users")
def users():
    return "This is users page"

@app.route("/user/<int:id>")
def user(id):
    return f"Hello {id}"

@app.route("/file/<path:fpath>")
def file(fpath):
    return fpath

@app.route("/unique/<uuid:user_id>")
def unique(user_id):
    return str(user_id)

if __name__ == "__main__":
    app.run(debug=True)