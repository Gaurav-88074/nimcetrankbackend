import requests
from bs4 import BeautifulSoup
import requests
def computeRightAnswerValue(rightAnswerText):
    data = rightAnswerText.split(".")
    return str(data[0]).strip()
def computeUserAnswerValue(userAnswerText):
    # data = rightAnswerText.split(".")
    index = userAnswerText.index("Chosen Option")
    s = userAnswerText[index:]
    # print(s)
    s = s.split(":")
    return str(s[-1]).strip()   
def computeMaths(result,rightAnswer,userAnswer):
    if rightAnswer==userAnswer:
        result["maths"]+=12
    else:
        result["maths"]-=3
def computeLogicalResoning(result,rightAnswer,userAnswer):
    if rightAnswer==userAnswer:
        result["lr"]+=6
    else:
        result["maths"]-=1.5
def computeComputer(result,rightAnswer,userAnswer):
    if rightAnswer==userAnswer:
        result["cs"]+=6
    else:
        result["cs"]-=1.5
def computeEnglish(result,rightAnswer,userAnswer):
    if rightAnswer==userAnswer:
        result["eng"]+=4
    else:
        result["eng"]-=1
def computeScore(questionNumber,result,rightAnswer,userAnswer):
    if questionNumber<=50:
        computeMaths(result,rightAnswer,userAnswer)
    elif questionNumber>=51 and questionNumber<=90:
        computeLogicalResoning(result,rightAnswer,userAnswer)
    elif questionNumber>=91 and questionNumber<=110:
        computeComputer(result,rightAnswer,userAnswer)
    elif questionNumber>=111 and questionNumber<=120:
        computeEnglish(result,rightAnswer,userAnswer)
def computeUserInfo(arr):
    applicationSequenceNumber = arr[1].text.strip()
    name = arr[3].text.strip()
    TC_name = arr[5].text.strip()
    return {
        'rollNumber' : applicationSequenceNumber,
        'candidateName' : name,
        'TC Name' : TC_name
    }
def printQuestionStats(questionsArray):
    totalAttempt = 0
    result = {
        "maths" : 0,
        "lr" : 0,
        "cs" :0,
        "eng":0
    }
    for questionNumber,question in enumerate(questionsArray):
        data  = str(question.text).strip()
        if "Not Answered" in data:
            pass
            # print(questionNumber," Not Answered")
        else:
            totalAttempt+=1
            rightAnswerObj = question.find(class_='rightAns')
            rightAnswer = computeRightAnswerValue(rightAnswerObj.text)
            userAnswer  = computeUserAnswerValue(data)

            computeScore(questionNumber+1,result,rightAnswer,userAnswer)
            # print(questionNumber+1,rightAnswer,userAnswer)
        # print("-----------------")
    # print(result)
    # print(sum(result.values()))
    return result