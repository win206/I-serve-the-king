label battlesys:
    python:
        class damage_sys:
            def __init__(self, power, attacker_multi, victim_multi, stunchance):
                self.dmgdealt = power * attacker_multi / victim_multi
                global emuhp 
                emuhp = round(emuhp - self.dmgdealt)
                self.stunchance = stunchance
        def stuncalc(stunchance):
            import random
            coinflip = random.randint(1, stunchance)
            if coinflip == 1:
                return True
            else:
                return False
        def dmg_statement(attacker, dmgdealt, victim, movename, stunchance):
            
            renpy.say("", "%s did %d damage to %s using %s! They are now at %s hp." %(attacker, dmgdealt, victim, movename, emuhp))
            if stuncalc(stunchance):
                renpy.say("", "%s is stunned and can't move!" %(victim))
                renpy.jump("battleUI")
            else:
                renpy.jump("emuturn")
            
    jump battleUI

label ice_beam:
    python:
        ice_beam = damage_sys(20, cirnodmgmulti, enemydefmulti, 5,)
        dmg_statement("Cirno", ice_beam.dmgdealt, "Emu", "Ice Beam", ice_beam.stunchance)

label ice_cage:
    python:
        ice_cage = damage_sys(10, cirnodmgmulti, enemydefmulti, 2)
        dmg_statement("Cirno", ice_cage.dmgdealt, "Emu", "Ice Beam", ice_cage.stunchance)
        
        
        

    