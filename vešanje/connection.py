import mysql.connector


class Connection:
   __connection = None
   @staticmethod 
   def getInstance():
      if(Connection.__connection == None):
         Connection()
      return Connection.__connection
   def __init__(self):
      if(Connection.__connection != None):
         raise Exception("This is Singlton")
      else:
         Connection.__connection = mysql.connector.connect(user='root', password='stevica011',host='127.0.0.1',database='words')