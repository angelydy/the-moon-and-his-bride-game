screen phoneUI():
    zorder 100

    tag phoneUI
    add "bg phone.png"
    modal True

    imagebutton:
            idle "home.png"
            hover "home_click.png"
            xalign 0.84
            yalign 0.935
            action Hide("phoneUI")

    hbox:
            style_prefix "right_menu"
            xalign 0.885
            yalign 0.82
            spacing 40

            imagebutton:
                    idle "map.png"
                    hover "map_hover.png"
                    action [Hide("phoneUI"),Show("mapUI")]

            imagebutton:
                    idle "characters.png"
                    hover "characters_hover.png"
                    action [Hide("phoneUI"),Show("charactersUI")]

            imagebutton:
                    idle "quest.png"
                    hover "quest_hover.png"
                    action Show("questlog")

screen mapUI():
        tag mapUI
        add "bg map.png"
        modal True
        imagebutton:
                idle "exit.png"
                hover "exit_hover.png"
                action Hide("mapUI")
                xalign 0.97
                ypos 65

        imagebutton:
                idle "locations/school.png"
                hover "locations/school_hover.png"
                action [Hide("mapUI"),SetVariable("subloc", "home"),Jump("school")]
                xalign 0.3
                yalign 0.6

        imagebutton:
                idle "locations/home.png"
                hover "locations/home_hover.png"
                action [Hide("mapUI"),Jump("lucas_mansion")]
                xalign 0.435
                yalign 0.495

        imagebutton:
                idle "locations/mall.png"
                hover "locations/mall_hover.png"
                action [Hide("mapUI"),Jump("mall")]
                xalign 0.135
                yalign 0.265

        imagebutton:
                idle "locations/cafe.png"
                hover "locations/cafe_hover.png"
                action [Hide("mapUI"),Jump("coffee")]
                xalign 0.595
                yalign 0.495

        imagebutton:
                idle "locations/home1.png"
                hover "locations/home1_hover.png"
                action [Hide("mapUI"),Jump("home")]
                xalign 0.895
                yalign 0.395
        
        imagebutton:
                idle "locations/police.png"
                hover "locations/police_hover.png"
                action NullAction()
                xalign 0.715
                yalign 0.798


screen phone():
    modal True
    hbox:
        style_prefix "right_menu"
        xalign 0.97
        ypos 20
        spacing 50

        if inv == True:
            imagebutton:
                    idle "inventory.png"
                    hover "inventory_hover.png"
                    action [Show("inventory"), Hide("quick_menu")]

        if tskip == True:
            imagebutton:
                idle "timeskip.png"
                hover "timeskip_hover.png"
                action Jump("timeskip")

        imagebutton:
            idle "phone.png"
            hover "phone_hover.png"
            action [Show("phoneUI")]

screen charactersUI():
        modal True
        tag charactersUI
        if thomasChar:
                add "characterScreen/bg characters.png"
        else:
                add "characterScreen/bg charNotAvail.png"

        imagebutton:
                idle "exit.png"
                hover "exit_hover.png"
                action Hide("charactersUI")
                xalign 0.97
                ypos 65

        imagebutton:
                idle "characterScreen/justineBtn.png"
                hover "characterScreen/justineBtn hover.png"
                action [Hide("charactersUI"),Show("justineUI")]
                xalign 0.1
                yalign 0.854

        imagebutton:
                idle "characterScreen/jakeBtn.png"
                hover "characterScreen/jakeBtn hover.png"
                action [Hide("charactersUI"),Show("jakeUI")]
                xalign 0.27
                yalign 0.854

        imagebutton:
                idle "characterScreen/lucasBtn.png"
                hover "characterScreen/lucasBtn hover.png"
                action [Hide("charactersUI"),Show("lucasUI")]
                xalign 0.44
                yalign 0.854

        imagebutton:
                idle "characterScreen/jennyBtn.png"
                hover "characterScreen/jennyBtn hover.png"
                action [Hide("charactersUI"),Show("jennyUI")]
                xalign 0.60
                yalign 0.854

        imagebutton:
                idle "characterScreen/lauraBtn.png"
                hover "characterScreen/lauraBtn hover.png"
                action [Hide("charactersUI"),Show("lauraUI")]
                xalign 0.76
                yalign 0.854

        imagebutton:
                idle "characterScreen/thomasBtn.png"
                hover "characterScreen/thomasBtn hover.png"
                if thomasChar:
                        action [Hide("charactersUI"),Show("thomasUI")]
                else:
                        action [Hide("charactersUI"),Show("characterNotAvailable")]
                xalign 0.89
                yalign 0.854

screen characterNotAvailable():
        modal True
        tag characterNotAvailable
        add "characterScreen/charNotAvail.png"

        imagebutton:
                idle "exit.png"
                hover "exit_hover.png"
                action [Hide("characterNotAvailable"), Show("charactersUI")]
                xalign 0.97
                ypos 65

screen justineUI():
        modal True
        add "characterScreen/justineInfo.png"

        imagebutton:
                idle "exit.png"
                hover "exit_hover.png"
                action [Hide("justineUI"),Show("charactersUI")]
                xalign 0.97
                ypos 65

screen jakeUI():
        modal True
        add "characterScreen/jakeInfo.png"

        imagebutton:
                idle "exit.png"
                hover "exit_hover.png"
                action [Hide("jakeUI"),Show("charactersUI")]
                xalign 0.97
                ypos 65

screen lucasUI():
        modal True
        add "characterScreen/lucasInfo.png"

        imagebutton:
                idle "exit.png"
                hover "exit_hover.png"
                action [Hide("lucasUI"),Show("charactersUI")]
                xalign 0.97
                ypos 65

screen lauraUI():
        modal True
        add "characterScreen/lauraInfo.png"

        imagebutton:
                idle "exit.png"
                hover "exit_hover.png"
                action [Hide("lauraUI"),Show("charactersUI")]
                xalign 0.97
                ypos 65

screen thomasUI():
        modal True
        add "characterScreen/thomasInfo.png"

        imagebutton:
                idle "exit.png"
                hover "exit_hover.png"
                action [Hide("thomasUI"),Show("charactersUI")]
                xalign 0.97
                ypos 65

screen jennyUI():
        modal True
        add "characterScreen/jennyInfo.png"
        
        imagebutton:
                idle "exit.png"
                hover "exit_hover.png"
                action [Hide("jennyUI"),Show("charactersUI")]
                xalign 0.97
                ypos 65

