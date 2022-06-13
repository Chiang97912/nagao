import sys
sys.path.append('../')
import time
from nagao import Nagao


def test_en():
    file_corpus = 'data/gameofthrones.txt'
    file_output = 'vocab-en.tsv'
    nagao = Nagao(lang='en', min_ngram=2, max_ngram=6, min_freq=5, min_lrc=2, min_lre=0.5, min_pmi=0, min_eta=0, threshold=0, use_disk=True, use_db=True, lower=True, clean=True)
    ts = time.time()
    nagao.process(file_corpus)
    nagao.save(file_output)
    print('total spend:', time.time() - ts)


def test_zh():
    file_corpus = 'data/天龙八部.txt'
    file_output = 'vocab-zh.tsv'
    nagao = Nagao(lang='zh', min_ngram=2, max_ngram=8, min_freq=6, min_lrc=2, min_lre=0.5, min_pmi=1e-5, min_eta=0, threshold=0, use_disk=True, use_db=True, lower=False, clean=True)
    ts = time.time()
    nagao.process(file_corpus)
    nagao.save(file_output)
    print('total spend:', time.time() - ts)


if __name__ == "__main__":
    test_zh()
