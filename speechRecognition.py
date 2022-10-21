import speech_recognition as sr
import moviepy.editor as mp
import os

def getFolder(path):
    pathBase = os.path.dirname(path)
    return pathBase

def recognize(path):
    print(path)
    my_clip = mp.VideoFileClip(path)
    my_clip.audio.write_audiofile(r"tmp_audio.wav")
    r = sr.Recognizer()
    tmp = sr.AudioFile("tmp_audio.wav")
    with tmp as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)

    recog = r.recognize_google(audio, language= 'es-MX')

    path_base = getFolder(path)
    #print(path_base)

    #text_file = open(path_base+"\\data.txt", "w")
    #text_file.write(recog)
    #text_file.close()

    os.remove("tmp_audio.wav")

    #return print("Se generó el txt con el audio reconocido.")

from vosk import  Model, KaldiRecognizer
import wave
import json


def recognize2(path):
    my_clip = mp.VideoFileClip(path)
    my_clip.audio.write_audiofile(r"tmp_audio.wav")

    wf = wave.open("tmp_audio.wav", "rb")
    model = Model(r'vosk-es')
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    results = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            results.append(part_result)
    part_result = json.loads(rec.FinalResult())
    results.append(part_result)

    path_base = getFolder(path)

    text = ''
    for r in results:
        text += r['text'] + ' '

    text_file = open(path_base+"\\data1.txt", "w")
    text_file.write(text)
    text_file.close()
    os.remove("tmp_audio.wav")
    print(results)
    return print("Se generó el txt con el audio reconocido.")


