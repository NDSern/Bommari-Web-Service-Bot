import sqlite3
import requests
from datetime import datetime
import json
import os
import sys
import re

sys.path.append(os.path.abspath("../Database"))

FILE = "../Database/modified.json"
DATABASE = "../Database/bommari.db"
PHOTO_PATH = "../Database/public/photos"
SPLIT_HERE = ";"
FIX_ROUTE_SPLIT_HERE = "|"

def check_for_valid_format(text:str):
    string_groups = text.split(SPLIT_HERE)
    print(string_groups)
    if len(string_groups) < 2:
        print("< 2 groups, likely have no semicolon\n")
        return False

    if len(string_groups) < 3:
        print("< 3 groups, likely have one semicolon\n")
        return False

    if len(string_groups) > 4:
        print("> 4 groups, likely have too many semicolon\n")
        return False
    
    # Likely have the correct format at this point
    return True
        

def format_description_in_message(text:str):
    desc = ""
    
    string_groups = text.split(SPLIT_HERE)
    name = string_groups[0].strip()
    
    # Check for errors in message format by user in Telegram chat, 
    # still input the data intp the database regardless, 
    # waiting for the data to be fixed
    
    # Angle
    if len(string_groups) < 2:
        print("<2 format", string_groups)
        return False
    
    grade = string_groups[1].strip().upper()
    if "?" in grade:
        desc += "Possible grade: " + grade + ". "
        grade = grade.replace("?","")
    
    # Degree
    if len(string_groups) < 3:
        print("<3 format", string_groups)
        return False
    
    angle = string_groups[2].strip()
    angle_numbers = re.findall(r'\d+', angle)
    if len(angle_numbers) > 0:
        angle = angle_numbers[0]
    
    # Description
    if len(string_groups) > 3:
        desc += string_groups[3].strip()
        
    return [name, grade, angle, desc]


def add_to_database(msg):
    db_connect = sqlite3.connect(DATABASE)
    cursor = db_connect.cursor()
    
    query = """
    INSERT INTO routes(id, date, user, photo, name, desc, grade, angle) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    try:
        name, grade, angle, desc = format_description_in_message(msg["text"])
    except Exception as e:
        print(e, file=sys.stderr)
        
    cursor.execute(query, (msg["id"], msg["date"], msg["from"], msg["photo"], name, desc, grade, angle))
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
    message_dict["from"] = message.from_user.first_name + (" " + message.from_user.last_name if message.from_user.last_name else "")
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

def change_route(msg:str):
    verify_change_in_table = False
    msgs = msg.split(FIX_ROUTE_SPLIT_HERE)
    if not len(msgs) == 2:
        print("Wrong format for the comment")
        return False
    
    initial_route_name = msgs[0][12:].strip()
    fixed_route_name = msgs[1].strip()
    print(initial_route_name)
    print(fixed_route_name)
    name, grade, angle, desc = format_description_in_message(fixed_route_name)
    
    db_connect = sqlite3.connect(DATABASE)
    cursor = db_connect.cursor()
    
    query = """
    UPDATE routes
    SET name = ?,
        grade = ?,
        angle = ?,
        desc = ?
    WHERE name = ?
    """
    
    cursor.execute(query, (name, grade, angle, desc, initial_route_name))
    verify_change_in_table = cursor.rowcount != 0
        
    cursor.close()
    db_connect.commit()
    db_connect.close()
    
    return verify_change_in_table

def delete_route(msg:str):
    verify_change_in_table = False
    name = msg[12:].strip()
    db_connect = sqlite3.connect(DATABASE)
    cursor = db_connect.cursor()
    
    query = """
    DELETE FROM routes
    WHERE name = ?
    """
    
    cursor.execute(query, (name,))
    verify_change_in_table = cursor.rowcount != 0
        
    cursor.close()
    db_connect.commit()
    db_connect.close()
    
    return verify_change_in_table

def update_route(msg):
    verify_change_in_table = False
    
    db_connect = sqlite3.connect(DATABASE)
    cursor = db_connect.cursor()
    
    query = """
    SELECT id FROM routes WHERE id = ?
    """
    
    cursor.execute(query, (msg.id,))
    data = cursor.fetchone()
    if not data:
        return False
    
    query = """
    DELETE FROM routes 
    WHERE id = ? 
    """
    
    cursor.execute(query, (msg.id,))
    verify_change_in_table = cursor.rowcount != 0
    
    cursor.close()
    db_connect.commit()
    db_connect.close()
    
    return verify_change_in_table