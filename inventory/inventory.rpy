init python:
    inv_page = 0
    class item:
        def __init__(self, name, cost = 0, image="", owned = False, physical = True):
            self.name = name
            self.cost = cost
            self.image = image
            self.owned = owned

    class Inventory:
        def __init__(self, money=15):
            self.money = money
            self.items = []

        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                item.owned = True
                self.items.append(item)
                return True
            else:
                return False
            #Buy

        def earn(self, amount):
            self.money += amount
            #Earn money?

    #Electronic
    cam = item("Camera", 15, image="/Items/camera.png")#100
    rec = item("Recorder", 15, image="/Items/recorder.png")#200
    lap = item("Laptop", 15, image="/Items/laptop.png")#500
    usb = item("USB", 15, image="/Items/usb.png")
    vidfile = item("Video",0, image="/Items/vidfile.png",physical = False)

    #Food
    meat = item("Meat", 15, image="/Items/meat.png")#50
    coke = item("Soft Drinks", 15, image="/Items/coke.png")#20
    cabbage = item("Cabbage", 15, image="/Items/cabbage.png")#30

    #Using
    inventory = Inventory()
