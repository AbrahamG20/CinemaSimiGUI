import speech_recognition as sr
import moviepy.editor as mp
import os

#ruta = r"C:\\Users\\Abraham\\Videos\\prueba.mp4"

def getFolder(path):
    pathBase = os.path.dirname(path)
    return pathBase

def recognize(path):
    my_clip = mp.VideoFileClip(path)
    my_clip.audio.write_audiofile(r"tmp_audio.wav")
    r = sr.Recognizer()
    tmp = sr.AudioFile("tmp_audio.wav")
    with tmp as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    recog = r.recognize_google(audio, language= 'es-MX')
    path_base = getFolder(path)
    text_file = open(path_base+"\\data.txt", "w")
    text_file.write(recog)
    text_file.close()
    os.remove("tmp_audio.wav")
    return print("Se generó el txt con el audio reconocido.")

