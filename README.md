# Twitter Discourse Analysis For Uncontentious Events


→ **What?** For a specific event, such as the Super Bowl, we want to analyze how the discourse in a country like the US has changed over the last five years (Regression). Further, we want to analyze how discourse varies in 3 nations: the US, Canada, and the UK/GB for such events.

→ **Why?** Because earlier studies were based on contentious issues such as politics, religion, and so on, and considered original tweets only. While we also look at replies to the original post and examine what future discourse could be.

→ **How?** 

<img src="https://user-images.githubusercontent.com/42632417/175763432-59aa627c-5792-4bc2-96ac-7c66984c81ef.png" height = 500 width = 900></img>


<!-- - Topic Modeling -> 20 topics 20 words analysis -> Main tweet vs. Replies
- LIWC
- Multi Dimensional analysis
- Graph Neural Network
- Knowledge Graph
- Word Analysis
- Feature Importance using TF-IDF -->


<hr>

→ Using n-Gram analysis, we can use it to analyze if country X and Country Y used different verbs about the given Event.



#### TODOs:
→ Link Prediction https://sci-hub.mksa.top/10.1016/j.jnca.2020.102716

→ Regression Analysis

→ Kullback Leibler Divergence


**Text Cleaning**
```

def preprocessing_text(text):
    #put everythin in lowercase
    text = text.lower()
    text = ' '.join([word for word in text.split(" ") if word not in remove_token])
    text = ' '.join([word for word in text.split(" ") if word not in stop_words_custom])
    text = ' '.join([word for word in text.split(" ") if detect_language(word) != 'Spanish'])
    text = ' '.join([word for word in text.split(" ") if word not in string.punctuation])
    text = ' '.join([contractions.fix(word) for word in text.split(" ")])
    text = ' '.join([w for w in text.split(" ") if w in words_list or not w.isalpha()])
    #Fix contractions
    text = pattern.sub('', text)
    # #Replace rt indicating that was a retweet
    clean_text = text.replace('rt', '')
    # # #Replace occurences of mentioning @UserNames
    clean_text = re.sub("@[A-Za-z0-9_]+", "", clean_text)
    # # #Replace links contained in the tweet
    clean_text = re.sub('http\S+', ' ', clean_text)
    clean_text = re.sub('www.[^ ]+', ' ', clean_text)
    # # #remove numbers
    clean_text = re.sub('[0-9]+', ' ', clean_text)
     # #remove emojis
    clean_text = emoji.get_emoji_regexp().sub(u'', clean_text)
    # # remove hastags fix again
    clean_text = re.sub("#[A-Za-z0-9_]+","", clean_text)
    # remove all punctuation except words and space
    clean_text = re.sub(r'[^\w\s]','', clean_text)
    # # #replace special characters and puntuation marks
    clean_text = re.sub('[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~’]', '', clean_text)
    # #join to remove extra space
    clean_text = ' '.join(clean_text.split())
    return clean_text

```
