label intro:
    $ chapter = 0
    $ selection = 0
    call day_0
    jump day_1

label tbc:
    hide screen phone
    scene black with dissolve
    image cont = "tbc.png"
    show cont:
        subpixel True pos (666, 200) zoom 1.21
    "{color=#FFF}To be Continued{/color}"
    return

label uc:
    hide screen phone
    scene black with dissolve
    image nf = "Under construction.png"
    show nf:
        subpixel True pos (0.37, 0.20)
    "{color=#FFF}Under Construction{/color}"
    return
