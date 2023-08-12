import os
import openai

openai.api_key = "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"  # Make sure to reset this key since you've exposed it.

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

while True:
    ask = input("Enter : ")
    if ask == "break":
        print("thank you")
        break
    else:
        response = openai.Completion.create( 
            model="text-davinci-003",
            prompt=ask,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human: ", " AI:"]
        )
        # You probably want to print the response or do something with it.
        print(response.choices[0].text.strip())  # This will print the AI's response.
