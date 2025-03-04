import re
import json
import sqlite3

FILE = "modified.json"
DATABASE = "bommari.db"
SPLIT_HERE = ";"

def open_file(file:str):
    with open(file, encoding="utf8", mode="r") as json_file:
        json_data = json.load(json_file)
    messages = json_data
    return messages

def format_description_in_message(text:str):
    desc = ""
    
    string_groups = text.split(SPLIT_HERE)
    name = string_groups[0].strip()
    
    grade = string_groups[1].strip().upper()
    if "?" in grade:
        desc += "Possible grade: " + grade + ". "
        grade = grade.replace("?","")
    
    angle = string_groups[2].strip()
    angle_numbers = re.findall(r'\d+', angle)
    if len(angle_numbers) > 0:
        angle = angle_numbers[0]
    
    if len(string_groups) > 3:
        desc += string_groups[3].strip()
        
    return [name, grade, angle, desc]




if __name__ == "__main__":
    try:
        dbConnect = sqlite3.connect(DATABASE)
        cursor = dbConnect.cursor()
        
        query = """
        CREATE TABLE IF NOT EXISTS routes(
            id      INTEGER     PRIMARY KEY AUTOINCREMENT,
            date    TEXT        NOT NULL,
            user    TEXT        NOT NULL,
            photo   TEXT        NOT NULL,
            name    TEXT        NOT NULL,
            desc    TEXT,
            grade   TEXT        NOT NULL,
            angle   TEXT        NOT NULL,
            layout  TEXT        NOT NULL    DEFAULT "2024/2025"
        );
        """
        cursor.execute(query)
        
        messages = open_file(FILE)
        
        for msg in messages:
            if msg["type"] == "service":
                continue
            # try:
            name, grade, angle, desc = format_description_in_message(msg["text"])
            query = """
            INSERT INTO routes(date, user, photo, name, desc, grade, angle) VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (msg["date"], msg["from"], msg["photo"], name, desc, grade, angle))
            # except:
            print(msg)
        
        messages_data = cursor.execute("SELECT * FROM routes")
        for row in messages_data:
            print(row)
        
        cursor.close()
        
    except sqlite3.Error as err:
        print("Error: ", err)

    dbConnect.commit()
    dbConnect.close()
