# lets create a small program called Mood_music

import random

mood_songs = {
    "sad": ["Let Her Go – Passenger", "Someone Like You – Adele"],
    "angry": ["Breaking the Habit – Linkin Park", "Duality – Slipknot"],
    "bored": ["Blinding Lights – The Weeknd", "Sugar – Maroon 5"],
    "tired": ["Lovely – Billie Eilish", "Fix You – Coldplay"],
    "happy": ["Happy – Pharrell", "Best Day of My Life – American Authors"],
    "confused": ["Lost – NF", "Demons – Imagine Dragons"]
}

def welcome():
    print("Welcome To The Mood Music.")
   
    while True:
        enter = input("Type 'Continue' to proceed futher or exit to stop the program.")
        if enter == 'continue':
            print('''Choose your mood for today
                [1] sad 
                [2] angry 
                [3] bored 
                [4] tired 
                [5] happy 
                [6] confused 
                ''')
            
            Choice = input("So what's your mood today? Choose your mood: ")
            mood = None
        
        
            if Choice =='1':
                mood = 'sad'
            elif Choice =='2':
                mood = 'angry'
            elif Choice == '3':
                mood = 'bored'
            elif Choice == '4':
                mood = 'tired'
            elif Choice == '5':
                mood = 'happy'
            elif Choice =='6':
                mood = 'confused'
            else: 
                print("Invalid Choice.")
            song = random.choice(mood_songs[mood])
            print(f"You should listen to: {song}")

        elif enter == 'exit': 
            print("see you again")
            break
        else: 
            print("Invalid input. Please type 'Continue' or 'exit'.\n")
            
def main():
    welcome()

#Entry point
if __name__ == "__main__":
    main()



   

   

