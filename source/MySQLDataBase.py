import mysql.connector
from DataBaseAPI import DataBaseAPI
import configparser

class MySQLDataBase(DataBaseAPI):

  def openConnection():

    config = configparser.ConfigParser()
    config.read("ConfigurationParameters.cfg")

    host = config["MYSQL_DATABASE"]["MYSQL_HOST"]
    user = config["MYSQL_DATABASE"]["MYSQL_USER"]
    password = config["MYSQL_DATABASE"]["MYSQL_PASSWORD"]
    database = config["MYSQL_DATABASE"]["MYSQL_DATABASE"]

    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )

    return mydb

  def insertProject(projectID, projectName, database):
    if database == "mysql":
      mydb = MySQLDataBase.openConnection()
      mycursor = mydb.cursor()

      sql = "INSERT INTO Project (id, name) VALUES (%s,%s)"
      val = (projectID, projectName)
      mycursor.execute(sql, val)

      mydb.commit()

  def insertScreen(projectID, screenName, blocksNumber, database):
    if database == "mysql":
      mydb = MySQLDataBase.openConnection()
      mycursor = mydb.cursor()

      sql = "INSERT INTO Screen (project_id, name, blocks_number) VALUES (%s,%s,%s)"
      val = (projectID, screenName, blocksNumber)
      mycursor.execute(sql, val)

      mydb.commit()

  def insertIssue(projectID, screenName, blockID, blockType, issueType, database):
    if database == "mysql":
      mydb = MySQLDataBase.openConnection()
      mycursor = mydb.cursor()

      sql = "INSERT INTO Issue (project_id, screen_name, block_id, block_type, issue_type) VALUES (%s,%s,%s,%s,%s)"
      val = (projectID, screenName, blockID, blockType, issueType)
      mycursor.execute(sql, val)

      mydb.commit()