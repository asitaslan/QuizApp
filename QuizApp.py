import random
class Question:
    def __init__(self,text,choice,answer):
        self.questions = text
        self. choice = choice
        self.answer = answer
    def checkAnswer(self, answer):
        if answer not in self.choice:
            raise ValueError("Your answer is not in Choices")
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))
        self.questionsIndex =0
        self.point = 0
    def getQuestions(self):
        return self.questions[self.questionsIndex]

    def displayQuestions(self):
        question = self.getQuestions()

        print(f"Question {self.questionsIndex +1} : {question.questions}")

        for i in question.choice:
            print("-" + i)

        answer = input("Your Answer :")
        if (question.checkAnswer(answer)):
            self.point += 33.3

        self.questionsIndex +=1

        if len(self.questions) == self.questionsIndex:
            result = round(self.point)
            print(result)
        else:
            self.displayQuestions()




q1 = Question("Which team is the last champions legue champion ", ["Bayern Munchen","Liverpool","Real Madrid", "PSG","Barcelona"],"Bayern Munchen")
q2 = Question("Which team is Premiere Legue champion",["Chelsea", "Liverpool", "Manchester United", "Manchester City", "Tothenam"],"Liverpool")
q3 = Question("Whic team is the best team in Turkey Super Legue",["Fenerbahce","Galatasaray","Besiktas","Trabzonspor","Basaksehir"],"Fenerbahce")

_questions = [q1,q2,q3]

quiz = Quiz(_questions)

print(quiz.displayQuestions())

