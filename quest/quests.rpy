init python:
    import renpy.store as store
    import renpy.exports as renpy

    #Quest Class
    class Quest(store.object):
        def __init__(self, name, description, available = False, completed = False, triggered = False, goal = 1):
            self.name = name
            self.description = description
            self.available = available
            self.completed = completed
            self.goal = goal
            self._progressCount = 0
            self.triggered = triggered

        @property
        def progressCount(self):
            return self._progressCount

        @progressCount.setter
        def progressCount(self, a):
            self._progressCount = a
            if self._progressCount >= self.goal:
                self.completed = True

        def incProgress(self):
            self.progressCount = self._progressCount + 1

        def shouldShow(self):
            if self.available and not(self.completed):
                return True
            return False

        def shouldTrigger(self):
            if self.completed and not(self.triggered):
                return True
            return False


#Declaring the Quest

################### Introduction ###################
#Day 1
default go_to_school = Quest("Go to School in the morning", "I should head to school and see what's up",True)
default go_to_class = Quest("Head to the class", "Maybe they head out first...")
default talk_to_jake = Quest("Ask Jake", "I should ask Jake in the canteen maybe he knows what happened in the party")
default go_to_afterclass = Quest("Attend the afternoon Class", "I should go back to class")
default talk_to_laura = Quest("I should find Laura", "Where's Laura? maybe she's in the Library")
default go_to_work = Quest("Go to work", "I need to go to work in the evening", True)
default evening_home = Quest("Go Home", "I'm tired, I should head back home")
default midnight_home = Quest("Sleep", "Go to sleep")

#Day 2
default go_to_school2 = Quest("Head to school", "I need to go to school maybe Jenny is back")
default talk_to_laura2 = Quest("Talk to Laura in School front", "What happened?! maybe Laura knows")
default visit_jake = Quest("Visit Jake at the Police Station", "I need to ask Jake about what really happened")
default evening_home2 = Quest("Go Home", "I need to think")


################### CHAPTER 1 ######################
default e_hallway_ch1 = Quest("Find Laura", "I need to tell Laura about what I found she must be in the hallway")
default e_roam_ch1 = Quest("Roam around the School", "Maybe I can find something or someone that can help")
default e_class_ch1 = Quest("Check on Laura", "Let's go to class Laura's waiting")
default e_hallway2_ch1 = Quest("Talk to Laura", "Laura's waiting for me outside the classroom")
default cctv_ch1 = Quest("Go to Lucas House", "Let's go to Lucas House to see what we can find")
default tweet_ch1 = Quest("Talk to Laura", "We need to talk to Laura in the Library")
default e_cctv_ch1 = Quest("Report back to Laura", "We need to tell Laura about what we found in Lucas's House")
default e_tweet_ch1 = Quest("Go to Hallway", "Exit Library")
default cafe_ch1 = Quest("Head Home", "You're tired, you should go home")
default e_cafe_ch1 = Quest("Meet Laura", "Laura wants to show me something in the Cafe")
default evidence_ch1 = Quest("Give the Evidence", "We need to give the evidence to the authorities")
default raid_ch1 = Quest("Place holder", "Place holder", goal = 2)
default raid2_ch1 = Quest("Talk to Laura", "Meet Laura in the canteen in the morning")
default start_raid_ch1 = Quest("Prepare", "Buy the required preparations: Ketchup, Brass Knuckle, USB", goal = 3)
default start2_raid_ch1 = Quest("Talk to the Gang", "Talk to Laura and Jake", goal = 2)
default chapter1_end = Quest("What's inside the video?", "I need to have a laptop so I can access the video")
default chapter1_end2 = Quest("What's inside the video?", "I need to show the video at the cafe during the afternoon")
