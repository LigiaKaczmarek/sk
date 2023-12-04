from flask import Flask, jsonify, request, abort
import json
app = Flask(_name_)
def load_books_data():
    with open('books.json', 'r') as file:
        data = json.load(file)
        return data
books_data = load_books_data()
def save_books_data():
    with open('books.json', 'w') as file:
json.dump(books_data, file, indent=4)
@app.route('/titles', methods=['GET']) def get_titles():
titles = [book['title'] for book in books_data['books']] return jsonify(titles)
@app.route('/titles/<isbn>', methods=['GET']) def get_book_by_isbn(isbn):
book = next((b for b in books_data['books'] if b['isbn'] == isbn), None)
    if book:0
        return jsonify(book)
    else:
        abort(404)
@app.route('/descriptions/<expression>', methods=['GET']) def get_books_by_description(expression):
matching_books = [book for book in books_data['books'] if expression in book['description']]
descriptions = [book['description'] for book in matching_books]
    return jsonify(descriptions)
@app.route('/titles/<isbn>', methods=['PUT']) def replace_author(isbn):
    author = request.args.get('author')
    for book in books_data['books']:
if book['isbn'] == isbn:
book['author'] = author
save_books_data()
return jsonify({"message": f"Author of book with
ISBN {isbn} replaced successfully"}) abort(404)
if _name_ == '_main_':
    app.run(debug=True)
