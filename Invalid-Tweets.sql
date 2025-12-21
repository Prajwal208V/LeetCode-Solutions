1# Write your MySQL query statement below
2SELECT tweet_id -- select tweet id
3FROM Tweets
4WHERE LENGTH(content) > 15; -- tweet is invalid if content length exceeds 15
5