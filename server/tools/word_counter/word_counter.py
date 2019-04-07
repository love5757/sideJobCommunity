import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def tag_counting(file):
    f = open(file, "r",encoding="utf8")

    from konlpy.tag import Okt

    lines = f.readlines()

    word_count = {}
    for line in lines :
        nlpy = Okt()
        nouns = nlpy.nouns(line)

        from collections import Counter
        count = Counter(nouns)

        for n, c in count.most_common(100):
            try:
                word_count[n] += c
            except:
                if len(n) >= 2 :
                    word_count[n] = c

    f = open("result.cvs", "w",encoding="utf8")
    for name in word_count:
        f.write("%s,%d\n" % (name,word_count[name]))

tag_counting(file = "../parser_test/source.txt")
