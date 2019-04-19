#!/usr/bin/env python

import re
import sys

class m:
    def getAnswer(pertanyaan,question,answer,ignore):
        questionsize = len(question)
        isAnswerExist = True

        for idx,sentence in enumerate(question):
            for kata in pertanyaan:
                if kata in ignore :
                    continue
                if re.search(kata.lower(),sentence)==None:
                    isAnswerExist = False
            
            if isAnswerExist :
                result = answer[idx]
                # print(answer[idx])
                break

            if idx==(questionsize-1):
                result = "Saya tidak mengerti pertanyaan anda"
                # print("Saya tidak mengerti pertanyaan anda")
            
            isAnswerExist = True

        # print("Anda : ", end='')
        # pertanyaan = input()
        # pertanyaan = pertanyaan.split(" ")
        
        return result

question = ["bagaimana kabar anda", "apakah jagung bisa dimakan", "apakah anda menyukai kentang", "siapakah anda", "halo", "apakah kamu single", \
            "dimana tinggal"]
answer = ["Baik", "Jagung bisa dimakan", "Tidak, Xyli tidak suka kentang", "Saya sadalah Xyli", "Hi", "Saya tidak bisa menjawab pertanyaan tersebut", \
    "Saya tinggal di lingkungan siber"]
ignore = ["itu", "anda", "kamu"]

m1 = m
qlen = len(sys.argv)-1
pertanyaan = ""
for i in range(1,qlen+1):
    if i == 1:
        pertanyaan = sys.argv[i]
        continue
    pertanyaan = pertanyaan + " " + sys.argv[i]
print(pertanyaan)
print(m1.getAnswer(pertanyaan,question,answer,ignore))