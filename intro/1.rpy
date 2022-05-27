label day_1:
    call day_cycle

    label morning_1:
        #scene room with dissolve
        "{cps=25}I should go to school before I'll be late"
        "{cps=25}I wonder what happened in the party..."
        call location
        return

    label afternoon_1:
        jump uc
        return

    label evening_1:
        jump uc
        return

    label midnight_1:
        jump uc
        return
