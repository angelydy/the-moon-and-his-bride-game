label timeskip:
    if energy <= 15:
        $ energy == 10
        jump day_cycle

    elif energy <= 10:
        $ energy == 5
        jump day_cycle

    elif energy <= 5:
        $ energy == 0
        jump day_cycle
