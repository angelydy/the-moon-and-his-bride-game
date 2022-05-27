label day_cycle:
    if energy == 15 or energy == 0:
        default location = "home"
        default subloc = "home"
    show screen phone
    if energy == 15:
        call morning
    elif energy == 10:
        call afternoon
    elif energy == 5:
        call evening
    elif energy == 0:
        call midnight

label morning:
    scene black with dissolve
    centered "{color=#FFF}Morning{/color}" with fade
    if day == 1:
        call morning_1
    $ energy -= 5
    jump day_cycle

label afternoon:
    scene black with dissolve
    centered "{color=#FFF}Afternoon{/color}" with fade
    if day == 1:
        call afternoon_1
    $ energy -= 5
    jump day_cycle

label evening:
    scene black with dissolve
    centered "{color=#FFF}Evening{/color}" with fade
    if day == 1:
        call evening_1
    $ energy -= 5
    jump day_cycle

label midnight:
    scene black with dissolve
    centered "{color=#FFF}Midnight{/color}" with fade
    call home
