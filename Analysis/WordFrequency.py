from collections import Counter
from DataGathering.getVoteData import getVoteData
from DataTransform.Helpers.sanitizeString import sanitizeString
from DataTransform.Helpers.testTransform import string_to_test

# https://github.com/amueller/word_cloud
from wordcloud import WordCloud

import matplotlib.pyplot as plt

votes = getVoteData()

for name,group in votes.groupby('Vote'):
    print(name)
    speeches = group['Discurso']
    concatSpeeches = ''
    for speech in speeches:
        concatSpeeches += ' ' + sanitizeString(str(speech))

    nWord = len(concatSpeeches.split())
    mostCommonWords = Counter(concatSpeeches.split()).most_common()
    for i in range(0,20):
        print(mostCommonWords[i][0],mostCommonWords[i][1]/(nWord))

    wordcloud = WordCloud(max_font_size=40, relative_scaling=.5,background_color='white',max_words=50).generate(concatSpeeches.replace('nao','').replace('sim',''))

    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('Temp/WordCloud_'+name+'.png')
    plt.close()
