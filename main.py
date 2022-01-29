import os
import sys
import datetime
import pywhatkit
import playsound
from gtts import gTTS
from random import choice
from commands import command
from contacts import contacts
import speech_recognition as sr

# list for keeping functions
list_func = []


def speak(text):
    # variable for renaming the mp3 file
    i = 0

    # voice
    tts = gTTS(text=text, lang="en")

    # variable containers voice
    filename = str("voice" + str(i) + ".mp3")

    # saves voice
    tts.save(filename)

    # plays saved sound
    playsound.playsound(filename)

    # remove previous file with voice
    os.remove(filename)


def music_func():
    # gives an opportunity to listen and understand
    r = sr.Recognizer()

    # speaks text from command dictionary
    speak(command["music"]["responses"][0])

    try:

        # open a mic
        with sr.Microphone() as source:

            # listen
            audio = r.listen(source)

            # recognize
            music = r.recognize_google(audio)

            print(music)

            while True:

                # speaks
                speak("Would you like to play " + music + "?")

                try:
                    with sr.Microphone() as source1:

                        # listen
                        audio = r.listen(source1)

                        # recognize
                        boolean = r.recognize_google(audio)

                        print(boolean)

                        if "yes" in boolean:
                            # open appropriate music in youtube
                            speak("Turning on " + music)
                            pywhatkit.playonyt(music)
                            break

                        else:
                            # restart
                            music_func()

                except sr.UnknownValueError:
                    speak("I don't understand you")
                    continue



    except sr.UnknownValueError:
        speak("I don't understand you")
        music_func()


def conversation_func():
    # speaks
    speak(choice(command["conversation"]["responses"]))


def name_func():
    # speaks
    speak(choice(command["name"]["responses"]))


def time_func():
    # speaks
    speak(choice(command["time"]["responses"]))


def history_func():
    # speaks
    speak(choice(command["history"]["responses"]))


def note_func():
    # speaks
    speak(choice(command["note"]["responses"]))

    # listens
    r = sr.Recognizer()

    try:

        # opens a mic
        with sr.Microphone() as source:

            # listen
            audio = r.listen(source)

            # recognize
            name = r.recognize_google(audio)

            print(name)


    except sr.UnknownValueError:
        # listens
        r = sr.Recognizer()


    speak("Would you love to name your file " + name + "?")


    while True:
        try:

            # opens a mic
            with sr.Microphone() as source:

                # listen
                audio = r.listen(source)

                # recognize
                answer = r.recognize_google(audio)

                print(answer)

                if "yes" in answer:
                    # creates a file
                    file = open(name + ".txt", "a")

                    # speaks
                    while True:
                        speak("What to add to your note?")

                        try:

                            # opens a mic
                            with sr.Microphone() as source1:

                                # listen
                                audio = r.listen(source1)

                                # recognize
                                text = r.recognize_google(audio)

                                print(text)

                                # writes some text into a file
                                file.write(text + "\n")

                                # speaks
                                speak("Note was added!")

                                # close the file
                                file.close()

                                break

                        except sr.UnknownValueError:
                            speak("I do not understand")
                            continue


                else:
                    note_func()

        except sr.UnknownValueError:
            speak("I do not understand")
            continue

        break


def onote_func():
    # speaks
    speak(choice(command["onote"]["responses"]))

    # listens
    r = sr.Recognizer()

    try:

        # opens a mic
        with sr.Microphone() as source:

            # listen
            audio = r.listen(source)

            # recognize
            name = r.recognize_google(audio)
            print(name)

            speak("Would you love to open a file ")
            while True:
                # speaks
                speak("Would you like to add some changes or just read the note?")

                # opens a mic
                with sr.Microphone() as source1:

                    # listen
                    audio = r.listen(source1)

                    # recognize
                    answer = r.recognize_google(audio)

                    print(answer)

                    try:

                        if "changes" in answer or "change" in answer:

                            # opens an existing file for changes
                            file = open(name + ".txt", "a")

                            # speaks
                            speak('What would you love to add to ' + name + " note")

                            # opens a mic
                            with sr.Microphone() as source2:

                                # listen
                                audio = r.listen(source2)

                                # recognize
                                change = r.recognize_google(audio)

                                print(change)

                                # write changes into the file
                                file.write(change)

                            break

                        elif "read" in answer:
                            # opens file
                            file = open(name + ".txt", "r")
                            print("-----File Content-----")
                            print(file.read())
                            print("----------------------")

                            break

                        else:
                            continue

                    except FileNotFoundError:
                        speak('No such file exists')
                        onote_func()
                        break

    except sr.UnknownValueError:
        onote_func()


def message_func():
    # speaks
    speak(choice(command["message"]["responses"]))

    # listens
    r = sr.Recognizer()

    try:
        # opens a mic
        with sr.Microphone() as source:
            # listen
            audio = r.listen(source)

            # recognize
            name = r.recognize_google(audio)

            print(name)

            for contact in contacts.keys():

                # if given name is the same with m=name from contacts list (file)
                if contact == name:

                    while True:

                        speak("What to send?")

                        try:
                            # open a mic

                            with sr.Microphone() as source1:

                                # listen
                                audio = r.listen(source1)

                                # recognize
                                said = r.recognize_google(audio)

                                speak("Would you like to send the text shown in Terminal?")

                                print(said)

                                try:
                                    # open a mic

                                    with sr.Microphone() as source2:
                                        # listen
                                        audio = r.listen(source2)

                                        # recognize
                                        answer = r.recognize_google(audio)

                                        if "yes" in answer:
                                            # send message to number, send "said", in appropriate datetime
                                            pywhatkit.sendwhatmsg(contacts[contact], said,
                                                            int(datetime.datetime.now().strftime('%H')),
                                                            int(datetime.datetime.now().strftime('%M')) + 1,
                                                            13)
                                            break

                                        else:
                                            continue
                                except sr.UnknownValueError:
                                    speak("I do not understand you")


                        except sr.UnknownValueError:
                            # listen
                            r = sr.Recognizer()

                        break

    except sr.UnknownValueError:
        # restart
        message_func()


def gratitude_func():
    # speaks
    speak(choice(command["gratitude"]["responses"]))


def health_func():
    # speaks
    speak(choice(command["health"]["responses"]))


def alarm_func():
    # speaks
    speak(choice(command["alarm"]["responses"]))

    # search for an alarm in the Internet
    pywhatkit.search("kukuklok.com")


def mail_func():
    # speaks
    speak(command["mail"]["responses"])

    # listen
    r = sr.Recognizer()

    try:
        # opens a mic
        with sr.Microphone() as source:

            # listen
            audio = r.listen(source)

            # recognize
            subject = r.recognize_google(audio)

            print(subject)

            # speaks
            speak("Tell the containing of your mail")

            try:
                # opens a mic
                with sr.Microphone() as source1:
                    # listen
                    audio = r.listen(source1)

                    # recognize
                    contain = r.recognize_google(audio)

                    print(contain)

                    # speaks
                    speak("To whome would you love to send your mail?")

                    try:
                        # opens a mic
                        with sr.Microphone() as source2:

                            # listen
                            audio = r.listen(source2)

                            # recognize
                            getter = r.recognize_google(audio)
                            print(getter)

                            # send mail                from                password   topic    your mail  to
                            pywhatkit.send_mail("akifmursalov@gmail.com", "Akif2003", subject, contain, getter)

                    except sr.UnknownValueError:
                        speak("I don't understand you")



            except sr.UnknownValueError:
                speak("I don't understand you")



    except sr.UnknownValueError:
        speak("I don't understand you")


def word(words):

    # checks all items from command dictionary
    for item in command.keys():

        # checks all items from all "patterns" for all "item"s
        for j in range(len(command[item]["patterns"])):

            # if
            if command[item]["patterns"][j] in words:

                if item != "greeting" and item != "exit":

                    for elem in command.keys():
                        list_func.append(elem)

                    index = list_func.index(item)

                    functions = [conversation_func, music_func, name_func, time_func, history_func, note_func,
                                 onote_func, message_func, gratitude_func, health_func, alarm_func, mail_func]

                    functions[index]()

                    break

                elif item == 'greeting':

                    for answer in range(0, len(command["greeting"]["patterns"])):

                        if command["greeting"]["patterns"][answer] in words:
                            speak(choice(command["greeting"]["responses"]))
                    break

                elif item == 'exit':

                    for answer in range(0, len(command['exit']["patterns"])):

                        if command['exit']["patterns"][answer] in words:
                            speak(choice(command['exit']["responses"]))

                            sys.exit(0)

                    break


def get_audio():
    speak("HELLO, NIGEL HERE TO HELP YOU!")
    r = sr.Recognizer()

    while True:

        try:

            with sr.Microphone() as source:

                audio = r.listen(source)

                said = r.recognize_google(audio)

                print(said)

                word(said)

        except sr.UnknownValueError:

            speak("I do not understand you!")

            r = sr.Recognizer()


get_audio()