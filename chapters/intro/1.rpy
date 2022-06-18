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
        show laura neutral with dissolve
        lg "{cps=25} Good morning!"
        mc "{cps=25} Good morning, Laura!"
        mc "{cps=25} Do you have assignment in Calculus?"
        lg "{cps=25} Yup! I went home early last night to do this..."
        lg "{cps=25} Here... {p} You can copy this if you want."
        mc "{cps=25} Thanks! By the way, it seems like there are more empty chairs than usual."
        show laura surprised with dissolve
        lg "{cps=25} Oh right! I didn't noticed Jenny didn't attend the first class"
        show laura neutral with dissolve
        lg "{cps=25} I haven't heard anything from her since last night."
        lg "{cps=25} What time did the party ended?"
        mc "{cps=25} I don't know... {p}I went home early."
        #bell rang
        show prof at right with moveinright
        "{color=#ffffff}Professor{/color}" "{cps=25} Good morning class, {p}Let us begin."
        lg "{cps=25} Let's talk later... {p} Maybe Jenny is just late.."
        hide laura
        "{color=#ffffff}Professor{/color}" "{cps=25} Let us begin."
        scene black with dissolve
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
        show jake happy with dissolve
        jk "{cps=25} Hey! What's up? {p} Did you attend the morning class?"
        mc "{cps=25} Yeah, let me guess you cut classes again?"
        show jake bragging with dissolve
        jk "{cps=25} Well..."
        jk "{cps=25} I overslept, I decided I shouldn't bother coming since I'm late."
        show jake happy with dissolve
        jk "{cps=25} Anyway, how about you?"
        jk "{cps=25} You enjoyed the party last night?"
        mc "{cps=25} I went home early last night to go to work."
        show jake bragging with dissolve
        jk "{cps=25} You are no fun dude! {p}Last night {p}was {p}wild!"
        mc "{cps=25} Really? So, what happened in the party?"
        show jake happy with dissolve
        jk "{cps=25} Truth be told, I can't remember much..."
        jk "{cps=25} But all I can remember is the wild music and bottomless alcoholic drinks."
        mc "{cps=25} Why?"
        jk "{cps=25} I was wasted last night! {p}I barely remember anything..."
        show jake nervous with dissolve
        jk "{cps=25} Come to think of it...  {p}I think Jenny let loose last night."
        th "{cps=25} I feel she drunk more than she can handle last night."
        th "{cps=25} That's uncharacteristic thing for her to do."
        mc "{cps=25} Speaking of, do you know where Jenny is?"
        mc "{cps=25} She did not come to school today."
        jk "{cps=25} Hmm... I don't know..."
        jk "{cps=25} Maybe she had a hangover and cannot attend today."
        jk "{cps=25} Also I found her purse in my room."
        jk "{cps=25} That's why I forced myself to come to school to give it back to her..."
        mc "{cps=25} Hmm... maybe she really had a hangover can't come to school today."

        #bell rang
        mc "{cps=25} I'll be heading out now."
        mc "{cps=25} See you around."
        show jake happy with dissolve
        jk "{cps=25} Why don’t you just come with me and cut class?"
        mc "{cps=25} No, thanks I think I'll pass..."
        jk "{cps=25} Okay... Your choice."
        jk "{cps=25} What’s so fun in studying anyway? Tss..."
        scene black with dissolve
        "(You left)"
        $ energy -= 1
        jump location

    label library_1:
        hide screen phone
        show laura angry at right with dissolve
        lg "{cps=25} You’re her boyfriend! How come you don’t have idea where she is?"
        th "{cps=25} Hmm... Isn't that laura?"
        show lucas sad at left with dissolve
        ln "{cps=25} We had a little fight last night..."
        ln "{cps=25} I might have said something that hurt her…"
        ln "{cps=25} That’s why I am looking for her, to apologize"
        show lucas serious with dissolve
        ln "{cps=25} I was wondering that maybe you know where she is?"
        ln "{cps=25} Since, you are her best friend after all."
        show laura neutral with dissolve
        lg "{cps=25} I don't know and I can't contact her"
        lg "{cps=25} Her phone keeps ringing but no answer..."

        "(You approached them)"

        mc "{cps=25} So, you also don’t know here she is?"
        lg "{cps=25} No... I am worried about her."
        lg "{cps=25} She’s not responding in my text messages."
        lg "{cps=25} She does not answer any of my calls."
        lg "{cps=25} I tried to reach her in her social media accounts..."
        lg "{cps=25} I’ve been trying to contact her the whole day..."
        mc "{cps=25} She did not attend a single class today."
        lg "{cps=25} Did you try calling her mom Lucas?"
        ln "{cps=25} I did..."
        ln "{cps=25} But there's no answer."
        mc "{cps=25} Have you tried to visit her home?"
        show lucas neutral with dissolve
        ln "{cps=25} I already did and no one’s there."
        ln "{cps=25} That’s why I am here in the library... {p}Hoping that she'll be here."
        lg "{cps=25} Lucas you said you had a fight with her."
        lg "{cps=25} Maybe she want to distance herself from you for the mean time?"
        lg "{cps=25} Or maybe she went out today to gather some ideas for her story as a way of relax."
        show lucas sad with dissolve
        ln "{cps=25} This is all my fault"
        lg "{cps=25} She does it when she's down or stressed..."
        mc "{cps=25} Maybe Laura's right"
        mc "{cps=25} She’ll be back"
        ln "{cps=25} *sigh*"
        ln "{cps=25} I really hope so..."
        mc "{cps=25} We'll tell you if we found her"
        show lucas neutral with dissolve
        ln "{cps=25} Thank you"
        ln "{cps=25} Maybe I'm being paranoid too much... I should head out, take my mind off things"

        hide lucas with fade
        "(Lucas left)"

        show laura neutral at center with dissolve
        lg "{cps=25} Where could she might be?"
        mc "{cps=25} Jenny..."
        lg "{cps=25} If she's gone somewhere or something bugging her out, she always open it up to me."
        lg "{cps=25} Something feels off..."
        mc "{cps=25} I don’t know... Maybe we're just being paranoid"
        mc "{cps=25} Look, I’ll call you if Jenny message me"
        lg "{cps=25} Okay... I really hope we're just being paranoid"
        $ energy -= 1
        $ talk_to_laura.completed = True
        $ evening_home.available = True
        jump day_cycle

    label evening_1:
        hide screen phone
        #MC AT HIS HOUSE
        $ evening_home.completed = True
        $ midnight_home.available = True
        mc "{cps=25} What a rough day! What should I do now?"

        menu choices_1:
            "What should I do first?"
            "Watch news":
                $ energy = 0
                call news_1

            "Eat dinner.":
                $ energy = 0
                call dinner_1
        jump day_cycle

        label news_1:
            scene tv_close with dissolve
            pause(1)
            scene tv_close hand
            pause(1)
            scene tv_open hand
            pause(1)
            scene tv_open with dissolve
            "{color=#ffffff}Broadcaster{/color}" "{cps=25} One of the most promising writer of today's generation mysteriously dissapeared"
            "{color=#ffffff}Broadcaster{/color}" "{cps=25} As the name of this writer cannot be disclosed as her family wish not to."
            "{color=#ffffff}Broadcaster{/color}" "{cps=25} According to the police, it seems like it is a missing person case..."
            "{color=#ffffff}Broadcaster{/color}" "{cps=25} And they already had a suspect."
            scene tv_close hand
            pause(1)
            scene tv_close
            th "{cps=25} *sigh*"
            th "{cps=25} I wonder how's Jenny..."
            th "{cps=25} I hope Laura's right."
            th "{cps=25} I should get some a good sleep, it's been a tiring day after all."
            return

        label dinner_1:
            th "{cps=25} I'm thinking should I buy BBQ or Glazed Chicken."
            menu:
                "What should I eat?"
                "Barbecue":
                    call rider

                "Glazed Chicken Lollipop":
                    call rider

        label rider:
            "{color=#ffffff}Rider{/color}" "{cps=25} Here is the food that you ordered sir."
            mc "{cps=25} Thank you, Sir! Have a safe ride!"
            th "{cps=25} I wonder where and what happened to Jenny..."
            th "{cps=25} I should finish this food so that I can get a good sleep."
        return

    label midnight_1:
        $ midnight_home.completed = True
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
            mc "{cps=25} Do you know what time is it? {p} It's already 3:00am in the morning!"
            "{color=#ffffff}???{/color}" "{cps=25} I'm sorry... {p} I disturb your sleep but-"
            mc "{cps=25} Yes, you are disturbing and you're annoying!"
            #MC turned off his phone.
            mc "{cps=25} I should turn off my phone so no one will disturb me at this hour... {p} Who the hell will call at this hour?"
            #Lights off
            mc "{cps=25} I hope I can still sleep after that"
            return

        label sleepagain:
            scene home evening with dissolve
            th "{cps=25} I should go back to sleep..."
            th "{cps=25} ZZZzz..."
            return
