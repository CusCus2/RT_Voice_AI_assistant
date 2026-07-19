import pyttsx3

def speak(text: str):
    if not text:
        return None
    
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        if voices:
            engine.setProperty("voice", voices[1].id)
        
        engine.setProperty("rate", 175)
        engine.say(text)
        engine.runAndWait()
    
    except Exception as e:
        print("an error occuredd in speak(): ", e)
        