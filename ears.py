import speech_recognition as sr

# pysical world inteface

def calibrate_microphone() -> None:
    recognizer = sr.Recognizer()
    MICROPHONE_INDEX = 3
    with sr.Microphone(device_index=MICROPHONE_INDEX) as source:
        print("Calibrating microphone. Please remain silent...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

    print(f"Energy threshold: {recognizer.energy_threshold}")

def listen():
    recognizer = sr.Recognizer()
    MICROPHONE_INDEX = 3
    try:
        with sr.Microphone(device_index=MICROPHONE_INDEX) as source:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Listening... (Speak now)")
        text = recognizer.recognize_google(audio)
        print("processing...")
        print(f"You said: {text}")
        return text
    
    except sr.WaitTimeoutError:
        print("No speech detected (timeout)")
        return None
    except sr.UnknownValueError:
        print("Sorry i didn't quite catch that.")
        return None
    except sr.RequestError:
        print("Speech recognition service unavailable")
        return None
    except Exception as e:
        print("An error occured in listen(): ", e)
        return None
    except OSError as error:
        print(f"Microphone error: {error}")
        return None