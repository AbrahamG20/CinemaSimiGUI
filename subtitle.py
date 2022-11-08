from moviepy.editor import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
import os
from tinytag import TinyTag
from speechRecognition import sentences, recognize
from machineTranslation import translate

generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')

def Subtitle1(subs, videoPath):
    subtitles = SubtitlesClip(subs, generator)
    video = VideoFileClip(videoPath)
    result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

    result.write_videofile("output.mp4", fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac", verbose= False)

#texto = "Ya que conteste todas tus preguntas tengo muchos para ti para empezar me lo firmo como sudas cuando acabes quieres firmarlo eres mi vengador favorito Por cierto estás bien  Sí claro En serio estoy muy bien de verlos a ellos"
#path = "C:\\Users\\Abraham\\Videos\\Captures\\prueba.mp4"

def getSubs(videoPath):
    video = TinyTag.get(videoPath)
    lenght = int(video.duration)
    subs = []
    recog = recognize(videoPath)
    #recog = "Ya que conteste todas tus preguntas tengo muchos para ti para empezar me lo firmo como sudas cuando acabes quieres firmarlo eres mi vengador favorito Por cierto estás bien  Sí claro En serio estoy muy bien de verlos a ellos"
    sents = sentences(recog)
    result = translate(sents)
    calc = lenght//len(result)
    leng = round(lenght/calc)
    for i in range(leng):
        try:
            appen = ((i*2,i*2+1),result[i])
            subs.append(appen)
        except IndexError:
            appen = ((i * 2, i * 2 + 1), result[len(result)-1])
            subs.append(appen)
    return subs

#print(getSubs(path))

def subtitle(videoPath):
    generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')

    subs = getSubs(videoPath)
    subtitles = SubtitlesClip(subs, generator)

    folder = os.path.dirname(videoPath)
    outPath = folder+"\\tempOutput.mp4"
    video = VideoFileClip(videoPath)

    result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

    result.write_videofile(outPath, fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True,
                              codec="libx264", audio_codec="aac")

def subtitle2(videoPath, folderPath, quality):
    generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')

    subs = getSubs(videoPath)
    subtitles = SubtitlesClip(subs, generator)

    base = os.path.basename(videoPath)
    outPath = folderPath + "\[SUB] " + base

    video = VideoFileClip(videoPath)
    result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

    result.write_videofile(outPath, fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True,
                              codec="libx264", audio_codec="aac")

#ruta = r"C:\\Users\\Abraham\\Videos\\prueba.mp4"
