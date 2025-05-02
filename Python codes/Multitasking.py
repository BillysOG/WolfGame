import threading as th
import time

def text():
    print("You're texting....")
    time.sleep(15)
    print("....You're done texting")
    
def music(song):
    print(f"You're listening to {song} ....")
    time.sleep(10)
    print(f"....You're done listening to {song}")
    
def play(game):
    print(f"You're playing {game} ....")
    time.sleep(5)
    print(f"....You're done playing {game}")
 
def main():   
    
    song = "Tyler, the Creator"
    game = "Genshin Impact"
    
    print("********************************\nMultitasking\n********************************")
    do1 = th.Thread(target = text)
    do2 = th.Thread(target = music, args = (song,))
    do3 = th.Thread(target = play, args = (game,))

    do1.start()
    do2.start()
    do3.start()

    do1.join()
    do2.join()
    do3.join()

    print("********************************\nYou're done multitasking\n********************************")
    
if __name__ == "__main__":
    main()