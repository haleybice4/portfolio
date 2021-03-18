# trivia challenge
# trivia game that reads a plain text file
#haley bice 12/2

#imports
import sys
from datetime import datetime

#functions
def open_file(file_name,mode):
    """ open and returns an open file with the given permissions """
    try:
        file = open("assets/test_files/"+file_name,mode)
    except IOError as e:
        print("unable to open the file", file_name, "ending program.\n", e)
        try:
            file = open("assets/errors/errors_log.txt","a+")
            time = datetime.now()
            error_time = time.strftime("%m/%d/%y %H:%M:%S")
            file.write(str(e)+" "+str(error_time)+"\n")
            input("\n\npress the enter key to exit.")
            sys.exit()
        except:
            sys.exit()
    else:
        return file




def next_line(file):
    try:
        line = file.readline()
        line = line.replace("/", "\n")
        return line
    except:
        print("could not read line")
        sys.exit()

def next_question(file):
    """return then next question block of data from the trivial file."""
    category = next_line(file)
    question = next_line(file)
    answers = []
    for i in range(4):
        answers.append(next_line(file))
    correct = next_line(file)
    if correct:
        correct = correct[0]
    explanation = next_line(file)
    return category, question, answers, correct, explanation

def get_name():
    try:
        time = datetime.now()
        test_time =  time.strftime("%m/%d/%y %H:%M")
        while True:
            name = input("what is your name?")
            if " " in name:
                name = name.title()
                return name, test_time
            else:
                print("invalid input")
                
    except:
            sys.exit()

def welcome(title, name, test_time):
    """Welcome the player."""
    print("welcome "+name+" to your Mid Term\n")
    print("your tester is "+title)
    
    
def create_Report_Card(name, score, totalQ):
    card = open("assets\\ReportCards\\"+name+".txt","w")
    card.write("name = "+name+"\n")
    card.write("nember correct = "+str(score))
    percentage = score/totalQ*100
    card.write("percentage correct = "+"%"+str(percentage))
    if percentage >= 90:
               card.write("letter grade = A")
    if percentage >= 80 and percentage <90:
               card.write("letter grade = B")
    if percentage >= 70 and percentage <80:
               card.write("letter grade = C")
    if percentage >= 60 and percentage <70:
               card.write("letter grade = D")
    elif percentage < 60:
               card.write("letter grade = F")
    card.close()

def main():
    file = open_file("james_midterm_test.txt", "r")#will need to change file name to match the test that youre taking
    title = next_line(file)
    name, test_time = get_name()
    welcome(title, name, test_time)
    score = 0
    totalQ = 0
    category, question, answers, correct, explanation = next_question(file)
    while category:
        totalQ += 1
        print(category)
        print(question)
        for i in range(len(answers)):
            print(str.format("\t{}:  {}", i+1, answers[i]))
            #get answer
        answer = input("what is your answer?")
            #check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score +=1
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("score:", score, "\n\n")
        #get next question block
        category, question, answers, correct, explanation = next_question(file)
    file.close()
    print("that was the last question!")
    print("you're final score is", score)
    create_Report_Card(name, score, totalQ)
    
    
   
     
    

main()
       
