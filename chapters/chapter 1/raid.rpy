label raid_ch1:
    # if start and start2 raid is completed
    hide screen phone
    #Behind the bush
    scene bush night with dissolve
    show jake happy at right with moveinright
    jk"{cps=25} Yo"
    show laura neutral at left with moveinleft
    lg"{cps=25} What’s the plan"
    mc"{cps=25} Okay, the plan is…"
    mc"{cps=25} Laura will be the distraction"
    mc"{cps=25} Use this"
    show ketchup with dissolve
    pause(1)
    hide ketchup with dissolve
    mc"{cps=25} I’ll look like blood in that way you can get the police attention"
    show laura surprised
    lg"{cps=25} Whaaaat!!"
    mc"{cps=25} SSHHH! Keep it down!"
    show laura angry
    lg"{cps=25} This is ridiculous"
    mc"{cps=25} Sure, go ahead if you have any better idea"
    lg"{cps=25} …"
    lg"{cps=25} Damn I have nothing…"
    lg"{cps=25} *sigh* {p}For jenny"
    mc"{cps=25} Okay, now Jake, I bought you this…"
    show brass_knuckles with dissolve
    pause(1)
    hide brass_knuckles
    jk"{cps=25} Cool!"
    lg"{cps=25} Very unfair"
    mc"{cps=25} Okay use that when we got in trouble…"
    mc"{cps=25} You guys ready?"
    show laura neutral
    lg"{cps=25} Ready"
    jk"{cps=25} Good to go"
    mc"{cps=25} Okay, let’s go."
    hide laura 
    hide jake 

    "OFFICER!"
    show police officer at right with moveinright
    "{color=#ffffff}Police{/color}" "{cps=25} Hmm…"
    show laurab neutral at left with moveinleft
    lg"{cps=25} HELP!"
    "{color=#ffffff}Police{/color}" "OMG, WHAT HAPPENED MA’AM?!"
    lg"{cps=25} Someone is chasing me"
    "{color=#ffffff}Police{/color}" "{cps=25} Get inside Ma’am I’ll deal with it"
    hide police officer with moveinright
    hide laura with moveinleft

    "(You and Jake sneak behind the police)"
    "(You and Jake got inside Lucas’s House)"
    mc"{cps=25} Okay Jake follow my lead"

    "HMM… WHAT ARE YOU GUYS DOING IN A PRIVATE PROPERT?!"
    with vpunch
    mc"{cps=25} SHIT!"
    show jake happy with dissolve
    jk"{cps=25} I got this… Go on ahead, I’ll catch on"
    mc"{cps=25} Okay, try to… stay alive."
    jk"{cps=25} Don’t worry I plan to"

    scene black with dissolve
    "(You Left)"

    #Security Room
    scene security room with dissolve
    th"{cps=25} Good thing the security room is empty"
    th"{cps=25} It must be the security guy Jake is fighting against"
    th"{cps=25} Jake will be fine can handle himself; I saw him go toe to toe against a tall muscular dude"
    th"{cps=25} I hope so…"
    "(You plugged the usb)"
    show usb with dissolve
    pause(1.0)
    hide usb

    th"{cps=25} So, what do we have here…"
    th"{cps=25} …"
    th"{cps=25} There’s nothing useful in here what the fuck?! There’s only one file!"
    th"{cps=25} Laura was right there’s no…"
    th"{cps=25} Wait a second… this isn’t an ordinary file…"
    th"{cps=25} This is a file without extension, maybe the computer cloud system went bugged that day"
    th"{cps=25} I’ll just restore the extension… then… baam!"
    th"{cps=25} A video file about that day! BINGO!"
    th"{cps=25} I need to move"

    #Lucas House
    mc"{cps=25} Jake?"
    show jake happy with dissolve
    jk"{cps=25} *huff* *Huff* *huff*"
    mc"{cps=25} Let’s go"
    jk"{cps=25} Alright…"
    mc"{cps=25} Damn, I’m amazed you took him down"
    jk"{cps=25} Told *huff* you *huff*"
    mc"{cps=25} You look like shit tho…"
    jk"{cps=25} You don’t say!"

    scene mansion_entrance evening with dissolve
    "(You signal Laura)"
    show laurab surprised at left with moveinleft
    lg"{cps=25} OMG! SIR I THINK I SAW HIM HE WENT INSIDE THE FRONT ENTRANCE"
    show police officer at right with moveinright
    "{color=#ffffff}Police{/color}" "{cps=25} Stay here I’ll check it out"
    "(The police left)"
    hide police officer with moveinright
    "(You approached Laura)"
    mc"{cps=25} Let’s get the out of here!"
    show jake happy at right with moveinright
    jk"{cps=25} WE’RE LIKE SPIES!!"

    scene black with dissolve
    "(You and the gang left)"

    scene bush night with dissolve
    mc"{cps=25} Fuck… things didn't exactly went what I thought it would be"
    show laura chuckle at left with moveinleft
    lg"{cps=25} What happened to you Jake? You look like you got hit by a truck"
    show jake happy at right with moveinright
    jk"{cps=25} I know *huff*, I know *huff*"
    jk"{cps=25} Let me {p}*huff* catch my {p}*huff* breath"
    show laura neutral
    lg"{cps=25} Good thing I’m the one in distraction duty"
    mc"{cps=25} You removed the ketchup?"
    lg"{cps=25} Yep, why would I not clean myself?"
    lg"{cps=25} Anyway, what did you find?"
    mc"{cps=25} It seems there’s no footage when I checked"
    lg"{cps=25} So, all this for nothing?"
    mc"{cps=25} Not at all, they missed one file…"
    lg"{cps=25} GREAAT! I would really lose my cool if we did that for nothing"
    jk"{cps=25} Hopefully that is something useful"
    mc"{cps=25} Hopefully…"
    mc"{cps=25} Let’s call this a day"
    mc"{cps=25} I’ll talk to you guys soon about what I’ll find"
    mc"{cps=25} Let’s lay low for a bit"
    lg"{cps=25} See you"
    jk"{cps=25} This night was crazy!"
    $ chapter1_end.available = True
    scene black with dissolve
    if inventory.itemCheck(lap):
        th"{cps=25} I'll show them as soon as possible at the library in the Afternoon"
        $ chapter1_end.completed = True
        $ chapter1_end2.available = True
    else:
        th"{cps=25} I need a laptop to show the gang what I found"
    $ energy = 0
    jump location
