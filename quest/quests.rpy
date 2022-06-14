init python:
    import renpy.store as store
    import renpy.exports as renpy

    #Quest Class
    class Quest(store.object):
        def __init__(self, name, description, available = False, completed = False, goal = 1):
            self.name = name
            self.description = description
            self.available = available
            self.completed = completed
            self.goal = goal
            self._progressCount = 0

        @property
        def progressCount(self):
            return self._progressCount

        @progressCount.setter
        def progressCount(self, a):
            self._progressCount = a
            if self._progressCount >= self.goal:
                self.completed = True

        def incprogress(self):
            self.progressCount = self._progressCount + 1

        def shouldShow(self):
            if self.available and not(self.completed):
                return True
            return False

#Declaring the Quest
default go_to_school = Quest("Go to School in the morning", "I should head to school and see what's up",True)
default go_to_class = Quest("Head to the class", "Maybe they head out first...")
default talk_to_jake = Quest("Ask Jake", "I should ask Jake in the canteen maybe he knows what happened in the party")
default go_to_afterclass = Quest("Attend the afternoon Class", "I should go back to class")
default talk_to_laura = Quest("I should find Laura", "Where's Laura? maybe she's in the Library")
default go_to_work = Quest("Go to work", "I need to go to work in the evening", True)
default evening_home = Quest("Go Home", "I'm tired, I should head back home")
default midnight_home = Quest("Sleep", "Go to sleep")
