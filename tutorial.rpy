label tutorial:
    image time_desc = "time desc.png"
    image phone_desc = "phone desc.png"
    image menu_desc = "buttons desc.png"
    image inventory_desc = "inventory desc.png"
    window hide
    if selection == 0:
        jump menudesc

    if selection == 1:
        jump phone

    elif selection == 2:
        if inv:
            jump invdesc
        return

    elif selection == 3:
        if tskip:
            jump timedesc
        return
    else:
        return

label menudesc:
    $ selection = 1
    show menu_desc with dissolve
    pause
    hide menu_desc with dissolve
    return

label phone:
    $ selection = 2
    show phone_desc with dissolve
    pause
    hide phone_desc with dissolve
    return

label invdesc:
    $ selection = 3
    show inventory_desc with dissolve
    pause
    hide inventory_desc with dissolve
    return

label timedesc:
    $ selection = 4
    show time_desc with dissolve
    pause
    hide time_desc with dissolve
    return
