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
def show_books():
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

@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    all_genres = mongo.db.genres.find()
    all_scores = mongo.db.scores.find()
    return render_template('editbook.html', book=the_book,
                           genres=all_genres,
                           scores=all_scores)

@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    books = mongo.db.books
    books.update( {'_id': ObjectId(book_id)},
    {
        'book_title': request.form.get('book_title'),
        'book_author': request.form.get('book_author'),
        'book_year': request.form.get('book_year'),
        'book_genre': request.form.get('book_genre'),
        'book_score': request.form.get('book_score'),
        'book_review': request.form.get('book_review')
    })
    return redirect(url_for('show_books'))

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('show_books'))

@app.route('/show_genres')
def show_genres():
    return render_template('genres.html',
                           genres=mongo.db.genres.find())

@app.route('/edit_genre/<genre_id>')
def edit_genre(genre_id):
    return render_template('editgenre.html',
                           genre=mongo.db.genres.find_one(
                           {'_id': ObjectId(genre_id)}))                               

@app.route('/update_genre/<genre_id>', methods=['POST'])
def update_genre(genre_id):
    mongo.db.genres.update(
        {'_id': ObjectId(genre_id)},
        {'book_genre': request.form.get('book_genre')})
    return redirect(url_for('show_genres'))

@app.route('/delete_genre/<genre_id>')
def delete_genre(genre_id):
    mongo.db.genres.remove({'_id': ObjectId(genre_id)})
    return redirect(url_for('show_genres'))    

@app.route('/add_genre', methods=['POST'])
def add_genre():
    genres = mongo.db.genres
    genre_doc = {'book_genre': request.form.get('book_genre')}
    genres.insert_one(genre_doc)
    return redirect(url_for('show_genres'))

@app.route('/add_new_genre')
def add_new_genre():
    return render_template('addgenre.html')    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=int(os.environ.get('PORT', 3000)),
            debug=True)