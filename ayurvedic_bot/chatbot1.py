import random

data = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hi", "Hello", "How are you", "What's up"],
            "responses": ["Hello!", "Hi there!", "How can I help you today?"]
        },
        {
            "tag": "headache",
            "patterns": ["I have a headache", "My head hurts", "Headache"],
            "responses": ["You might be dehydrated. Try drinking more water.", "Consider taking a break and resting for a while.", "Over-the-counter pain relievers could help."]
        },
        {
            "tag": "fever",
            "patterns": ["I have a fever", "I'm running a temperature", "Fever"],
            "responses": ["Rest is crucial. Make sure to stay hydrated.", "You may want to consult a doctor if the fever persists.", "Over-the-counter fever reducers may help."]
        },
        {
            "tag": "cough",
            "patterns": ["I have a cough", "I can't stop coughing", "Cough"],
            "responses": ["Warm tea with honey can soothe a cough.", "Avoid irritants, and consider cough syrups for relief.", "Consult a doctor if the cough persists."]
        },
        {
            "tag": "fatigue",
            "patterns": ["I feel tired", "I have no energy", "Fatigue"],
            "responses": ["Make sure you're getting enough sleep.", "Balanced nutrition can help combat fatigue.", "Consider light exercise to boost your energy levels."]
        },
        {
            "tag": "stomachache",
            "patterns": ["My stomach hurts", "I have a stomachache", "Stomachache"],
            "responses": ["Avoid heavy or spicy meals.", "Peppermint tea or ginger may help soothe a stomachache.", "Consult a doctor if the pain persists."]
        },
        {
            "tag": "allergies",
            "patterns": ["I have allergies", "Allergic reaction", "Sneezing and itching"],
            "responses": ["Identify and avoid allergens as much as possible.", "Consider taking antihistamines for relief.", "Consult with an allergist for a comprehensive evaluation."]
        },
        {
            "tag": "insomnia",
            "patterns": ["I can't sleep", "Insomnia", "Trouble sleeping"],
            "responses": ["Establish a bedtime routine and create a comfortable sleep environment.", "Avoid caffeine and electronic devices before bedtime.", "If insomnia persists, consult a healthcare professional."]
        },
        {
            "tag":"help",
            "patterns":["I need help","Can you help me","I need your assistance"],
            "response":["how can i help you","Sure i can help you","Explain me"]
        },
        # Add more intents as needed
    ]
}

def get_response(user_input):
    user_input = user_input.lower()
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(intent["responses"])
    return "I'm sorry, I'm not sure how to help with that. It's always best to consult with a healthcare professional."

# Chatbot loop
while True:
    user_input = input("User: ")
    
    # Check if the user wants to stop
    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Chatbot: Goodbye!")
        break
    
    response = get_response(user_input)
    print("Chatbot:", response)

