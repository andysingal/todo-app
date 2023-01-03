import json
FILENAME = "../file/questions.json"
with open(FILENAME,"r") as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question['question_text'])
    for index,alternatives in enumerate(question["alternatives"]):
          print(index + 1,"-", alternatives)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice




for index,question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{result}: {index + 1}Your answer: {question['user_choice']}, " \
       f"Correct Answer: {question['correct_answer']}"
    print(message)

# print(data)
print(score, "/", len(data))




