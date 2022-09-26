# EC463-Mini-project
Python App that analyze twitter user's sentiment and bot score

Steps:
1. download anaconda (botometer uses a older version of tweepy so package version control is needed)
2. conda env create -f environment.yml
3. conda activate EC463-miniproject
4. python test_senitment.py (replace this with miniproject.py when done)

Files:
1. environment.yml (package version control)
2. test_scrapping.py (botometer + tweepy)
3. test_sentiment.py (google cloud language API)
4. miniproject.py (combined WIP)

To-do:
1. get google cloud language API working in test_sentiment.py
2. put everything together in miniproject.py
3. update environment.yml if new package is used

documentSentiment contains the overall sentiment of the document, which consists of the following fields:
score of the sentiment ranges between -1.0 (negative) and 1.0 (positive) and corresponds to the overall emotional leaning of the text.
magnitude indicates the overall strength of emotion (both positive and negative) within the given text, between 0.0 and +inf. Unlike score, magnitude is not normalized; each expression of emotion within the text (both positive and negative) contributes to the text's magnitude (so longer text blocks may have greater magnitudes).