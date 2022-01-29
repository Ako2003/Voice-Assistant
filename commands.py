import datetime

command = {
    "conversation":
        {"patterns":["how old are you"],
         "responses": ["I am much more younger than you!", "It is not you deal, cute!", "50000 bytes"]},
    "music":
        {"patterns":["play music", "turn on music"],
         "responses": ["Which music who you like to listen?"],
         },
    "name":
        {"patterns":["what's your name"],
         "responses": ["My name is Nigel"],
         },
    "time":
        {"patterns": ["what's time now", "could you tell the time"],
         "responses": ["Current time is " + datetime.datetime.now().strftime('%d,%H:%M')],
         },
    "history":
        {"patterns":["talk about yourself"],
         "responses": ["I am a Voice Assistant! I help people to do different tasks, to create notes, turn on music and etc. Could I do something for you?"]},
    "note":
        {"patterns":["create a file"],
         "responses":["Give a name to your file!"]},
    "onote":
        {"patterns":["open a file","open the file"],
         "responses":["Which file would you like to open?"]},
    "message":
        {"patterns":["send a message"],
         "responses":["To whom would you like to send a message?"]},
    "gratitude":
        {"patterns":["thank you", "thanks"],
         "responses":["You are welcome!", "Don't thank, that is my business"]},
    "health":
        {"patterns":["how are you"],
         "responses":["I am fine and you?", "Better than yesterday", "I do not have any feelings"]},
    "alarm":
        {"patterns":["put an alarm"],
         "responses":["Putting an alarm"]},
    "mail":
        {"patterns":["send a mail","send email"],
         "responses":["Give a subject to your mail"]},
    "exit":
        {"patterns":["bye", "goodbye", "exit", "quit", "good night"],
         "responses": ["Bye. Have a good day!"]},
    "greeting":
        {"patterns":["what's up", "how is it going", "good day"],
         "responses": ["Hello! I am a Voice Assistant. What can I do for you?"]}
}
