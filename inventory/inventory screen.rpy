screen inventory:
    add "bg inventory"
    modal True

    imagebutton:
        idle "exit.png"
        hover "exit_hover.png"
        action Hide("inventory")
        xalign 0.97
        ypos 20

    hbox:
        text "[inventory.money]"
        xalign 0.355
        yalign 0.765

    vpgrid:
        cols 4
        rows 4
        xpos 510 ypos 340 spacing 75
        draggable True
        mousewheel True
        ysize 420
        yinitial 0
        scrollbars "vertical"
        side_spacing 140

        for item in inventory.items:
            frame:
                imagebutton:
                    idle item.image
                    hover item.image
                    action NullAction()
        
                


    