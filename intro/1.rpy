init python:
    thomasChar = False

label day_1:
    call load_quest
    $ day = 1
    $ tskip = True
    $ inv = True
    $ phone = True
    jump day_cycle

    label morning_1:
        hide screen phone
        "{cps=25}I should go to school before I am late"
        "{cps=25}I wonder what happened in the party..."
        call tutorial
        call tutorial
        call tutorial
        return

    label school_1:
        hide screen phone
        "{cps=25}Hmm..."
        "{cps=25}It seems Laura and Jenny are not here yet or have they gone to the classroom already?"
        $ go_to_school.completed = True
        "{cps=25}I should head to the class now"
        $ go_to_class.available = True
        return

    label classroom_1:
        hide screen phone
        lg "{cps=25} Good morning!"
        mc "{cps=25} Good morning, Laura!"
        mc "{cps=25} Do you have assignment in Calculus?"
        lg "{cps=25} Yup! I went home early last night to do this..."
        lg "{cps=25} Here... {p} You can copy this if you want."
        mc "{cps=25} Thanks! By the way, it seems like there are more empty chairs than usual."
        lg "{cps=25} Jenny is not yet here too."
        mc "{cps=25} Hmm.. maybe she had a hangover from the party?"
        lg "{cps=25} I guess so! {p} I haven't heard anything from her since last night.
        {p} what time does the party ended?"
        mc "{cps=25} I don't know! {p}I went home early too"
        #bell rang
        "{color=#ffffff}Professor{/color}" "{cps=25} Good morning class, {p}let us begin"
        lg "{cps=25} Let's talk later... {p} Maybe Jenny will be late.."
        "(You spend your morning studying)"
        $ go_to_class.completed = True
        $ energy -= 5
        $ talk_to_jake.available = True
        jump day_cycle


    label canteen_1:
        hide screen phone
        $ talk_to_jake.completed = True
        $ go_to_afterclass.available = True
        #Lunch time
        #Canteen
        jk "{cps=25} Hey! What's up? {p} Did you attend the morning class?"
        mc "{cps=25} Hi, Jake! Yes."
        jk "{cps=25} Why? {p} You were in the party last night. {p}You’re supposed to be sleepless.
        You should’ve spent your time sleeping and resting than attending boring morning classes. "
        mc "{cps=25} I went home early last night for work so I had enough sleep."
        jk "{cps=25} You are no fun dude! {p} Last night was crazy!"
        mc "{cps=25} Really? So, what time did the party ended?"
        jk "{cps=25} I don’t know!"
        mc "{cps=25} What do you mean you don't know?"
        jk "{cps=25} I was wasted last night! {p}I barely remember anything..."
        jk "{cps=25} All I can remember is the wild music... {p}bottomless alcoholic drinks"
        jk "{cps=25} Smell of smokes and some hot girls..."
        jk "{cps=25} Come to think of it...  {p}I think Jenny gone wild too"
        jk "{cps=25} She was so hot last night!"
        mc "{cps=25} Jenny? You mean Jenny Williams?"
        jk "{cps=25} yup! Jenny Williams!"
        mc "{cps=25} She's your cousin, right?"
        jk "{cps=25} Yupp! But it doesn’t mean I don't find her pretty."
        mc "{cps=25} What I mean is you’re cousins..."
        mc "{cps=25} I thought you might know where she is?"
        mc "{cps=25} She did not come to school today"
        jk "{cps=25} Hmm... I don't know..."
        mc "{cps=25} She did not drive you home last night?"
        jk "{cps=25} I don’t know…  {p}but I found her purse in my room."
        jk "{cps=25} So... {p}Maybe she did drive me home."
        mc "{cps=25} Maybe she just had a hangover.."

        #bell rang
        mc "{cps=25} It's time for afternoon class"
        mc "{cps=25} See you around"
        jk "{cps=25} Why don’t you just come with me cut class?"
        mc "{cps=25} No, thanks I think I'll pass..."
        mc "{cps=25} We have a quiz. Bye!"
        jk "{cps=25} Okay... Your life, your choice"
        jk "{cps=25} What’s so fun in studying anyway? Tss"
        "(You left)"
        $ energy -= 1
        jump location

    label library_1:
        hide screen phone
        lg "{cps=25} You’re her boyfriend! How come you don’t have idea where she is?"
        "You at Thinking" "{cps=25} Hmm.. Is that laura?"
        ln "{cps=25} We had a little fight last night..."
        ln "{cps=25}I said something that hurt her…"
        ln "{cps=25}That’s why I am looking for her now... {p}To apologize."
        ln  "{cps=25} I was wondering that maybe you know where she is? since you are her best friend"
        lg "{cps=25} I told you! I don't know! I can't contact her"
        mc "{cps=25} So, you also don’t know here she is?"
        lg "{cps=25} No.. I am frustratedly worried about her"
        lg "{cps=25} She’s not responding in my text messages."
        lg "{cps=25} She does not answer any of my calls"
        lg "{cps=25} I even tried to reach her in her social media accounts..."
        lg "{cps=25} I’ve been trying to contact her the whole day..."
        mc "{cps=25} Well, she did not attend a single class today."
        lg "{cps=25} Did you try calling her mom?"
        ln "{cps=25} I did... {p}But there's no answer"
        mc "{cps=25} Try to visit her home?"
        ln "{cps=25} I already did. No one’s there. That’s why I am here. Hoping to see her here."
        lg "{cps=25} Lucas you said you had a fight with her."
        lg "{cps=25} Maybe she went out for some air?"
        lg "{cps=25} She’s also a writer so maybe... "
        lg "{cps=25} She went out today to gather some ideas for her story."
        ln "{cps=25} You think so?"
        lg "{cps=25} That’s what she does when she’s having a writer’s block."
        lg "{cps=25} Roaming around to be inspired and to think of new ideas."
        mc "{cps=25} Maybe Laura's right"
        mc "{cps=25} Sooner or later, she’ll be back"
        ln "{cps=25} I don’t know. But I won’t sit still waiting for her {p}I will find her."
        lg "{cps=25} Then, go!"
        mc "{cps=25} Contact us once you found her!"
        ln "{cps=25} Thanks for the help"

        "(Lucas go away)"

        lg "{cps=25} Did you receive a message from Jenny?"
        mc "{cps=25} No... What about you? Do you know where she is?"
        lg "{cps=25} No… something’s weird..."
        lg "{cps=25} Something feels off... {p}I have a bad feeling about this."
        mc "{cps=25} I don’t know"
        mc "{cps=25} I’ll call you once I got a news {p}Do the same."
        lg "{cps=25} Okay"
        mc "{cps=25} I'll be heading out to work... {p}Take care!"
        lg "{cps=25} You too!"
        $ energy -= 1
        call evening
        $ talk_to_laura.completed = True
        jump entrance

    label evening_1:
        hide screen phone
        #MC AT HIS HOUSE
        $ evening_home.completed = True
        $ midnight_home.available = True
        mc "{cps=25} What a rough day! What should I do now?"
        mc "{cps=25} Should I watch news or eat dinner first?"

        menu choices_1:
            "What should I do first?"
            "Watch news":
                $ energy = 0
                jump news_1

            "Eat dinner.":
                $ energy = 0
                jump dinner_1

        label news_1:
            #scene TV
            #turns on TV
            "Broadcaster" "{cps=25} One of the most promising writer of today's generation was gone after the party..."
            "Broadcaster" "{cps=25} Her family and friends has been looking for her the whole day...
            {p} It has been 24 hours since she was last seen in the party..."
            "Broadcaster" "{cps=25} According to the police, it seems like it is a kidnapping case... {p} and they already has a suspect."
            "Broadcaster" "{cps=25} They cannot say the name of this writer as her family wish to."
            #turns off TV
            "{color=#ffffff}Thinking{/color}" "{cps=25}*sighs*"
            "{color=#ffffff}Thinking{/color}" "{cps=25} I wonder how's Jenny..."
            "{color=#ffffff}Thinking{/color}" "{cps=25} I hope Laura's right... {p} maybe she's just unwinding"
            "{color=#ffffff}Thinking{/color}" "{cps=25} I should get some a good sleep, it's been a tiring day after all."
            jump day_cycle

        label dinner_1:
            "{color=#ffffff}Thinking{/color}" "{cps=25} I'm thinking should I buy BBQ or Glazed Chicken."
            menu:
                "What should I eat?"
                "Barbecue":
                    jump rider

                "Glazed Chicken Lollipop":
                    jump rider

        label rider:
            "Rider" "{cps=25} Here is the food that you ordered sir."
            mc "{cps=25} Thank you, Sir! Have a safe ride!"
            "{color=#ffffff}Thinking{/color}" "{cps=25} I wonder where and what happened to Jenny..."
            "{color=#ffffff}Thinking{/color}" "{cps=25} I should finish this food so that I can get a good sleep."
        jump day_cycle

    label midnight_1:
        hide screen phone
        scene black with fade
        pause
        #Phone rings
        menu calling:
            "What is it this time?"
            "Answer":
                $ energy = 15
                call answered

            "Don't answer":
                $ energy = 15
                call sleepagain
        return

        label answered:
            #MC answered the phone
            #Lights on
            scene home evening with dissolve
            mc "{cps=25} Do you know what time is it? {p} It's effing 3:00am!"
            "{color=#ffffff}???{/color}" "{cps=25} I'm sorry... {p} I disturb your sleep but-"
            mc "{cps=25} Yes, you are disturbing and you're annoying!"
            #MC turned off his phone.
            mc "{cps=25} I should turn off my phone so no one will disturb me at this hour... {p} Who the hell will call at this hour?"
            #Lights off
            mc "{cps=25} I hope I can still sleep after that"
            return

        label sleepagain:
            scene home evening with dissolve
            "{color=#ffffff}Thinking{/color}" "{cps=25} I should go back to sleep..."
            "{color=#ffffff}Thinking{/color}" "{cps=25} ZZZzz..."
            return
