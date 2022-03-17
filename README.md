# Book_record_app
For: assessment

Endpoints:
  1. /create_book/<book_name> : Use to create a book record. Uses GET request. Returns success string if created, else error.
  2. /add_book_to_lib/<book_name> : Use to add a book record into library. Returns error if book record not created before adding to library. Returns success string if added, else error.
  3. /view_lib : Use to check all book names in library. Returns string with all book names.

How to see demo: Goto http://bhaveshbooks.pythonanywhere.com/

Approach:

I used Flask. I couldn't use database as I made my mind it will take time, hence I tried inbuilt data structure to create demo atleast and this will clear memory on every instance.

Tried to show basic Request-Response architecture and understanding of Flask.

Improvements: This is a demo. Everypart can be optimised. How? 

1. Authenticate user using OAuth or some key based authentication.
2. Better type casting in creating endpoints.
3. One can provide JSON responses instead of what Im doing as string responses.
4. For retrieving all books or library records, we can use pagination or a limit as well because at a scalable level it might not be feasible to list all books in one go.

That's all for now. Please let me know if any explanation needed on shared repo and approach.
