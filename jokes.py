import pyjokes
from pytube import * 
joke1= pyjokes.get_joke(language="en",category="neutral")
print(joke1)
print(eval(input(" :")))
# a=20;b=34;c=45
# print(f"There is {a} pens in box {b} and {c}")
link="https://youtu.be/Njyx5ZuwEHI"
path="E:\Mo & WS"
myvideo=YouTube(link)
w=myvideo.streams.filter(only_audio=True)
w[2].download(path)