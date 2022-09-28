from tinytag import TinyTag

# Pass the filename into the
# Tinytag.get() method and store
# the result in audio variable
import math
import time

path = "C:/Users/Abraham/Videos/Test_Cinemasimi.mp4"
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

audio = TinyTag.get(path)

# Use the attributes
# and Display
print("Peso del video: " + convert_size(audio.filesize))
print("Duración del video: " + time.strftime('%H:%M:%S', time.gmtime(audio.duration)))
print("Formato de video: " + path[len(path)-4:])