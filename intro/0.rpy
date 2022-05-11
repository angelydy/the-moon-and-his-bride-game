label day_0:

    label morning_0:

        label intro_0:
            scene black
            centered "{color=#cc6600}Morning{/color}"
            scene player_bedroom day with dissolve
            #alarm sound effect
            mc """
            {cps=25}Hnngh...
            {cps=25}It's morning already...
            """
            "{cps=25}(You will be given a choice. What you choose from here on out affects the outcome of the game)"

        menu late_0:
            "What should I do first"
            "Take a Bath":
                $ late = False
                jump bath_0

            "Eat my breakfast":
                $ late = True
                jump breakfast_0

        label bath_0:
            #scene bath
            #bath sound effect
            """
            {cps=25}My name is [mc]
            {cps=25}I am a just your typical simple person {p}trying to get by through college
            {cps=25}I study in the morning till afternoon
            {cps=25}and during evening I work as a part timer to get by from my day to day bills
            """
            mc "{cps=25}Done! {p}I still have a... few more time"
            jump news_0

        label breakfast_0:
            #scene breakfast
            #eating sound effect
            """
            {cps=25}My name is [mc]
            {cps=25}I am a just your typical simple person {p}trying to get by through college
            {cps=25}I study in the morning till afternoon
            {cps=25}and during evening I work as a part timer to get by from my day to day bills
            """
            mc "{cps=25}Done, {p}I still have a... little bit of time"
            jump news_0

        label news_0:
            mc """
            {cps=25}Hmm... I feel like checking the news today before I go
            {cps=25}Just checking wouldn't hurt....
            {cps=25}Hmm... I wonder what's on the News today
            """
            "*Opens the TV*"
            #scene tv
            "Broadcaster" "{cps=25}Breaking News!{p} There seems to be an upcoming Blue Moon this week..."
            "Broadcaster" "{cps=25}We all know that Blue Moon only occurs every 33 months, 41 times per century or about every 19 years.
            Tell us your thought about this..."
            "NASA Scientist" "{cps=25}Blue moon are second full moon in a month, it happens to be blue because of the Earth's atmosphere
            containing dust or smoke particles of a certain size"
            "NASA Scientist" "{cps=25}It is theorized that the blue moon will occur this upcoming sunday"
            "*You turned off the TV*"
            mc "{cps=25}Hmm... {p}Nice, I hope there's going to be a blue moon this month so I can invite the gang"
            if late:
                mc "{cps=25}Shit! {p}I'm late"
            else:
                mc "{cps=25}I should probably leave or I'm going to be late for school"

        label school_0:

            if late:
                #scene school classroom
                with vpunch
                "?" "{cps=25}YOU'RE LATE!"
                "You looked at where the voice came from"
                #show Laura angry
                "?" "{cps=25}How many times do I need to tell you not to be late! {p}Since we're a team, our professor will gave us a minus!"
                "{cps=25}This is Laura Godfrey. {p}She's like a living speaker, who always says what's on her mind but she's a responsible student
                and quite a famous person around the school"
                "{cps=25}She's totally hooked up into social medias and when it comes to listening to humors... {p}She's always up to date"
                #show Jenny worried
                "?" "{cps=25}Laura... {p}Uhm... please don't scold [mc] {p}I'm sure that [mc] tried his best {p}Right [mc]?"
                """
                {cps=25}This is Jenny Williams, {p}She's always sweet, kind, caring and very thoughtful person. She's like a motherly figure
                towards her friends
                {cps=25}She's also a writer {p}She wrote the best selling book of the year and became an award winning author
                {cps=25}Laura, Jenny and me are child hood friends. {p}We grew up together{p}constantly making fun of each other
                {cps=25}But Laura and Jenny are more close to each other. They're like mother and her child
                """

            else:
                #scene school entrance
                #Birds Sound effect
                "?" "{cps=25}[mc] ver here!"
                "You looked at where the voice came from"
                #show Jenny amazed
                "?" "{cps=25}You came!"
                "{cps=25}This is Jenny Williams, {p}She's always sweet, kind, caring and very thoughtful person. She's like a motherly figure
                towards her friends"
                "{cps=25}She's also a writer, who wrote the best selling book of the year"
                "?" "{cps=25}Hey DOFUS! {p}I really thought you would come late!"
                #show Laura surprised
                "{cps=25}This is Laura Godfrey. {p}She's like a living speaker, who always says what's on her mind but she's a responsible student
                and quite a famous person around the school"
                "{cps=25}She's totally hooked up into social medias and when it comes to listening to humors... {p}She's always up to date"
                #show Jenny
                jn "{cps=25}Laura... that's really ruuude {p}[mc] really tried his best to come early! {p}Right [mc]?"
                mc "{cps=25}Yeah, I did... It's early in the morning Laura and you're yelling already {p}Give the birds a break for godsake"
                lg "{cps=25}Want to die early morning?"
                "{cps=25}Laura, Jenny and me are child hood friends. {p}We grew up together constantly making fun of each other"
                "{cps=25}But Laura and Jenny are more close to each other. They're bestfriends for a long a time"
                #bellring sound effect
                jn "{cps=25}Continue your fight later. {p}We should head to the class"

                with vpunch
                #show Jenny neutral
                #show Laura neutral
                #show Jake Happy
                "?" "YOOOO! {p}[mc]"
                #show Jake smiling
                "?" "{cps=25}Our professor isn't here yet. {p}Bet he botched his early class to smoke..."
                "?" "{cps=25}You.. me... Laura... and Jenny. {p}We could head to the canteen"
                "{cps=25}This is Jake {p}Jenny's Cousin, he's similar to Laura but different at the same time {p}They're both Loud bu the only difference is that Jake is irresponsible so that's another reason why Laura and Jake doesn't get along"
                #show Jenny concerned
                jn "{cps=25}But... Isn't that wrong?"
                #show Jake bragging
                jk "{cps=25}Well.. {p}It isn't cutting classes when there's no classes right?"
                #show Laura pissed
                lg "{cps=25}Shut up jake. {p}Don't listen to him Jenny or you'll end up in the guidance"
                jk "{cps=25}Sheesh... {p}You need to loosen up once in a while Laura, {p}Can't have fun when you can't take a risk right Jenny?"
                jn "{cps=25}I don't know..."
                jk "{cps=25}We won't take long"
                "{cps=25}The main reason why Jake and Laura don't get along is because they're like a devil and angel, influencing Jenny's action"
                jk "{cps=25}Come on... It's not like our professor will suddenly be behind my back"
                #show professor behind jake
                "Professor" "{cps=25}What's is it Mr. Jake Williams? {p}I heard you wanted to go to the canteen"
                #show Jake nervous
                jk "{cps=25}No sir {p}I was... {p}talking about... {p}Thinking about volunteering in the canteen sir!"
                "Professor" "{cps=25}Very well during the afternoon head out to the canteen tell them I sent you to volunteer"
                #show Jenny and Laura chuckles
                "*Jenny and Laura chuckles)"
                "Professor" "{cps=25}Take a sit class. So we can start"
                "(The class proceeds as usual)"
                jump afternoon_0

    label afternoon_0:
        scene black
        centered "{color=#cc6600}Afternoon{/color}"
        #scene classroom afternoon
        lg "{cps=25}Thought the class was never gonna end!!"
        #show Laura angry
        #Show Jenny embarrassed
        lg "{cps=25}GOD...{p}I DON'T KNOW WHY I BOTHERED TO LISTEN"
        lg "{cps=25}For godsake he's just simply READING OUR LESSON!"
        lg "{cps=25}Do you really call that TEACHING?"
        lg "{cps=25}I WOULDN'T!"
        lg "{cps=25}Gosh... listening to Sir made me hungry"
        lg "{cps=25}Jenny let's go to the canteen?"
        jn "{cps=25}Suuure"
        #show Jenny shy
        jn "{cps=25}Uhm... {p}[mc]?"
        jn "{cps=25}Would you like to come with us?"
        mc "{cps=25}I..."
        with vpunch
        jk "{cps=25}YO!{p}[mc]!"
        #Show Jake nervous
        jk "{cps=25}DUDE CAN YOU HELP ME?"
        jk "{cps=25}SIR IS DEAD SERIOUS ABOUT MAKING ME DO COMMUNITY SERVICE IN THE CANTEEN!"
        jk "{cps=25}I'M FREAKING SCARED OF THE OLD CANTEEN LADY..."
        jk "{cps=25}SHE'S LIKE A FREAKING GORILLA!"
        jk "{cps=25}I swear that she would beat me into a pulp if I make mistakes"
        jk "{cps=25}Simply the thought of it makes me shiver..."

        menu jk_jen:
            jk "Can you help me?"
            "Yeah, sure bro, I can help you out":
                $ canteen0 = False
                jump jake_0

            "No, sorry bro, wish I could help":
                $ canteen0 = True
                jump jenny_0

        label jake0:
            #show Jake happy
            jk "{cps=25}YOOOO DUDE THANKS!"
            jk "{cps=25}I OWE YOU BIG!"
            "*Short time passes by while carrying stocks of food to the storage"
            #scene Canteen
            #show Jake tired
            jk "{cps=25}A little bit more..."
            jk "{cps=25}Err... {p}Too heavy..."
            #show Jake nervous
            jk "{cps=25}Help help help help... [mc] HELP!"
            "*You rushed to help Jake who carried a box too heavy for him to carry alone"
            jk "{cps=25}Almost got my back crushed"
            "(You noticed two distinct figure walkin past the crowd)"
            jk "{cps=25}Anyways, we're done here let's head back to Jenny and Laura"
            "You meet up with Jenny and Laura"
            jump afternoon_01

        label jenny_0:
            jk "{cps=25}Aight bro wish me luck..."
            #hide jake
            jn "{cps=25}I kinda feel bad for Jake"
            lg "{cps=25}Well he asked for it..."
            lg "{cps=25}Let's go?"
            "(Time passes by eating together while chatting)"
            "(A random person approached Jenny)"
            #show Lucas happy
            "?" "{cps=25}Hey love"
            "?" "{cps=25}I was just looking for you"
            "?" "{cps=25}Where you've been?"
            jn "{cps=25}I was just hanging out with my friends"
            "?" "{cps=25}I see..."
            "He looked towards you and then glanced at Jenny"
            jn "{cps=25}Oh sorry! {p}[mc] this is Lucas my boyfriend"
            ln "{cps=25}I'm Lucas"
            "He offered a handshake"
            "You and Lucas shook hands"
            ln "{cps=25}So love, I'm going to hold a celeberation party about your great success at the Mansion"
            jn "{cps=25}Can I invite anyone?"
            #show lucas chuckles
            ln "{cps=25}*chuckles*"
            ln "{cps=25}Oh dear, you're really are adorable"
            ln "{cps=25}Ofcourse!"
            ln "{cps=25}You can invite anyone since it's your party"
            "?" "{cps=25}Lucas"
            "?" "{cps=25}Our council advisor is looking for us"
            ln "{cps=25}I got to go love, see you later"
            ln "{cps=25}Nice meeting you [mc]"
            #hide lucas and Justine
            "(They left)"
            lg "{cps=25}Wow... He really loves you doesn't he?"
            "(Justine approaches)"

    label afternoon_01:
        jk "{cps=25}Hmmm..."
        jk "{cps=25}Is that Lucas Norris and Justine Raymond?"
        mc "{cps=25}Who?"
        jk "{cps=25}Lucas and Justine {p}they're like elites here in school"
        #scene Lucas portrait
        lg "{cps=25}Yeah, Lucas Norris {p}He's Jenny's boyfriend"
        #show Jenny blush
        jn "{cps=25}Laura!"
        lg "{cps=25}Whaaat? just saying {p}Anyways..."
        lg "{cps=25}Lucas is a \"people person\" if you ask me which is the reason why he became the president of the student council"
        lg "{cps=25}His very friendly more approachable, thoughtful, confident and very smart"
        lg "{cps=25}Also Lucas's recent project gained world wide attention because of miraculously bringing dead mice back to life although it has other effects on the mice but a great feat nonetheless"
        lg "{cps=25}and Beside Lucas is Justine Raymond {p}He's the council vice president and as smart as Lucas but they're like night and day"
        #scene Justine portrait
        jk "{cps=25}But unlike Lucas he isn't friendly, he always makes sarcastic comments and his mostly known for his cold actions that are driven with logic and reason"
        jk "{cps=25}Sometimes I feel his more like a emotionless robot than a human. I wonder how they get along"
        jk "{cps=25}If I were you I wouldn't even think of approaching Justine..."
        mc "{cps=25}Why?"
        jk "{cps=25}He has this scary reputation that he's dangerous and cunning {p}even delinquents don't want to mess with him"
        lg "{cps=25}I heard a rumor that he's a sadistic maniac who blackmails people"
        jk "{cps=25}Also Justine and Jenny always mostly have a fight with each other"
        #show Jenny sad
        jn "{cps=25}He's a meanie!"
        lg "{cps=25}It's okay I'm here I won't let him get close to you"
        lg "{cps=25}I'll kick his ass real hard to the point he can't poop many years to come"
        jk "{cps=25}Well... I wouldn't be surprised if Justine plans to eliminate Jenny or something"
        with vpunch
        "(Laura kicked Jake's knee)"
        #show Jake hurt
        jk "{cps=25}OW!"
        lg "{cps=25}That's not funny!"
        jk "{cps=25}I was just JOKING!"
        lg "{cps=25}Still not funny"
        menu:
            "Calm down Laura! it's just a joke":
                lg "{cps=25}Still a bad joke"
                jk "{cps=25}See?"
            "Yeah it was a bad joke bro...":
                jk "{cps=25}Aight my bad, my apologies"

        jk "{cps=25}But when it comes to a fight me and [mc] will be by your side Jenny"
        #show Jenny happy
        jn "{cps=25}Thanks guys"

        scene black
        "(Time passes by until the school beng rings)"

        jk "{cps=25}FINALLY! SCHOOL IS OVER!!"
        lg "{cps=25}Hey idiot you're shouting like you won't come to school for tommorow"
        jk "{cps=25}I know, I'm just living my life like the school's about to end"
        jn "{cps=25}Uhm... guys?"
        jn "{cps=25}Remember what Lucas said?"
        jk "{cps=25}Yeah?"
        lg "{cps=25}What about it?"
        jn "{cps=25}I'm kinda awkward with Lucas's guests so..."
        jn "{cps=25}Will you guys come with me in the party?"
        jk "{cps=25}HELL YEAH! Who would decline on that offer, it's Lucas Mansion!"
        lg "{cps=25}Ofcourse dear, especially when you're that cute when asking"
        jn "{cps=25}[mc]?"

        menu partychoice_0:
            "Sure why not":
                $ partychoice_0 = True
                jn "{cps=25}Yay!"
                jk "{cps=25}The more the merrier!"
                lg "{cps=25}You finally did a right choice once in your little life"

            "Sorry... I have a work to do":
                $ partychoice_0 = False
                jn "{cps=25}Aww... It's okay"
                jk "{cps=25}Bummer!"
                lg "{cps=25}You should really rethink your life choices"
                mc "{cps=25}Sorry guys... I need to go home now"
                jump midnight_0

        jn "{cps=25}Guys... Thank you so much!"
        lg "{cps=25}Pfft small thing"
        jn "{cps=25}So I'll meet you all in the evening at Lucas's house?"
        jn "{cps=25}And surely don't be late!"
        jk "{cps=25}Yeah! expect me there before everyone else"
        lg "{cps=25}Well, I'm never late"
        if late:
            "(Everyone stares at you)"
            menu:
                "Why are you guys staring at me?":
                    lg "{cps=25}Duh... you're the only one who's always late"
                "That was only for today! It'll be the last time!":
                    lg "{cps=25}Yeah sure Dofus"

        if canteen0:
            jn """
            {cps=25}Uhm... [mc]?
            {cps=25}Can you uhm... {p}come with me to the signing event?
            Please...
            {cps=25}Lucas isn't done at the office yet...
            {cps=25}and I don't think I can handle a crowd on my own
            """
            menu:
                "Yeah sure, I can come with you":
                    jn "{cps=25}Yay! I owe a you alot"
                    jn "{cps=25}Let's go"
                    "(You and Jenny headed out)"
                    #jump fansign_0
                    jump evening_0

                "Sorry I need to head home":
                    jn "{cps=25}Oh... sorry didn't mean to bother you"
                    jn "{cps=25}Take care on the way home!"
                    "(You went home to prepare for the evening)"
                    jump evening_0

        else:
            jn "{cps=25}Anyways I'll be heading out to the signing event now {p}see you guys later"
            jump evening_0

    label evening_0:
        scene black
        centered "{color=#cc6600}Evening{/color}"

        #Show Laura in Formal
        lg "{cps=25}Wow... I really thought you would be late"
        jk "{cps=25}My boy [mc] turning a new leaf"
        menu:
            "Why would I be late?":
                lg "{cps=25}Uhm... duh? you are kinda late sometimes"
            "I'm never late, you guys are just too early":
                jk "{cps=25}MAH MEN!"
                lg "{cps=25}Pfft... boys will be boys..."
        "You guys really came!"
        #show Jenny in formal
        lg "{cps=25}Why wouldn't we be?"
        jk "{cps=25}Wow look at this young lady..."
        jk "{cps=25}Looking good"
        "?" "{cps=25}I know right that's what I've been trying to tell her"
        #show lucas smile
        ln "{cps=25}Hey guys,"
        jk "{cps=25}Yo Lucas"
        lg "{cps=25}Hey"
        ln "{cps=25}Jenny was excited waiting for you guys to come right Jenny?"
        jn "{cps=25}Lucaaaas!"
        ln "{cps=25}Alright alright, calm down love {p}*chuckles*"
        ln "{cps=25}Oh yeah of course where are my manners?"
        ln "{cps=25}You guys, {p}please do come in"
        "(You and the gang went inside)"
        jk "{cps=25}Woah! such a huge house"
        lg "{cps=25}Wow very... {p}luxurious?"
        ln "{cps=25}Thank you for the compliments appreciate it"
        ln "{cps=25}So uhm... {p}We have drinks at the counter, and food being serve from the kitchen"
        ln "{cps=25}We also have a pool in the side and a garden feel free to roam around except for the bedrooms"
        ln "{cps=25}I'm sorry guys I won't be the one accompanying you tonight"
        ln "{cps=25}My love?"
        jn "{cps=25}Hmm yes?"
        ln "{cps=25}I'll be heading out to to greet our other guests"
        ln "{cps=25}Can you accompany our guess?"
        jn "{cps=25}Gladly {p}Go on we'll here around"
        ln "{cps=25}Okay love, guys ask me if you need help for anything, enjoy the party"
        "(Lucas left)"
        jn "{cps=25}So... who wants a tour?"
        jk "{cps=25}Aye!"
        lg "{cps=25}Mee!"
        menu:
            "I think I'll stay here for a while":
                jn "{cps=25}Okay, uhm try not to {p}get lost"
                jn "{cps=25}You can follow us if you want"
                jump stay_0

            "I'll go with you guys":
                jn "{cps=25}Okaay guys, try not to {p}get lost"
                jump tour_0

        label stay_0:
            "(You stayed in the lobby, observing the people from the party for a while)"
            centered "Perception ++"
            $ perception += 10
            "By observing you're trying to figure out peoples life style and social status"
            "?" "{cps=25}Does observing people leads you to satisfaction? {p}Or does it make it you a creep?"
            "(You at the person beside you)"
            "?" "{cps=25}My conclusion... {p}Most people only see whats on the surface and ignores to understand the persons action deeply"
            "?" "{cps=25}Hence being called... {p}A creep"
            menu:
                "You're Justine Raymond":
                    jr "{cps=25}I never took you for a type who listens on what's going on in School"
                    mc "{cps=25}I am aware, but I don't bother caring"
                    jr "{cps=25}Good"

                "I'm not a creep":
                    mc "{cps=25}Between us, I'm not the creep here"
                    jr "{cps=25}Well I'm not the one observing people identifying them from their social status am I?"
                    mc "{cps=25}Fair point"

                "Leave me alone":
                    jr "{cps=25}If you insist..."
                    jump solo_0

            mc "{cps=25}What do you want?"
            jr "{cps=25}Nothing... {p}For now"
            mc "{cps=25}You sound shady"
            jr "{cps=25}Maybe"
            mc "{cps=25}I wonder why you're here"
            jr "{cps=25}I am not a friend of Jenny's but I am a friend of the owner"
            jr "{cps=25}You're suspicious of me I can tell, a suspcicion that's no stranger to me"
            jr "{cps=25}You're reason to be suspicious of me isn't wrong... {p}but I came tell you one thing..."
            jr "{cps=25}{i}{color=#9e1a03}There are things you should stay away from...{/color}{/i}"

        label tour_0:


    label midnight_0:
        scene black
        if partychoice_0 == False:
            centered "{color=#cc6600}Evening{/color}"
            "(You spend your evening working)"
        centered "{color=#cc6600}Midnight{/color}"
        #scene room
        mc "*ughh...*"
        mc "{cps=25}I can't feel my body anymore... crap"
        "(You lay in the bed)"
        mc """
        {cps=25}I wonder if they had fun and went home safely
        {cps=25}I feel weird
        {cps=25}Meh {p}I'm just being paranoid
        {cps=25}I should take a rest...
        """
