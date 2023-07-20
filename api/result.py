import os
def giveMeAnswerKey():
    try:
        file = os.open("answer.txt","r")
        data = file.readlines()
        ans = dict()
        for i in data[:]:
            v = i.strip()
            v = v.split(" ")
            a,b = v
            a = a.strip()
            b = b.strip()
            ans[a] = b
        print(ans)
        return ans
    except:
        print("error")
