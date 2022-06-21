label lucas_mansion_time:
    show screen phone
    if chapter != 1:
        hide screen phone
        "{cps=25}I have no business there..."
        jump location
    elif energy <= 15 and energy > 10:
        scene mansion_entrance morning with dissolve
        jump lucas_mansion
    elif energy <= 10 and energy > 5:
        scene mansion_entrance afternoon with dissolve
        jump lucas_mansion
    elif energy <= 5 and energy != 0:
        scene mansion_entrance evening with dissolve
        jump lucas_mansion
    elif energy <= 0:
        jump home

label lucas_mansion:
    hide screen phone
    if chapter == 1:
        $ location == "lucas"
        th"{cps=25} The place looks heavily guarded…"
        th"{cps=25} There are police and security guards everywhere, I wonder if they will let me pass"
        show screen phone
        menu:
            "Walk to the front":
                call security
                if cctv_ch1.shouldShow():
                    $ cctv_ch1.completed = True
                    $ e_cctv_ch1.available = True
                jump lucas_mansion_time

            "Sneak around":
                call sneak_around
                if cctv_ch1.shouldShow():
                    $ cctv_ch1.completed = True
                    $ e_cctv_ch1.available = True
                jump lucas_mansion_time


        label security:
            hide screen phone
            "Security" "{cps=25} Sir you are not permitted to go through"
            menu:
                "I’ll head back":
                    return
                "I’m Lucas’s friend":
                    call friend
                    return

        label friend:
            hide screen phone
            "Security" "{cps=25} We can’t let you in unless Mr. Lucas said so and Mr. Lucas hasn’t gone home yet"
            mc"{cps=25} Hmm..."
            th"{cps=25} I need Lucas’s permission but where could he be?"
            return

        label sneak_around:
            hide screen phone
            scene black with dissolve
            "(You sneaked around)"
            "Police" "{cps=25}What are you doing?"
            mc"{cps=25} Shit!"
            "Police" "{cps=25} This is a private area and site of investigation do not go any further"
            mc"{cps=25} I’m sorry officer"
            th"{cps=25} I need a distraction to get inside and someone to accompany me once I’m inside"
            return

    else:
        jump lobby

label lobby:
    scene lobby
    with dissolve
    menu:
        "Living Room":
            jump living_room
        "Dining Room":
            jump dining_room
        "Recreation Room":
            jump recreation_room
        "Second Floor":
            "Out of limit"
            jump lobby
            #jump second_floor
        "Head out":
            if chapter == 0:
                scene black with dissolve
                "(You left the Party)"
                jump work_0

label dining_room:
    scene dining room
    with dissolve
    menu:
        "Kitchen":
            jump kitchen
        #"Rest room":
            #"(Someone's using the restroom)"
            #jump dining_room
            #jump restroom1
        "Pool":
            jump pool
        "Lobby":
            jump lobby

label kitchen:
    scene kitchen
    with dissolve
    menu:
        "Go back":
            jump dining_room

label restroom1:
    #scene restroom1
    menu:
        "Go back":
            jump dining_room

label pool:
    scene pool
    with dissolve
    menu:
        "Go back":
            jump dining_room

label living_room:
    scene living room
    with dissolve
    if day == 0:
        show jake tired at left with dissolve
        "(You see Jake drinking in the living room)"
    menu:
        "Talk to Jake" if jaketalk_0:
            jump jaketalk_0
        "Bar":
            jump Bar
        "Basement":
            "I shouldn't go there"
            jump living_room
            #jump basement
        "Theater":
            "Theater's locked"
            jump living_room
            #jump theater
        "Lobby":
            jump lobby

label Bar:
    scene tbar
    with dissolve
    menu:
        "Go back":
            jump living_room

label basement:
    #scene Basement
    menu:
        "Go back":
            jump living_room

label theater:
    #scene Theater
    menu:
        "Go back":
            jump living_room

label recreation_room:
    scene recreation
    with dissolve
    menu:
        "Garden":
            jump garden
        #"Restroom":
            #"Someone's using the rest room"
            #jump recreation_room
            #jump restroom2
        "Art Room":
            jump art_room
        "Lobby":
            jump lobby

label garden:
    scene garden
    with dissolve
    menu:
        "Go back":
            jump recreation_room

label restroom2:
    #scene Restroom2
    menu:
        "Go back":
            jump recreation_room

label art_room:
    scene art room
    with dissolve
    menu:
        "Go back":
            jump recreation_room

label second_floor:
    menu:
        "Hallway Left":
            jump hallway_left
        "Halllway Right":
            jump hallway_right
        "Lobby":
            jump lobby

label hallway_left:
    menu:
        "Guest Room":
            "Lucas said no going to the rooms"
            jump hallway_left
        "Norris Office":
            "Lucas said no going to the rooms"
            jump hallway_left
        "Hallway Right":
            call hallway_mid
        "Second Floor":
            jump second_floor

label hallway_right:
    #scene hallway
    menu:
        "Balcony":
            jump balcony
        "Guest Room":
            "Lucas said there's no going to the rooms"
            jump hallway_left
        "Hallway Left":
            call hallway_mid
        "Second Floor":
            jump second_floor

label hallway_mid:
    #scene hallway
    menu:
        "Lucas Room":
            "Lucas said there's no going to the rooms"
            jump hallway_mid
        "Masters Bed Room":
            "Lucas said there's no going to the rooms"
            jump hallway_mid
        "Library":
            "Door won't budge"
            jump hallway_mid
        "Go back":
            return

label balcony:
    menu:
        "Go back":
            jump hallway_right
