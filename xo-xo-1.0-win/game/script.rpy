define alee = Character("Aleena", color="#0066FF", image="bla")

label start:
    "Five minutes have passed, and now it's time to decide what game to play with friends."

    play music "audio/background.mp3" 

    scene hall  
    scene joan_bg
    "Joan: Hey, what game should we play today."
    scene shrey_bg
    "Shreyansh: I don't know, I'm up for anything."
    hide joan
    hide shrey
    scene sauri_bg
    "Saurav: How about some classic board game."

    scene alee_bg

    alee "Aleena: You know, I'm suddenly reminded of Asta Chamma, that Indian ludo game we used to play with shells."

    "In a rush of nostalgia, Aleena leaves the room and runs to her bedroom."

    show room with dissolve

    "Aleena rummages through her closet and finds the old Asta Chamma board and four shells."

    scene board_room

    alee "Aleena: I found it! Let's play Asta Chamma, just like the old times."

    scene board

    "Now, it's time for some nostalgic fun."    

    jump start_game

label start_game:
    "Do you want to play the game?"
    menu:
        "Yes":
            $ play_game = True
        "No":
            $ play_game = False

    if play_game:
        "You chose to play the game."
    else:
        "You chose not to play the game."

    python:
        if play_game:
            import subprocess
            subprocess.run(["C:/Users/Lenovo/anaconda3/python.exe", "C:/Users/Lenovo/Documents/SEM 5/Advanced Python/chutiya/indian_ludo/game.py"])
        else:
            pass
