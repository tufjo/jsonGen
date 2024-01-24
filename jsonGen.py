import zipfile
import time
import os
import json
import pandas as pd
import requests
from convertToJSON import gen_json

myPath = os.path.dirname(__file__) #jsonGenFolder
sourcePath = os.path.join(myPath, "source")
outPath = os.path.join(myPath, "output")
dictPath = os.path.join(myPath, 'dict')

def createFolders():
    list = [sourcePath, outPath, dictPath]
    for item in list:
        if not os.path.exists(item):
            os.makedirs(item)

def delayTime(path, name):
   dirPath = os.path.join(path, name)
   while os.listdir(dirPath) == []:
      time.sleep(1)
      print('waiting...')

def csv_to_json(CSVpath):
    data = pd.read_csv(CSVpath)
    base = os.path.basename(CSVpath).replace('.csv', '.json')
    data_dict = data.to_dict(orient='records')
    json_object = json.dumps(data_dict, indent=4)
    with open(os.path.join(dictPath, base), "w") as outfile:
        outfile.write(json_object)

id = ''
def download_file(item):
    print('downloading...')
    global id

    # check if directory exists
    os.makedirs('source', exist_ok=True)

    id=''
    pr = item.split('/')[-2]
    tt = "https://dl.stickershop.line.naver.jp/products/0/0/1/" + pr + "/iphone/stickers@2x.zip"
    download_path = os.path.join(os.path.dirname(__file__), 'source', 'stickers@2x.zip')
    # Send a GET request to the URL with certificate verification disabled
    response = requests.get(tt, verify=False)
    # Check if the request was successful (status code 200 = successful)
    if response.status_code == 200:
       #open file and write
       with open(download_path, 'wb') as file:
          file.write(response.content)
          print(f"File downloaded successfully to {download_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
    id=pr
    print('Downloaded!')

def unZip(path):
    print('unzipping...')   
    with zipfile.ZipFile(os.path.join(path, "stickers@2x.zip"), 'r') as zip_ref:
        zip_ref.extractall(sourcePath)
    print('Unzipped!')

image_list = []

def loadImage(path):
    print('loading images...')
    global image_list
    image_list = []
    files = os.listdir(path)
    for file in files:
        if file.endswith("@2x.png") and not (file.endswith("key@2x.png") or file.endswith("tab_off@2x.png") or file.endswith("tab_on@2x.png")):
           image_list.append(os.path.join(sourcePath, file))
    print('Loaded!')
    

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
   


def jsonGenerator(self, name):
    base = os.path.join(dictPath, os.path.basename(name).replace('.csv', '.json'))
    js = pd.read_json(base)
    for i, item in enumerate(js["sticker-href"]):
        if os.listdir(sourcePath) == []:
            print("no files")
        else:
           delete_files(sourcePath)

        download_file(item)
        delayTime(myPath, 'source')
        unZip(sourcePath)
        delayTime(myPath, 'source')
        loadImage(sourcePath)
        gen_json(image_list, id, js["sticker"][i], js["author"][i])

        progress_text = f"Processing {i + 1}/{len(js)}"
        self.progressNum.configure(text=progress_text)
        self.progressNum.update_idletasks()

        time.sleep(1)
        delete_files(sourcePath)
    print("All done :D")
    
    self.progressNum.configure(text=progress_text + " Completed")

"""
print(len(js)) #length of the dictionary(how many "pairs" of item)
print(js["sticker-href"][1]) #get the second item from the "link"
"""