import sqlite3
import os

class DB():

    def __init__(self):
        self.connect_database()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS "DICTS" (
                "Name"	TEXT NOT NULL,
                "Is_Preset"	BOOLEAN NOT NULL,
                PRIMARY KEY("Name")
                );''')
        
        for dictname in list(PRESETDICTS):
            self.cur.execute("INSERT OR IGNORE INTO DICTS ('Name', 'Is_Preset') VALUES\n('{}', 'TRUE')".format(dictname))
        
            command = '''CREATE TABLE IF NOT EXISTS"{}" (
                    "Word"	TEXT NOT NULL,
                    "Definition"	TEXT NOT NULL,
                    PRIMARY KEY("Word")
                    );'''.format(dictname)
            self.cur.execute(command)

            for word in list(PRESETDICTS[dictname]):
                self.cur.execute('''INSERT OR IGNORE INTO \'''' + dictname + '''' ('Word', 'Definition') VALUES''' + '''
                        ('{}', '{}')'''.format(word, PRESETDICTS[dictname][word]))

        self.close_database()

    def connect_database(self):
        # connection
        self.conn = sqlite3.connect(os.path.abspath('./dict_db/spellwell_db'))
        # cursor
        self.cur = self.conn.cursor()

    def close_database(self):
        self.conn.commit()
        self.conn.close()


    def saveDict(self, dictname, dictionary):
        self.connect_database()
        
        # you can only edit user created (non-preset) dictionaries 
        self.cur.execute("INSERT OR IGNORE INTO DICTS ('Name', 'Is_Preset') VALUES\n('{}', 'FALSE')".format(dictname))

        self.cur.execute('DROP TABLE IF EXISTS "{}";'.format(dictname))
    
        command = '''CREATE TABLE "{}" (
                "Word"	TEXT NOT NULL,
                "Definition"	TEXT NOT NULL,
                PRIMARY KEY("Word")
                );'''.format(dictname)
        self.cur.execute(command)

        for word in list(dictionary):
            self.cur.execute('''INSERT OR REPLACE INTO \'''' + dictname + '''' ('Word', 'Definition') VALUES''' + '''
                    ('{}', '{}')'''.format(word, dictionary[word]))
        self.close_database()

    def deleteDict(self, dictname):
        self.connect_database()
        self.cur.execute('DROP TABLE IF EXISTS "{}";'.format(dictname))
        self.cur.execute("DELETE FROM 'DICTS' WHERE Name='{}'".format(dictname))
        self.close_database()


    def getDict(self, name):
        self.connect_database()
        self.cur.execute("SELECT * FROM '{}'".format(name))
        rows = self.cur.fetchall()
        dictionary = {}
        for row in rows:
            word = row[0]
            definition = row[1]
            dictionary[word] = definition
        self.close_database()
        return dictionary 

    def getDictNames(self, preset):
        self.connect_database()
        if preset:
            preset = 'TRUE'
        else:
            preset = 'FALSE'
        self.cur.execute("SELECT * FROM 'DICTS' WHERE Is_Preset='" + preset + "'")
        rows = self.cur.fetchall()
        names = []
        for row in rows:
            name = row[0]
            names.append(name)
        self.close_database()
        return names 

    def checkIsPreset(self, dictname):
        return dictname in list(PRESETDICTS)

PRESETDICTS = {"animals":{"cat": "best animal that meows", 
                    "dog": "best animal that barks",
                    "giraffe": "very tall animal", 
                    "unicorn": "magical animal(?)"},

            "body": {"nose": "the body part you use to smell", 
                "mouth": "the body part you use to speak",
                "teeth": "the body parts you use to chew your food", 
                "legs": "the body parts you use to walk or run", 
                "hands": "the body parts you use to write or type"},

           "polygons": {"triangle": "the polygon that has three sides", 
                    "quadrilateral": "the polygon that has four sides",
                    "pentagon": "the polygon that has five sides", 
                    "hexagon": "the polygon that has six sides", 
                    "heptagon": "the polygon that has seven sides"},
    
           "medical": {"doctor": "a qualified practitioner of medicine", 
                    "stethoscope": "a medical instrument for listening to the heartbeat",
                    "surgical mask": "a mask work in surgery", 
                    "surgical gown": "something a surgeon wears during surgery", 
                    "gloves": "worn on hands by surgeons"},
    
            "numbers": {"one": "the number 1", 
                    "one hundred": "the number 100",
                    "five hundred": "the number 500", 
                    "one thousand": "the number 1000", 
                    "two thousand": "the number 2000"}}
