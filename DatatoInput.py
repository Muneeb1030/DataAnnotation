#Script written to get the desired columns from the csvs
import pandas as pd

#since the file is csv and some special chracter like ? or "" are replace by there codes rather than character
df = pd.read_csv("Data/Corona_NLP_test.csv",encoding="utf-8",encoding_errors="replace")
# print(df.head())
tweets = df["OriginalTweet"].tolist() #lists are created to write in file in required format
# print(tweets[:10])

#processing is done to avoid extra lines and spaces in tweets
processed_tweets = []
for tweet in tweets:#get each tweet one after another
    lines = tweet.split('\n')#split the text when encounter "\n" and make a list
    # print(lines)
    #after splitting the spaced lines will occur in list sparately 
    non_empty_lines = [line.strip() for line in lines if line.strip()]#Remove if white space
    processed_tweet = '\n'.join(non_empty_lines) #join the splited term
    processed_tweets.append(processed_tweet)

sentiments = df["Sentiment"].tolist() # Sentiments 

#writing to file in required format
with open("Data/Test.txt","w", encoding="utf-8") as file:
    for idx,_ in enumerate(tweets):
        file.write(f"Tweet: {processed_tweets[idx]}\n")
        file.write(f"Emotion: {sentiments[idx]}\n\n")