import sqlite3
conn = sqlite3.connect('microblog.db') 

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS User(
            userID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            passW TEXT,
            email TEXT,
            bio TEXT
        )""")

#if originalpost is 0, its not a repost
c.execute("""CREATE TABLE IF NOT EXISTS Post(
            postID INTEGER PRIMARY KEY AUTOINCREMENT,
            userID INTEGER,
            orgPostID INTEGER, 
            link TEXT,
            content TEXT,
            timestamp TEXT,
            FOREIGN KEY(userID) REFERENCES user(userID),
            FOREIGN KEY(orgPostID) REFERENCES Post(postId)
    )""")

#followerID follows the influenceID
c.execute("""CREATE TABLE IF NOT EXISTS Following(
            influencerID INTEGER,
            followerID INTEGER,
            FOREIGN KEY(influencerID) REFERENCES user(userID),
            FOREIGN KEY(followerID) REFERENCES user(userID)
    )""")


c.execute("INSERT INTO User VALUES('1','Chaney','chaneypassword','chaney.chantipaporn@gmail.com','chaneybio')")
c.execute("INSERT INTO User VALUES('2','Nhat','nhatpassword','nhat.nguyen@gmail.com','nhatbio')")
c.execute("INSERT INTO User VALUES('3','Tony','tonypassword','tony.tony@gmail.com','tonybio')")
c.execute("INSERT INTO User VALUES('4','Someone','someonepassword','someone.else@gmail.com','someonebio')")

c.execute("INSERT INTO Post VALUES('1','1', '0','N/A','chaneypost', datetime('now'))")
c.execute("INSERT INTO Post VALUES('2','2', '0','N/A','nhatpost', datetime('now'))")
c.execute("INSERT INTO Post VALUES('3','3', '0','N/A','tonypost', datetime('now'))")

c.execute("INSERT INTO Following VALUES('1','2')") #nhat follows chaney
c.execute("INSERT INTO Following VALUES('1','3')") 
c.execute("INSERT INTO Following VALUES('1','4')")
c.execute("INSERT INTO Following VALUES('2','3')")
c.execute("INSERT INTO Following VALUES('3','2')")

conn.commit()
conn.close()

