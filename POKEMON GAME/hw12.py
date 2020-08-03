import tkinter as tk
import random

#FIRST: Implement and test your Pokemon class below
class Pokemon:
    def __init__(self,name, dex, catchRate = 0, speed = 0):
        self.name = name
        self.dex = dex
        self.catchRate = int(catchRate)
        self.speed = speed
        
    def __str__(self):
        return self.name

#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        print("In SafariSimulator init")
        
        #Read in the data file from pokedex.csv at some point here
        #It's up to you how you store and handle the data 
        #(e.g., list, dictionary, etc.),
        #but you must use your Pokemon class in some capacity

        f = open("pokedex.csv")
        read = f.readlines()
        self.list1= []

        for x in read:
            
            poke = x.split(',')

            if poke[0] == "Dex":
                continue 
           
            self.list1.append(Pokemon(poke[1],poke[0], poke[2], poke[3] ))
            

        self.pokeBalls = 30
        self.capturedPoke = []
        
        self.current = random.choice(self.list1)
        
       
        
        #Initialize any instance variables you want to keep track of

        #DO NOT MODIFY: These lines set window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()
        self.createWidgets()

        #Call nextPokemon() method here to initialize your first random pokemon
        

        
        #Call nextPokemon() method here to initialize your first random pokemon
    
    def createWidgets(self):
        print("In createWidgets")
        #See the image in the instructions for the general layout required
        #"Run Away" button has been completed for you as an example:
   
        
       
        self.throw = tk.Button(self)
        self.throw["text"] =  "Throw Safari Ball " + str(self.pokeBalls) + " left"
        self.throw["command"] = self.throwBall
        self.throw.pack()

        self.runAwayButton = tk.Button(self)
        self.runAwayButton ["text"] = "Run Away"
        self.runAwayButton ["command"] = self.nextPokemon
        print(self.runAwayButton)
        self.runAwayButton.pack()
       
        self.text = tk.Label(self, bg='grey',width=50)
        self.text['bg'] = "grey"
        self.text["text"]= "You encoutnered a wild " + str(self.current)
        self.text.pack(fill = 'x', pady = 5 , padx = 5)
       
       
        self.insert_image = tk.PhotoImage(file = "sprites\\"+ str(self.current.dex)+".gif")
        self.imagelab = tk.Label(self)
        self.imagelab["image"] = self.insert_image
        self.imagelab.image = self.insert_image
        self.imagelab.pack()
       
        self.endtext = tk.Label(bg='grey')
        self.endtext["text"] = "Your Chance of catching it is " +str(int(min((self.current.catchRate+1), 151) / 449.5* 100))+("%!")
        self.endtext.pack(fill = "x", pady = 5 , padx = 5)

        self.throwText = tk.Label(bg='grey')
        self.throwText["text"] = "Pokemon has a " +str(round((2 * int(self.current.speed)/256)*100)) + "% of running away"  
        self.throwText.pack(fill = "x", pady = 5 , padx = 5)

        
        #You need to create an additional "throwButton"

        #A label for status messages has been completed for you as an example:
        

        #You need to create two additional labels:

        #Complete and pack the pokemonImageLabel here.

        #Complete and pack the catchProbLabel here.

    def nextPokemon(self):
        print("In nextPokemon")
        self.current = random.choice(self.list1)
        

        self.text['text'] = "You encoutnered a wild " + str(self.current.name)
        
                
        
        self.imagelab1= tk.PhotoImage(file = "sprites\\"+ str(self.current.dex)+".gif")
        self.imagelab["image"] = self.imagelab1

        self.endtext["text"] = "Your Chance of catching it is " + str(int(min((self.current.catchRate+1), 151) / 449.5* 100))+ "%!"

       
        self.throwText["text"] = "Pokemon has a " +str(round((2 * int(self.current.speed)/256)*100)) + "% of running away"  


           
        #This method must:
            #Choose a random pokemon
            #Get the info for the appropriate pokemon
            #Ensure text in messageLabel and catchProbLabel matches the pokemon
            #Change the pokemonImageLabel to show the right pokemon

        #Hint: to see how to create an image, look at the documentation 
        #for the PhotoImage/Label classes in tkinter.
      


        
        #Once you generate a PhotoImage object, it can be displayed 
        #by setting self.pokemonImageLabel["image"] to it
        
        #Note: the PhotoImage object MUST be stored as an instance
        #variable for some object (you can just set it to self.photo).
        #Not doing this will, for weird memory reasons, cause the image 
        #to not be displayed.
        
    def throwBall(self):
        print("In throwBall")
        
        #This method must:

            #Decrement the number of balls remaining
            #Try to catch the pokemon
            #Check to see if endAdventure() should be called

        if self.pokeBalls == 0:
            print("job well done")
            self.endAdventure()
            
        else:
            rand = random.random()
            ball = min((self.current.catchRate+1), 151) / 449.5

            self.pokeBalls -= 1
            self.throw["text"]= "Throw Pokeball ("+str(self.pokeBalls)+" left)"
        


            if rand < ball:
                self.text['text'] = "Caught"
                self.capturedPoke.append(self.current)
                self.nextPokemon()
            else:
               self.text['text'] = "Aargh! It escaped "

            
                  
            

        #To determine whether or not a pokemon is caught, generate a random
        #number between 0 and 1, using random.random().  If this number is
        #less than min((catchRate+1), 151) / 449.5, then it is caught. 
        #catchRate is the integer in the Catch Rate column in pokedex.csv, 
        #for whatever pokemon is being targetted.
        
        #Don't forget to update the throwButton's text to reflect one 
        #less Safari Ball (even if the pokemon is not caught, it still 
        #wastes a ball).
        
        #If the pokemon is not caught, you must change the messageLabel
        #text to "Aargh! It escaped!"
        
        #Don't forget to call nextPokemon to generate a new pokemon 
        #if this one is caught.
        
    def endAdventure(self):
        print("In endAdventure")

        self.text['text'] = "You're all out of balls, I hope you had fun!"

        
        #This method must: 

            #Display adventure completion message
            #List captured pokemon

        #Hint: to remove a widget from the layout, you can call the 
        #pack_forget() method.
        
        #For example, self.pokemonImageLabel.pack_forget() removes 
        #the pokemon image.
        self.imagelab.pack_forget()
        self.runAwayButton.pack_forget()
        self.throw.pack_forget()
        self.throwText.pack_forget()
        

        if len(self.capturedPoke) == 0:
            print("sorry no pokemons")

        else:
            caughtpoke = ""
            for x in self.capturedPoke:
                caughtpoke += str(x) +"\n"
        
        self.endtext["text"] = "You Caught " + str(len(self.capturedPoke))+ " Pokemons:" + "\n" + caughtpoke




#DO NOT MODIFY: These lines start your app
app = SafariSimulator(tk.Tk())
app.mainloop()
