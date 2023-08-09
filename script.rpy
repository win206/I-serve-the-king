# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image byakuya = "byakuya.png"
image ichika = "Ichika.png"
image aizenreveal = Movie(play="aizen.webm")
image bgmap = "map/bg map.png"
define e = Character('???', color='#33AAEE')
define B = Character('Byakuya', color='#ffb7c5')
define L = Character("One Piece", color='#000000')
define happy = 0
define flash = Fade(.1, 0.5, .25, color="#b02121")
define money = 0
define moneydrop = 0
define item = "none"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    show ichika
    e ":3"

    e "Remember, one must imagine Sisyphus happy."
    define push = 1
    "Before you stands a boulder at the foot of a steep, never-ending hill, and a door. [push]"
    hide ichika
    label choice:
        "You stand at the foot of the hill."
        menu:

            "Begin pushing the rock up the hill.":
                jump rock
            "Fight god":
                jump battle
            "Open the door.":
                jump door 
            "Map development test":
                jump map 
            "list test :3":
                jump lists
            "save coot":
                jump scavenge
    label rock:
        play sound "audio/sisyphus.mp3"
        show sisyphus
        with Dissolve(0.5)
        pause 0.5
        hide sisyphus
        with dissolve
        if push == 1:
            "You begin pushing the rock."
        elif push == 2:
            "All Sisyphus' silent joy is contained therein. His fate belongs to him."
        elif push == 3:
            "Happiness and the absurd are two sons of the same earth. They are inseparable."
        elif push == 4:
            "Likewise, the absurd man, when he contemplates his torment, silences all the idols."
        elif push == 5:
            "In the universe suddenly restored to its silence, the myriad wondering little voices of the earth rise up."
        elif push == 6:
            "You are approaching the top of the hill. But will that truly resolve anything?"
        elif push >= 6:
            "You are running out of strength."
            python:
                import random
                happy = random.randint(1,3)
            if happy == 1:
                "The indominable will of the human spirit supports you."
                jump musicshop_pressed
            else:
                "In a cruel twist of fate, the boulder slips out of your grasp, rolling all the way to the foot of the hill."
                "One always finds one's burden again. But Sisyphus teaches the higher fidelity that negates the gods and raises rocks. He too concludes that all is well."
                "This universe henceforth without a master seems to him neither sterile nor futile. Each atom of that stone, each mineral flake of that night filled mountain, in itself forms a world. The struggle itself toward the heights is enough to fill a man's heart."
                "One must imagine Sisyphus happy. You begin the trek back down."
                jump start 
        menu:
            "Keep pushing.":
                $ push += 1
                jump rock
            "Stop pushing.":
                jump end
   
    label map:
        scene bgmap
        call screen MapUI
        
        
    label door:
        "You open the door."
        menu doormenu:
            "Close.":
                jump choice
            "Open.":
                jump door2
    
    label door2:
        "You really open the door."
        scene blender
        show byakuya
        with Fade(0.5, 2.0, 1.0)
        B "What the fuck are you doing here"
        
        B "Get the fuck out of here you fucking quincy"
        hide byakuya
        show sworddrop
        with dissolve
        play sound sworddrop
        pause 2
        "{i}His sword falls out of his grip and through the floor{/i}"
        show bankai2
        with dissolve
        "Rows of blades rise from the ground, forming pillars on both sides of Byakuya."
        voice bankai
        play music bankaitheme volume 0.3
        B "Bankai... Senbonzakura Kageyoshi."
        B "You will die not knowing what happened."
        hide bankai2
        hide sworddrop
        show byakuya
        with flash
        "I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE I'M GONNA KILL EVERYONE"
        jump end

    label lists:
        define droplist = ['Star Amulet', 'Quincy Puffer', 'Skill Box']
        python:
            import random
            item = random.choice(droplist)
        "raid won"
        
        "[item] obtained."
        jump choice

   

    label musicshop_pressed:
        scene blender
        show aizen
        with fade
        "Welcome."
        hide aizen2
        $ renpy.movie_cutscene("aizenreveal.webm")
        show aizen2
        "To my Soul Society."
        jump end

    label scavenge:
        "anti inf loop text [moneydrop]"
        #item stuff goes here
        python:
            import random 
            moneydrop = random.randint(1,5)
        if moneydrop == 1:
            python:
                from random import randint
                moneydrop = random.randint(1,10)
                money += moneydrop 
            "you found [moneydrop] dollars you now have [money] dollars"
        else:
            "you so brokoe you broke ass bitch :sob:"
        
        if money >= 100:
            "You can't scavenge any more"
            jump end
        else:
            "Keep going"
            jump scavenge

    label luffy:
        hide screen MapUI
        scene bg stupid
        show luffy at right
        L "I can feel the drums of liberation inside me! Nothing will get in the way of my fig-{nw}"
        show homelessbitch at left with moveinleft
        pause(0.1)
        play sound "<from 0 to 1>bounce.mp3"
        show luffy2 as luffy:
            xalign 1.0 yalign 0.5
        pause
        jump choice

    label battle:
        hide screen MapUI
        scene bg domain
        "Battle Start"
        "Test"
        show emu:
            xalign 0.71  yalign 0.35
        with moveintop
        "test"
        show cirno:
            xalign 0.228 yalign 0.678
        with moveinbottom
        jump battlesys
        
        

    # This ends the game.
    label end:
        return