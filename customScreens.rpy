screen phoneUI():
        tag phoneUI
        add "bg phone.png"

        imagebutton:
                idle "home.png"
                hover "home_click.png"
                xalign 0.84 
                yalign 0.935
                action Rollback()

        hbox:
                style_prefix "right_menu"
                
                xalign 0.91
                yalign 0.82
                spacing 40
                
                imagebutton:
                        idle "map.png"
                        hover "map_hover.png"
                        action ShowMenu("mapUI")

                imagebutton:
                        idle "characters.png"
                        hover "characters_hover.png"
                        action NullAction()

                imagebutton:
                        idle "quest.png"
                        hover "quest_hover.png"
                        action NullAction()

                imagebutton:
                        idle "inventory.png"
                        hover "inventory_hover.png"
                        action NullAction()

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
                action NullAction()
                xalign 0.3
                yalign 0.6

        imagebutton:
                idle "locations/home.png"
                hover "locations/home_hover.png"
                action Jump("lobby")
                xalign 0.435
                yalign 0.495

