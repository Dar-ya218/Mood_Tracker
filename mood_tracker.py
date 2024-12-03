def get_mood_emoji(mood):
    emojis = {
        1: "😫",
        2: "😕",
        3: "😊",
        4: "😃",
        5: "🤩"
    }
    return emojis.get(mood, "🤔")

def get_mood_message(mood):
    messages = {
        1: "Cheer up! At least you're not a Windows update!",
        2: "Could be worse... you could be debugging CSS!",
        3: "Perfectly balanced, as all things should be!",
        4: "Look at you, spreading joy like a WiFi router spreads signals!",
        5: "You're so bright, you're making the sun jealous!"
    }
    return messages.get(mood, "You're feeling... indescribable?")