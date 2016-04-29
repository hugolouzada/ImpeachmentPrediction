import pandas as pd

from DataGathering import VoteData2016
from DataGathering.VoteTargetFactory import VoteTargetFactory


def getVoteData():
    df= pd.read_csv(VoteData2016)
    df['Vote'] =  VoteTargetFactory.get(df)
    df.drop('Voto',axis=1,inplace=True)
    return df

# print(getVoteData())