label ch1_end:
    #if end and end2 is finish
    hide screen phone
    show laura neutral at left with moveinleft
    lg"{cps=25} So how is it?"
    show jake happy at right with moveinright
    jk"{cps=25} I'm excited to see the face of the person I'll bash my fist upon"
    mc"{cps=25} Guys, check this out…"
    "The video shows a different area in Lucas’s House"
    "The cctv is positioned in ceiling monitoring people that goes and out of the room"
    "It caught Jenny trying to go out of the room until a unknown person’s hand covered Jenny’s mouth as she loose conscious"
    show laura surprised
    lg"{cps=25} OMG"
    jk"{cps=25} Jenny!"
    "The cctv also caught another person, a witness to what happened"
    scene black with dissolve

    init python:
        thomasChar = True
    scene cafe with dissolve
    show thomas neutral at left with dissolve
    show jake happy at right with moveinright
    jk"{cps=25} This person…"
    jk"{cps=25} I REMEMBER NOW! I KNOW THIS PERSON!"
    hide thomas neutral

    jk"{cps=25} THIS IS THE JANITOR OF LUCAS"
    show laura neutral at left with dissolve
    lg"{cps=25} The janitor?"
    jk"{cps=25} Mister thomas"
    jk"{cps=25} He was there!"
    jk"{cps=25} He was there, when Justine and Jenny talked about something in the room"
    jk"{cps=25} He is also the witness in what happened in the room in the video!"
    mc"{cps=25} Hmm… it would make sense as the janitor was supposed to be the last person in the party"
    mc"{cps=25} As they clean up all the mess…"
    th"{cps=25} Could this be it?!"
    th"{cps=25} The Janitor is the key to finding out the truth behind the wall"
    th"{cps=25} We must find him before someone does…"
    hide thomas with dissolve
    centered "{color=#FFF}(End of Chapter 1){/color}" with fade
    $ chapter = 2
    $ renpy.block_rollback()
    jump initialize
