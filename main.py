import random

class TriviaQuiz:
    def __init__(self):
        self.questions = {
            "What is the capital of France?": ["Paris", "Berlin", "Madrid", "Rome"],
            "Which planet is known as the Red Planet?": ["Mars", "Jupiter", "Saturn", "Venus"],
            "Who painted the Mona Lisa?": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
            "What is the largest mammal in the world?": ["Blue whale", "Elephant", "Giraffe", "Hippopotamus"],
            "Which country is famous for its tulips and windmills?": ["Netherlands", "Italy", "Australia", "Canada"]
        }
        self.score = 0
        self.max_questions = 5  # Number of questions to ask
        self.current_questions = random.sample(list(self.questions.keys()), self.max_questions)
    
    def display_question(self, question):
        print(question)
        options = self.questions[question]
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
    
    def play_game(self):
        print("Welcome to the Trivia Quiz!")
        print("Answer each question by entering the number of your choice.")
        
        for question in self.current_questions:
            self.display_question(question)
            user_answer = input("Your answer (1-4): ").strip()
            
            if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
                correct_answer_index = self.questions[question].index(self.questions[question][0]) + 1
                if int(user_answer) == correct_answer_index:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Sorry, the correct answer was {self.questions[question][0]}.")
            else:
                print("Invalid input! Please enter a number from 1 to 4.")
        
        print(f"\nQuiz complete! Your final score is: {self.score}/{self.max_questions}")

if __name__ == "__main__":
    game = TriviaQuiz()
    game.play_game()
