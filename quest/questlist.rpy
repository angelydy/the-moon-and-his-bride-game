init python:
    import renpy.store as store
    import renpy.exports as renpy

    class QuestList (store.object):
        def __init__(self):
            self.quest_list = []

        def addQuest(self, quest):
            self.quest_list.append(quest)

default my_quests = QuestList()

#Adding the Quest to list
label load_quest:
    $ my_quests.addQuest(go_to_school)
    $ my_quests.addQuest(go_to_class)
    $ my_quests.addQuest(talk_to_jake)
    $ my_quests.addQuest(go_to_afterclass)
    $ my_quests.addQuest(talk_to_laura)
    $ my_quests.addQuest(go_to_work)
    $ my_quests.addQuest(evening_home)
    return
