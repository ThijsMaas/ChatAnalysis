#!usr/bin/python3
"""
Author: Thijs Maas
"""
from sys import argv
from collections import Counter
import re
import pandas as pd
import numpy as np
import matplotlib as plt
import holoviews as hv
hv.extension('bokeh')

import formatmessages as fm

def dataframe(chatfile):
    """Return a formated pandas dataframe of a whatsapp chatfile"""
    data = [i for i in fm.main(chatfile)]
    df = pd.DataFrame(data, columns = ["date", "time", "author", "content"], index=range(39999))
    return df

def countemoji(message):
    """returns emoji count in a string"""
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]", flags=re.UNICODE)

    char_with_modifier = re.compile(emoji_pattern)
    return len(re.findall(char_with_modifier, message))

def del_non_message():
    pass



if __name__ == "__main__":
    chatfile = argv[1]
    df = dataframe(chatfile)
    view = hv.Scatter(df, "time", "content")
    view
    #print(df)

    # groupby_author = df.groupby("author")
    # for author, value in groupby_author["content"]:
    #     print(author+":", value.count())
    
    
        


