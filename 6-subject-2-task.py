
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
import pandas as pd
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()

def create_connection_in_memory():
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(":memory:")
       print(f"Connected, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()

          


if __name__ == '__main__':
   create_connection(r"Stations.db")
   create_connection_in_memory()

engine=create_engine('sqlite:///C:/Users/Kuba P/Desktop/Code/Projects/6-subject/Stations.db')

df=pd.read_excel('C:/Users/Kuba P/Desktop/clean_stations.xlsx')
df1=pd.read_excel('C:/Users/Kuba P/Desktop/clean_measure.xlsx')

df.to_sql('clean_stations', con=engine, if_exists='append', index=False)
df1.to_sql('clean_measure', con=engine, if_exists='append', index=False)

conn=engine.connect()
print(conn.execute('SELECT * FROM clean_measure WHERE tobs>70'))


