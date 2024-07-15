import pyttsx3

def initialize_engine():
   
    engine = pyttsx3.init()
    return engine

def speak(engine, text):
    
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    engine = initialize_engine()
    print("Welcome to RoboSpeaker")
    while True:
        x = input("Enter your text: ")
        if x.lower() == "exit":
            speak(engine, "Bye, I am going")
            break
        speak(engine, x)
