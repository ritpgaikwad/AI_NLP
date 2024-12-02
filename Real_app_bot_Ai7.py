import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm good, thank you!", "I'm doing great!"]),
    (r"my name is (.*)", ["Hello %1, nice to meet you!"]),
    (r"(.*) your name?", ["I'm a chatbot created for fun!"]),
    (r"quit", ["Goodbye! Take care."])
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

# Start the conversation
chatbot.converse()
