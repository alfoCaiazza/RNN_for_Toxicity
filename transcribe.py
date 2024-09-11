from speech_recognition import Recognizer, Microphone


def get_audio():
    r = Recognizer()

    #Setting local microphone as sound source
    with Microphone() as source:
        print("Ready to listen ... ")
        # Recognizer is goins to create an mp3 file with the sound detected by the source
        audio =  r.listen(source)

        # Conver speech to text
        text = r.recognize_google(audio)

        return(text)