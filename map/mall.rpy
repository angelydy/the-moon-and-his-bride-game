label mall:
    hide screen phone
    $ location = "mall"
    scene mall with dissolve
    show screen phone
    menu:
        "Electronic Store":
            jump electronic
        "Grocerry Store":
            jump grocery


label electronic:
    scene mall electronics with dissolve
    jump eshop

label grocery:
    scene mall grocery with dissolve
    jump gshop

label eshop:
    hide screen phone
    show electronics clerk with dissolve
    "{cps=25}Hi what would you like to buy?"
    menu:

        "[cam.name]" if not cam.owned:
            menu:
                "Would you like to buy a [cam.name]"
                "Yes":
                    if inventory.buy(cam):
                        "Thank you for your purchase!"
                        $ renpy.block_rollback()
                        call buy_more
                        jump eshop
                    else:
                        "Not enough money"
                        call buy_more
                        jump eshop
                "No":
                    call buy_more
                    jump eshop

        "[rec.name]" if not rec.owned:
            menu:
                "Would you like to buy a [rec.name]"
                "Yes":
                    if inventory.buy(rec):
                        "Thank you for your purchase!"
                        $ renpy.block_rollback()
                        call buy_more
                        jump eshop
                    else:
                        "Not enough money"
                        call buy_more
                        jump eshop
                "No":
                    call buy_more
                    jump eshop

        "[lap.name]" if not lap.owned:
            menu:
                "Would you like to buy a [lap.name] ([lap.cost])"
                "Yes":
                    if inventory.buy(lap):
                        "Thank you for your purchase!"
                        if chapter1_end.shouldShow():
                            $ chapter1_end.completed = True
                            $ chapter1_end2.available = True
                        $ renpy.block_rollback()
                        call buy_more
                        jump eshop
                    else:
                        "Not enough money"
                        call buy_more
                        jump eshop
                "No":
                    call buy_more
                    jump eshop

        "[usb.name]" if not usb.owned:
            menu:
                "Would you like to buy a [usb.name]"
                "Yes":
                    if inventory.buy(usb):
                        "Thank you for your purchase!"
                        $ start_raid_ch1.incProgress()
                        $ renpy.block_rollback()
                        call buy_more
                        jump eshop

                    else:
                        "Not enough money"
                        call buy_more
                        jump eshop
                "No":
                    call buy_more
                    jump eshop

        "[knuckle.name]" if not knuckle.owned:
            menu:
                "Would you like to buy a [knuckle.name]"
                "Yes":
                    if inventory.buy(knuckle):
                        "Thank you for your purchase!"
                        $ start_raid_ch1.incProgress()
                        $ renpy.block_rollback()
                        call buy_more
                        jump eshop

                    else:
                        "Not enough money"
                        call buy_more
                        jump eshop
                "No":
                    call buy_more
                    jump eshop

        "Go back":
            jump mall

label gshop:
    hide screen phone
    show grocery clerk with dissolve
    "{cps=25}Hi, what would you like to buy?"
    menu:
        "[meat.name]" if not meat.owned:
            menu:
                "Would you like to buy a [meat.name]"
                "Yes":
                    if inventory.buy(meat):
                        "Thank you for your purchase!"
                        $ renpy.block_rollback()
                        call buy_more
                        jump gshop
                    else:
                        "Not enough money"
                        call buy_more
                        jump gshop
                "No":
                    call buy_more
                    jump gshop

        "[coke.name]" if not coke.owned:
            menu:
                "Would you like to buy a [coke.name]"
                "Yes":
                    if inventory.buy(coke):
                        "Thank you for your purchase!"
                        $ renpy.block_rollback()
                        call buy_more
                        jump gshop
                    else:
                        "Not enough money"
                        call buy_more
                        jump gshop
                "No":
                    call buy_more
                    jump gshop

        "[cabbage.name]" if not cabbage.owned:
            menu:
                "Would you like to buy a [cabbage.name]"
                "Yes":
                    if inventory.buy(cabbage):
                        "Thank you for your purchase!"
                        $ renpy.block_rollback()
                        call buy_more
                        jump gshop
                    else:
                        "Not enough money"
                        call buy_more
                        jump gshop
                "No":
                    call buy_more
                    jump gshop

        "[ketchup.name]" if not ketchup.owned:
            menu:
                "Would you like to buy a [ketchup.name]"
                "Yes":
                    if inventory.buy(ketchup):
                        "Thank you for your purchase!"
                        $ start_raid_ch1.incProgress()
                        $ renpy.block_rollback()
                        call buy_more
                        jump gshop

                    else:
                        "Not enough money"
                        call buy_more
                        jump gshop
                "No":
                    call buy_more
                    jump gshop

        "Go back":
            jump mall

label buy_more:
    "Anything else?"
    menu:
        "Yes":
            return
        "I'm good":
            "Have a nice day and please do come back real soon!"
            jump mall
