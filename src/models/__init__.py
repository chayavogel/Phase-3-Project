#/Users/chayavogel/Documents/Solar-System-Explorer/src/models/__init__.py
import sqlite3

CONN = sqlite3.connect('solar_system.db')
CURSOR = CONN.cursor()
