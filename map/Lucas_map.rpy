label lobby:
    #scene Kitchen
    menu:
        "Living Room":
            jump living_room
        "Dining Room":
            jump dining_room
        "Recreation Room":
            jump recreation_room
        "Second Floor":
            jump second_floor

label dining_room:
    #scene Dining Room
    menu:
        "Kitchen":
            jump kitchen
        "Rest room":
            jump restroom1
        "Pool":
            jump pool
        "Lobby":
            jump lobby

label kitchen:
    #scene kitchen
    menu:
        "Go back":
            jump dining_room

label restroom1:
    #scene restroom1
    menu:
        "Go back":
            jump dining_room

label pool:
    #scene pool
    menu:
        "Go back":
            jump dining_room

label living_room:
    #scene living room
    menu:
        "Bar":
            jump Bar
        "Basement":
            jump basement
        "Theater":
            jump theater
        "Lobby":
            jump lobby

label Bar:
    #scene Bar
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
    #scene Recreation Room
    menu:
        "Garden":
            jump garden
        "Restroom":
            "Someone's using the rest room"
            jump recreation_room
            #jump restroom2
        "Art Room":
            jump art_room
        "Lobby":
            jump lobby

label garden:
    #scene Garden
    menu:
        "Go back":
            jump recreation_room

label restroom2:
    #scene Restroom2
    menu:
        "Go back":
            jump recreation_room

label art_room:
    #scene Art room
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
            jump hallway_mid
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
            jump hallway_mid
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
        "Hallway Left":
            jump hallway_left
        "Hallway Right":
            jump hallway_right

label balcony:
    menu:
        "Go back":
            jump hallway_right
