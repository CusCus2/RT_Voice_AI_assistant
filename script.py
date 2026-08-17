import brain as br
import ears as er
import mouth as mt

def main():
    print("--- Voice Assistant Started ---")
    print("Calibrating ...")
    recognizer = er.calibrate_microphone()
    mt.speak("Hello, I am ready. You can start speaking.")

    while True:
        print("executing listen")
        user_input = er.listen(recognizer)

        if not user_input:
            print("nothing heard")
            continue
        
        if user_input.lower().strip() in ["exit", "stop", "quit"]:
            mt.speak("Goodbye")
            print("Exiting....")
            break

        ai_response = br.think(user_input)
        mt.speak(ai_response)

if __name__ == "__main__":
    main()
