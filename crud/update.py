# crud/create.py
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def update_user(user_id, username):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "UPDATE users SET username = %s WHERE id = %s;"
            cursor.execute(query, (username, user_id))
            conn.commit()
            cursor.close()
            print(f"User {username} updated successfully.")
        except Exception as e:
            print(f"Error updating user: {e}")
        finally:
            conn.close()

update_user(1,"safeer sifarath")