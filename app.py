import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'my_book_reading_history'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-ftnmb.mongodb.net/my_book_reading_history?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/show_books')
def hello():
    return render_template("books.html", books=mongo.db.books.find())

@app.route('/add_book')
def add_book():
    return render_template('addbook.html',
    scores=mongo.db.scores.find(),
    genres=mongo.db.genres.find())

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('show_books'))    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=int(os.environ.get('PORT', 3000)),
            debug=True)