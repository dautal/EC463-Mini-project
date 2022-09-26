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
    * user: Twitter user object (from the user) plus the language inferred from majority of tweets
    * raw scores: bot score in the [0,1] range, both using English (all features) and Universal (language-independent) features; 
    in each case we * * have the overall score and the sub-scores for each bot class (see below for subclass names and definitions)
    * display scores: same as raw scores, but in the [0,5] range
    * cap: conditional probability that accounts with a score equal to or greater than this are automated; based on inferred language
    * Meanings of the bot type scores:

    * fake_follower: bots purchased to increase follower counts
    * self_declared: bots from botwiki.org
    * astroturf: manually labeled political bots and accounts involved in follow trains that systematically delete content
    * spammer: accounts labeled as spambots from several datasets
    * financial: bots that post using cashtags
    * other: miscellaneous other bots obtained from manual annotation, user feedback, etc.

### Sentiment:
    * score of the sentiment ranges between -1.0 (negative) and 1.0 (positive) and corresponds to the overall emotional leaning of the text.
    * magnitude indicates the overall strength of emotion (both positive and negative) within the given text, between 0.0 and +inf. Unlike score, magnitude is not normalized; each expression of emotion within the text (both positive and negative) contributes to the text's magnitude (so longer text blocks may have greater magnitudes).
