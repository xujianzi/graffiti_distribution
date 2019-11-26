# Graffiti_Distribution

|Author|Jian Xu|
|---|---
|E-mail|jxu109@binghamton.edu

python + tweepy + Flickr API + Jupyternotebook to realize extracting tweets from the Twitter and applying sentimental analysis for the text in tweets.
***
## Reference files:

* [Project Address](https://github.com/xujianzi/climate_change)
* [Twitter Extracting](https://github.com/xujianzi/climate_change/tree/master/twitter_extracting)
* [Twitter Analysis]()
---
## Contents:
* [Project Description](#Project-Description)
* [Function Description](#Function-Description)
* [Tweets Extracting](#Tweets-Extracting)
* [Tweets Prepocessing](#Tweets-Prepocessing)
* [Tweets Analysis](#Tweets-Analysis)

---
## Project Description
This project aims to extract tweets by different users or varied keywords at a specific time spam with the mean of Python, Tweepy, and Twitter API. And we do the time analysis and sentimental analysis to the tweets data with the help of Pandas, Numpy, matplotlib.

---
## Function Description

### 1.Function Structure
![Function Structure](https://github.com/xujianzi/climate_change/blob/master/github_images/strcuture1.JPG "Function Structure Demostration")
### 2.Main fuction demostration
#### 2.1. Extracting tweets by users:
```python
def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id = self.twitter_user).items(num_tweets):
            tweets.append(tweet)
            print ('...%s tweets have been downloaded so far' % len(tweets))
        return tweets
```
#### 2.2.Extracting tweets by keywords:
```python
    def get_search_tweets(self, num_tweets = 200, old_id= None, young_id = None):
        # Function to extract tweets about specific motif from time A to time B
        # num_tweets: the tweets number you want to extract
        # old_id: extracting tweets more older than the id of one specific tweet
        # young_id: extracting tweets more recent than the id of a tweet
        obj_tweets = []       
        for tweet in Cursor(self.twitter_client.search, q = self.twitter_user, 
        since_id = young_id, max_id = old_id).items():
            obj_tweets.append(tweet)
            print ('...%s tweets have been downloaded so far...' % len(obj_tweets))
            if len(obj_tweets) >= num_tweets:
                break
        return obj_tweets
```   
---
## Tweets Extracting
### 1. Initialzation variables
```python
twitter_client = twitter_processing.TwitterClient()
tweet_analyzer = twitter_processing.TweetAnalyzer()
```
### 2.Extracting tweets from mutiple users(This example uses mutiple presses)
```python
    news_screen_name = ['AP', 'cnni','BBCWorld','Reuters', 'TIME', 'RT_com', 'XHNews',   
    
    'washingtonpost','Discovermag', 'cbsnews', 'bbcbreaking', 'theonion', 'mashable', 'abc', 
    
    'discovery', 'NASA','natgeo', 'theeconomist', 'cnnbrk', 'nytimes']
    news_names_list = news_screen_name
    dir_name = 'news_folder'
    tweets_nums = 20
    Path(dir_name).mkdir(exist_ok= True)
    folder = Path(dir_name)
    for news in news_names_list:
        twitter_client = twitter_processing.TwitterClient(news)
        tweet_analyzer = twitter_processing.TweetAnalyzer() 
        temp_tweets = twitter_client.get_user_timeline_tweets(tweets_nums)
        temp_df = tweet_analyzer.tweets_to_data_frame(temp_tweets)
        p = os.path.join(folder,str(news)+ r'.csv')
        temp_df.to_csv(p,mode ='a', index = False, sep=',')
```
### 3.Extracting tweets about a keywords
>Note: The system may sleep up to 5 minutes when the maxmium request is reached.
```python
def main():
    '''
    save the tweets data as jason format.
    '''
    folder = Path(dir_name)
    filepath = os.path.join(folder,filename)
    twitter_client = twitter_processing.TwitterClient(motif)
    temp_tweets = twitter_client.get_search_tweets(num_tweets = num_tweets)
    with open(filepath, 'a') as f:
        for tweet in temp_tweets:
            js = json.dumps(tweet._json)
            f.write(js)
            f.write('\n')

def users_extract():
    pass
    

if __name__ == "__main__":
    motif = "trump"
    num_tweets = 10
    filename = 'temp_tweets.txt'
    dir_name = r'E:\Gitfolder\climate_change1'
    main()
```
### 4.Program running display
![Program running display](https://github.com/xujianzi/climate_change/blob/master/github_images/running_display.gif "running.gif")
***
## Tweets Prepocessing
> Note: The Tweets prepocessing and analysis is under Anaconda environment to achieve better interatction.
### 1.Downloaded Tweets Discription
Tweets are saved as two types: json and csv. To make it be better manituplated and analyzed with Pandas, numpy, and matplotlib. All types of data are converted to csv format and imported to the Jupyter Notebook.

### 2.Tweets Information as csv.
#### 2.1 The reports of 9 presses display
![presses hist](https://github.com/xujianzi/climate_change/blob/master/github_images/Climate%20mentions.png "Presses hist")

#### 2.2 The media tweets display
![Presses Tweets](https://github.com/xujianzi/climate_change/blob/master/github_images/media.gif "Presses_Tweets")
### 3.Data clean
Clean data sets by keyword, release time and user information, and remove duplicated irrelevant data. There are over 500 presses data and 20,000 users data left.
***
## Tweets Analysis
### 1.Amazon Rainforest fire hotspot by time
The Data are aquired from the NASA fire spot map. The data collections are from August to October.

![Fire map](https://github.com/xujianzi/climate_change/blob/master/github_images/firespot.gif "Fire map.gif")

### 2.Presses time series analysis
Long time period:

![Press time series](https://github.com/xujianzi/climate_change/blob/master/github_images/Press_time_series.png "Presses long period")
Time period from August to October:

![Press time series1](https://github.com/xujianzi/climate_change/blob/master/github_images/Press_time_series1.png "Presses shot period")

### 3.Sentimental analysis and data normalization
3.1 Sentimental Analysis

| Semantic value | Representation|
|:--------:|:------------:|
| 1 | positive |
| 0 | neutrual |
|-1 | nagative |

3.2 Data normalizaiton
To compare data in the comparable scale, I use the min_max normalization.

     x = (x - min_x)/(max_x - min_x) 

### 4.Users time series analysis
![users time series](https://github.com/xujianzi/climate_change/blob/master/github_images/4.1.png "users time series")

### 5.Time series changes for presses 
![Presses time series](https://github.com/xujianzi/climate_change/blob/master/github_images/5.1.png "Presses time series")
### 6.Time series changes comaparison for presses and users

### 7.Spatial Analysis for people who concern about fire

![Global Map](https://github.com/xujianzi/climate_change/blob/master/github_images/climate_tweets.jpg "Global map")

-----------------------------