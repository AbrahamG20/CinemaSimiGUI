import speech_recognition as sr
from moviepy.editor import VideoFileClip
import os
import re

def getFolder(path):
    pathBase = os.path.dirname(path)
    return pathBase

def recognize(path):
    my_clip = VideoFileClip(path)
    my_clip.audio.write_audiofile(r"tmp_audio.wav")
    r = sr.Recognizer()
    tmp = sr.AudioFile("tmp_audio.wav")
    with tmp as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)

    recog = r.recognize_google(audio, language= 'es-MX')
    os.remove("tmp_audio.wav")

    return recog


#texto = "Ya que conteste todas tus preguntas tengo muchos para ti para empezar me lo firmo como sudas cuando acabes quieres firmarlo eres mi vengador favorito Por cierto estás bien  Sí claro En serio estoy muy bien de verlos a ellos"

def sentences(text):
    text = str(text)
    newText = text[0].upper() + text[1:]
    fragments = re.findall('[A-Z][^A-Z]*', newText)
    finalText = []

    for i in range(len(fragments)):
        w = 5
        count = 0
        for word in fragments[i].split():
            count+=1
            words = fragments[i].split()
        if count > w:
            nmb = round(count/w)
            for j in range(nmb):
                ini = w * j
                fin = (j+1) * w
                sentence = words[ini:fin]
                sentence = " ".join(sentence)
                finalText.append(sentence)
        else:
            finalText.append(fragments[i])
    return finalText


#path = "C:\\Users\\Abraham\\Videos\\Captures\\prueba.mp4"

#recog = recognize(path)
#print(sentences(recog))
