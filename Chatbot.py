# Build a simple chatbot that responds to user inputs based on
# predefined rules. Use if-else statements or pattern matching
# techniques to identify user queries and provide appropriate
# responses. This will give you a basic understanding of natural language processing and conversation flow.
import random
def chatbot():
    print("Hello! I am your helpful chatbot. How can I assist you today?")
    
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised!",
        "Why don’t some couples go to the gym? Because some relationships don’t work out!"
    ]
    
    songs = [
        "Blinding Lights - The Weeknd",
        "Shape of You - Ed Sheeran",
        "Levitating - Dua Lipa",
        "Stay - Justin Bieber & The Kid LAROI",
        "Good 4 U - Olivia Rodrigo",
        "Save Your Tears - The Weeknd",
        "Peaches - Justin Bieber feat. Daniel Caesar & Giveon",
        "Heat Waves - Glass Animals"
    ]
    
    while True:
        user_input = input("You: ").lower() 

      
        if user_input in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a wonderful day!")
            break
      
        elif user_input in ['hi', 'hello', 'hey']:
            print("Chatbot: Hello! How can I assist you today?")
    
        elif 'your name' in user_input:
            print("Chatbot: I am a chatbot without a personal name. You can call me Chatbot!")
 
        elif 'weather' in user_input:
            print("Chatbot: I am unable to check real-time weather, but you can visit any weather app or website like 'weather.com'.")
        
      
        elif 'science' in user_input:
            print("Chatbot: Science is the study of the natural world through observation and experiment. Key fields include physics, biology, chemistry, and earth science.")
  
        elif 'technology' in user_input:
            print("Chatbot: Technology refers to the application of scientific knowledge for practical purposes. It encompasses fields like computing, AI, electronics, and biotechnology.")

        elif 'mathematics' in user_input or 'math' in user_input:
            print("Chatbot: Mathematics is the abstract science of numbers, quantities, and shapes. Some branches include algebra, calculus, and geometry.")

        elif 'history' in user_input:
            print("Chatbot: History is the study of past events, particularly human activities. Key events include the rise and fall of civilizations, world wars, and significant cultural shifts.")

        elif 'who is' in user_input or 'who was' in user_input:
            name = user_input.replace('who is', '').replace('who was', '').strip()
            if name == 'albert einstein':
                print("Chatbot: Albert Einstein was a theoretical physicist known for developing the theory of relativity, one of the two pillars of modern physics.")
            elif name == 'isaac newton':
                print("Chatbot: Sir Isaac Newton was an English mathematician and physicist who is widely recognized for his laws of motion and universal gravitation.")
            elif name == 'martin luther king':
                print("Chatbot: Dr. Martin Luther King Jr. was an American civil rights leader who advocated for racial equality and justice. He is famous for his 'I Have a Dream' speech.")
            else:
                print(f"Chatbot: Sorry, I don't have information on {name}.")

        elif 'fun fact' in user_input:
            print("Chatbot: Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!")

        elif 'help' in user_input or 'advice' in user_input:
            print("Chatbot: I'd be happy to help! Please provide more details on what you need help with.")

        elif 'inspiration' in user_input or 'quote' in user_input:
            print("Chatbot: 'The only way to do great work is to love what you do.' - Steve Jobs")

        elif 'thank you' in user_input:
            print("Chatbot: You're welcome! I'm happy to assist.")

        elif 'joke' in user_input:
            joke = random.choice(jokes)
            print(f"Chatbot: Here's a joke for you: {joke}")

        elif 'song' in user_input or 'music' in user_input or 'suggest song' in user_input:
            song = random.choice(songs)
            print(f"Chatbot: How about listening to '{song}'? It's a great track!")

        else:
            print("Chatbot: I'm sorry, I didn't quite understand that. Could you rephrase or ask about something else?")

chatbot()
