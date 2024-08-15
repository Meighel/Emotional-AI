from textblob import TextBlob
import random

responses = {
    "positive": [
        "That's great to hear!",
        "I'm glad you're feeling positive.",
        "Awesome!",
        "Enjoy your day!",
        "Even in dark times, we can still see how beautiful life is."
    ],
    "down": [
        "I'm sorry to hear that.",
        "That must be tough.",
        "Things will get better soon."
    ],
    "scared": [
        "It's okay, let the feelings flow.",
        "Focus on your breathing, slowly count 1, 2, 3.",
        "You can sit on the ground for a moment."
    ],
    "regret": [
        "Have self-compassion; we are mere humans after all.",
        "People only do what makes them less miserable.",
        "Forgive yourself, because you are the only one who can give yourself pure chances.",
        "Take everything as it was, and use it as a merit for growth.",
        "Don't beat yourself too hard; there's more to life than living in the past."
    ],
    "jealous": [
        "If you feel that way, try to do it yourself instead of just watching others do what you want.",
        "Take a deep breath; not every feeling needs to be acted on to be resolved.",
        "Try to focus on yourself and find the truth within you."
    ],
    "pride": [
        "You don't have to let go that fast, but also don't get stuck.",
        "Be kind to others and to yourself.",
        "They are just humans too, but it's up to you what you can tolerate."
    ],
    "neutral": ["That's interesting.", "Okay.", "I see."],
    "comfort": [
        "I'm glad you can see the light after all.",
        "You're being a tough cookie; you've got this!",
        "You are embracing the realness of humanity, both the bad and the good sides."
    ],
    "reassuring": [
        "It's okay, you're going to be all right.",
        "These feelings only come and go.",
        "You always have that courage in you."
    ]
}

emotion_list = ["Happy", "Sad", "Anxious", "Fear", "Jealousy", "Guilt", "Shame", "Remorse", "Prideful", "Thankful", "Grieving", "Calm"]


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
