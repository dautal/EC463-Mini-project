# EC463-Mini-project
Python App that analyze twitter user's sentiment and bot score

### Steps:
1. download anaconda (botometer uses a older version of tweepy so package version control is needed)
2. go to the project directory
3. download json file and change os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your/path"
4. conda env create -f environment.yml
5. conda activate EC463_miniproject
6. python miniproject.py 

## Meaning of the results:

### Botometer: 
#### Meanings of the elements in the response
* **user**: Twitter user object (from the user) plus the language inferred from majority of tweets
* **raw scores**: bot score in the [0,1] range, both using English (all features) and Universal (language-independent) features; in each case we have the overall score and the sub-scores for each bot class (see below for subclass names and definitions)
* **cap**: conditional probability that accounts with a score equal to or greater than this are automated; based on inferred language

#### Meanings of the bot type scores:

* **fake_follower**: bots purchased to increase follower counts
* **self_declared**: bots from botwiki.org
* **astroturf**: manually labeled political bots and accounts involved in follow trains that systematically delete content
* **spammer**: accounts labeled as spambots from several datasets
* **financial**: bots that post using cashtags
* **other**: miscellaneous other bots obtained from manual annotation, user feedback, etc.

### Sentiment:
* **score** of the sentiment ranges between -1.0 (negative) and 1.0 (positive) and 
    corresponds to the overall emotional leaning of the text.
* **magnitude** indicates the overall strength of emotion (both positive and negative) within the given text, between 0.0 and +inf. 
    Unlike score, magnitude is not normalized; each expression of emotion within the text (both positive and negative) 
    contributes to the text's magnitude (so longer text blocks may have greater magnitudes).
    
### Our Results: 
<img width="1127" alt="test1" src="https://user-images.githubusercontent.com/75428513/192183290-b26aacc7-8d1a-4c92-856a-62cf35f65bd2.png">
<img width="1128" alt="test2" src="https://user-images.githubusercontent.com/75428513/192183296-110d12df-a4b0-4f13-9d0a-1c1e0e6af838.png">
