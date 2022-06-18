init python:
    import renpy.store as store
    import renpy.exports as renpy

    class QuestList (store.object):
        def __init__(self):
            self.quest_list = []

        def addQuest(self, quest):
            self.quest_list.append(quest)

default mq = QuestList()

#Adding the Quest to list
label load_quest:

    ################### Introduction ###################

    #Day 1
    $ mq.addQuest(go_to_school)
    $ mq.addQuest(go_to_class)
    $ mq.addQuest(talk_to_jake)
    $ mq.addQuest(go_to_afterclass)
    $ mq.addQuest(talk_to_laura)
    $ mq.addQuest(go_to_work)
    $ mq.addQuest(evening_home)

    #Day 2
    $ mq.addQuest(go_to_school2)
    $ mq.addQuest(talk_to_laura2)
    $ mq.addQuest(visit_jake)
    $ mq.addQuest(evening_home2)


    ################### CHAPTER 1 ###################
    $ mq.addQuest(e_hallway_ch1)
    $ mq.addQuest(e_roam_ch1)
    $ mq.addQuest(e_class_ch1)
    $ mq.addQuest(e_hallway2_ch1)
    $ mq.addQuest(cctv_ch1)
    $ mq.addQuest(tweet_ch1)
    $ mq.addQuest(e_cctv_ch1)
    $ mq.addQuest(e_tweet_ch1)
    $ mq.addQuest(cafe_ch1)
    $ mq.addQuest(e_cafe_ch1)
    $ mq.addQuest(raid_ch1)
    $ mq.addQuest(start_raid_ch1)
    $ mq.addQuest(start2_raid_ch1)
    $ mq.addQuest(evidence_ch1)
    $ mq.addQuest(chapter1_end)
    $ mq.addQuest(chapter1_end2)
    return
