label day_cycle:
    hide screen phone
    if energy == 15 or energy == 0:
        default location = "home"
        default subloc = "home"
        if energy == 15:
            call morning
        elif energy == 0:
            call midnight
    elif energy == 10:
        call afternoon
    elif energy == 5:
        call evening


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
    if talk_to_laura.shouldShow():
        return
    jump location

label midnight:
    hide screen phone
    scene black with dissolve
    centered "{color=#FFF}Midnight{/color}" with fade
    jump location
