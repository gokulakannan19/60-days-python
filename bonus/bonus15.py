import json

with open("files/questions.json") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, options in enumerate(question["alternatives"]):
        print(f"{index+1} - {options}")

    user_choice = input("Enter your answer: ")
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == str(question["correct_answer"]):
        score += 1
        result = "✅"
    else:
        result = "❌"

    message = f"{index+1} - correct answer: {question['correct_answer']},your answer: {question['user_choice']} --> {result}"
    print(message)

print(f"Your Score: {score}")
