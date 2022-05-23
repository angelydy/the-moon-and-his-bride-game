screen mapUI():
        tag mapUI
        add "bg map.png"
        modal True

        imagebutton:
                idle "map.png"
                hover "map_hover.png"
                action ShowMenu("mapUI")
                xalign 0.78
                ypos 65

        imagebutton:
                idle "characters.png"
                hover "characters_hover.png"
                action NullAction()
                xalign 0.83
                ypos 65

        imagebutton:
                idle "quest.png"
                hover "quest_hover.png"
                action NullAction()
                xalign 0.88
                ypos 65

        imagebutton:
                idle "inventory.png"
                hover "inventory_hover.png"
                action NullAction()
                xalign 0.925
                ypos 65

        imagebutton:
                idle "exit.png"
                hover "exit_hover.png"
                action Rollback()
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
                action NullAction()
                xalign 0.435
                yalign 0.495

