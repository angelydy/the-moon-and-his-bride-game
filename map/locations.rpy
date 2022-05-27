label location:
    if location == "home":
        call home
    elif location == "coffee":
        call coffee
    elif location == "school":
        elif subloc == "entrance":
            jump entrance
        elif subloc == "hallway1f":
            jump hallway1f
        elif subloc == "gym":
            jump gym
    elif location == "lucas_mansion":
        call lucas_mansion

label home:
    $ location = "home"
    if energy <= 15:
        #scene home morning with dissolve
        $ renpy.pause(hard = True)
    elif energy <= 10:
        #scene home afternoon with dissolve
        $ renpy.pause(hard = True)
    elif energy <= 5:
        #scene home evening with dissolve
        $ renpy.pause(hard = True)
    elif energy <= 0:
        hide screen phone
        #scene home evening with dissolve
        menu:
            "Go to sleep":
                $ day += 1
                $ energy = 15
                jump day_cycle
            "Reflect" if ponder:
                call ponder
                jump day_cycle

    label ponder:
        "{cps=25}Nothings on my mind right now..."
        "{cps=25}I should probably sleep it's late"
        return

label coffee:
    $ location = "coffee"
    #scene coffee with dissolve
    if energy <= 5 and energy != 0:
        "(You worked as a barista)"
        if acquired == False:
            $ money += 15
            $ acquired == True
        centered "{color=#85bb65}Money = +15${/color}"
    else:
        "Coffee shop only opens at evening..."
        return
