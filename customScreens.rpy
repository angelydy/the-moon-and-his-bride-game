screen mapUI():
        tag mapUI
        add "bg map.png"
        modal True

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
                action Jump("lobby")
                xalign 0.435
                yalign 0.495

