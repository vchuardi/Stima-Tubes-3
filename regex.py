import re

question = ["bagaimana kabar anda", "apakah jagung bisa dimakan", "apakah anda menyukai kentang", "siapakah anda"]
answer = ["Baik", "Jagung bisa dimakan", "Tidak, Xyli tidak suka kentang", "Saya adalah Xyli"]
synonym = [("anda", "kamu", "mu", "lu", "loe"),("kabar", "keadaan")]
ignore = ["itu", "anda"]

#print(synonym[0][0])

questionsize = len(question)
print("Hi, selamat datang di chatbot Xyli")
print("Apakah anda memiliki pertanyaan yang ingin ditanyakan?")
print("Anda : ", end='')
pertanyaan = input()
pertanyaan = pertanyaan.split(" ")

while pertanyaan[0]!="exit" :
    isAnswerExist = True

    print("Xyli : ", end='')


    for idx,sentence in enumerate(question):
        for kata in pertanyaan:
            b = True
            #print(idx)
            if kata in ignore :
                continue
            if re.search(kata.lower(),sentence)==None:
                #print("b")
                for i in range(len(synonym)):
                    #print(synonym[i])
                    #print(kata)
                    #print("lower:", kata.lower())
                    if kata.lower() in synonym[i]:
                        b=False
                        #print("c")
                        for j in range(len(synonym[i])):
                            if re.search(synonym[i][j].lower(),sentence)!= None:
                                a=True
                                #kata=synonym[i][j]
                                #print(synonym[i][j])
                                #print("j=", j)
                                """"
                                if re.search(kata.lower(),sentence)!=None:
                                    a=True
                                    break
                                """


                        #if j==len(synonym[i])-1:
                        if a:
                            #isAnswerExist=False
                            break
                        else:
                            isAnswerExist = False
                if b:
                    isAnswerExist = False




                #if a:
                    # isAnswerExist=False
                    #break
                #else:
                    #isAnswerExist = False
                #if i==len(synonym)-1:
                    #isAnswerExist = False
                    #break


        if isAnswerExist :
            print(answer[idx])
            break

        if idx==(questionsize-1) and not isAnswerExist :
            print("Xyli tidak mengerti pertanyaan anda")

        isAnswerExist = True

    print("Anda : ", end='')
    pertanyaan = input()
    pertanyaan = pertanyaan.split(" ")
