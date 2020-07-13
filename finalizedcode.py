from tkinter import *
import random
import time



class Application(Frame):
    def __init__(self, master):
       
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.pick_rnumber()
        self.number_of_tries()
    
    

        
    
    
    def create_widgets(self):
        self.starttimevalue = time.time()
        self.starttime = time.strftime("%H:%M:%S")
        #self.runtime(starttime)
        #Create timer label
        Label(self, text= "Start Time = {}".format(self.starttime)).grid(row = 0,column = 0, sticky = W)
        #Create title label
        #Customize the label for Anjali
        #Label(self, text = 'Harrisons Number Guess Game'
        Label(self, text = 'Anjalis Number Guess Game'
              ).grid(row = 0, column = 2, columnspan = 1, sticky = N)
        # create instruction labels
        #Decrease the Random Number Range from 1-100 to 1-50
        #Label(self, text = 'Try and guess a number between 1-100'
        Label(self, text = 'Try and guess a number between 1-50'
              ).grid(row = 1, column = 0, columnspan = 3, sticky = W)
        Label(self, text = 'Try to guess in as few attempts as possible'
              ).grid(row = 2, column = 0, columnspan = 3, sticky = W)
        Label(self, text = 'You will recieve input after each guess on whether your guess is too LOW or too HIGH'
              ).grid(row = 3, column = 0, columnspan = 3, sticky = W)
        # Create a label and number entry
        Label(self, text = 'Your guess: '
              ).grid(row = 4, column = 0, sticky = W)
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 4, column = 1, sticky = W)
        self.guess_ent.focus() # put cursor in entry
        # create label and text box for number of tries
        Label(self, text = 'Number of tries: '
              ).grid(row = 5, column = 0, sticky = W)
        self.no_tries_txt = Text(self, width = 2, height = 1, wrap = NONE)
        self.no_tries_txt.grid(row = 5, column = 1, sticky = W)
        # create guess button
        Button(self, text = 'Guess', command = self.check_if_correct
               ).grid(row = 5, column = 2, sticky = W)
        self.result_txt = Text(self, width = 80, height = 15, wrap = WORD)
        self.result_txt.grid(row = 6, column = 0, columnspan = 4)
    def pick_rnumber(self):
        #Decrease the Random Number Range from 1-100 to 1-50
        #self.rand_number = random.randint(1, 100)
        self.rand_number = random.randint(1, 50)
        #This print statement facilitates testing so that we can test for the correct guess
        print(self.rand_number) # test
    def check_if_correct(self):
        self.result = ""
        gnum = self.guess_ent.get()
        gnum = int(gnum)
        if gnum == self.rand_number:
            gnum = str(gnum)
            self.result = gnum + "  is the correct number!! Congrats"
            self.tries += 1
        elif gnum < self.rand_number:
            gnum = str(gnum)
            self.result = gnum + " is TOO LOW....HINT: Try guessing higher.\n"
            self.tries += 1
        elif gnum > self.rand_number:
            gnum = str(gnum)
            self.result = gnum + " is TOO HIGH....HINT: Try guessing lower.\n"
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
    def timeout(self):
        end_time = starttimevalue + 30.0
        while time.time() < end_time:
            time_remaining = end_time - time.time()
            return "You have "+str(time_remaining)+" seconds remaining"
        return "Time's up."
# main
root = Tk()
root.title('Guess the Number')
app = Application(root)
root.mainloop()
