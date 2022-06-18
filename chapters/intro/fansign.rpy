label fansign_0:
    scene black
    with fade
    "(You accompanied Jenny in the Fan sign event)"
    scene mall with dissolve
    mc"{cps=25} ohhhh you have lots of fans huh…"
    show jenny surprised with dissolve
    jn"{cps=25} I am so surprise too.. I never thought I’ll be having fans… You know.. writing is just my hobby…"
    mc"{cps=25} It means you’re really a great author…"
    jn"{cps=25} I guess so... But I’m still growing as an author…"
    show student_3 at left with moveinleft
    "Event organizer" "{cps=25} Ma’am Jenny, you can take your seat.. We’ll start in 5 minutes…"
    jn"{cps=25} Can he come with me?"
    "Event org" "{cps=25} sure ma’am.."
    hide student_3 with moveoutleft
    jn"{cps=25} Thank you… Here, [mc]… can you hold these pens for me? …"
    mc"{cps=25} Ohh... sheesh! This is a lot…"
    show jenny happy with dissolve
    jn"{cps=25} *chuckles* stay behind me.."
    mc"{cps=25} I got your back…"
    scene black with dissolve
    "(After 3 hrs)"
    scene mall with dissolve
    mc"{cps=25} Are your hands, okay?"
    show jenny neutral with dissolve
    jn"{cps=25} It hurts a little… But I’m okay…"
    mc"{cps=25} You look so tired…"
    show jenny happy with dissolve
    jn"{cps=25} I’m okay.. It’s worth it.. By the way… Are you still going to the party? It’s not that I don’t want you to come. It’s just that you might be tired…"
    menu:
        "Of course, I'm going":
            jump f1
        "I don't think I can come... My body suddenly felt heavy, I'm sorry":
            jump f2

label f1:
    show jenny surprised with dissolve
    jn"{cps=25} Yayy!! You’re the best.. I’ll just go home to change my clothes then I’ll go straight to the party…"
    mc"{cps=25} Okay, see you there.."
    show jenny neutral with dissolve
    jn"{cps=25} Do you want me to drive you home I can call my driver?"
    menu:
        "Is it okay? I mean our way back are different":
            jump f1_1
        "No thank you for the offer":
            jump f1_2

label f1_1:
    show jenny happy with dissolve
    jn"{cps=25} It’s fine, you helped me here anyway.."
    mc"{cps=25} Thank you…"
    scene black with dissolve
    "(Jenny drove you home)"
    scene home afternoon with dissolve
    mc"{cps=25} Thank you, Jenny!"
    show jenny happy with dissolve
    jn"{cps=25} You’re always welcome.. See you at the party.."
    mc"{cps=25} Sure, thank you!"
    jump next

label f1_2:
    mc"{cps=25} Our ways are different…"
    show jenny happy with dissolve
    jn"{cps=25} It’s okay, you helped me here anyways.."
    mc"{cps=25} I’m really okay.. you should hurry for your party…"
    show jenny neutral with dissolve
    jn"{cps=25} Okay… See you then?"
    mc"{cps=25} Sure.. see you.."
    show jenny happy with dissolve
    jn"{cps=25} Bye!"
    mc"{cps=25} Bye!"
    jump next

label f2:
    show jenny neutral with dissolve
    jn"{cps=25} Aww... Sorry... I tired you out.."
    mc"{cps=25} No! It’s okay.."
    jn"{cps=25} Wait.. I think I have meds here.."
    mc"{cps=25} Thank you but I have my meds at home.. I just need to take a little rest before I go to work..."
    jn"{cps=25} So, you can’t come?"
    mc"{cps=25} Sorry… but I promise I’ll make it up to you…"
    jn"{cps=25} That’s sad.. see you tomorrow then?"
    mc"{cps=25} Sure.. See you.. Enjoy the party.. And congratulations again for the success of the event.."
    jn"{cps=25} Thank you, [mc]…"
    scene black with dissolve
    "(You went back home and go to work)"
    jump work_0

label next:
    mc"{cps=25} I still have some time for the party before going to work…"
    scene black with dissolve
    "(You went to the party)"
    jump evening_0
