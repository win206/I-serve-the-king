define C = Character("Cirno", color='#76d1ff')
define E = Character("Emu", color='#FF66BC')
define cirnomaxhp = 54
define cirnohp = cirnomaxhp
define emumaxhp = 90
define emuhp = emumaxhp
define cirnodmgmulti = 1
define cirnodefmulti = 1
define enemydmgmulti = 1
define enemydefmulti = 1
define dmgdealt = 0
define godikeepmakingvariables = 0
define movename = " "
define stun = False
define volt = False
define bankai = False

label battleUI:
    if cirnohp >= 0:
        call screen battleUI
    else:
        "How the fuck did you lose????????????????????????????????????"
        jump killyourself

label attackUI:
    call screen attackUI
label voltstanding:
    if volt == False:
        show volt as cirno
        C "Quincy Voll Stern Dich: Barthlomew"
        show voltcirno as cirno
        $ cirnodmgmulti = 2
        $ cirnodefmulti = 0.5
        $ volt = True
        "Attack and Defense Increased!"
    else:
        "Alr have volt popped"
    python:
        def test(wow):
            renpy.say(wow, "test")
        test("fish")
    jump emuturn

label emuturn:
    if bankai == False:
        show pinkbankai as emu
        E "Bankai"
        show emubankai as emu
        $ enemydmgmulti = 1.2
        $ enemydefmulti = 1.2
        $ bankai = True
        jump battleUI
    else:
        $ dmgdealt = 20 * enemydmgmulti / cirnodefmulti
        $ cirnohp -= dmgdealt
        "Emu uses North, dealing [dmgdealt] hp!"
        jump battleUI





#label dmgcalc:
    #$ dmgdealt = dmgdealt * cirnodmgmulti / enemydefmulti
    #$ emuhp -= dmgdealt
    #if stun == True:
        #"Cirno used [movename], dealing [dmgdealt] damage and stunned the enemy for 1 turn!"
        #jump lifecheck
    #else:
        #"Cirno used [movename], dealing [dmgdealt] damage!"
        #jump lifecheck
    
label lifecheck:
    if emuhp >= 0:
        if stun == False:
            jump emuturn
        else:
            jump battleUI
    else:
        "EMU FUC KING DI ED"
        "BATTLE WON"
        jump choice
label run:
    "Ran away successfully! You fucking pussy"
    scene bg room
    hide emu
    hide cirno 
    with dissolve
    jump choice
