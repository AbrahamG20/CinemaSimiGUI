from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from tinytag import TinyTag

generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')

def Subtitle1(subs, videoPath):
    subtitles = SubtitlesClip(subs, generator)
    video = VideoFileClip(videoPath)
    result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

    result.write_videofile("output.mp4", fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

def getSubs(videoPath):
    video = TinyTag.get(videoPath)
    lenght = int(video.duration)
    subs = []
    for i in range(lenght):
        appen = ((i,i+1),"Texto de prueba "+ str(i))
        subs.append(appen)
    return subs

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
    outPath = folderPath + "\SUB_" + base

    video = VideoFileClip(videoPath)
    result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

    result.write_videofile(outPath, fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True,
                              codec="libx264", audio_codec="aac")

#ruta = r"C:\\Users\\Abraham\\Videos\\prueba.mp4"
