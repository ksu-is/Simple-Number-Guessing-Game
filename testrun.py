# guess the number in a GUI
from tkinter import *
import random
class Application(Frame):
    ''' GUI guess the number application  '''
    def __init__(self, master):
        '''initialise frame'''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.pick_rnumber()
        self.number_of_tries()
    def create_widgets(self):
        '''create widgets for GUI guess game'''
        #Create title label
        Label(self, text = 'Harrisons Number Guessing Game'
              ).grid(row = 0, column = 1, columnspan = 2, sticky = N)
        # create instruction labels
        Label(self, text = 'Try and guess a number between 1-1000'
              ).grid(row = 1, column = 0, columnspan = 3, sticky = W)
        Label(self, text = 'Try to guess in as few attempts as possible'
              ).grid(row = 2, column = 0, columnspan = 3, sticky = W)
        Label(self, text = 'I will tell you to go higher or lower after each guess'
              ).grid(row = 3, column = 0, columnspan = 3, sticky = W)
        # Create a label and number entry
        Label(self, text = 'Your guess: '
              ).grid(row = 4, column = 0, sticky = W)
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 4, column = 1, sticky = W)
        self.guess_ent.focus() # put cursor in entry
        # create label and text box for number of tries
        Label(self, text = ' number of tries: '
              ).grid(row = 5, column = 0, sticky = W)
        self.no_tries_txt = Text(self, width = 2, height = 1, wrap = NONE)
        self.no_tries_txt.grid(row = 5, column = 1, sticky = W)
        # create guess button
        Button(self, text = 'Guess', command = self.check_if_correct
               ).grid(row = 5, column = 2, sticky = W)
        self.result_txt = Text(self, width = 80, height = 15, wrap = WORD)
        self.result_txt.grid(row = 6, column = 0, columnspan = 4)
    def pick_rnumber(self):
        self.rand_number = random.randint(1, 1000)
        print(self.rand_number) # test
    def check_if_correct(self):
        self.result = ""
        gnum = self.guess_ent.get()
        gnum = int(gnum)
        if gnum == self.rand_number:
            gnum = str(gnum)
            self.result = gnum + "  is the magic number!! let the trumpets sound\n"
            self.tries += 1
        elif gnum < self.rand_number:
            gnum = str(gnum)
            self.result = gnum + " is too low, Guess higher.\n"
            self.tries += 1
        elif gnum > self.rand_number:
            gnum = str(gnum)
            self.result = gnum + " is too high, Guess lower.\n"
            self.tries += 1
        self.give_result()
        print(self.tries) # test
    def number_of_tries(self):
        self.tries = 0
    def give_result(self):
        # display the results
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, self.result)
        self.no_tries_txt.delete(0.0, END)
        self.no_tries_txt.insert(0.0, self.tries)
# main
root = Tk()
root.title('Guess the Number')
app = Application(root)
root.mainloop()
