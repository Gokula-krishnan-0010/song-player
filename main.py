import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def play_song(folder, song_name):
    song_path = os.path.join(folder, song_name)

    if not os.path.exists(song_path):
        print("Song '{song_name}' doesn't exist")
        return
    
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    print(f"Now playing '{song_name}' \n")
    while(True):
        print("Choose commands: [P]ause [R]esume [S]top")
        command = input(">>> ").strip()
        command = command.upper()
        if(command == 'P'):
            pygame.mixer.music.pause()
            print("Song Paused")
        elif(command == 'R'):
            pygame.mixer.music.unpause()
            print("Song Resumed")
        elif(command == 'S'):
            pygame.mixer.music.stop()
            print("Song Stopped")
            return # terminating the play_song fn.
        else:
            print("Invalid command!")
        print()



def main():

    # Check if 'pygame' module is installed
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Pygame initialization failed! {e}")
        return # terminating main fn.
    
    # Check if 'music' folder exist
    folder = "music"
    if not os.path.isdir(folder):
        print(f"Folder '{folder}' doesn't exist!")
        return # terminating main fn.

    # Check if any '.mp3' file exist
    song_lst = [song for song in os.listdir(folder) if(song[-4:] == '.mp3')]
    if not song_lst:
        print(f"There is no song in folder '{folder}' !")
        return # terminating main fn.
    
    # Printing the song list
    print('\n', '*'*5, 'Song player' ,'*'*5)
    print(f"List of songs in folder '{folder}' : \n")
    for index, song in enumerate(song_lst, start=1):
        print(f"{index}. {song[:-4]}")
    print()


    while(True):
        print("Choose the song # to play (or [Q]uit [L]ist of song): ")
        choice = input(">>> ").strip()
        if(choice.upper() == 'Q'):
            print(f"Bye! Have a great day!")
            break # Exiting the program
        elif(choice.upper() == 'L'):
            print('*'*5, 'Song player' ,'*'*5)
            print(f"List of songs in folder '{folder}' :", '\n')
            for index, song in enumerate(song_lst, start=1):
                print(f"{index}. {song[:-4]}")
            print()
            continue # Make theh user choose again

        elif not choice.isdigit():
            print("Enter a valid song no. \n")
            continue # Make the user choose again

        choice = int(choice)-1
        if(0 <= choice < len(song_lst)):
            play_song(folder, song_lst[choice])
        else:
            print("Enter a valid song no. \n")
            continue # Make the user choose again
        print()



if __name__ == "__main__":
    main()