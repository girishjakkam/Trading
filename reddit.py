import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import praw
import seaborn as sns
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import time


reddit = praw.Reddit(client_id='a29NjhYpNR_Ow7UgdL5GaA',
                     client_secret='c61uYiURyenNskk3Dnf62BY8DHaLEw',
                     username='ggggggggzzzz',
                     password='gggggggggg',
                     user_agent='Mytest/V.1.0')
					 
print(reddit.user.me())


subreddit = reddit.subreddit("wallstreetbets")


#for submission in subreddit.top(time_filter= 'day' , limit=10):
    #print(submission.title)
#for submission in subreddit.top(time_filter= 'week' , limit=10):
    #print(submission.title)
#for submission in subreddit.new(limit=10):
    #print(submission.title)
#for submission in subreddit.hot(limit=10):
    #print(submission.title)

data = []
for submission in subreddit.hot(limit=1000):
    data.append({"title": submission.title, "selftext": submission.selftext, "author": submission.author, "created_utc": submission.created_utc, "score": submission.score, "num_comments": submission.num_comments})

# Create a data frame from the list of dictionaries
df = pd.DataFrame(data, columns=["title", "selftext", "author", "created_utc", "score", "num_comments"])

#df.head()
#df.describe()
#df.groupby("score")
df = df.sort_values(by='score', ascending=False)
#print(df)


'''
plt.hist(df["score"], bins = 50)
plt.xlabel("title")
plt.ylabel("score")
plt.title("title vs score UTC")
plt.show()

sns.lineplot(x="title", y="score", data=df)
plt.show()
'''

text = " ".join(review for review in df.title)
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = set(STOPWORDS), 
                min_font_size = 10).generate(text)

plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 









