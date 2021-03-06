label morning_2:
    hide screen phone
    th"{cps=25} Maybe Jenny will attend for today's class."
    $ go_to_school2.available = True
    return

label school_2:
    hide screen phone
    $ go_to_school2.completed = True
#Saw the police taking jake
#School
    show laura surprised at left with dissolve
    show police officer:
         xpos 0.58
    with dissolve
    show jake nervous at right with dissolve
    jk"{cps=25} I have no idea what are you talking about!"
    pol"{cps=25} You have the right to remain silent."
    jk"{cps=25}I swear, I never would have done it!"
    pol"{cps=25} What ever you say or do will be used against you in the court."
    hide jake with moveoutright
    hide police with moveoutright
    $ talk_to_laura2.available = True
    return

label talk_laura:
    hide screen phone
    $ talk_to_laura2.completed = True
    mc"{cps=25} Laura what happened?!"
    show laura neutral at center with moveinright
    lg"{cps=25} Jenny’s parents file a case against Jake regarding Jenny’s loss."
    lg"{cps=25} They are now taking him for questioning."

    mc"{cps=25} What?! {p}Why jake?"

    lg"{cps=25} I don’t know the details."
    lg"{cps=25} But from what I heard..."
    lg"{cps=25} They found Jenny’s purse in his room."
    lg"{cps=25} They suspected Jake for to be the one responsible for Jenny."

    mc"{cps=25} I don't get it... Why Jake? He’s Jenny’s cousin."
    mc"{cps=25} He’s not the type of person to have an ulterior motive."
    mc"{cps=25} Why would they think he’d do that?"

    lg"{cps=25} I don’t know... Although it’s not impossible."
    mc"{cps=25} Do you believe them?"

    lg"{cps=25} We all know Jake..."
    show laura angry with dissolve
    lg"{cps=25} He may be an idiot, {p}careless {p}and always up to no good..."
    show laura neutral with dissolve
    lg"{cps=25} but he has a kind heart."
    mc"{cps=25} That’s it! We know Jake and I believe he’s not capable of doing that act."
    mc"{cps=25} He may be a bad influence, {p}but he cares for Jenny."
    lg"{cps=25} Yeah and I still can’t believe that he could do such a thing..."
    mc"{cps=25} Listen Jake told me his short story about what happened back then in the canteen."
    mc"{cps=25} He told me he couldn’t remember anything after he got wasted at the party."
    mc"{cps=25} When he woke up the next day, he found himself in his room."
    mc"{cps=25} He also found Jenny’s purse on his side table, so he concluded that Jenny drove him back home."
    lg"{cps=25} He's our friend, but still the evidence is pointing at him."
    mc"{cps=25} I feel something is missing in the story..."
    mc"{cps=25} There's a saying... You can’t know what is happening behind the walls."
    mc"{cps=25} If you're just listening to the sound that comes from the wall."
    mc"{cps=25} Jake is our friend. {p}We know he’s not capable of harming Jenny."
    mc"{cps=25} We only heard the story from the authorities."
    #show laura sad
    lg"{cps=25} I don’t know what to believe anymore."
    lg"{cps=25} I am scared that something bad happened to Jenny..."

    lg"{cps=25} What should we do now?"
    mc"{cps=25} Something is wrong and I can feel it..."
    mc"{cps=25} We should find out more about what happened"
    mc"{cps=25} I swear to you I will get to the bottom of this..."
    $ visit_jake.available = True
    $ pstation = True
    return

label police_2:
    hide screen phone
    scene police interrogate with dissolve
    show jake happy with dissolve
    $ visit_jake.completed = True
    jk"{cps=25} [mc]! Over here!"
    mc"{cps=25} How are you holding up?"
    #showo jake nervous
    jk"{cps=25} Not good... {p}They’re accusing me of something I didn't do."
    jk"{cps=25} You gotta help me. {p}I am innocent, I swear!"
    mc"{cps=25} I trust you."
    mc"{cps=25} I really want to help, but I need you to help yourself by telling the truth..."
    mc"{cps=25} What really happened?"
    show jake tired with dissolve
    jk"{cps=25} Jenny’s mom went to my place to ask me about Jenny whereabouts..."
    jk"{cps=25} I let her into my home and found Jenny’s purse."
    jk"{cps=25} Then she claimed that I hid Jenny."
    jk"{cps=25} I swear, [mc] it isn't me."
    jk"{cps=25} I really don’t know where she is."
    jk"{cps=25} I’ve been looking for her to give her purse back. But I can't find her anywhere..."
    show jake nervous with dissolve
    jk"{cps=25} The next thing I know... {p}The police are taking me."
    jk"{cps=25} They said it’s just for questioning."
    jk"{cps=25} I told them the truth but I feel they buy my alibi."
    jk"{cps=25} [mc] please help me."

    mc"{cps=25} Do you remember who escorted you back home?"
    show jake tired with dissolve
    jk"{cps=25} No... I can’t remember much."
    jk"{cps=25} My memories are kind of fuzzy..."
    show jake nervous with dissolve
    jk"{cps=25} You know me, I never blacked out when I drink."
    jk"{cps=25} I feel something was wrong with my drink at the party that caused me to black out."

    mc"{cps=25} Please try to remember what happened."
    show jake tired with dissolve
    jk"{cps=25} I'll try..."
    show jake nervous with dissolve
    jk"{cps=25} I was... drinking at the party and there were people I talked to after I picked myself up."
    jk"{cps=25} There was a person... {p}I can’t remember who..."
    jk"{cps=25} He or she was offering me drinks as the crowd pressured me to drink it."
    jk"{cps=25} I drank... After that Everything was loud and wild that night."
    show jake tired with dissolve
    jk"{cps=25} I can’t remember what happened next..."
    show jake nervous with dissolve
    jk"{cps=25} But I am sure that I didn’t black out... {p}Not until I talked to Jenny, before she left."
    show jake tired with dissolve
    jk"{cps=25} After that, I can’t remember anything..."

    mc"{cps=25} I’ll try my best to find a way to clear your name..."

    show jake happy with dissolve
    jk"{cps=25} [mc] thank you…"
    show jake nervous with dissolve
    pol "3 minutes"
    mc"{cps=25} Thank you, Jake. Tell me if you remember anything else."
    show jake happy with dissolve
    mc"{cps=25} Laura and I will do what we can to help you."
    mc"{cps=25} We’ll get through this and we need you to help us."
    mc"{cps=25} I feel Jenny is still alive somewhere."
    show jake nervous with dissolve
    jk"{cps=25} Wait... there is this last thing that I remembered..."
    jk"{cps=25} I woke up in a car, I think... I’m not sure..."
    jk"{cps=25} But my vision is blurry and I can barely keep myself awake for a few seconds."
    jk"{cps=25} I heard someone whistling a song before I completely lost consciousness."
    jk"{cps=25} The whistling was familiar."
    scene black with dissolve
    "(The police took Jake back)"
    mc"{cps=25} Hmm..."
    mc"{cps=25} I should head back home and think about what I discovered today"
    $ evening_home2.available = True
    $ energy = 5
    $ location = "home"
    jump day_cycle

label evening_2:
    hide screen phone
#home
    th "{cps=25} What I know so far is that Jake’s drink was spiked."
    th "{cps=25} He and Jenny talked about something..."
    th "{cps=25} Jake blacked out and someone escorted Jake back and the whistle… what was it?"
    th "{cps=25} Hmm… I cannot solve this alone."
    th "{cps=25} I don’t even know where to start."
    "(There's a letter in the doorway)"
    mc"{cps=25} Huh? What’s this?"
    mc"{cps=25} A letter?"
    "LETTER""Riddle:"
    "LETTER""Wolves will howl."
    "LETTER""Awakened by an owl."
    "LETTER""Look at me, and you’ll stare in awe."
    "(There are sentences that doesn't make sense with their first capital letters highlighted)"
    "LETTER""J"
    "LETTER""E"
    "LETTER""N"
    "LETTER""N"
    "LETTER""Y"
    "LETTER""I"
    "LETTER""S"
    "LETTER""A"
    "LETTER""L"
    "LETTER""I"
    "LETTER""V"
    "J E N N Y    {p}I S     {p}A L I V E"

    th "{cps=25} This doesn’t make any sense..."
    th "{cps=25} There is a non-sense paragraph with the first letters capitalized and it seems to be highlighted."
    th "{cps=25} Also there’s this riddle..."
    th "{cps=25} What does it mean? Jenny is missing..."
    th "{cps=25} Then there’s this random letter with some weird riddle that came out of nowhere..."
    th "{cps=25} Thinking I feel this isn’t a coincidence."
    th "{cps=25} This must be connected somehow."
    th "{cps=25} This riddle has something to do with Jenny’s incident."
    th "{cps=25} I feel I should tell Laura what I found..."
    $ evening_home2.completed = True
    jump intro_end
    return

label intro_end:
    hide screen phone
    scene black with fade
    centered "{color=#FFF}(End of Introduction Chapter){/color}" with fade
    $ chapter += 1
    $ renpy.block_rollback()
    jump initialize
