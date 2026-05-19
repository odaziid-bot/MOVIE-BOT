import sqlite3

#База данных

def user_db(name, fav_genre):

    conn = sqlite3.connect("user_database.db")
    
    cursor = conn.cursor()

    cursor.execute("""
                  CREATE TABLE IF NOT EXISTS users(
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  fav_genre TEXT)
                  """)

    cursor.execute("""
                      INSERT INTO users (name, fav_genre)
                       VALUES (?, ?)
                       """, (name, fav_genre))
    
    cursor.execute("""
                   SELECT * FROM users
                   """)
    
    all_data = cursor.fetchall()

    for row in all_data:
        print(*row)


    conn.commit()