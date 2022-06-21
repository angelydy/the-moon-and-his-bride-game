init python:
    inv_page = 0
    class item:
        def __init__(self, name, cost = 0, image="", owned = False):
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

        def itemCheck(self, reqitem):
            for item in inventory.items:
                if item.name == reqitem.name:
                    reqitem.owned = False
                    self.items.remove(reqitem)
                    return True



    #Electronic
    cam = item("Camera", 200, image="/Items/camera.png")
    rec = item("Recorder", 100, image="/Items/recorder.png")
    lap = item("Laptop", 0, image="/Items/laptop.png")#400
    usb = item("USB", 100, image="/Items/usb.png")#100
    knuckle=item("Brass Knuckle", 400, image = "/Items/brass_knuckles.png")#400


    #Food
    meat = item("Meat", 100, image="/Items/meat.png")#50
    coke = item("Soft Drinks", 50, image="/Items/coke.png")
    cabbage = item("Cabbage", 50, image="/Items/cabbage.png")
    ketchup = item("Ketchup", 100, image="/Items/ketchup.png")#100

    #Extras
    vidfile = item("Evidence", 0, image="/Items/vidfile.png")

    #Using
    inventory = Inventory()
