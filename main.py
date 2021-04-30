import moviepy.editor as mp
import speech_recognition as sr
from os import path

print("Hi, would you like to speak into your microfone or do you want a video file processed? (mic/file)")
choice = input()

if choice == "mic":

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Try saying something!")
        audio = r.listen(source)

    try:
        f = open("text.txt", "w+")
        f.write("Contents of the sound:\n\n" + r.recognize_google(audio))
        f.close()

        print("Check your home directory!")


    except sr.UnknownValueError:
        print("Something went wrong! I didn't get what you said...")

    except sr.RequestError as e:
        print("Sorry, there has been an error, we couldn't process your request! {0}".format(e))
        

elif choice == "file":
    print("What will be the file's name with the file extension? (Your file needs to be in the same directory as this file)")
    cho_ice = input()

    video = mp.VideoFileClip(path.join(path.dirname(path.realpath(__file__)), cho_ice))
    video.audio.write_audiofile(path.join(path.dirname(path.realpath(__file__)), "audio.wav"))


    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio.wav")

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)


    try:
        f = open("text.txt", "w+")
        f.write("Contents of the video:\n\n" + r.recognize_google(audio))
        f.close()

        print("Check your home directory!")

    except sr.UnknownValueError:
        print("Something went wrong! I didn't get what it said...")

    except sr.RequestError as e:
        print("Sorry, there has been an error, we couldn't process your request! {0}".format(e))

else: 
    print("lol sorry idk what that is")
    