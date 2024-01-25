import base64
import json
from PIL import Image
from io import BytesIO
import os

myPath = os.path.dirname(__file__)
outputPath = os.path.join(myPath, "output")
sourcePath = os.path.join(myPath, "source")

def gen_json(sticker_board, id, name, author):
    if sticker_board == []:
       return

    first = []
    second = []

    for item in sticker_board:
        if item.endswith("tab_on@2x.png"):
            cTrayIcon = Image.open(item)
            image_size = cTrayIcon.size
            fsize = (96,96)

            left = (image_size[0] - fsize[0]) // 2
            top = (image_size[1] - fsize[1]) // 2
            right = left + fsize[0]
            bottom = top + fsize[1]

            cropped_image = cTrayIcon.crop((left, top, right, bottom))
            resized_image = cropped_image.resize(fsize, Image.LANCZOS)

            #Convert tray icon to base64
            buffered_tray = BytesIO()
            resized_image.save(buffered_tray, format="PNG")
            str_tray_icon = base64.b64encode(buffered_tray.getvalue()).decode('utf-8')

    if len(sticker_board) > 30 :
        half = len(sticker_board)//2
        first = sticker_board[:half]
        second = sticker_board[half:]
    else:
        first = sticker_board

    i = 0
    while i < 2:
        type = first
        str_identifier = id
        str_pack = name
        if i == 1:
            type = second
            str_identifier = str(id) + "p2"
            str_pack = name + "part2"
        if second == []:
            i+=2
        else:    
            i+=1

        str_author = author

        array_stickers = []
        str_stickers = []

        for img_path in type:
            temp_canvas = Image.new('RGBA', (512, 512), (255, 255, 255, 0))
            temp_img = Image.open(img_path)

            scale = min(512 / temp_img.width, 512 / temp_img.height)
            x = int(256 - (temp_img.width / 2) * scale)
            y = int(256 - (temp_img.height / 2) * scale)

            temp_canvas.paste(temp_img.resize((int(temp_img.width * scale), int(temp_img.height * scale))), (x, y))

            buffered_sticker = BytesIO()
            temp_canvas.save(buffered_sticker, format="WEBP", quality=85)
            str_stickers.append({"image_data": base64.b64encode(buffered_sticker.getvalue()).decode('utf-8')})

        out_json = {
            "identifier": str_identifier,
            "name": str_pack,
            "publisher": str_author,
            "tray_image": str_tray_icon,
            "stickers": str_stickers
        }

        with open(os.path.join(outputPath, str_pack + '.json'), 'w', encoding='utf-8') as json_file:
            json.dump(out_json, json_file, ensure_ascii=False, indent=2)
            print("File "+str_pack+" written!")
