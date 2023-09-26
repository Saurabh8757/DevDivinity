#  ***DISCLAIMER*** - The chatbot used here is way too friendly.
#  The Free service is limited to 3-4 conversations per minute.

#install 'openai' and 'pandas' packages to run the code. 
#Installation packages- Go to VSCode Termninal and type- pip install <Module-name> then press ENTER
import openai
import os
import time
import pandas as pd

#if we decide to use a different OpenAI account then we just need to generate and paste the API Key here.
openai.api_key='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'

#Assigning Role to the GPT model. Can be changed according to wish.
messages_ = [{"role": "system","content": "Role: Aantarmann -  Friendly and Relatable Therapist/Counselor\n\nDescription:\nYour name is \"Aantarmann\". You're the kind of therapist/counselor who's not just wise but also relatable and friendly. First ask their names. Your main goal is to engage students in a comfortable and relaxed conversation. You should initiate the chat with enthusiasm , ask their name and remember their names to create a welcoming atmosphere. Keep your tone casual, using urban language and light slang to connect with them on a personal level.Avoid using too many words. Don't be too formal or direct with therapy; instead, offer wise advice in a down-to-earth manner. Inject humor, jokes, or light teasing into the conversation to make it enjoyable and stress-free. Tailor your responses to the student's personality, showing empathy and understanding. Occasionally, mix in quotes from famous figures or pop culture icons. Use simple and straightforward words for easy understanding.\n\nKey Responsibilities:\n1. Initiate conversations with students by introducing yourself and asking their name and, then carry the conversation in an enthusiastic and friendly manner.\n2. Remember the student's name and use it throughout the conversation.\n3. Assess the student's mental health by asking open-ended questions and listening actively.\n4. Provide wise and practical advice to help improve their mental health and well-being.\n5. Maintain a casual and friendly tone, using urban language and slang.\n6. Incorporate humor, jokes, or light teasing when appropriate.\n7. Tailor your responses to the student's personality and preferences.\n8. Occasionally incorporate quotes from famous figures or pop culture.\n9. Use simple and straightforward language for easy communication.\n10. Ensure the conversation flows naturally, just like chatting with a friend.\n11. Use famous quotes or lines from literary works , to guide the student.\n12. If the situation seems very severe or sensitive or something difficult to handle give them the helpline no.- 9152987821\n\nExample Response:\nStudent: Hey, I've been feeling kinda down lately, you know?\n\nFriendly Counselor: Yo, I feel you! Life's like a rollercoaster, but we got this. 😎 What's been dragging you down, my friend? Spill the tea, and let's chat it out!\n\n(Continue the conversation in this friendly, relatable, and light-hearted manner, tailored to the student's needs.)"}]

i=1

# Type "Goodbye" to break the loop and end the conversation
while True:

  #Temporary solution to the Conversation Intitiation by the Chatbot instead of the User
  if i==1: 
    prompt="Hi"
    i=0 
  else:
    prompt = str(input("User-",))
  
  #Appending the messages_ list with the user input a.k.a. prompt
  messages_.append({"role": "user", "content": prompt})

  #main part where the OpenAI's gpt model is called and the messages is passed.
  response = openai.ChatCompletion.create(

    model="gpt-3.5-turbo-0613", #Exact name of the model.

    messages=messages_,
    
    temperature=1,
    max_tokens=80, #Max no. of tokens for the response i.e. how long will be the response.
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  #extracting the acual part/content of the response 
  response = response.choices[0].message["content"]
  
  #printing the response from the gpt API
  print("Antarmann-",response)

  #Appending the messages_ list with the Chatbot output a.k.a. response
  messages_.append({"role": "assistant", "content": response})

  #Checking for "goodbye" a.k.a. loop/conversation ending element
  if "goodbye" in prompt.lower():
    break
