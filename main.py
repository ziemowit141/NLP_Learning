# from AbusedMail import Mail
#
# mail = Mail("1st_mail")
#
# for line in mail.file:
#     print(line)
# import mysql.connector
import sqlalchemy as db
engine = db.create_engine('mysql+mysqlconnector://adept@localhost:3306/TwitterDatabase')
connection = engine.connect()
metadata = db.MetaData()
twitter_table = db.Table('Tweet', metadata, autoload=True, autoload_with=engine)
print(twitter_table.columns.keys())
