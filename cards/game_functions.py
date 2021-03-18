import sys
import datetime



def get_name(question):
    while True:
        name=input(question)
        if len(name)>=2:
            return name
        print("name isn't long enough")


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


def get_number(question, low, high):
    while True:
        number=input(question)
        if number.isnumeric():
            number=int(number)
            if number>=low and number<=high:
                return number
        print("Not a good input")



def get_player_names(player_name, family_list):
    player_name = get_name("Enter wagon leaders name")
    family=get_number("How many members are in your family", 2,5)
    for i in range(family):
        name = get_name("Enter family member name")
        family_list.append(name)
    return player_name, family_list




def welcome(title, name, test_time):
    """Welcome the player."""
    print("welcome "+name+" to your Mid Term\n")
    print("your tester is "+title)


class Player(object):
   def __init__(self,name):
        self.name=get_name
        self.score=0
