##A simple program that authors a simple letter for you

class Letter:
    ##initializes the sender and the receiver of the letter
    def __init__(self, letterFrom, letterTo):
        self.sender = letterFrom
        self.receiver = letterTo

    def createText(self, text):
        self.line = str(text)

    ##adds a line to the letter
    def addLine(self, line):
        self.line += line

    ##returns the entire text of the letter
    def getText(self):
        print(self.line)
        return

def write():
    print("Letter writer \nWrite the sender and receiver for your letter\n")
    sender = input("Sender of the letter: ")
    receiver = input("Receiver of the letter: ")

    letter = Letter(sender, receiver)
    letter.createText("Dear "+receiver+": \n\n")

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
            text = "\nSincerely, \n\n"+sender+""
            letter.addLine(text)
            letter.getText()

        else:
            letter.getText()
            break

write()