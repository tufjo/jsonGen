<p align="center">
<img src=".\img_src\thumb.png" />
</p>
<h1>Line Store Webscrap to Whatsapp Sticker :D</h1>
Currently, it's totally functional despite the rough look (it currently only supports static stickers, not emojis and animated stickers)
<br>This is a very niche use case but I feel like someone out there might also need it so here it is
<br>
<br>To use this current version follow the following instruction:
<br>You can **download** the Zip, unzip
<br>Or you can **clone** from github via following steps:

```sh
cd "file location" #choose where you can the file to be placed
git clone https://github.com/tufjo/jsonGen
```

<br>Then you'll need to run the following commands in your terminal, these are the components the code needs

```sh
pip install Pillow
pip install pandas
pip install requests
pip install customtkinter
```

Currently, it doesn't ship with an executable file the only way is to open main.py with a IDE of your choice eg. vscode
<br>run the code and Voila! there you have the thing!
<br>just select your csv and click on process & convert and you'll get your stickers ready!
<br>note: before exporting your .csv, make sure there are three columns named:

#example
|     sticker     | sticker-href | author |
| awesome_sticker | https://link | tufjo_ |

