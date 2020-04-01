from script30 import *
sentence=neko_lines()
for i in range(0, len(sentence) - 2):   
    if sentence[i]['pos'] == '名詞' and \
        sentence[i+1]['surface'] == 'の' and \
        sentence[i+1]['pos'] == '助詞' and \
        sentence[i+1]['pos1'] == '連体化' and \
        sentence[i+2]['pos'] == '名詞':
        print('{}の{}'.format(sentence[i]['surface'], sentence[i+2]['surface']))