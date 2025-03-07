import sqlite3
import requests
from datetime import datetime
import json
import os
import sys
sys.path.append(os.path.abspath("../Database"))
from database import format_description_in_message

FILE = "../Database/modified.json"
DATABASE = "../Database/bommari.db"
PHOTO_PATH = "../Database/public/photos"

def add_to_database(msg):
    db_connect = sqlite3.connect(DATABASE)
    cursor = db_connect.cursor()
    
    query = """
    INSERT INTO routes(date, user, photo, name, desc, grade, angle) VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    name, grade, angle, desc = format_description_in_message(msg["text"])
    cursor.execute(query, (msg["date"], msg["from"], msg["photo"], name, desc, grade, angle))
    cursor.close()
    db_connect.commit()
    db_connect.close()
    
def add_to_json_database(msg):
    file_path = os.path.abspath(FILE)
    with open(file_path, encoding="utf8", mode="r") as f:
        json_data = json.load(f)
        
    json_data.append(msg)
    
    with open(file_path, encoding="utf8", mode="w") as f:
        json.dump(json_data, f)

def input_data_to_database(message):
    print(message.caption)
    formatted_date_for_photo_name = datetime.fromtimestamp(message.date).strftime('%d-%m-%Y_%H-%M-%S')
    photo_name = "photo_" + str(message.id) + "@" + formatted_date_for_photo_name + ".jpg"
    print(photo_name)
    
    formatted_date_for_database = datetime.fromtimestamp(message.date).strftime('%Y-%m-%dT%H:%M:%S')
    
    message_dict = {}
    message_dict["id"] = message.id
    message_dict["type"] = "Bot message"
    message_dict["date"] = formatted_date_for_database
    message_dict["date_unixtime"] = str(message.date)
    message_dict["from"] = message.from_user.first_name + " " + message.from_user.last_name
    message_dict["from_id"] = message.from_user.id
    message_dict["photo"] = "photos/" + photo_name
    message_dict["photo_file_size"] = message.json["photo"][-1]["file_size"]
    message_dict["width"] = message.json["photo"][-1]["width"]
    message_dict["height"] = message.json["photo"][-1]["height"]
    message_dict["text"] = message.caption
    
    add_to_database(message_dict)
    add_to_json_database(message_dict)
    
    return str(photo_name)
    
def download_photo(link, name):
    print(link)
    r = requests.get(link)
    r.raise_for_status()
    
    photo_repo = PHOTO_PATH
    os.makedirs(photo_repo, exist_ok=True)
    
    photo = os.path.join(photo_repo, name)
    
    with open(photo, "wb") as p:
        p.write(r.content)
    print("Success!")
