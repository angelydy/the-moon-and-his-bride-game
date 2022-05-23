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
    scene pool night
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
