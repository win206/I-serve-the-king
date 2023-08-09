## Screen with Stats Button
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump ("call_mapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")
        # This was the same code used in the vlog.

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.
label call_mapUI:
    call screen MapUI

screen MapUI:
    add "map/bg map.png"

    imagebutton:
        xpos 116
        ypos 412
        idle "map/idle.png"
        hover "map/mainstreethover.png"
        action Jump("luffy")
        
    imagebutton:
        xpos 1190
        ypos 531
        idle "map/idle2.png"
        hover "map/musicstorehover.png"
        action Call("musicshop_pressed")

screen battleUI:
    fixed:
        xmaximum 1920
        ymaximum 200 
        ypos absolute(800)
        #left_padding 1400
        #right_padding 225
        #ypadding 1
        xalign 0.5
        add "straightsex.jpg"
        
        
        hbox:
            fixed:
                ymaximum 200
                xmaximum 450
                xpos 400
                
                text "What will Emolga do? \n Cirno:[cirnohp]HP \n Emu:[emuhp]HP"
            frame:
                ypadding 45
                left_margin 1250
                grid 2 2:
                    
                    spacing 10
                    textbutton "Battle" action Jump("attackUI")
                    textbutton "Run" action Jump("run")
                    textbutton "Items"
                    textbutton "Swap"
        #vbox:
            #text "Display"
            #null height 10
            #textbutton "Fullscreen" action Preference("display", "fullscreen")
            #textbutton "Window" action Preference("display", "window")
screen attackUI:
    fixed:
        xmaximum 1920
        ymaximum 200 
        ypos absolute(800)
        #left_padding 1400
        #right_padding 225
        #ypadding 1
        xalign 0.5
        add "straightsex.jpg"
        
        
        hbox:
            fixed:
                ymaximum 200
                xmaximum 450
                xpos 400
                hbox:
                    textbutton "Ice Cage" action Jump("ice_cage")
                    textbutton "Ice Beam" action Jump("ice_beam")
                    textbutton "Voll Stern Dich" action Jump("voltstanding")
            frame:
                ypadding 45
                left_margin 1250
                grid 2 2:
                    
                    spacing 10
                    textbutton "Back" action Call("battleUI")