label location:
    show screen phone
    if location == "home":
        jump home
    elif location == "coffee":
        jump coffee
    elif location == "school":
        jump school
    elif location == "mall":
        jump mall
    else:
        return

label home:
    hide screen phone
    $ location = "home"
    if energy <= 15 and energy > 10:
        scene home morning with dissolve
        if day == 1:
            call morning_1
        window hide
        show screen phone
        $ renpy.pause(hard = True)
    elif energy <= 10 and energy > 5:
        scene home afternoon with dissolve
        show screen phone
        $ renpy.pause(hard = True)
    elif energy <= 5 and energy != 0:
        scene home evening with dissolve
        show screen phone
        if evening_home.shouldShow():
            jump evening_1
        menu:
            "Go to sleep":
                $ day += 1
                $ energy = 15
                $ acquired = False
                jump day_cycle

    elif energy <= 0:
        scene home evening with dissolve
        menu:
            "Go to sleep":
                if midnight_home.shouldShow():
                    call midnight_1
                $ day += 1
                $ energy = 15
                $ acquired = False
                jump day_cycle

label coffee:
    hide screen phone
    if energy <= 5:
        $ location = "coffee"
        scene coffee with dissolve
        show screen phone
        hide screen phone
        menu:
            "Work" if energy <= 5 and energy != 0:
                "(You worked as a barista)"
                if go_to_work.shouldShow():
                    $ go_to_work.completed = True
                    $ evening_home.available = True
                $ inventory.earn(15)
                $ acquired == True
                $ energy -= 3
                $ renpy.block_rollback()
                centered "{color=#85bb65}Money = +15${/color}"
        jump home
    elif energy <= 0:
        jump home

    else:
        "Coffee shop only opens at evening"
        jump location

return
