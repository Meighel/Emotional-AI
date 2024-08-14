from textblob import TextBlob
import random

# Responses based on sentiment
positive_responses = ["That's great to hear!", "I'm glad you're feeling positive.", "Awesome!", "Enjoy your day!", "Even there is a dark parts in life, we can still see how beautiful it is."]
down_responses = ["I'm sorry to hear that.", "That must be tough.", "Things will get better soon."]
scared_responses = ["It is okay, let them flow.", "Focus on your breathing, slowly count 1, 2, 3.", "You can sit on the ground for a moment."]
regret_responses = ["Have self-compassion, we are mere humans after all", "People only do what makes them less miserable", "Forgive yourself, beacuse you are the only one who can give pure chances to yourself", "Take everything as it was, and use it a merit of growth", "Don't beat yourself too hard, there is more to life than living in the past"]
jealous_responses = ["If you feel that way, try to do it yourself instead of just watching other doing what you want", "Take a deep break, not every feeling needs to be acted on to be resolved", "Try to focus on yourself and find the truth within you"]
pride_responses = ["You don't have to let go that fast, but also don't get stuck", "Be kind to others and to yourself", "They are just humans too, but it's up to you what you can tolerate"]


neutral_responses = ["That's interesting.", "Okay.", "I see."]

comfort_response = ["I am glad you can see the light after all", "You are being a tough cookie, you got this!", "You are embracing realness of humanity, the bad and the good side"]
reassuring_response = ["It's okay, you are going to be all right", "This feelings only come and go", "You always have that courage in you"]


emotion_list = ["Happy", "Sad", "Anxious", "Fear", "Jealousy", "Guilt", "Shame", "Remorse", "Prideful", "Thankful", "Grieving", "Calm"]

# Analyze sentiment and respond based on the type of emotion
class AnalyzeProblem:
    @staticmethod
    def positive(user_input):
        return random.choice(positive_responses)

    @staticmethod
    def scared(user_input):
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        if sentiment <= 0:
            return random.choice(scared_responses)
        elif sentiment > 0:
            return random.choice(reassuring_response)


    @staticmethod
    def down(user_input):
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        if sentiment <= 0: 
            return random.choice(down_responses)
        elif sentiment > 0:
            return random.choice(comfort_response)

    @staticmethod
    def regret(user_input):
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        if sentiment <= 0:
            return random.choice(regret_responses)
        elif sentiment > 0:
            return random.choice(comfort_response)

    @staticmethod    
    def jealous(user_input):
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        if sentiment <= 0:
            return random.choice(jealous_responses)
        elif sentiment > 0:
            return random.choice(reassuring_response)

    @staticmethod
    def pride(user_input):
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        if sentiment <= 0:
            return random.choice(pride_responses)
        elif sentiment > 0:
            return random.choice(neutral_responses)
    

# List available emotions
def choice_feeling():
    print("Please choose an emotion from the list below:\n")
    for emotion in emotion_list:
        print(emotion)

def get_response_based_on_emotion(emotion, user_input):
    if emotion in ["Happy", "Thankful", "Calm"]:
        return AnalyzeProblem.positive(user_input)
    elif emotion in ["Sad", "Grieving"]:
        return AnalyzeProblem.down(user_input)
    elif emotion in ["Anxious", "Fear"]:
        return AnalyzeProblem.scared(user_input)
    elif emotion in ["Guilt", "Shame", "Remorse"]:
        return AnalyzeProblem.regret(user_input)
    elif emotion in ["Jealousy"]:
        return AnalyzeProblem.jealous(user_input)
    elif emotion in ["Prideful"]:
        return AnalyzeProblem.pride(user_input)
    else:
        return random.choice(neutral_responses)

# Main interaction
def main():
    choice_feeling()
    
    user_emotion = input("Please choose an emotion from the list above: ").capitalize()
    if user_emotion.lower() in ['exit', 'quit', 'bye', 'goodbye']:
        print("Goodbye!")
        return
    if user_emotion not in emotion_list:
        print("Please choose a valid emotion from the list.")
        return
    
    user_rant = input("How can I help you today? Feel free to rant: ")
    if user_rant.lower() in ['exit', 'quit', 'bye', 'goodbye']:
        print("Goodbye!")
        return
    
    response = get_response_based_on_emotion(user_emotion, user_rant)
    print(response)

if __name__ == "__main__":
    main()

    while True:
        choice = input("Would you like to talk with us again? (yes/no) ")
        if choice == "yes":
            main()
        elif choice in ['no', 'exit', 'quit', 'bye', 'goodbye']:
            exit
        else:
            exit