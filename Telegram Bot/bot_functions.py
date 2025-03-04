import sqlite3
import requests
from datetime import datetime
import json
import os

FILE = "../modified.json"
DATABASE = "../bommari.db"

def input_data_to_database(message):
    print(message.caption)
    formatted_date = datetime.fromtimestamp(message.date).strftime('%d-%m-%Y_%H-%M-%S')
    photo_name = "photo_" + str(message.id) + "@" + formatted_date + ".jpg"
    print(photo_name)
    
    message_dict = {}
    message_dict["id"] = message.id
    message_dict["type"] = "Bot message"
    message_dict["date"] = formatted_date
    message_dict["date_unixtime"] = str(message.date)
    message_dict["from"] = message.from_user.first_name + " " + message.from_user.last_name
    message_dict["from_id"] = message.from_user.id
    message_dict["photo"] = "photos/" + photo_name
    message_dict["photo_file_size"] = message.photo[-1].file_size
    message_dict["width"] = message.photo[-1].width
    message_dict["height"] = message.photo[-1].height
    message_dict["text"] = message.caption
    
    message_json = json.dumps(message_dict)
    print(message_json)
    
    return str(photo_name)
    
def download_photo(link, name):
    print(link)
    r = requests.get(link)
    r.raise_for_status()
    
    photo_repo = "../Database/photos"
    os.makedirs(photo_repo, exist_ok=True)
    
    photo = os.path.join(photo_repo, name)
    
    with open(photo, "wb") as p:
        p.write(r.content)
    print("Success!")
    