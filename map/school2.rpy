label school:
    hide screen phone
    $ location = "school"
    if subloc == "entrace":
        jump entrance
    elif subloc == "hallway1f":
        jump hallway1f
    elif subloc == "gym":
        jump gym
    elif subloc == "locker":
        jump locker
    elif subloc == "canteen":
        jump canteen
    elif subloc == "back":
        jump back
    elif subloc == "restroom":
        jump restroom
    elif subloc == "hallway2f":
        jump hallway2f
    elif subloc == "classroom":
        jump classroom
    elif subloc == "library":
        jump library
    elif subloc == "council":
        jump council
    else:
        jump entrance



label entrance:
    $ subloc = "entrance"
    show screen phone
    if energy <= 15 and energy > 10:
        scene school morning with dissolve
        if go_to_school.shouldShow():
            call school_1
            show screen phone
        elif go_to_school2.shouldShow():
            call school_2
            show screen phone
        menu:
            "Talk to Laura" if day == 2:
                hide screen phone
                if talk_to_laura2.shouldShow():
                    call talk_laura
                lg "..."
                jump entrance
            "Hallway":
                jump hallway1f

    elif energy <= 10 and energy > 5:
        scene school afternoon with dissolve
        menu:
            "Go Home":
                jump home
            "Hallway":
                jump hallway1f


    elif energy <= 5 and energy != 0:
        scene school evening with dissolve
        menu:
            "Go Home":
                jump home
            "Hallway":
                jump hallway1f

    elif energy <= 0:
        jump home



label hallway1f:
    $ subloc = "hallway1f"
    show screen phone
    if energy <= 15 and energy > 10:
        scene hallway morning with dissolve
        menu:
            "Gym":
                jump gym
            "Canteen":
                jump canteen
            "Restroom":
                jump restroom
            "2F Hallway":
                jump hallway2f
            "Go outside":
                jump entrance

    elif energy <= 10 and energy > 5:
        scene hallway afternoon with dissolve
        menu:
            "Gym":
                jump gym
            "Canteen":
                jump canteen
            "Restroom":
                jump restroom
            "2F Hallway":
                jump hallway2f
            "Go outside":
                jump entrance

    elif energy <= 5 and energy != 0:
        scene hallway evening with dissolve
        menu:
            "Gym":
                jump gym
            "Canteen":
                jump canteen
            "Restroom":
                jump restroom
            "2F Hallway":
                jump hallway2f
            "Go back":
                jump entrance

    elif energy <= 0:
        jump home



label restroom:
    $ subloc = "restroom"
    show screen phone
    if energy <= 15 and energy > 10:
        scene restroom with dissolve
        menu:
            "Go back":
                jump hallway1f
    elif energy <= 10 and energy > 5:
        scene restroom with dissolve
        menu:
            "Go back":
                jump hallway1f
    elif energy <= 5 and energy != 0:
        scene restroom with dissolve
        menu:
            "Go back":
                jump hallway1f
    elif energy <= 0:
        jump home




label gym:
    $ subloc = "gym"
    show screen phone
    if energy <= 15 and energy > 10:
        scene gym morning with dissolve
        menu:
            "Talk to Jake":
                hide screen phone
                jk"{cps=25} ..."
                if start2_raid_ch1.shouldShow:
                    call jaketalk_ch1
                jump location
            "Locker Room":
                jump locker
            "Go back":
                jump hallway1f

    elif energy <= 10 and energy > 5:
        scene gym afternoon with dissolve
        menu:
            "Locker Room":
                jump locker
            "Go back":
                jump hallway1f

    elif energy <= 5 and energy != 0:
        scene gym evening with dissolve
        menu:
            "Locker Room":
                jump locker
            "Go back":
                jump hallway1f

    elif energy <= 0:
        jump home



label locker:
    $ subloc = "locker"
    show screen phone
    if energy <= 15 and energy > 10:
        scene locker morning with dissolve
        menu:
            "Go back":
                jump gym
    elif energy <= 10 and energy > 5:
        scene locker afternoon with dissolve
        menu:
            "Go back":
                jump gym
    elif energy <= 5 and energy != 0:
        scene locker evening with dissolve
        menu:
            "Go back":
                jump gym
    elif energy <= 0:
        jump home



label canteen:
    $ subloc = "canteen"
    show screen phone
    if energy <= 15 and energy > 10:
        scene canteen morning with dissolve
        menu:
            "Talk to Laura" if raid_ch1.shouldShow():
                call canteen2_ch1
                jump location
            "Back Room":
                jump back
            "Go back":
                jump hallway1f

    elif energy <= 10 and energy > 5:
        scene canteen afternoon with dissolve
        menu:
            "Talk to Jake" if talk_to_jake.shouldShow():
                jump canteen_1
            "Talk to Lucas" if e_roam_ch1.shouldShow():
                call canteen_ch1
                jump location
            "Back Room":
                jump back
            "Go back":
                jump hallway1f

    elif energy <= 5 and energy != 0:
        scene canteen evening with dissolve
        menu:
            "Back Room":
                jump back
            "Go back":
                jump hallway1f

    elif energy <= 0:
        jump home



label back:
    $ subloc = "back"
    show screen phone
    if energy <= 15 and energy > 10:
        scene back morning with dissolve
        menu:
            "Go back":
                jump canteen
    elif energy <= 10 and energy > 5:
        scene back afternoon with dissolve
        menu:
            "Go back":
                jump canteen
    elif energy <= 5 and energy != 0:
        scene back evening with dissolve
        menu:
            "Go back":
                jump canteen
    elif energy <= 0:
        jump home



label hallway2f:
    $ subloc = "hallway2f"
    show screen phone
    if energy <= 15 and energy > 10:
        scene hallway morning with dissolve
        menu:
            "Talk to Laura" if e_hallway_ch1.shouldShow():
                if e_hallway_ch1.shouldShow():
                    call school_ch1
                    jump location
                elif e_hallway2_ch1.shouldShow():
                    call hallway_ch1
                    jump location
                jump location
            "Classroom":
                jump classroom
            "Library":
                jump library
            "Council Office":
                jump council
            "Go back to 1F Hallway":
                jump hallway1f
    elif energy <= 10 and energy > 5:
        scene hallway afternoon with dissolve
        if e_tweet_ch1.shouldShow():
            call f2hallway_ch1
            jump location
        menu:
            "Talk to Laura" if e_hallway2_ch1.shouldShow():
                call hallway_ch1
                jump location
            "Classroom":
                jump classroom
            "Library":
                jump library
            "Council Office":
                jump council
            "Go back to 1F Hallway":
                jump hallway1f
    elif energy <= 5 and energy != 0:
        scene hallway evening with dissolve
        menu:
            "Classroom":
                jump classroom
            "Library":
                jump library
            "Council Office":
                jump council
            "Go back to 1F Hallway":
                jump hallway1f
    elif energy <= 0:
        jump home



label classroom:
    $ subloc = "classroom"
    show screen phone
    if energy <= 15 and energy > 10:
        scene classroom morning with dissolve
        if go_to_class.shouldShow():
            jump classroom_1
        menu:
            "Go to Class":
                if e_class_ch1.shouldShow():
                    call classroom_ch1
                    jump location
                $ energy -= 5
                jump classroom
            "Go back":
                jump hallway2f
    elif energy <= 10 and energy > 5:
        scene classroom afternoon with dissolve
        if go_to_afterclass.shouldShow():
            menu:
                "Go to Class" if go_to_afterclass.shouldShow() or e_class_ch1.shouldShow():
                    hide screen phone
                    scene black with dissolve
                    "(You spend your time studying)"
                    if go_to_afterclass.shouldShow():
                        $ go_to_afterclass.completed = True
                        $ talk_to_laura.available = True
                    elif e_class_ch1.shouldShow():
                        call classroom_ch1
                    $ energy -= 3
                    jump location
        menu:
            "Go to Class" if day != 1:
                hide screen phone
                scene black with dissolve
                "(You spend your time studying)"
                $ energy -= 5
                jump day_cycle
            "Go back":
                jump hallway2f
    elif energy <= 5 and energy != 0:
        scene classroom evening with dissolve
        menu:
            "Go back":
                jump hallway2f
    elif energy <= 0:
        jump home




label library:
    $ subloc = "library"
    show screen phone
    if energy <= 15 and energy > 10:
        scene library morning with dissolve
        menu:
            "Go back":
                jump hallway2f
    elif energy <= 10 and energy > 5:
        scene library afternoon with dissolve
        menu:
            "Talk to Laura":
                hide screen phone
                lg "..."
                if talk_to_laura.shouldShow():
                    jump library_1
                elif tweet_ch1.shouldShow():
                    call library_ch1
                elif start2_raid_ch1.shouldShow():
                    call lauratalk_ch1
                jump location
            "Go back":
                jump hallway2f
    elif energy <= 5 and energy != 0:
        scene library evening with dissolve
        menu:
            "Go back":
                jump hallway2f
    elif energy <= 0:
        jump home



label council:
    $ subloc = "council"
    show screen phone
    if energy <= 15 and energy > 10:
        scene council morning with dissolve
        menu:
            "Go back":
                jump hallway2f
    elif energy <= 10 and energy > 5:
        scene council afternoon with dissolve
        menu:
            "Go back":
                jump hallway2f
    elif energy <= 5 and energy != 0:
        scene council evening with dissolve
        menu:
            "Go back":
                jump hallway2f
    elif energy <= 0:
        jump home
