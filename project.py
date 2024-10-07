import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#Book Recommendation System r
books = {
    "The Alchemist": ["inspiring", "motivational", "hopeful"],
    "To Kill a Mockingbird": ["thought-provoking", "sad"],
    "1984": ["disturbing", "thought-provoking", "sad"],
    "Pride and Prejudice": ["romantic", "happy"],
    "Great Gatsby": ["tragic", "thought-provoking"],
    "Moby Dick": ["adventurous", "intense"],
    "War and Peace": ["intense", "thought-provoking"],
    "The Catcher in the Rye": ["melancholy", "thought-provoking"],
    "The Hobbit": ["adventurous", "happy"],
    "Harry Potter and the Sorcerer's Stone": ["magical", "happy"],
    "The Fault in Our Stars": ["sad", "romantic"],
    "The Road": ["dark", "thought-provoking"],
    "Life of Pi": ["inspiring", "adventurous"],
    "The Book Thief": ["sad", "inspiring"],
    "The Shining": ["scary", "intense"],
    "Dracula": ["scary", "intense"],
    "Frankenstein": ["scary", "thought-provoking"],
    "Jane Eyre": ["romantic", "thought-provoking"],
    "Wuthering Heights": ["romantic", "tragic"],
    "Brave New World": ["disturbing", "thought-provoking"],
}

def main():

    print("How are you feeling")
    mood = input("Enter your mood: ").strip().lower()
    recs = recommend_books(mood)
    if recs:
        print("You can read:")
        for book in recs:
            print(f"- {book}")
        visualize_recs(recs)
    else:
        print("No recommendations")

def recommend_books(mood):
    recommendations = [book for book, moods in books.items() if mood in moods]
    return recommendations

def visualize_recs(recs):
    data = [(book, len(books[book])) for book in recs]

    df = pd.DataFrame(data, columns=['Book', 'Emotional Tags'])

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Book', y='Emotional Tags', data=df, palette='viridis')

    plt.xlabel('Book::::')
    plt.ylabel('eemotional tags')
    plt.title('Recommended:')

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

def load_books():
    return books

if __name__ == "__main__":
    main()
