label timeskip:
    hide screen phone
    if energy <= 15 and energy > 10:
        $ energy = 10
        jump day_cycle

    elif energy <= 10 and energy > 5:
        $ energy = 5
        jump day_cycle

    elif energy <= 5 and energy != 0:
        $ energy = 0
        jump day_cycle
