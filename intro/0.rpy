init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("eye.png", .99, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("eye.png", .99, ramplen=128, reverse=True, time_warp=eyewarp)

    #Variables
    late = True
    canteen0 = False
    partychoice_0 = True
    findjake = False
    jaketalk_0 = True
    jakeoffend_0 = False

image black:
    Solid("#000")
image white:
    Solid("#FFF")


label day_0:
    $ day = 0
    label morning_0:
        scene black
        with dissolve
        play music "/audio/morning_0.mp3"
        call tutorial
        $ name = renpy.input("What is your nickname? (If left empty name will be Owen)", length = 10)
        $ name = name.strip()
        if not name:
            $ name = "Mike"
        centered "{color=#FFF}(You will be given a choice. What you choose from here on out affects the outcome of the game){/color}" with fade
        scene white
        with eye_open
        stop music
        scene home morning
        #alarm sound effect
        play music "/audio/alarm_morning0.mp3"
        mc "{cps=25}*Hnng*{p}It's morning already..."
        stop music fadeout 0.5

        menu late_0:
            "What should I do first"
            "Take a Bath":
                $ late = False
                jump bath_0

            "Eat my breakfast":
                $ late = True
                jump breakfast_0

        label bath_0:
            scene bath
            with dissolve
            #bath sound effect
            play music "/audio/bathing_sound.mp3"
            "{cps=25}My name is {color=cc6600}[mc]{/color}"
            "{cps=25}I am just your typical simple person  {p}trying to get by through college."
            "{cps=25}I study in the morning till afternoon"
            "{cps=25}I work as a part-timer in the evenings to supplement my income."
            mc "{cps=25}Done... {p}Hmmm..."
            mc "I still have a... {p}few minutes left"
            stop music
            jump news_0

        label breakfast_0:
            scene breakfast
            with dissolve
            #eating sound effect
            play music "/audio/eating_sound.mp3"
            "{cps=25}My name is {color=cc6600}[mc]{/color}"
            "{cps=25}I am just your typical simple person  {p}trying to get by through college."
            "{cps=25}I study in the morning till afternoon"
            "{cps=25}I work as a part-timer in the evenings to supplement my income."
            mc "{cps=25}Done... {p}Hmmm..."
            mc "{cps=25}I still have a... {p}little bit of time left"
            stop music
            jump news_0

        label news_0:
            scene tv close
            mc "{cps=25}Hmm... I feel like checking the news today before I go"
            mc "{cps=25}Just checking wouldn't hurt..."
            scene tv close hand
            mc "{cps=25}I wonder what's on the news today."
            "(Opens the TV)"
            scene tv open hand
            scene tv open
            play music "/audio/tv_voice.mp3"
            "{color=#FFF}Broadcaster{/color}" "{cps=25}Breaking News!{p} There seems to be an upcoming Blue Moon this week..."
            "{color=#FFF}Broadcaster{/color}" "{cps=25}We all know that a blue moon only occurs every 33 months, 41 times per century, or about every 19 years."
            "{color=#FFF}Broadcaster{/color}" "{cps=25}Tell us your thoughts about this..."
            "{color=#FFF}NASA Scientist{/color}" "{cps=25}A blue moon is the second full moon in a month. It happens to be blue because of the Earth's atmosphere."
            "{color=#FFF}NASA Scientist{/color}" "{cps=25}Containing dust or smoke particles of a certain size."
            "{color=#FFF}NASA Scientist{/color}" "{cps=25}It is theorized that the blue moon will occur this upcoming Sunday."
            scene tv close hand
            "(You turned off the TV)"
            stop music fadeout 1
            mc "{cps=25}Hmm... {p}I hope there's going to be a blue moon this month so I can invite the gang."
            if late:
                mc "{cps=25}Shit... {p}I'm late"

            else:
                mc "{cps=25}I should probably leave, or I'm going to be late for school."
            scene black
            with fade
            "(You went to School)"

        label school_0:
            if late:
                scene classroom morning
                with dissolve
                with vpunch
                play music "/audio/classroom_0.mp3"
                uk "{cps=25}YOU'RE LATE!"
                "(You looked at where the voice came from)"
                show laura angry with dissolve
                uk "{cps=25}How many times do I need to tell you not to be late! {p}This is a group work. So, one mistake and everyone will receive a minus point."
                "{cps=25}This is Laura Godfrey. {p}She's like a living speaker who always says what's on her mind, but she's a responsible student
                is quite a famous person around the school."
                "{cps=25}She's totally hooked up on social media and when it comes to listening to humor... {p}She's always up to date"
                hide laura angry with dissolve
                #show Jenny worried
                uk "{cps=25}Laura... {p}Uhm... please don't scold [mc] {p}I'm sure that [mc] tried his best {p}Right [mc]?"
                "{cps=25}This is Jenny Williams, {p}She's always sweet, kind, caring, and a very thoughtful person. She's like a motherly figure towards her friends."
                "{cps=25}She's also a writer {p}She wrote the best selling book of the year and became an award winning author"
                #show Jenny neutral
                show laura neutral as laura2 at left with dissolve
                "{cps=25}Laura, Jenny and me are child hood friends. {p}We grew up together, constantly making fun of each other."
                "{cps=25}But Laura and Jenny are closer to each other. They're like a mother and her child."
                stop music

            else:
                scene school morning
                with dissolve
                #Birds Sound effect
                play music "/audio/bird_chirping.mp3"
                uk "{cps=25}[mc] over here!"
                stop music
                "(You looked at where the voice came from)"
                #show Jenny amazed
                play music "/audio/classroom_0.mp3"
                uk "{cps=25}You came!"
                "{cps=25}This is Jenny Williams, {p}She's always sweet, kind, caring, and a very thoughtful person. She's like a motherly figure towards her friends."
                "{cps=25}She's also a writer {p}She wrote the best selling book of the year and became an award winning author"
                uk "{cps=25}Hey DOFUS! {p}I really thought you would come late!"
                show laura neutral with dissolve
                "{cps=25}This is Laura Godfrey. {p}She's like a living speaker who always says what's on her mind, but she's a responsible student
                is quite a famous person around the school."
                "{cps=25}She's totally hooked up on social media and when it comes to listening to humor... {p}She's always up to date"
                #show Jenny
                hide laura neutral with dissolve
                jn "{cps=25}Laura... that's really ruuude"
                jn "{cps=25}[mc] really tried his best to come early!"
                jn "{cps=25}Right [mc]?"
                mc "{cps=25}Yeah, I did... It's early in the morning Laura and you're yelling already {p}Give the birds a break for godsake"
                show laura pissed at left with dissolve
                lg "{cps=25}Want to die early morning?"
                "{cps=25}Laura, Jenny and me are child hood friends. {p}We grew up together, constantly making fun of each other."
                "{cps=25}But Laura and Jenny are closer to each other. They were best friends for a long time."
                hide laura pissed with dissolve
                stop music
                #bellring sound effect
                play music "/audio/school_bell.mp3"
                jn "{cps=25}Continue your fight later. {p}We should head to the class."
                stop music


            scene classroom morning
            with dissolve
            with vpunch
            play music "/audio/classroom_0.mp3"
            show jake smiling with dissolve
            uk "YOOOO! {p}[mc]!"
            uk "{cps=25}Our professor isn't here yet. {p}I'm sure he skipped his early class to smoke."
            uk "{cps=25}You.. me... Laura... and Jenny. {p}We could head to the canteen"
            "{cps=25}This is Jake {p}Jenny's cousin; he's similar to Laura but different at the same time."
            "{cps=25}They're both loud, but the only difference is that Jake is irresponsible, so that's another reason why Laura and Jake don't get along."
            hide jake smiling with dissolve
            #show Jenny concerned
            jn "{cps=25}But... Isn't that wrong?"
            show jake bragging as jakebragging at right with moveinright
            jk "{cps=25}Well.. {p}It isn't cutting classes when there are no classes, right?"
            show laura pissed as laurapissed at left with moveinleft
            lg "{cps=25}Shut up jake. {p}Don't listen to him, Jenny, or you'll end up in the guidance."
            jk "{cps=25}Sheesh... {p}You need to loosen up once in a while, Laura. {p}You can't have fun when you can't take a risk, right Jenny?"
            jn "{cps=25}I don't know..."
            jk "{cps=25}It won't take long."
            #hide jenny
            "{cps=25}The main reason Jake and Laura don't get along is because they're like a devil and angel, influencing Jenny's actions."
            hide laura pissed as laurapissed at left with dissolve
            hide jake bragging as jakebragging at right with dissolve
            show jake bragging at center
            jk "{cps=25}Come on... It's not like our professor will suddenly be behind my back."
            stop music fadeout 1.0
            "{color=#ffffff}Professor{/color}" "{cps=25}What is it, Mr. Jake Williams? {p}I heard you wanted to go to the canteen."
            show jake nervous with dissolve
            jk "{cps=25}No sir {p}I was... {p}Uhmm..."
            jk "{cps=25}talking about... {p}I'm thinking about volunteering in the canteen, sir!"
            hide jake nervous with dissolve
            "{color=#ffffff}Professor{/color}" "{cps=25}Very well, during the afternoon, head out to the canteen and tell them I sent you to volunteer."
            #show Jenny and Laura chuckles
            show laura chuckle as laurachuckle at left with dissolve
            "(Jenny and Laura chuckles)"
            hide laura chuckle as laurachuckle at left with dissolve
            "{color=#ffffff}Professor{/color}" "{cps=25}Everyone take a sit so we can start"
            scene black
            with dissolve
            "(The class proceeds as usual)"
            scene classroom morning
            with dissolve
            play music "/audio/chatters_0.mp3"
            show laura angry with dissolve
            lg "{cps=25}I THOUGHT THE CLASS WAS NEVER GOING TO END!"
            #Show Jenny embarrassed
            lg "{cps=25}GOD...{p}I DON'T KNOW WHY I BOTHERED TO LISTEN"
            lg "{cps=25}For godsake he's just simply READING OUR LESSON!"
            lg "{cps=25}Do you really call that TEACHING?"
            lg "{cps=25}I WOULDN'T!"
            lg "{cps=25}Gosh... listening to Sir made me hungry"
            lg "{cps=25}Jenny let's go to the canteen?"
            hide laura angry with dissolve
            jn "{cps=25}Suuure"
            #show Jenny shy
            jn "{cps=25}Uhm... {p}[mc]?"
            jn "{cps=25}Would you like to come with us?"
            mc "{cps=25}I..."
            with vpunch
            show jake nervous
            jk "{cps=25}YO!{p}[mc]!"
            jk "{cps=25}DUDE CAN YOU HELP ME?"
            jk "{cps=25}SIR IS DEAD SERIOUS ABOUT MAKING ME DO COMMUNITY SERVICE IN THE CANTEEN!"
            jk "{cps=25}I'M FREAKING SCARED OF THE OLD CANTEEN LADY..."
            jk "{cps=25}SHE'S LIKE A FREAKING GORILLA!"
            jk "{cps=25}I swear... she'll beat me into a pulp if I make mistakes"
            jk "{cps=25}The simple thought of it makes me shiver..."
            stop music

            menu jk_jen:
                jk "Can you help me?"
                "Yeah, sure bro, I can help you out":
                    $ canteen0 = False
                    jump jake_0

                "No, sorry bro, wish I could help":
                    $ canteen0 = True
                    jump jenny_0

            label jake_0:
                show jake happy with dissolve
                jk "{cps=25}YOOOO DUDE THANKS!"
                jk "{cps=25}I OWE YOU BIG!"
                scene back morning
                with dissolve
                "(Short time passes by while carrying stocks of food to the storage)"
                show jake tired with dissolve
                jk "{cps=25}A little bit more..."
                jk "{cps=25}Err... {p}Too heavy..."
                show jake nervous with dissolve
                jk "{cps=25}Help help help help... [mc] HELP!"
                "(You rushed to help Jake who carried a box too heavy for him to carry alone)"
                jk "{cps=25}Almost got my back crushed"
                show jake happy with dissolve
                jk "{cps=25}Thanks bro you really did me a solid"
                jk "{cps=25}Anyways, we're done here let's head back to Jenny and Laura"
                scene black
                with fade
                "(You meet up with Jenny and Laura)"
                jump justinecomes_01

            label jenny_0:
                jk "{cps=25}Aight bro wish me luck..."
                hide jake nervous with fade
                "(Jake Left)"
                #show jenny
                jn "{cps=25}I feel bad for Jake"
                show laura neutral with dissolve
                lg "{cps=25}Well he asked for it..."
                lg "{cps=25}Let's go?"
                hide laura neutral with dissolve
                scene canteen morning
                with dissolve
                play music "/audio/chatters_0.mp3"
                "(Time passed by eating together while chatting)"
                "(A random person approached Jenny)"
                show lucas happy with dissolve
                uk "{cps=25}Hey love..."
                uk "{cps=25}I was just looking for you"
                uk "{cps=25}Where you've been?"
                hide lucas happy with dissolve
                #show jenny
                jn "{cps=25}I was just hanging out with my friends"
                uk "{cps=25}I see..."
                "(He looked towards you and then glanced at Jenny)"
                jn "{cps=25}Oh sorry! {p}[mc] this is Lucas my boyfriend"
                jn "{cps=25}Lucas this is [mc] my friend"
                show lucas neutral with dissolve
                ln "{cps=25}My name is Lucas"
                "(He offered a handshake)"
                "(You and Lucas shook hands)"
                ln "{cps=25}So love, I'm going to hold a celebration party for your great success at the Mansion."
                hide lucas neutral with dissolve
                #show jenny sa right
                jn "{cps=25}Can I invite anyone?"
                #hide jenny sa right
                show lucas happy with dissolve
                ln "{cps=25}*chuckles*"
                ln "{cps=25}Oh dear... you're really are adorable"
                ln "{cps=25}Of course!"
                ln "{cps=25}You can invite anyone since it's your party"
                stop music

            label justinecomes_01:
                scene canteen morning
                with dissolve
                play music "/audio/chatters_0.mp3"
                show justine neutral at right with moveinleft
                uk "{cps=25}Lucas"
                uk "{cps=25}Our council advisor is looking for us"
                show lucas neutral with dissolve
                ln "{cps=25}I got to go love, see you later"
                if canteen0:
                    ln "{cps=25}Nice meeting you [mc]"
                hide justine with moveoutright
                hide lucas neutral with fade
                "(They left)"
                show laura chuckle with dissolve
                lg "{cps=25}Wow... He really loves you doesn't he?"
                hide laura chuckle with dissolve
                "(Justine approaches)"
                show jake happy with moveinright
                jk "{cps=25}Hmmm..."
                jk "{cps=25}Is that Lucas Norris and Justine Raymond?"
                mc "{cps=25}Who?"
                jk "{cps=25}Lucas and Justine {p}they're like elites here in school"
                hide jake with dissolve
                #scene Lucas portrait
                show laura neutral as lauraneautral at left with dissolve
                lg "{cps=25}Yeah, Lucas Norris {p}He's Jenny's boyfriend"

                #show Jenny blush
                jn "{cps=25}Laura!"
                hide laura neutral as lauraneautral at left
                show laura chuckle as laurachuckle at left
                lg "{cps=25}Whaaat? just stating the facts {p}Anyways..."
                #hide jenny
                hide laura chuckle as laurachuckle at left with dissolve
                show laura neutral with dissolve
                lg "{cps=25}Lucas is a \"people person\" if you ask me, which is the reason he became the president of the student council."
                lg "{cps=25}He is very friendly, approachable, thoughtful, confident and very smart."
                lg "{cps=25}Also, Lucas's recent project gained world wide attention because of its miraculously bringing dead mice back to life."
                lg "{cps=25}Although it has other side effects on the mice, it is a great feat nonetheless."
                lg "{cps=25}And beside Lucas is Justine Raymond."
                lg "{cps=25}He's the council vice president and as smart as Lucas, but they're like night and day."
                #scene Justine portrait
                hide laura
                show jake bragging with dissolve
                jk "{cps=25}But unlike Lucas, he isn't friendly; he always makes sarcastic comments and he is mostly known for his cold actions that are driven by logic and reason."
                jk "{cps=25}Sometimes I feel more like an emotionless robot than a human."
                jk "{cps=25}I wonder how they get along..."
                show jake nervous with dissolve
                jk "{cps=25}If I were you, I wouldn't even think of approaching Justine..."
                mc "{cps=25}Why?"
                jk "{cps=25}He has this scary reputation that he's dangerous and cunning {}Even delinquents don't want to mess with him."
                show laura neutral at left with moveinleft
                lg "{cps=25}I heard some rumors that he's a sadistic maniac who blackmails people."
                show jake happy  with dissolve
                jk "{cps=25}Also, Justine and Jenny always have a fight with each other."
                #show Jenny sad
                jn "{cps=25}He's a meanie!"
                lg "{cps=25}It's okay, I'm here. I won't let him get close to you."
                lg "{cps=25}I'll kick his ass real hard to the point he can't poop for many years to come."
                jk "{cps=25}Well... I wouldn't be surprised if Justine planned to kidnap Jenny or something."
                with vpunch
                show laura angry with dissolve
                show jake nervous with dissolve
                "(Laura kicked Jake's knee)"
                #show Jake hurt
                jk "{cps=25}OW!"
                lg "{cps=25}That's not funny!"
                jk "{cps=25}I was just JOKING!"
                show laura pissed with dissolve
                lg "{cps=25}Still not funny"
                menu:
                    "Calm down Laura! it's just a joke":
                        lg "{cps=25}Still a bad joke"
                        jk "{cps=25}See?"
                    "Yeah it was a bad joke bro...":
                        jk "{cps=25}Aight my bad, my apologies"

                show laura neutral with dissolve
                show jake happy with dissolve
                jk "{cps=25}But when it comes to a fight, me and [mc] will be by your side, Jenny."
                #show Jenny happy
                jn "{cps=25}Thanks guys"
                stop music
                jump afternoon_0

    label afternoon_0:
        scene black
        with dissolve
        play music "/audio/afternoon_0.mp3"
        "(Time passes by until the school beng rings)"
        centered "{color=#FFF}Afternoon{/color}" with fade
        stop music fadeout 0.5
        scene classroom afternoon
        with dissolve
        with vpunch
        play music "/audio/classroom_0.mp3"
        show jake smiling at right with dissolve
        jk "{cps=25}FINALLY! SCHOOL IS OVER!!"
        show laura neutral at left with moveinleft
        lg "{cps=25}Hey idiot you're shouting like you won't come to school tommorow"
        show jake happy at right with dissolve
        jk "{cps=25}I know, I'm just living my life like school's about to end."
        jn "{cps=25}Uhm... guys?"
        jn "{cps=25}Remember what Lucas said?"
        jk "{cps=25}Yeah?"
        lg "{cps=25}What about it?"
        jn "{cps=25}I'm kinda awkward with Lucas's guests so..."
        jn "{cps=25}Will you guys come with me in the party?"
        show jake smiling at right with dissolve
        jk "{cps=25}HELL YEAH!"
        jk "{cps=25}Who would decline on that offer? {p}It's Lucas's Mansion!"
        show laura chuckle with dissolve
        lg "{cps=25}Of course dear, especially when you're that cute when asking."
        jn "{cps=25}[mc]?"

        menu partychoice_0:
            "Sure why not":
                $ partychoice_0 = True
                jn "{cps=25}Yay!"
                jk "{cps=25}The more the merrier!"
                lg "{cps=25}You finally made the right choice once in your little life."

            "Sorry... I have a work to do":
                $ partychoice_0 = False
                show laura neutral at left with dissolve
                show jake tired with dissolve
                jn "{cps=25}Aww... It's okay"
                jk "{cps=25}Bummer..."
                lg "{cps=25}You should really rethink your life choices"
                mc "{cps=25}Sorry guys... I have work to attend to"
                "{cps=25}(You left ahead to go to work)"
                stop music fadeout 0.5
                jump midnight_0

        jn "{cps=25}Guys... Thank you so much!"
        lg "{cps=25}Pfft small thing"
        jn "{cps=25}So I'll meet you all in the evening at Lucas's house?"
        jn "{cps=25}And surely don't be late!"
        jk "{cps=25}Yeah! Expect me there before everyone else."
        lg "{cps=25}Well, I'm never late"
        stop music
        if late:
            "(Everyone stares at you)"
            menu:
                "Why are you guys staring at me?":
                    lg "{cps=25}Duh... you're the only one who's always late"
                "That was only for today! It'll be the last time!":
                    lg "{cps=25}Yeah sure Dofus"

        if canteen0:
            jk "{cps=25}I need to go home get and prepare for the evening"
            jk "{cps=25}Sayonara"
            hide jake with fade
            "(Jake Left)"
            show laura neutral at left with dissolve
            lg "{cps=25}Yeah me too... {p}let's go home together Jenny?"
            jn "{cps=25}I think I'll pass for now Laura"
            lg "{cps=25}Okay sure, see you later?"
            jn "{cps=25}Lateeer"
            hide laura at left with fade
            "(Laura Left)"
            jn "{cps=25}Uhm... [mc]?"
            "{cps=25}Can you uhm... {p}come with me to the signing event?"
            "Please..."
            "{cps=25}Lucas isn't done at the office yet..."
            "{cps=25}and I don't think I can handle a crowd on my own"
            menu:
                "Yeah sure, I can come with you":
                    jn "{cps=25}Yay! I owe a you alot"
                    jn "{cps=25}Let's go"
                    "(You and Jenny headed out)"
                    jump fansign_0

                "Sorry I'll pass":
                    mc "{cps=25}I need to prepare for the evening"
                    jn "{cps=25}Oh... okay sorry for if I botherd you"
                    jn "{cps=25}See you later, don't be late!"
                    jn "{cps=25}Take care on your way home"
                    "(You went home to prepare for the evening)"
                    jump evening_0

        else:
            jn "{cps=25}Anyways I'll be heading out to the signing event now {p}see you guys later"
            jump evening_0

        label fansign_0:
            scene black
            with fade
            "(You accompanied Jenny in the Fan sign event)"
            call uc
            jump evening_0

    label evening_0:
        scene black
        with dissolve
        centered "{color=#FFF}Evening{/color}" with fade
        scene mansion entrance with dissolve
        show laura neutral at left with moveinleft
        lg "{cps=25}Wow... I really thought you would be late"
        show jake happy at right with moveinright
        jk "{cps=25}My boy [mc] turning a new leaf"
        menu:
            "Why would I be late?":
                lg "{cps=25}Uhm... duh? you are kinda late sometimes"
            "I'm never late, you guys are just too early":
                show jake smiling at right with dissolve
                jk "{cps=25}MAH MEN!"
                lg "{cps=25}Pfft... boys will be boys..."

        #show Jenny in formal
        jn "{cps=25}You guys really came!"
        show laura surprised at left with dissolve
        lg "{cps=25}Why wouldn't we be?"
        jk "{cps=25}Wow look at this young lady..."
        jk "{cps=25}Looking good"
        scene mansion entrance with dissolve
        uk "{cps=25}I know right that's what I've been trying to tell her"
        show lucas happy with dissolve
        ln "{cps=25}Hey guys,"
        hide lucas
        show jake happy at left with moveinleft
        jk "{cps=25}Yo Lucas"
        show laura neutral with dissolve
        lg "{cps=25}Hey"
        show lucas happy at right with moveinright
        ln "{cps=25}Jenny was excitedly waiting for you guys to come right Jenny?"
        #show jenny
        jn "{cps=25}Lucaaaas!"
        ln "{cps=25}Alright alright, calm down love"
        ln "{cps=25}*chuckles*"
        show lucas neutral at right with dissolve
        ln "{cps=25}Oh yeah of course... {p}Where are my manners?"
        ln "{cps=25}You guys, {p}please do come in"
        scene black
        with fade
        "(You and the gang went inside)"
        scene lobby with dissolve
        show jake smiling with dissolve
        jk "{cps=25}Woah! such a huge house"
        hide jake with dissolve
        show laura surprised with dissolve
        lg "{cps=25}Wow very... {p}luxurious"
        hide laura with dissolve
        show lucas happy at center with dissolve
        ln "{cps=25}Thank you for the compliments appreciate it"
        ln "{cps=25}So uhm... {p}We have drinks at the bar, and food being serve from the kitchen"
        ln "{cps=25}We also have a pool in the side and a garden"
        ln "{cps=25}Feel free to roam around except for the bedrooms..."
        ln "{cps=25}They are out of bounds"
        show lucas neutral at center with dissolve
        ln "{cps=25}Hmm..."
        ln "{cps=25}I'm sorry guys I won't be the one accompanying you tonight"
        ln "{cps=25}My love?"
        show lucas neutral at right with moveinleft
        jn "{cps=25}Hmm yes?"
        ln "{cps=25}I'll be heading out to to greet our other guests"
        ln "{cps=25}Can you accompany our guests?"
        jn "{cps=25}Gladly! {p}Go on..."
        jn "{cps=25}We'll be around the house"
        ln "{cps=25}Okay love..."
        show lucas happy at right with dissolve
        ln "{cps=25}Guys ask me if you need help for anything I'll be at the bar attending our guests a drink"
        ln "{cps=25}Please do enjoy the party"
        hide lucas with fade
        "(Lucas left)"
        jn "{cps=25}So... uhm... {p}Who wants a tour?"
        show jake smiling with vpunch
        jk "{cps=25}Aye!"
        show laura chuckle at right with vpunch
        lg "{cps=25}Mee!"
        menu:
            "I think I'll stay here for a while":
                show laura neutral at right with dissolve
                show jake happy with dissolve
                jn "{cps=25}Okay, uhm try not to... {p}get lost"
                jn "{cps=25}You can follow us if you want"
                jump stay_0

            "I'll go with you guys":
                jn "{cps=25}Okaay guys, try not to get lost"
                jump tour_0

        label stay_0:
            "(You stayed in the lobby)"
            scene black
            with fade
            "(You observed the people from the party for a while)"
            centered "{color=#cc6600}{cps=25}Perception++{/color}"
            $ perception += 10
            "Observing you're trying to figure out peoples life style and social status this increases your perception"
            "Perception: The higher your perception skill is the more you see about the others personality"
            "(Short time passes by)"
            scene lobby with dissolve
            uk "{cps=25}Does observing people leads you to satisfaction? {p}Or does it make it you a creep?"
            "(You look at the person beside you)"
            show justine neutral with dissolve
            jr "{cps=25}My conclusion... {p}Most people only see whats on the surface and ignores to understand the person's action deeply"
            jr "{cps=25}Hence being called... {p}\"A creep\""
            menu:
                "You're Justine Raymond":
                    jr "{cps=25}I never took you for a type who listens on what's going on in School"
                    mc "{cps=25}I am aware, but I don't bother caring what rumors go around school"
                    jr "{cps=25}Good"

                "I'm not a creep":
                    mc "{cps=25}Between us, I'm not the creep here"
                    jr "{cps=25}Well I'm not the one whose observing people judging them from their social status am I?"
                    mc "{cps=25}Fair point"

                "Leave me alone":
                    jr "{cps=25}If you insist..."
                    jump solo_0

            mc "{cps=25}So what do you want?"
            jr "{cps=25}Nothing... {p}For now"
            mc "{cps=25}You're being shady"
            jr "{cps=25}Maybe..."
            mc "{cps=25}I wonder why you're here?"
            jr "{cps=25}I feel like you're asking me if I let myself in without getting invited {p}The answer is no"
            jr "{cps=25}I am not a friend of Jenny's but I am a friend of the owner"
            jr "{cps=25}You seem to keep your guard up, a suspcicion that's no stranger to me"
            jr "{cps=25}An action that I see as a proper response to me {p}but I came tell you one thing..."
            jump solo_0

        label solo_0:
            "(Lucas intervenes with the conversation up)"
            show lucas neutral at left with moveinleft
            ln "{cps=25}Hey [mc], I see you met my friend Justine..."
            ln "{cps=25}Hmm..."
            ln "{cps=25}What's wrong?"
            mc "{cps=25}Nothing"
            show justine neutral at right with moveinleft
            jr "{cps=25}I'm going to get a drink"
            scene lobby with dissolve
            show justine neutral with dissolve
            "(Justine walked towards you and whispered)"
            jr "{cps=25}{i}{color=#9e1a03}{size=-10}There are people you should stay away from...{/size}{/color}{/i}"
            hide justine with fade
            "(Justine left)"
            show lucas neutral with dissolve
            ln "{cps=25}Sorry for my friend, he's being weird sometimes"
            if canteen0 == False:
                ln "{cps=25}Also, [mc] Jake's been looking for you in the living room"
                $ findjake = True
            else:
                ln "{cps=25}Oh yeah I've been looking for you"
                mc "{cps=25}What's up?"
                ln "{cps=25}Came to tell you we have a bar here with drinks of different kind"
                ln "{cps=25}Even unique ones"
                ln "{cps=25}You should check it out"
                ln "{cps=25}You could find me there and Jake's also drinking in the Living room"
            mc "{cps=25}Thanks Lucas I'll head there later"
            hide lucas with fade
            "(Lucas left)"
            "(You stayed for a while thinking about what Justine whispered)"
            jump lobby

        label tour_0:
            call uc
            jump lobby

        label jaketalk_0:
            #Living room
            #show Jake drunk with drink
            menu:
                "Getting yourself hammered?":
                    hide jake with dissolve
                    show jake happy with dissolve
                    jk "{cps=25}Oh why yes! {p}and why the hell not!"

                "You're looking for me?":
                    hide jake with dissolve
                    show jake smiling with dissolve
                    jk "{cps=25}Ahh... yes I remember"

                "You okay?":
                    hide jake with dissolve
                    show jake smiling with dissolve
                    jk "{cps=25}Why would I not be!"
                    jk "{cps=25}Pfft... I am perfectly fine.."

            jk "{cps=25}Been lookin all over for yaa!"
            jk "{cps=25}Where you've been?"
            jk "{cps=25}Anywayz,Thiss iz some good stuuf..."
            jk "{cps=25}Stuf... like a happy pill"
            show jake nervous with dissolve
            jk "{cps=25}Heh... can't even drink in the house"
            jk "{cps=25}You know... people always tell me things that I couldn't do..."
            show jake tired with dissolve
            jk "{cps=25}\"Jake you can't do that\" \"Jake can't do this\""
            show jake nervous with dissolve
            jk "{cps=25}Sick and tired of them man..."
            jk "{cps=25}You know man..."
            jk "{cps=25}I always get compared to Jenny"
            jk "{cps=25}I'm tired of \"You should be like Jenny\""
            jk "{cps=25}or... \"Jenny can do this why can't you?\""
            jk "{cps=25}It's not that I hate Jenny"
            show jake tired with dissolve
            jk "{cps=25}I am just tired of expectations..."
            jk "{cps=25}That's why... I run away from them you know..."
            jk "{cps=25}Expectations... I always do the opposite"
            jk "{cps=25}It's what they believe I'm good at..."
            jk "{cps=25}\"Making things worst\""
            menu:
                "You should listen to them, be more responsible":
                    show jake nervous with dissolve
                    jk "{cps=25}Man... FUCK... YOU"
                    jk "{cps=25}Get out of my fucking sight"
                    jk "{cps=25}Before I beat the shit out of you"
                    $ jaketalk_0 = False
                    $ jakeoffend_0 = True
                    jump living_room
                "It's okay":
                    mc "{cps=25}It happens... we all have someone expecting something from us"
                    mc "{cps=25}Like the way you guys expect me not to be late"
                    if late:
                        show jake happy with dissolve
                        jk "{cps=25}But you... are late..."
                        mc "{cps=25}That's not the point"
                    show jake nervous with dissolve
                    mc "{cps=25}The point is it's okay... if you let them down..."
                    mc "{cps=25}What's important is.."
                    mc "{cps=25}you're trying your best"
                    mc "{cps=25}And thats what matters"
                    mc "{cps=25}You're going to be alright"
                    show jake happy with dissolve
                    jk "{cps=25}Thanks... I really needed that"
                    jk "{cps=25}You really always got my back"
                    jk "{cps=25}You're real solid you know that?"
                    jk "{cps=25}Thank you..."
            jk "{cps=25}Wow..."
            jk "{cps=25}This stuf... is really something..."
            jk "{cps=25}Really takes off the weight out of my chest"
            jk "{cps=25}I feel like you got somewhere else to be"
            jk "{cps=25}And..."
            jk "{cps=25}I really need some time alone with this... {p}drink"
            $ jaketalk_0 = False
            "(You left)"
            jump living_room

    label midnight_0:
        scene black
        with dissolve
        play music "/audio/midnight_0.mp3"
        if partychoice_0 == False:
            centered "{color=#FFF}Evening{/color}" with fade
            "(You spend your evening working)"
        centered "{color=#FFF}Night{/color}" with fade
        scene home evening
        with dissolve
        mc "{cps=25}Crap {p} *ughh*"
        mc "{cps=25}I can't feel my body anymore... "
        "(You lay in the bed)"
        mc "{cps=25}I wonder if they had fun and went home safely"
        mc "{cps=25}I feel...{p} Weird about it..."
        mc "{cps=25}Maybe I'm just being paranoid..."
        mc "{cps=25}I should take a rest..."
        stop music fadeout 0.5
        return
