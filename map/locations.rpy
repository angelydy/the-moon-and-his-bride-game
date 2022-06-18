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
    elif location == "pstation":
        jump pstation
    elif location == "lucas":
        jump lucas_mansion
    else:
        return

label home:
    hide screen phone
    $ location = "home"
    if energy <= 15 and energy > 10:
        scene home morning with dissolve
        if day == 1:
            call morning_1
        elif day == 2:
            call morning_2
        elif chapter == 1:
            call start_ch1
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
        elif evening_home2.shouldShow():
            jump evening_2
        elif e_class_ch1.shouldTrigger == True:
            call home_ch1
            show screen phone
        elif cafe_ch1.shouldShow():
            call homeevening_ch1
            jump location
        elif evidence_ch1.shouldTrigger():
            call homeevening2_ch1
            jump location
        menu:
            "Go to sleep":
                $ day += 1
                $ energy = 15
                jump day_cycle

    elif energy <= 0:
        scene home evening with dissolve
        menu:
            "Go to sleep":
                if midnight_home.shouldShow():
                    call midnight_1
                $ day += 1
                $ energy = 15
                jump day_cycle

label coffee:
    hide screen phone
    if energy <= 10:
        $ location = "coffee"
        scene coffee with dissolve
        show screen phone
        hide screen phone
        menu:
            "Work" if energy <= 5 and energy != 0:
                "(You worked as a barista)"
                if go_to_work.shouldShow():
                    $ go_to_work.completed = True
                $ inventory.earn(15)
                $ energy -= 3
                $ renpy.block_rollback()
                centered "{color=#85bb65}Money = +15${/color}"
            "Hangout with Laura" if e_cafe_ch1.shouldShow():
                call cafe_ch1
                jump location
        jump home
    elif energy <= 0:
        jump home

    else:
        "Coffee shop only opens at evening"
        jump location

label pstation:
    hide screen phone
    if energy <= 10 and energy > 5:
        $ location = "pstation"
        show screen phone
        scene police lobby with dissolve
        menu:
            "Ask to talk to Jake" if visit_jake.shouldShow:
                hide screen phone
                "Police" "{cps=25} You have few minutes to talk to the detainee"
                if visit_jake.shouldShow():
                    call police_2
            "Show Evidence" if evidence_ch1.shouldShow():
                hide screen phone
                "Police" "{cps=25} Hmm?"
                "(You surrendered the evidence to the Police)"
                "Police" "{cps=25} This evidence will be checked thoroughly"
                $ evidence_ch1.completed = True
                jump location
    else:
        "I can only go there during afternoon"
        jump location
