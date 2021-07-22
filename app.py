import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Home
@app.route("/")
@app.route("/home/")
def home():
    books = list(mongo.db.books.find())
    """To display 3 books from the category"""
    sci_fi = mongo.db.books.find(
        {"category_name": "Sci-fi"}).sort("_id", -1).limit(3)
    fiction = mongo.db.books.find(
        {"category_name": "Fiction"}).sort("_id", -1).limit(3)
    non_fiction = mongo.db.books.find(
        {"category_name": "Non-fiction"}).sort("_id", -1).limit(3)
    fantasy = mongo.db.books.find(
        {"category_name": "Fantasy"}).sort("_id", -1).limit(3)
    classic = mongo.db.books.find(
        {"category_name": "Classic"}).sort("_id", -1).limit(3)

    return render_template(
        "home.html",
        books=books, sci_fi=sci_fi, fiction=fiction,
        non_fiction=non_fiction, fantasy=fantasy, classic=classic)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    if len(books) == 0:
        flash("No Results Found")

    return render_template("home.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # make a variable for checking the password
            password_match = check_password_hash(
                existing_user["password"],
                request.form.get("password")
            )
            # ensure hashed password matches user input
            if password_match:
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        books = list(mongo.db.books.find())
        uploaded = list(mongo.db.books.find({"uploaded_by": session["user"]}))
        return render_template(
            "profile.html", username=username, books=books, uploaded=uploaded)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "category_name": request.form.get("category_name"),
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_length": request.form.get("book_length"),
            "book_description": request.form.get("book_description"),
            "book_url": request.form.get("book_url"),
            "book_review": request.form.get("book_review"),
            "book_rate": request.form.get("book_rate"),
            "uploaded_by": session["user"]
        }
        mongo.db.books.insert_one(book)
        flash("Book Successfully Added")
        return redirect(url_for("home"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_book.html", categories=categories)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_length": request.form.get("book_length"),
            "book_description": request.form.get("book_description"),
            "book_url": request.form.get("book_url"),
            "book_review": request.form.get("book_review"),
            "book_rate": request.form.get("book_rate"),
            "uploaded_by": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Successfully Updated")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_book.html", book=book, categories=categories)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully Deleted")
    return redirect(url_for("home"))


# one book
@app.route("/single_book/<book_id>")
def single_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    return render_template(
        "single_book.html", book=book)


# category pages
@app.route("/category")
def category():
    categories = request.args.get("categories")
    books = mongo.db.books.find()

    return render_template(
        "category.html", books=books, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
