import pandas as pd

from DataGathering import VoteData2016

def getVoteData():
    return pd.read_csv(VoteData2016)

# print(getVoteData())