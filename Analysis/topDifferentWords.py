from collections import Counter

import matplotlib.pyplot as plt
import scipy as sp
from wordcloud import WordCloud

from DataGathering.sanitizeString import sanitizeString


class topDifferentWords:

    def __init__(self,votes):

        yesWordsDic = {}
        noWordsDic = {}


        for name,group in votes.groupby('Vote'):
            speeches = group['Discurso']
            concatSpeeches = ''
            for speech in speeches:
                concatSpeeches += ' ' + sanitizeString(str(speech))

            nWord = len(concatSpeeches.split())
            mostCommonWords = Counter(concatSpeeches.split()).most_common()
            for i in range(0,len(mostCommonWords)):
                if name== True:
                    yesWordsDic[mostCommonWords[i][0]] = mostCommonWords[i][1] / (nWord)
                else:
                    noWordsDic[mostCommonWords[i][0]]  = mostCommonWords[i][1] / (nWord)

        self.wordRelativeFreqDic = yesWordsDic.copy()

        for pair in noWordsDic.items():
            if pair[0] in self.wordRelativeFreqDic:
                self.wordRelativeFreqDic[pair[0]] = self.wordRelativeFreqDic[pair[0]] - pair[1]
            else:
                self.wordRelativeFreqDic[pair[0]] = -pair[1]


    def topWords(self,vote,plotWordCloud=True):

        freqs = list(self.wordRelativeFreqDic.values())

        topWord = {}
        percLimit = 1
        # print("Top words on ",vote)
        if vote=='Yes':
            thr = sp.percentile(freqs,q=100-percLimit)
        else:
            thr = sp.percentile(freqs,q=percLimit)
        total = 0
        for pair in self.wordRelativeFreqDic.items():
            if (vote=='Yes' and pair[1]>thr) or (vote=='No' and pair[1]<thr):
                topWord[pair[0]] = abs(pair[1])
                total += topWord[pair[0]]

        if plotWordCloud:
            for key in topWord:
                topWord[key] = topWord[key]/total
                print(key,topWord[key])


            wordcloud = WordCloud(max_font_size=40, relative_scaling=.5,background_color='white',max_words=50).generate_from_frequencies(topWord.items())

            plt.figure()
            plt.imshow(wordcloud)
            plt.axis("off")
            plt.savefig('Temp/WordCloud_TopOnly'+vote+'.png')
            plt.close()

        listKeys = list(topWord.keys())
        try:
            listKeys.remove('sim')
        except:
            pass
        try:
            listKeys.remove('nao')
        except:
            pass

        return listKeys

# topDif = topDifferentWords(getVoteData())
#
# print(topDif.topWords('Yes'))
# print(topDif.topWords('No'))