screen questlog:
    tag questsUI
    add "bg quests.png"
    modal True

    imagebutton:
        idle "exit.png"
        hover "exit_hover.png"
        action Hide("questsUI")
        xalign 0.97
        ypos 65

    vbox:
        xalign 0.2
        ypos 215
        spacing 62
        xmaximum 650

        for quest in mq.quest_list:
            if not quest.completed and quest.available:
                text "[quest.description] : [quest.name]"
