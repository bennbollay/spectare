import os
import sys
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/benn/.google/spectare-71684f33af9a.json'

from trans.google_sample import sample_translate as translate
from objdet.google_sample import sample_objdet as objdet
from stt.google_sample import sample_stt as stt

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(sys.argv[0] + ' [translate, objdet, stt]')
        exit()

    if sys.argv[1] == 'translate':
        result = translate()
    elif sys.argv[1] == 'objdet':
        result = objdet()
    elif sys.argv[1] == 'stt':
        result = stt()
    else:
        print(sys.argv[0] + ' [translate, objdet, stt]')
        exit()

    print(json.dumps(result, indent=2, ensure_ascii=False))

