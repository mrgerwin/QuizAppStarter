from guizero import App, info, Text, PushButton, ButtonGroup, Picture, TextBox
import random

def nameChanged():
    nameLabel.value = "Your Name is: " + nameTextBox.value

def shuffleChoices():
    pass

def nextPressed():
    global index
    index += 1
    if index >= len(ImageList):
        index = 0
    print(index)
    updateQuestion()
    
    for item in ScoreList:
        if item == False:
            return
        
    info("Quiz Over", "Your Score is: " + str(score))
        
def updateQuestion():
    global index
    
    picture.image = ImageList[index]
    question.value = questionList[index]
    correctLabel.value = ""
    
    temp = []
    for choiceButton in answerChoices.get_group_as_list():
        temp.append(choiceButton[0])
    for choice in temp:
        answerChoices.remove(choice)
    for choice in choicesList[index]:
        answerChoices.append(choice)
        

def checkAnswer():
    global score
    if ScoreList[index] == False:
        if answerList[index] == answerChoices.value:
            print("Correct")
            correctLabel.value = "Correct"
            score += 1
            print(score)
            ScoreLabel.value = "Score = " + str(score) + "/" + str(len(questionList))
        else:
            print("Incorrect")
            correctLabel.value = "Incorrect"
    
    ScoreList[index] = True
    
def submitPressed():
    checkAnswer()
    

questionList = []
question1 = "Select the word that means an object from some class."
question2 = "Variables that are used to describe data of objects are called _______________."
question3 = "Functions that are used to describe the behavior of objects are called _______________."
question4 = "What is a string when referred to in computer programming?"
question5 = "In computer programming, is a list a type of function?"

questionList.append(question1)
questionList.append(question2)
questionList.append(question3)
questionList.append(question4)
questionList.append(question5)


answerList = ["Instance", "Properties", "Methods", "Text", "No"]
choicesList = [["Creation", "Instance", "Establishment", "Definition"], ["Properties","Numbers", "Files", "Descripters"], ["Regulators", "Events", "Elaborators", "Methods"],["Yarn", "Guitars", "Text", "Functions"], ["Yes", "No"]]

ImageList = ["ImageQuestion1.png", "ImageQuestion2.png", "ImageQuestion3.png", "ImageQuestion4.png", "ImageQuestion5.png"]

ScoreList = [False, False, False, False, False]

index = 0
score = 0

app = App(title="Quiz App", height = 800, width = 1200)
nameLabel = Text(app, text="Your Name: ")
nameTextBox = TextBox(app, command=nameChanged)
picture = Picture(app, image = "ImageQuestion1.png")
question = Text(app, text = question1)
submitButton = PushButton(app, text = "Submit Answer", command = submitPressed)
nextButton = PushButton(app, text = "Next Question", command = nextPressed)
answerChoices = ButtonGroup(app, options = ["Creation", "Instance", "Establishment", "Definition"], selected = None)

correctLabel = Text(app, text="")

ScoreLabel = Text(app, text="")

app.display()