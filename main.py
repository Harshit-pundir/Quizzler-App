from ui import QuizInterface
from quiz_brain import QuizBrain
from data import question_data  # This should fetch data from API or static list

# Step 1: Initialize the quiz logic handler
quiz = QuizBrain(question_data)

# Step 2: Launch the UI
quiz_ui = QuizInterface(quiz)
