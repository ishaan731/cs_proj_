# Title: Book Recommendation System Based on Emotional Analysis
#### Video Demo:  <https://youtu.be/BbISGTEOm9U>
#### Description:
This final project by me is a book recommendation system that suggests books based on the user's current mood. Users input their mood, and then the program recommends books from a list of 20 books that match their mood along with the emotional tags.

The user first enters their current mood when prompted( Eg- Sad, happy, etc) and then the program checks this mood with the emotional tags contained in a list within each of the books. The program also uses the (.strip()) and (.lower()) method calls to ensure consistency. If the emotional tags matches the user's current mood, that book is diplayed.

Using seaborn, the graphs are plotted. I have used the virdis color palette to give each book a different color. On the x-axis, the books with the same emotioanal tags are displayed and on the y-axis the number of emotional tags are there.

If the number of emotional tags is more, the book has a higher value on the y-axis. Thus the user should read the book with the higher number of emotional tags.



## Functions explanation from project files
- project.py: It is the .py file that contains the main code
  - main(): It handles the initial user interaction, welcome message,etc.
  - recommend_books(mood): It recommends books based on the user's mood which is input by the user itself.
  - visualize_recs(recs): It just visualizes the books recomended according on the emotional tags.
  - load_books(): Finally loads all the book data.

- test_project.py: It is the pytest file that has some tests for the functions in `project.py`.
  - test_recommed_books(): It Tests the `recommend_books` function.
  - test_no_recs(): It Tests the `recommend_books` function for an unknown mood.
  - test_load_books(): It Tests the `load_books` function.

## Running the program
-pip install matplotlib
-pip install seaborn
-pip install pandas

## Design Choices:
Decided to use seaborn instead of just matplotlib so that there is a clear color distinction between the different books.
