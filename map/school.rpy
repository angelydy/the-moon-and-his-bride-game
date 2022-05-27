label school:
    $ location = "school"
    if energy <= 15:
        jump school_morning
    elif energy <= 10:
        jump school_afternoon
    elif energy <= 5:
        jump school_evening
    elif energy <= 0:
        jump home

label school_morning:
    jump entrance_morning

label locker_morning:


label canteen_morning:
    #scene canteen morning with dissolve
    menu:
        "Back Room":
            call back_morning
            jump canteen_morning
        "Go back":
            return

label back_morning:
    #scene back morning with dissolve
    menu:
        "Go back":
            return

label restroom_morning:
    #scene back morning with dissolve
    menu:
        "Go back":
            return

label hallway2f_morning:
    #scene hallway2f morning with dissolve
    menu:
        "Classroom":
            call classroom_morning
            jump hallway2f_morning
        "Library":
            call library_morning
            jump hallway2f_morning
        "Council Office":
            call council_morning
            jump hallway2f_morning
        "Go back":
            return

label classroom_morning:
    #scene classroom morning with dissolve
    menu:
        "Go to class" if energy == 15:
            $ energy -= 5
            #stats increase
            jump classroom_afternoon





label school_afternoon:
    jump entrance_afternoon

label locker_afternoon:
    #scene locker morning with dissolve
    menu:
        "Go back":
            return

label canteen_afternoon:
    #scene canteen afternoon with dissolve
    menu:
        "Back Room":
            call back_afternoon
            jump canteen_afternoon
        "Go back":
            return

label back_afternoon:
    #scene back afternoon with dissolve
    menu:
        "Go back":
            return

label restroom_afternoon:
    #scene back morning with dissolve
    menu:
        "Go back":
            return

label hallway2f_afternoon:
    #scene hallway2f afternoon with dissolve
    menu:
        "Classroom":
            call classroom_afternoon
        "Library":
            call library_afternoon
        "Council Office":
            call council_afternoon
        "Go back":
            return





label school_evening:
    jump entrance_evening

label locker_evening:
    #scene locker morning with dissolve
    menu:
        "Go back":
            return


label canteen_evening:
    #scene canteen evening with dissolve
    menu:
        "Back Room":
            call back_evening
        "Go back":
            return

label back_evening:
    #scene back evening with dissolve
    menu:
        "Go back":
            return

label restroom_evening:
    #scene back morning with dissolve
    menu:
        "Go back":
            return

label hallway2f_evening:
    #scene hallway2f evening with dissolve
    menu:
        "Classroom":
            call classroom_evening
        "Library":
            call library_evening
        "Council Office":
            call council_evening
        "Go back":
            return
