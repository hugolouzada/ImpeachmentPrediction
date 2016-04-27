from DataGathering.getVoteData import getVoteData
import matplotlib.pyplot as plt

def getSpeechSize(df):
    return df['Discurso'].map(lambda d: len(str(d)))

def testSpeechSize():
    votes = getVoteData()
    votes['SpeechSize'] = getSpeechSize(votes)

    plt.figure()
    votes.boxplot(column='SpeechSize',by='Vote')
    plt.savefig("test.png")


testSpeechSize()