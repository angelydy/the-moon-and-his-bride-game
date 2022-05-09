label intro:

    #To do here

    centered "Morning"
    #alarm sound effect
    mc """
    {cps=25}Hnngh...
    It's morning already...
    """
    "*You will be given a choice. What you choose affects the outcome of the game*"

    menu late:
        "What should I do first"
        "Take a Bath":
            $ late = False
            jump bath
        "Eat my breakfast":
            $ late = True
            jump breakfast

    label bath:
        #scene bath
        #bath sound effect
        mc "{cps=25}Done, {p}I still have a few more time"
        jump news

    label breakfast:
        #scene breakfast
        #eating sound effect
        mc "{cps=25}Done, {p}I still have a little bit of time"

    label news:
        mc "{cps=25}I should check what's on the News today"
        "*Opens the TV*"
        #scene tv
        "Broadcaster" "{cps=25}Breaking News!{p} There seems to be an upcoming Blue Moon this week..."
        "Broadcaster" "{cps=25}We all know that Blue Moon only occurs every 33 months, 41 times per century or about every 19 years.
        Tell us your thought about this..."
        "NASA Scientist" "{cps=25}Blue moon are second full moon in a month, it happens to be blue because of the Earth's atmosphere
        containing dust or smoke particles of a certain size"
        "NASA Scientist" "{cps=25}It is theorized that the blue moon will occur this upcoming sunday"
        "*You turned off the TV*"
        mc "{cps=25}Hmm... {p}I really hope there's going to be a blue moon this month."
        if late:
            mc "{cps=25}Shit... {p}I'm late!"
        else:
            mc "{cps=25}I should probably leave or I'm going to be late for school"
        jump morning0

    label morning0:
        if late:
            #scene school classroom
            with vpunch
            "?""{cps=25}YOU'RE LATE!"
            "You looked at where the voice came from"
            #show Laura angry
            "?" "{cps=25}How many times do I need to tell you not to be late! {p}Since we're a team, our professor will gave us a minus!"
            "{cps=25}This is Laura Godfrey. {p}She's like a living speaker, who always says what's on her mind but she's a responsible student
            and quite a famous person around the school"
            "{cps=25}She's totally hooked up into social medias and when it comes to listening to humors... {p}She's always up to date"
            #show Jenny worried
            "?" "{cps=25}Laura... {p}Uhm... please don't scold [mc] {p}I'm sure that [mc] didn't mean it {p}Right [mc]?"
            "{cps=25}This is Jenny Williams, {p}She's always sweet, kind, caring and very thoughtful person. She's like a motherly figure
            towards her friends"
            "{cps=25}She's also a writer{p}who wrote the best selling book of the year"
            "{cps=25}Laura, Jenny and me are child hood friends. {p}We grew up together{p}constantly making fun of each other"
            "{cps=25}But Laura and Jenny are more close to each other. They're like mother and her child"

        else:
            #scene school entrance
            #Birds Sound effect
            "?" "{cps=25}[mc] over here!"
            "You looked at where the voice came from"
            #show Jenny amazed
            "?" "{cps=25}You came!"
            "{cps=25}This is Jenny Williams, {p}She's always sweet, kind, caring and very thoughtful person. She's like a motherly figure
            towards her friends"
            "{cps=25}She's also a writer, who wrote the best selling book of the year"
            "?" "{cps=25}Hey dofus! {p}I really thought you would come late"
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

        #scene school classroom
        with vpunch
        #show Jenny neutral
        #show Laura neutral
        #show Jake Happy
        "?" "YOOOO! {p}[mc]"
        #show Jake smiling
        "?" "{cps=25}Our professor isn't here yet. {p}Bet he botched his early class to smoke..."
        "?" "{cps=25}You.. me... Laura... and Jenny. {p}We could head to the canteen"
        "{cps=25}This is Jake {p}Jenny's Cousin, he's similar to Laura but very different {p}They're both Loud, the only difference is Jake is irresponsible so that's another reason why Laura and Jake doesn't get along"
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
        jk "{cps=25}No sir {p}I was... {p}talking about... {p}Thinking about volunteering in the canteen sir"
        "Professor" "{cps=25}Very well during the afternoon head out to the canteen tell them I sent you to volunteer"
        #show Jenny and Laura chuckles
        "*Jenny and Laura chuckles*"
        "Professor" "{cps=25}Take a sit class. So we can start"
        "*The class proceeds as usual*"
        jump afternoon0

    label afternoon0:
        scene black
        centered "Afternoon"
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
                jump jake0

            "No, sorry bro, wish I could help":
                $ canteen0 = True
                jump jenny0

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
            "*You noticed two distinct figure walkin past the crowd*"
            jk "{cps=25}Anyways, we're done here let's head back to Jenny and Laura"
            "You meet up with Jenny and Laura"
            jump afternoon05

        label jenny0:
            jk "{cps=25}Aight bro wish me luck..."
            #hide jake
            jn "{cps=25}I kinda feel bad for Jake"
            lg "{cps=25}Well he asked for it..."
            lg "{cps=25}Let's go?"
            "*Time passes by eating together while also chatting"
            "*A random person approached Jenny*"
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
            "They left"
            lg "{cps=25}Wow... he's pretty bold"
            "*Justine approaches*"

    label afternoon05:
        jk "{cps=25}Hmmm..."
        jk "{cps=25}That's Lucas Norris and Justine Raymond"
        mc "{cps=25}Who?"
        jk "{cps=25}Lucas and Justine {p}they're like elites here in school"
        #scene Lucas portrait
        jk "{cps=25}Lucas Norris {p}He's Jenny's boyfriend, a people person if you ask me which is the reason why he became the president of the council"
        jk "{cps=25}His very friendly, thoughtful, confident and very smart"
        jk "{cps=25}Lucas's recent project gained world wide attention because of miraculously bringing dead mice back to life although it has other effects on the mice but a great feat nonetheless"
        jk "{cps=25}Beside Lucas is Justine Raymond {p}He's the council vice president and as smart as Lucas but they're like night and day"
        #scene Justine portrait
        jk "{cps=25}But unlike Lucas he isn't friendly, he always makes sarcastic comments and his mostly known for his cold actions that are driven with logic and reason"
        jk "{cps=25}Sometimes I feel his more like a emotionless robot than a human"
        jk "{cps=25}If I were you I wouldn't even think of approaching Justine..."
        mc "{cps=25}Why?"
        jk "{cps=25}He has this bad reputation that he's dangerously cunning and always scheming"
        jk "{cps=25}I feel bad for Jenny tho... {p}Justine and Jenny always disagree with each other"
        mc "{cps=25}Why tho?"
        jk "{cps=25}I have no idea..."
        jk "{cps=25}I wouldn't be surprised if Justine plans to eliminate Jenny or something"

    scene black
    centered "To be Continued"
    return
