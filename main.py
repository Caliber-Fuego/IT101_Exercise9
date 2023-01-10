##A simple program that authors a simple letter for you

class Letter:
    ##initializes the sender and the receiver of the letter
    def __init__(self, letterFrom, letterTo):
        self.sender = letterFrom
        self.receiver = letterTo

    ##Intializes the text for the letter
    def createText(self):
        self.line = str()

    ##adds a line to the letter
    def addLine(self, line):
        self.line += line

    ##returns the entire text of the letter
    def getText(self):
        print("Dear "+self.receiver+": \n")
        print(self.line)
        print("Sincerely, \n\n"+self.sender+"")
        return

def write():
    print("Letter writer \nWrite the sender and receiver for your letter\n")
    sender = input("Sender of the letter: ")
    receiver = input("Receiver of the letter: ")

    letter = Letter(sender, receiver)
    letter.createText()

    while True:
        print("Letter Options: \n1. Add a line \n2. View Letter \n3. Finish Writing Letter\n0. Exit")
        choice = input()
        if choice == "1":
            userinput = input("Input the text you want to add to the letter: ")
            text = userinput + "\n"
            letter.addLine(text)
            print("\n")

        elif choice == "2":
            letter.getText()
            print("\n")

        elif choice == "3":
            letter.getText()
            break
        else:
            letter.getText()
            break

write()