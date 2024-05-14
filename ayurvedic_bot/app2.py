from flask import Flask, render_template, request
import random
import sys
import csv
app = Flask(__name__)
def load_data_from_csv(csv_file):
    intents_data = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            intents_data.append({
                'tag': row['tag'],
                'patterns': row['patterns'].split(','),
                'responses': row['responses'].split(',')
            })
    return {'intents': intents_data}

data = load_data_from_csv('intents_data.csv')
def get_response(user_input):
    user_input = user_input.lower()
      # Check for the exit command
    if user_input == 'exit':
        print("Chatbot terminated.")
        sys.exit()
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(intent["responses"])
    return "I'm sorry, I'm not sure how to help with that. It's always best to consult with a healthcare professional."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']

    response = get_response(user_input)
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)
