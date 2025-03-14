import random

def generate_emoji(keyword: str) -> str:
    """
    Returns an emoji based on the user's input keyword.

    :param keyword: A string describing the emotion (e.g., "laugh", "cry").
    :return: A string containing an emoji.
    """
    emoji_dict = {
        "laugh": ["😂", "🤣", "😆", "😁"],
        "cry": ["😢", "😭", "😿"],
        "love": ["❤️", "😍", "😘", "💖"],
        "angry": ["😡", "😠", "🤬"],
        "happy": ["😊", "😃", "😄", "😁"],
        "sad": ["😞", "😔", "😟", "😢"],
        "surprised": ["😲", "😱", "🤯"],
        "cool": ["😎", "🕶️", "😏"],
        "confused": ["😕", "🤨", "😵"],
        "sleepy": ["😴", "💤", "🥱"]
    }

    # Convert input to lowercase and fetch emoji list
    emojis = emoji_dict.get(keyword.lower(), ["🤔"])  # Default to 🤔 if not found
    
    # Return a random emoji from the category
    return random.choice(emojis)


# Example usage
if __name__ == "__main__":
    user_input = input("Enter an emotion (laugh, cry, love, etc.): ")
    print("Your emoji:", generate_emoji(user_input))
