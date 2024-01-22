import zipfile
import time
import os
import json
import pandas as pd
import webbrowser
from apath import theJson, theCSV
from convertToJSON import gen_json

#jsonGenFolder path is os.path.dirname(__file__)
myPath = os.path.dirname(__file__)
sourcePath = os.path.join(myPath, "source")

def processLink(times, item):
    pr = item.split('/')[-2]
    tt = "dl.stickershop.line.naver.jp/products/0/0/1/" + pr + "/iphone/stickers@2x.zip"
    webbrowser.open(tt)

def unZip(path):    
    with zipfile.ZipFile(os.path.join(path, "stickers@2x.zip"), 'r') as zip_ref:
        zip_ref.extractall(sourcePath)

image_list = []

def loadImage(path):
    global image_list
    image_list = []
    files = os.listdir(path)
    for file in files:
        if file.endswith("@2x.png") and not (file.endswith("key@2x.png") or file.endswith("tab_off@2x.png") or file.endswith("tab_on@2x.png")):
           image_list.append(os.path.join(sourcePath, file))

def delete_files(path):
   try:
     files = os.listdir(path)
     for file in files:
       file_path = os.path.join(path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print("All files deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")

def test_json(list, times, name, author):
   print(list)
   print("id" + str(times))
   print("sticker name" + name)
   print("author name" + author)
   

def jsonGenerator():
    js = pd.read_json(theJson)
    for i, item in enumerate(js["sticker-href"]):
        if os.listdir(sourcePath) == []:
            print("no files")
        else:
           delete_files(sourcePath)

        processLink(i, item)
        time.sleep(3)
        unZip(sourcePath)
        time.sleep(3)
        loadImage(sourcePath)
        gen_json(image_list, i, js["sticker"][i], js["author"][i])

        time.sleep(3)
        delete_files(sourcePath)
    print("All done :D")

jsonGenerator()


"""
print(len(js)) #length of the dictionary(how many "pairs" of item)
print(js["sticker-href"][1]) #get the second item from the "link"
"""


"""
{"image_data":"the image"}]}
"""
#time.sleep(5)