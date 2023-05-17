import json
from urllib.request import urlopen
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

'''
This script plays a 10 count console game of trivia
Then the W/L data is generated into a graph
That is then presented on the screen.

                                Jodi
'''
def pullData(data):
    try:
        quizUrl = "https://the-trivia-api.com/api/questions/"
        df = pd.read_json(quizUrl)

        return(df)
    except:
        print("An error occured at pullData().")

def sortData(inccorectList):
    #function stores incorrect answers and returns 1d array.
    try:
        quickArray = []
        for x in inccorectList:
            quickArray.append(x)

        return quickArray
    except:
        print("An error occured at sortData().")

def checkAnswer(dataArray):
    try:

        print(dataArray)
        playerChoice = dataArray[0]
        correctAnswer = dataArray[1]
        answers = dataArray[2]
        translateAnswer = {1:0,2:1,3:2,4:3}
        choice = translateAnswer.get(int(playerChoice))

        if answers[choice] == correctAnswer:
            print("Correct! "+correctAnswer)
            return "O"
        else:
            print("Incorrect! Correct Answer is: "+correctAnswer)
            return "X"
    except:
        print("An error occured at checkAnswer")

def playGame(data):
    try:
        #Additional columns from API that can be incorporated into script
        #category = (data.category)
        #QuesId = data.id
        #difficulty = data.difficulty

        #Variables storing the correct answer, the incorrect answers, and the question
        correctAnswer = data.correctAnswer
        incorrectAnswers = data.incorrectAnswers
        question = np.array(data.question)

        #Numebrs will display on console to indicate numbers the user can press
        optionsArray = [1,2,3,4]
        scoreKeeper = []

        #Enumerating over questions. Each loop will check the players answer, and record W/L
        for num,ques in enumerate(question):

            testChoices = sortData(incorrectAnswers[num])
            testChoices.append(correctAnswer[num])
            random.shuffle(testChoices)
            print(ques)
            print(testChoices)
            print(optionsArray)
            userAns = input("Please select you answer:")

            #Storing data needed for next Func call
            answerCheckArray = [userAns,correctAnswer[num],testChoices]

            #checkAnswer will verify if player has W or L, and return score to record in scoreKeeper array
            score = checkAnswer(answerCheckArray)
            scoreKeeper.append(score)

        #returns final scores from Game
        return(scoreKeeper)
    except:
        print("An error ocured at playGame().")

#Func to format Graph of Game results
def formatGameGraph(scoreData):
    try:
        wins = []
        losses = []

        for score in scoreData:
            if score == "O":
                wins.append(score)
            else:
                losses.append(score)

        #building Graph
        graphData = [len(wins),len(losses)]
        yMax = len(scoreData)

        fix,ax = plt.subplots()
        plt.axis([None,None,0,yMax])
        xAxis = ["Wins","Losses"]
        bar_colors = ['tab:green','tab:red']
        ax.bar(xAxis,graphData,color=bar_colors)

        ax.set_ylabel("Number of Games")
        ax.set_title('Game Win and Losses')

        #returns created graph
        return(plt)
    except:
        print("An Error occurred at formatGameGraph().")

#Shows graph/do other stuff with final graph.
def finalReport(graphData):
    try:
        graphData.show()
    except:
        print("An error occured at finalReport().")

if __name__ == "__main__":

    data = []

    data = pullData(data)
    scores = playGame(data)
    graph = formatGameGraph(scores)
    finalReport(graph)

