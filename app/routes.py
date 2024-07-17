from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Book

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/book/new', methods=['GET', 'POST'])
def new_book():
    if request.method == 'POST':
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            published_date=request.form['published_date'],
            isbn=request.form['isbn']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_book.html')

@app.route('/book/<int:id>/edit', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.published_date = request.form['published_date']
        book.isbn = request.form['isbn']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_book.html', book=book)

@app.route('/book/<int:id>/delete', methods=['POST'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('Livro excluído com sucesso!', 'success')
    return redirect(url_for('index'))
