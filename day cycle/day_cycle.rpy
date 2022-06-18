label day_cycle:
    hide screen phone
    if energy == 15 or energy == 0:
        default location = "home"
        default subloc = "home"
        if energy == 15:
            jump morning
        elif energy == 0:
            jump midnight
    elif energy == 10:
        jump afternoon
    elif energy == 5:
        jump evening


label morning:
    hide screen phone
    scene black with dissolve
    centered "{color=#FFF}Morning{/color}" with fade
    jump location

label afternoon:
    hide screen phone
    scene black with dissolve
    centered "{color=#FFF}Afternoon{/color}" with fade
    jump location

label evening:
    hide screen phone
    scene black with dissolve
    centered "{color=#FFF}Evening{/color}" with fade
    jump location

label midnight:
    hide screen phone
    scene black with dissolve
    centered "{color=#FFF}Midnight{/color}" with fade
    jump location
