import random

# Dictionary of movie questions and answers
questions = {
    "What year was the movie 'The Shawshank Redemption' released?": ["1994", "1996", "1999", "2001"],
    "Who directed the movie 'Pulp Fiction'?": ["Quentin Tarantino", "Martin Scorsese", "Steven Spielberg", "Christopher Nolan"],
    "Which actor played the character Tony Stark/Iron Man in the Marvel Cinematic Universe?": ["Robert Downey Jr.", "Chris Hemsworth", "Chris Evans", "Mark Ruffalo"],
    "Which movie won the Academy Award for Best Picture in 2020?": ["Parasite", "Joker", "1917", "Once Upon a Time in Hollywood"],
    "Who played the character Darth Vader in the original 'Star Wars' trilogy?": ["David Prowse", "James Earl Jones", "Mark Hamill", "Harrison Ford"],
    "Which movie features the character Jack Dawson and Rose DeWitt Bukater?": ["Titanic", "The Great Gatsby", "Romeo + Juliet", "The Notebook"],
    "Which actress won an Academy Award for her role in 'La La Land'?": ["Emma Stone", "Jennifer Lawrence", "Natalie Portman", "Cate Blanchett"],
    "Which director is known for movies such as 'Inception' and 'The Dark Knight'?": ["Christopher Nolan", "David Fincher", "Denis Villeneuve", "Martin Scorsese"],
    "Which movie is based on the novel by J.R.R. Tolkien?": ["The Lord of the Rings", "Harry Potter and the Philosopher's Stone", "The Chronicles of Narnia", "Dune"],
    "Who directed the movie 'The Social Network'?": ["David Fincher", "Martin Scorsese", "Quentin Tarantino", "Steven Spielberg"],
    "Which actor won an Academy Award for his role in 'The Revenant'?": ["Leonardo DiCaprio", "Brad Pitt", "Joaquin Phoenix", "Eddie Redmayne"],
    "Which movie features the iconic line, 'Here's Johnny!'?": ["The Shining", "Psycho", "A Clockwork Orange", "The Exorcist"],
    "Who played the character Neo in the movie 'The Matrix'?": ["Keanu Reeves", "Brad Pitt", "Tom Cruise", "Johnny Depp"],
    "Which movie features the character Hannibal Lecter?": ["The Silence of the Lambs", "Seven", "American Psycho", "Saw"],
    "Who directed the movie 'Eternal Sunshine of the Spotless Mind'?": ["Michel Gondry", "Spike Jonze", "Charlie Kaufman", "David Lynch"],
    "Which actress won an Academy Award for her role in 'Black Swan'?": ["Natalie Portman", "Meryl Streep", "Cate Blanchett", "Kate Winslet"],
    "Which movie is set in the Wizarding World?": ["Harry Potter and the Philosopher's Stone", "The Chronicles of Narnia", "The Lord of the Rings", "Alice in Wonderland"],
    "Who directed the movie 'Gone Girl'?": ["David Fincher", "Quentin Tarantino", "Christopher Nolan", "Martin Scorsese"],
    "Which actor played the character James Bond in 'Casino Royale'?": ["Daniel Craig", "Pierce Brosnan", "Sean Connery", "Roger Moore"],
    "Which movie features the song 'Let It Go'?": ["Frozen", "Moana", "Tangled", "Coco"]
}

# List of possible choices for the questions
choices = ["A", "B", "C", "D"]

# Function to ask a question and check the answer
def ask_question(question, answer):
    print(question)
    for i in range(len(choices)):
        print(f"{choices[i]}. {answer[i]}")
    user_choice = input("Your answer (A, B, C, or D): ").upper()
    if user_choice == choices[answer.index("correct")]:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

# Shuffle the order of the questions
question_keys = list(questions.keys())
random.shuffle(question_keys)

# Initialize the score
score = 0

# Ask each question and update the score
for question in question_keys:
    answer = questions[question]
    score += ask_question(question, answer)
    print()

# Display the final score
print("Game over!")
print(f"Your score: {score} out of {len(questions)}")
