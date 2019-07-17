import mysql.connector
from twitter import *

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "test"
)
t = Twitter(
    auth=OAuth('2546324216-d7UR9Ks2XJTryE6L4sqXNbMZLDOaUnckWGW36VD', '2t1xd7dtRThqZTD4sLVe1QVBlrZuxOZHpNnFIrfiiPDth', 'Vrw2H4BUsvQaevche3FhKw9g6', 'aDOQuFrh9FUVLoaJd7AqLwbk5mWnHf84C9AUyKIGHe2LopYhzz'))



# Get your "home" timeline
# x=t.statuses.home_timeline()
data = t.statuses.user_timeline(screen_name="VSReddy_MP")
print(data)


mycursor = mydb.cursor()	
def load_tweettext_tosql(x):
	for each in x:
		print (each['created_at'],each['text'])
		# mycursor.execute("insert into twitter_data(tweet) values ('"+each['text']+"');")
	mydb.commit()

# mycursor.execute("drop table if exists twitter_data")
# mycursor.execute("create table twitter_data (tweet nvarchar(500),dates timestamp)")		
# load_tweettext_tosql(data)

			




