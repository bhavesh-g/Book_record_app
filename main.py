from flask import Flask, render_template, request
import requests, bs4, time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sample.html')
book={}
library={}

@app.route('/create_book/<book_name>')
def create_book(book_name):
    # print(request.form)
    if (request.method == 'POST'):
        return "error"

    else:
        book[book_name]=1
        return book_name+" created"+"<br><br><a href='/'>Home</a>"

@app.route('/add_book_to_lib/<book_name>')
def create_lib(book_name):
    # print(request.form)
    if (request.method == 'POST'):
        return "error"

    else:
        if book_name in book:
            library['book_record'+book_name]=1
            return book_name+" added to lib"+"<br><br><a href='/'>Home</a>"
        else:
            return "Create book first!"+"<br><br><a href='/'>Home</a>"
    print(book,library)
# return

@app.route('/view_lib')
def view_lib():
    # print(request.form)
    if (request.method == 'POST'):
        return "error"

    else:
        s=''
        for each in library:
            s=s+'\n'+each
        return 'Books in lib:\n\n'+s+"<br><br><a href='/'>Home</a>"




if __name__ == "__main__":
    app.run(debug=True)