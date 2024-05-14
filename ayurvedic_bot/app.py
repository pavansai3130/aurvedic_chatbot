from flask import Flask, render_template, request
import random
import sys
import csv
app = Flask(__name__)
data = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hi","Hello","How are you", "What's up","greeting"],
            "responses": ["Hello!", "Hi there!", "How can I help you today?"]
        },
        {
            "tag": "headache",
            "patterns": ["I have a headache", "My head hurts", "Headache"],
            "responses": ["Godnati bhasma,Chandrakala rasa,Kamadugha rasa,Bhoonimbadi khada,Shirashooladi vajra rasa, Pathyadi khada."]
        },
        {
            "tag": "fever",
            "patterns": ["I have a fever", "I'm running a temperature", "Fever"],
            "responses": ["Amritarishtam is a fermented liquid medicine made with the ingredients as given in classical Ayurvedic text."]
        },
        {
            "tag": "cough",
            "patterns": ["I have a cough", "I can't stop coughing", "Cough"],
            "responses": ["Warm tea with honey can soothe a cough.","Mulethi is an effective Ayurvedic herb for cough."]
        },
        {
            "tag": "fatigue",
            "patterns": ["I feel tired", "I have no energy", "Fatigue"],
            "responses": ["Make sure you're getting enough sleep.", "Balanced nutrition can help combat fatigue.", "Consider light exercise to boost your energy levels."]
        },
        {
            "tag": "stomachache",
            "patterns": ["My stomach hurts", "I have a stomachache", "Stomachache"],
            "responses": ["Peppermint tea or ginger may help soothe a stomachache."]
        },
        {
            "tag": "acne",
            "patterns": ["I have acne", "Acne breakout", "Pimples","acne"],
            "responses": ["Turmeric and Honey Face Mask: Mix 1 teaspoon of turmeric powder with 2 teaspoons of honey to form a paste. Apply it to the affected areas and leave it on for 15-20 minutes before rinsing off."]
        },
        {
            "tag": "anxiety",
            "patterns": ["Feeling anxious", "Anxiety", "Stressed out","anxiety"],
            "responses": ["Ashwagandha Capsules: It is made of pure Ashwagandha root extracts, helps to boost your well-being naturally."]
        },
        {
            "tag": "asthma",
            "patterns": ["I have asthma", "Asthma attack", "Difficulty breathing"],
            "responses": ["Use your inhaler as prescribed.","Dabur's Shwaasamrit is one of the top ayurvedic medicines for asthma & bronchitis packed with the goodness of powerful herbal ingredients & medicinal plants ."]
        },
        {
            "tag": "chestpain",
            "patterns": ["I have chest pain", "Chest tightness", "Pain in my chest"],
            "responses": ["Seek emergency medical attention immediately.","Guggulu, Amalaki, Lasuna, Pushkarmoola, and Jatamasi."]
        },
        {
            "tag": "chickenpox",
            "patterns": ["I have chickenpox", "Chickenpox rash", "Itchy blisters"],
            "responses": ["Keep the affected area clean and avoid scratching.","Neem.Take 1 tsp powder mixed into a glass of water per day before meal as a nutritious drink, or as directed by the physician."]
        },
        {
            "tag": "dehydration",
            "patterns": ["I am dehydrated", "Feeling thirsty", "Dry mouth"],
            "responses": ["Drink plenty of water throughout the day.","To treat dehydration, take 2-3 tablespoons of coriander. powder in a vessel and pour 10 cups of boiling water in. it. Set it aside for 4-5 hours or overnight."]
        },
        {
            "tag": "dustallergy",
            "patterns": ["I have dust allergy", "Allergic to dust", "Sneezing and itching"],
            "responses": ["Keep living spaces clean and dust-free.", "Black Cumin,Honey,Turmeric."]
        },
        {
            "tag": "diabetes",
            "patterns": ["I have diabetes", "High blood sugar", "Diabetic symptoms"],
            "responses": ["Monitor blood sugar levels regularly.","Giloy or Guduchi powerful herb that helps manage blood sugar levels and helps to improve general immunity."]
        },
        {
            "tag": "diarrhea",
            "patterns": ["I have diarrhea", "Upset stomach", "Frequent bowel movements"],
            "responses": ["Stay hydrated by drinking plenty of fluids.","Kutaja Ghana Vati is an ancient Ayurvedic remedy for diarrhoea, used in India since at least 600 B.C.he formulation includes herbs such as Kutaja,Mustaka,Chitraka, and Haridra."]
        },
        {
            "tag": "dizziness",
            "patterns": ["I feel dizzy", "Dizziness", "Lightheadedness"],
            "responses": ["Sit or lie down in a safe place.", "sutasekara rasa taken with aamla juice and honey is very beneficial for dizzyness."]
        },
        {
            "tag": "drymouth",
            "patterns": ["I have a dry mouth", "Mouth feels dry", "Lack of saliva"],
            "responses": ["Stay hydrated by sipping water frequently.","We get relief from dry mouth by holding a few tablespoons of coconut or sesame oil in the mouth for 10 to 15 minutes without swallowing."]
        },
        {
            "tag": "earache",
            "patterns": ["I have an earache", "Ear pain", "Ear discomfort"],
            "responses": ["Avoid inserting objects into the ear.","This ayurvedic formulation treats inflammation in the ear. Mix it with honey and consume it."]
        },
        {
            "tag": "eyeirritation",
            "patterns": ["I have eye irritation", "Itchy eyes", "Redness in eyes"],
            "responses": ["The commonly used Ayurvedic medicines for eye itching are HaridraKhand, MahatraiphalaGhrta, Drakshadi Ghrita."]
        },
        {
            "tag": "flu",
            "patterns": ["I have flu", "Flu symptoms", "Feeling feverish"],
            "responses": ["Rest and stay hydrated.","Ginger Zingiber officinale."]
        },
        {
            "tag": "itching",
            "patterns": ["I have itching", "Itchy skin", "Persistent itchiness"],
            "responses": ["Karela-Jamun Ras is made up of pure Karela and Jamun juice, with no artificial additives."]
        },
        {
            "tag": "legcramps",
            "patterns": ["I have leg cramps", "Cramping in legs", "Muscle spasms"],
            "responses": ["Stretch and massage the affected muscles.","Massage the muscle with Mahanarayana taila or Praharini taila to relax it."]
        },
        {
            "tag": "migraine",
            "patterns": ["I have a migraine", "Severe headache", "Aura before headache"],
            "responses": ["Godnati bhasma, Chandrakala rasa, Bhoonimbadi khada, Shirashooladi vajra rasa, Pathyadi khada"]
        },
        {
            "tag": "loosemotion",
            "patterns": ["I have loose motions", "Watery stools", "Frequent bowel movements"],
            "responses": ["Stay hydrated with oral rehydration solutions.", "Kutajarishta is very useful Ayurvedic medicine used in the treatment of loose motion."]
        },
        {
            "tag": "nosebleed",
            "patterns": ["I have a nosebleed", "Bleeding from the nose", "Nasal bleeding"],
            "responses": ["Fine powder of alum (spatika/phitkari) along with cow ghee, instilled in the form of nasal drops, will stop bleeding"]
        },
        {
            "tag": "obesity",
            "patterns": ["I am obese", "Struggling with weight", "Obesity"],
            "responses": ["Herbal remedies such as Triphala, Guggul, and Vidanga are commonly used to reduce excess fat and improve digestion."]
        },
        {
            "tag": "sunburn",
            "patterns": ["I have sunburn", "Sunburned skin", "Red and painful skin"],
            "responses": ["Cool the affected area with a cold compress.","Mix equal amounts of powdered sandalwood and turmeric with a little cool water and apply the paste to the sunburn."]
        },
        {
            "tag": "skinrash",
            "patterns": ["I have a skin rash", "Rash on skin", "Itchy skin"],
            "responses": ["neem, turmeric, aloe vera gel, oatmeal bath, essential oils"]
        },
        {
            "tag": "throatpain",
            "patterns": ["I have throat pain", "Sore throat", "Painful swallowing"],
            "responses": ["Gargle with warm saltwater.","Mulethi. This Ayurvedic plant is useful for sore throat problems."]
        },
        {
            "tag": "toothdecay",
            "patterns": ["I have tooth decay", "Toothache", "Cavity pain"],
            "responses": ["Triphala Churna is a powdered version of the triphala herb."]
        },
        {
            "tag": "tuberculosis",
            "patterns": ["I have tuberculosis", "TB symptoms", "Persistent cough"],
            "responses": ["TB in Ayurveda include ashwagandha, turmeric and neem"]
        },
        {
            "tag": "vomiting",
            "patterns": ["I am vomiting", "Vomiting", "Feel nauseous"],
            "responses": ["In nausea, Lavangadi Vati, Eladi Vati, Amalaki Rasayana, Ardraka khanda"]
        },
        {
            "tag": "bodypain",
            "patterns": ["I have body pain", "Body pain", "Aching muscles"],
            "responses": ["natural painkillers in Ayurveda include Brahmi, Yavani, Jatamansi, and Haritaki. Taking natural painkillers is the best because it does not cause any side effects"]
        }
        # Add more intents as needed
    ]
}
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
