screen mapUI():
        tag mapUI
        add "bg map.png"

        imagebutton:
                idle "map.png"
                hover "map_hover.png"
                action ShowMenu("mapUI")
                xalign 0.78
                ypos 30

        imagebutton:
                idle "characters.png"
                hover "characters_hover.png"
                action Rollback()
                xalign 0.82
                ypos 30

        imagebutton:
                idle "quest.png"
                hover "quest_hover.png"
                action Rollback()
                xalign 0.92
                ypos 30

        imagebutton:
                idle "inventory.png"
                hover "inventory_hover.png"
                action Rollback()
                xalign 0.97
                ypos 30

        imagebutton:
                idle "exit.png"
                hover "exit_hover.png"
                action Rollback()
                xalign 0.97
                ypos 30


