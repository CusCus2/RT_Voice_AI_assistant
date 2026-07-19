import ollama
import time

def think(text: str):
    if not text:
        return None
    
    start = time.perf_counter()
    print("Thinking....")

    try:
        response = ollama.chat(
            model="llama3",
            messages= [
                {
                    "role" : "user",
                    "content" : text,
                }
            ],
        )
        response_text = response["message"]["content"]
        latency = time.perf_counter() - start
        print(f"AI: {response_text}")
        print("Latency: ", latency)
        return response_text
    
    except Exception as e:
        print("An error occured in think(): ", e)
        return "Sorry, something went wrong with thinking."