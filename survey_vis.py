from wordcloud import WordCloud

def survey_wordcloud(freq_dict):
    """Accepts a dictionary where the keys are the strings for the WC and values are counts.
       Outputs a WordCloud object that can be viewed with matplotlib"""
    return WordCloud(background_color="black",
               width=3000,height=1000,
               relative_scaling=0.5,
               colormap='tab20c',
               normalize_plurals=True
              ).generate_from_frequencies(freq_dict)