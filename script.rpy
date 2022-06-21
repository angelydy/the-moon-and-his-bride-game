label start:
    stop music fadeout 1.0
    $ chapter = 0
    $ selection = 0
    jump initialize
    return

label initialize:
    if chapter == 0:
        jump intro
    elif chapter == 1:
        jump chapter1
    elif chapter == 2:
        call tbc
        pause
    return

label tbc:
    hide screen phone
    scene black with dissolve
    window hide
    image cont = "tbc.png"
    pause (1)
    show cont:
        subpixel True pos (666, 200) zoom 1.21
    "{color=#FFF}To be continued{/color}" with dissolve
    $ MainMenu(confirm=False)()

label uc:
    hide screen phone
    scene black with dissolve
    image nf = "Under construction.png"
    show nf:
        subpixel True pos (0.37, 0.20)
    "{color=#FFF}Under Construction{/color}"
    return
