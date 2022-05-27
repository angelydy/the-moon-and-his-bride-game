label school:
    jump entrance

label entrance:
    $ location = "entrance"
    if energy <= 15:
        #scene entrance morning with dissolve
        menu:
            "Talk to Laura" if not day == 1:
                "Good morning"
                lg "Good morning"
                "..."
                jump entrance_morning
            "Hallway":
                call hallway_morning
                jump entrance_morning

    elif energy <= 10:
            #scene entrance afternoon with dissolve
            menu:
                "Go Home":
                    jump home
                "Hallway":
                    call hallway_afternoon
                    jump entrance_afternoon

    elif energy <= 5:
        #scene entrance afternoon with dissolve
        menu:
            "Go Home":
                jump home
            "Hallway":
                call hallway_afternoon
                jump entrance_afternoon

    elif energy == 0:
        jump home

label hallway1f
    $ location == "hallway1f"
    if energy <= 15:
        menu:
            "Gym":
                call gym_morning
                jump hallway1f
            "Canteen":
                call canteen_morning
                jump hallway1f
            "Restroom":
                call restroom_morning
                jump hallway1f
            "2F Hallway":
                call hallway2f_morning
                jump hallway1f
            "Go back":
                return

    elif energy <= 10:
        #scene hallway afternoon with dissolve
        menu:
            "Gym":
                call gym_afternoon
                jump hallway1f
            "Canteen":
                call canteen_afternoon
                jump hallway1f
            "Restroom":
                call restroom_afternoon
                jump hallway1f
            "2F Hallway":
                call hallway2f_afternoon
                jump hallway1f
            "Go back":
                return

        elif energy <= 5:
            #scene hallway evening with dissolve
            menu:
                "Gym":
                    call gym_evening
                    jump hallway1f
                "Canteen":
                    call canteen_evening
                    jump hallway1f
                "Restroom":
                    call restroom_evening
                    jump hallway1f
                "2F Hallway":
                    call hallway2f_evening
                    jump hallway1f
                "Go back":
                    return

        elif energy == 0:
            jump home

label gym:
    $ location = "gym"
    if energy <= 15:
        #scene gym morning with dissolve
        menu:
            "Locker Room":
                call locker_morning
                jump gym
            "Go back":
                return

    elif energy <= 10:
        #scene gym afternoon with dissolve
        menu:
            "Locker Room":
                call locker_afternoon
                jump gym
            "Go back":
                return

    elif energy <= 5:
        #scene gym evening with dissolve
        menu:
            "Locker Room":
                call locker_evening
                jump gym
            "Go back":
                return

    elif energy == 0:
        jump home

label locker:
    $ location = home
