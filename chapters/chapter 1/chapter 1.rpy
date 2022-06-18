label chapter1:
    scene black with dissolve
    centered "{color=#FFF}(Chapter 1: Fits the puzzle){/color}" with fade
    $ energy = 15
    $ day = 3
    $ mall = True
    $ tempday = day
    jump day_cycle

label start_ch1:
    hide screen phone
    th"{cps=25} I should tell what I know to Laura"
    $ e_hallway_ch1.available = True
    return

label school_ch1:
    #School
    hide screen phone
    $ e_hallway_ch1.completed = True
    th"{cps=25} Wolves will howl… Awakened by owl… Look at me, and you’ll stare in awe…"
    th"{cps=25} What could it be? Jenny is missing and this riddle has something to do with her."
    lg"{cps=25} [mc] Any news? You did not attend our afternoon class yesterday. What happened?"
    mc"{cps=25} I went in police station to talk to jake."
    lg"{cps=25} What!? Why?"
    mc"{cps=25} I needed to talk to Jake"
    lg"{cps=25} What happened? What did he say?"
    mc"{cps=25} I talked to jake. He said he’s innocent and he’s asking for help…"
    mc"{cps=25} Laura, Jake needs us. He needs our help."
    mc"{cps=25} This may sound hard as person of logical reason but believe me... He’s innocent."
    lg"{cps=25} But all the evidences are pointing him…"
    mc"{cps=25} Just like you, Jenny is important to me… And I want to know where she is and what really happened to her."
    mc"{cps=25} I want to find the person behind this case and jake is not that person"
    mc"{cps=25} I would not allow an innocent man live their whole life inside the cell while the real culprit is freely breathing outside..."
    mc"{cps=25} It’s not fair."
    lg"{cps=25} Then what do you want me to do?"
    mc"{cps=25} Let’s help jake"
    lg"{cps=25} How?"
    mc"{cps=25} I found this last night in my doorway…"
    lg"{cps=25} What’s this?"
    mc"{cps=25} It’s a letter… a riddle maybe? but look… it says save jenny before it’s too late… It means jenny is still alive…"
    lg"{cps=25} Of course! Who said she’s dead!?"
    mc"{cps=25} That’s not what I mean…"
    mc"{cps=25} Listen, It says save jenny before it is too late..."
    mc"{cps=25} Meaning, something worse might happen to jenny… and the riddle…"
    mc"{cps=25} it has something to do with it…"
    lg"{cps=25} We need to know what does the riddle mean…"
    lg"{cps=25} Then what?"
    mc"{cps=25} I don’t know... At least we have a lead that we can start off"
    lg"{cps=25} Okay… I’ll keep this paper…"
    lg"{cps=25} I’ll head to the library later to research this riddle."
    mc"{cps=25} Okay, you do that… there are things I need to take care first"
    $ e_roam_ch1.available = True
    return

label canteen_ch1:
    $ e_roam_ch1.completed = True
    hide screen phone
    #afternoon
    #Canteen
    th"{cps=25} If Jake was wasted, who fetched him home?"
    th"{cps=25} Let us say, it was Jenny since she left her purse in Jake's room."
    th"{cps=25} But, Jenny does not know how to drive..."
    th"{cps=25} It means can't be her... {p}but who?"
    th"{cps=25} He can be the possible culprit?"
    th"{cps=25} He might be the last person she’s with..."
    th"{cps=25} Why didn’t I think of that sooner?"
    "(You see Lucas seating)"
    mc"{cps=25} Hmm, Lucas? Why are you here?"
    ln"{cps=25} …"
    ln"{cps=25} Oh hey [mc], nothing…"
    ln"{cps=25} It’s funny how I feel that I would see Jenny here…"
    ln"{cps=25} Since you guys’ mostly hangout here… You, Laura and Jake..."
    ln"{cps=25} It’s just sad it happened so fast I saw her before the party but the next day… gone"
    mc"{cps=25} We are also desperate to know where she is and what happened to her…"
    ln"{cps=25} I already employed some of the best private investigators to look for her but… to no luck"
    ln"{cps=25} I don’t know what I will do without her…"
    ln"{cps=25} You know how much I love her… I would tear down the whole world if I needed to, just to bring her back to me"
    ln"{cps=25} I don’t know what I can do to Jake if something bad happened to my Jenny…"
    mc"{cps=25} Are you sure it is jake?"
    ln"{cps=25} He’s the primary suspect… evidences are pointing at him…"
    mc"{cps=25} What if it is not him?"
    ln"{cps=25} Who else it can be? He’s the closest person that can possibly do that…"
    ln"{cps=25} Besides it was him who influenced Jenny to be… that way"
    mc"{cps=25} What do you mean?"
    ln"{cps=25} …"
    ln"{cps=25} Nothing…"
    mc"{cps=25} Hmm… but as you said Jake is the primary suspect… it also means his not guilty unless proven… At least not yet…"
    ln"{cps=25} All I want is to bring my Jenny back…"
    mc"{cps=25} Everything will be fine, Lucas…"
    ln"{cps=25} I hope so…"
    ln"{cps=25} I need to go"
    mc"{cps=25} Where are you going?"
    ln"{cps=25} To her favorite place… National Library, maybe I can find something that can lead me to her"
    mc"{cps=25} Hopefully…"
    ln"{cps=25} Talk to me when you find something"
    mc"{cps=25} Sure…"
    scene black with dissolve
    th"{cps=25} Where are they could be hiding you, Jenny? Everyone misses you now…"
    $ e_class_ch1.available = True
    return

label classroom_ch1:
    $ e_class_ch1.completed = True
    hide screen phone
    #Classroom
    mc"{cps=25} So, what did you found out?"
    lg"{cps=25} Tss.."
    lg"{cps=25} I was preoccupied by this riddle to the point that I even bought books about riddles instead of books for our research…"
    lg"{cps=25} Ugh… I will surely cut off jenny’s hair if I fail this subject…"
    lg"{cps=25} If it wasn’t for her... Tss…"
    "{color=#ffffff}Professor{/color}" "{cps=25} Yes, Miss Laura? You’re saying something?"
    lg"{cps=25} No, Sir… Sorry…"
    mc"{cps=25} Let’s just talk later…"
    return

label home_ch1:
    #show only if e_class_ch1 complete
    $ e_class_ch1.triggered = True
    hide screen phone
    mc"{cps=25} Let’s check out today’s news"
    #Turn on TV
    #NASA news
    "{color=#ffffff}Reporter{/color}" "{cps=25} The upcoming Blue Moon will crest this coming weekend."
    "{color=#ffffff}Reporter{/color}" "{cps=25} By lucky coincidence, the moon will be near the planet again!"
    #Phone rings
    mc"{cps=25} Hello?"
    lg"{cps=25} Blue Moon"
    mc"{cps=25} Laura?"
    lg"{cps=25} It is Blue Moon."
    mc"{cps=25} Yeah... I heard in the news..."
    lg"{cps=25} The answer in the riddle is Blue Moon…"
    lg"{cps=25} Wolves in movies are howling during Blue Moon..."
    lg"{cps=25} The owls are awake during the full moon and to top it all everyone is waiting for the Blue Moon..."
    lg"{cps=25} Everyone wants to see the blue moon."
    lg"{cps=25} In the riddle… It says, look at me and you’ll stare in awe… It is the blue moon [mc]"
    mc"{cps=25} Does it mean we have to save jenny before blue moon?"
    lg"{cps=25} And we only have plenty of time... What should we do?"
    mc"{cps=25} I’ll think of something…"
    mc"{cps=25} Let’s talk tomorrow personally…"
    lg"{cps=25} Okay... I’ll be here if you need me"

    th"{cps=25} Shit… I never thought of the day of blue moon to be like this…"
    th"{cps=25} It supposed to be the day we’re going to have fun…"
    th"{cps=25} But instead, Jenny’s missing and Jake is detained."
    th"{cps=25} Who ever is behind this I’ll make them pay."
    $ e_hallway2_ch1.available = True
    return

label hallway_ch1:
    $ e_hallway2_ch1.completed = True
    hide screen phone
    #Next day…
    #Hallway Morning
    lg"{cps=25} So, what’s the plan?"
    mc"{cps=25} We have to help jake first..."
    mc"{cps=25} He might remember something that can help us and its better if he’s with us in case we got into trouble."
    lg"{cps=25} But how?"
    mc"{cps=25} We have to gather evidences that will prove he’s innocent."
    mc"{cps=25} Hmm… Jenny was last seen in the party"
    mc"{cps=25} If I remember correctly there are CCTVs in Lucas’s house, right?"
    #show cctv image
    mc"{cps=25} We could use that…"
    #hide cctv pause
    lg"{cps=25} Hmm, the authorities said the footages are gone"
    mc"{cps=25} That’s weird…"
    mc"{cps=25} I feel there’s something going on…"
    mc"{cps=25} I am planning to go to Lucas’s house to check"
    lg"{cps=25} Okay, tell me if you find anything regarding the CCTV…"
    $ cctv_ch1.available = True
    $ tweet_ch1.available = True
    return

label library_ch1:
    $ tweet_ch1.completed = True
    hide screen phone
    #Library Afternoon
    lg"{cps=25} Let us start gathering information about the party"
    lg"{cps=25} Ugh! I shouldn’t have gone early..."
    lg"{cps=25} If I just know that this will happen…"
    mc"{cps=25} It’s not your fault..."
    mc"{cps=25} What are you doing?"
    lg"{cps=25} Scrolling in my feed..."
    mc"{cps=25} At this time?"
    lg"{cps=25} I’m trying to gather information about what happened in the party..."
    lg"{cps=25} For sure, anyone posted status during the party…"
    lg"{cps=25} LOOK!"
    mc"{cps=25} Shh! lower your voice…"
    lg"{cps=25} What is it?"
    lg"{cps=25} There are lots of tweet about Jake’s issue regarding Jenny’s sudden loss."
    lg"{cps=25} Here!"
    lg"{cps=25} It says..."
    lg"{cps=25} “I knew it was Jake! he was hammered in the party and he’s bugging Jenny.“"
    lg"{cps=25} Here are the replies…"
    lg"{cps=25} “I saw it too… and jenny tried to avoid Jake”"
    lg"{cps=25} “I don’t think it is Jake... {p}I think it is Justine... {p}My camera caught him and Jenny together before dissappearing”"
    mc"{cps=25} Who is it?"
    lg"{cps=25} A random user."
    mc"{cps=25} Do you think we can get a copy from him?"
    lg"{cps=25} I’ll try…"
    lg"{cps=25} Oh, I know him... He’s a member of English club"
    lg"{cps=25} I remember the English club have meeting every afternoon"
    lg"{cps=25} Maybe we could find him"
    mc"{cps=25} Let’s go then…"
    $ e_tweet_ch1.available = True
    return

label checkHouse_ch1:
    #after checking the Lucas House
    hide screen phone
    #school
    #Hallway Morning
    lg"{cps=25} How did it went?"
    mc"{cps=25} No luck, couldn’t get past the police or the guards"
    lg"{cps=25} Hmm… you could ask Lucas"
    mc"{cps=25} I don’t know where Lucas is, he’s nowhere to be found."
    lg"{cps=25} I’ll ask around where Lucas is… or you can think of another way to get in"
    mc"{cps=25} I know a way, but we will need Jake."
    lg"{cps=25} I’ll call you when I got info about where Lucas is"
    return

label f2hallway_ch1:
    $ e_tweet_ch1.completed = True
    hide screen phone
    lg"{cps=25} Isn’t that Justine?"
    mc"{cps=25} Hmm… I think so why?"
    lg"{cps=25} He’s in the party right?"
    mc"{cps=25} Yeah, I remember…"
    lg"{cps=25} Maybe we can ask him"
    mc"{cps=25} Hey Justine"
    jr"{cps=25} …"
    lg"{cps=25} Do you know what happened in the party?"
    jr"{cps=25} Not everything…"
    lg"{cps=25} Do you know anything about what happened to Jenny."
    jr"{cps=25} No, I was with Lucas all those time… and are you guys authorities"
    mc"{cps=25} No…"
    jr"{cps=25} Figures, then I have nothing to tell you about."
    lg"{cps=25} Wow! We are just concern here trying to find our friend and if you don’t want to help us you can shove this book right in your ass!"
    jr"{cps=25} Hmm? Are you using threats? Not effective"
    mc"{cps=25} Laura, we should leave..."
    scene black with dissolve
    "(You and Laura left Justine be)"
    scene hallway afternoon with dissolve
    lg"{cps=25} Why did you stopped me?"
    mc"{cps=25} I know you’re worried and panicking but you shouldn’t lose your cool like that"
    lg"{cps=25} How could I? I bet he knows something and that’s why he’s keeping his mouth shut"
    mc"{cps=25} Maybe… But we don’t know that"
    lg"{cps=25} *sigh* Sorry…"
    mc"{cps=25} It’s alright…"
    lg"{cps=25} Thank you"
    mc"{cps=25} For what?"
    lg"{cps=25} Bringing me back to my senses"
    mc"{cps=25} Small thing, don’t mention it"
    mc"{cps=25} Let’s focus on what we’re here for"
    lg"{cps=25} Right! The club room should be along the way here"
    mc"{cps=25} Let’s go"
    scene black with dissolve
    "(You knock at the door)"
    scene club_room with dissolve
    lg"{cps=25} Hello, everyone! Is Ms. Buenaventura here?"
    uk"{cps=25} Looking for me?"
    lg"{cps=25} Hey, sorry for disturbing your club meeting"
    lg"{cps=25} Can I talk to you? {p}In private"
    lg"{cps=25} Just an important matter"
    "{color=#ffffff}Ms. Buenaventura{/color}" "{cps=25}Sure…"
    lg"{cps=25} [mc] you can wait for me outside"
    scene black with dissolve
    "(You waited for Laura)"
    scene hallway afternoon with dissolve
    mc"{cps=25} What did she said?"
    lg"{cps=25} She said that it can really be Jake…"
    mc"{cps=25} Why?"
    lg"{cps=25} She think she saw Justine with jenny in the party…"
    lg"{cps=25} Then she said, Justine likes Jenny…"
    mc"{cps=25} Hmm… that’s not what I expected… but okay… continue"
    lg"{cps=25} After that Jenny went towards Jake for whatever reason… then later on, Jenny was gone… That’s what she saw..."
    mc"{cps=25} I feel this story can’t be true… knowing Justine and Jenny's history... Then there’s Justine personality…"
    mc"{cps=25} Can you show me the proof?"
    lg"{cps=25} Sorry, she hasn’t sent the proof yet"
    lg"{cps=25} But I’ll show you when I got it"
    mc"{cps=25} Sure…"
    mc"{cps=25} Let’s call it a day"
    $ cafe_ch1.available = True
    return

label homeevening_ch1:
    $ cafe_ch1.completed = True
    hide screen phone
    #Home
    mc"{cps=25} Life sucks big time, I hope Jenny’s fine."
    "(*Phone vibrates*)"
    mc"{cps=25} Hmm?"
    "{color=#ffffff}Message received{/color}" "{cps=2} Laura: I got it! Let’s    meet tomorrow at the café in the afternoon"
    mc"{cps=25} *Exhales* I hope she has good news…"
    scene black with dissovlve
    "(You went to sleep)"
    $ e_cafe_ch1.available = True
    return

label cafe_ch1:
    $ e_cafe_ch1.completed = True
    hide screen phone
    #Café
    lg"{cps=25} Here look at the video! It’s kind of blurry but the video also recorded Jake near the bar"
    lg"{cps=25} You can also see Jenny and Jake talking"
    lg"{cps=25} Justine approached Jenny, the conversation is inaudible"
    lg"{cps=25} Jenny went with Justine {p} They’re talking in private..."
    lg"{cps=25} Until Justine noticed someone’s recording them so he closed the door."
    lg"{cps=25} Ms. Buenaventura also said Jenny disappeared during that time."
    th"{cps=25} Based on the video Jake seems to be hammered but still conscious…"
    th"{cps=25} So, it’s true that Jake talked to Jenny"
    th"{cps=25} Jenny then talked to Justine in private before she disappeared…"
    th"{cps=25} Hmm… Justine…"
    lg"{cps=25} What do you think?"
    mc"{cps=25} What I think is..."
    mc"{cps=25} Justine was last person in contact with Jenny before she disappeared…"
    lg"{cps=25} What about Jake?"
    mc"{cps=25} Based on what Jake told me that during the party the last thing he remembers before moments of blacking out is Jenny walking out with someone"
    lg"{cps=25} So, Justine has higher chance of being a primary suspect than Jake?"
    mc"{cps=25} I think so…"
    mc"{cps=25} How come the authorities doesn’t know this?"
    lg"{cps=25} What Mrs. Buenaventura said, she lay low after what happened… she’s afraid of what can Justine do to her"
    mc"{cps=25} Hmm…"
    mc"{cps=25} Can we use this to help Jake?"
    lg"{cps=25} It finally makes sense… Let’s go to the station and surrender this."
    #Obtain evidence item in inventory
    $ evidence_ch1.available = True
    return

label homeevening2_ch1:
    #execute after evidence was pass
    #should show after 2 days passed
    hide screen phone
    #Home
    th"{cps=25} It’s been a long day… I hope Jake gets out."
    th"{cps=25} In the meantime, I should do something to get that CCTV footage"
    $ raid_ch1.available = True
    return

label canteen2_ch1:
    $ raid_ch1.completed = True
    hide screen phone
    #School Canteen
    lg"{cps=25} I haven’t seen Jake out yet"
    mc"{cps=25} Should I go visit him?"
    jk"{cps=25} You don’t have to I’m here."
    mc"{cps=25} Jake!! How come you’re here?"
    jk"{cps=25} They let me out thanks to you guys"
    jk"{cps=25} Because of the evidence you presented to the authorities they let me go"
    jk"{cps=25} But I haven’t escaped the list of suspects just yet… so their eyes are still on me."
    jk"{cps=25} Another thing is Justine is now the primary suspect"
    lg"{cps=25} I’m glad you’re out now… Do you need anything?"
    jk"{cps=25} Meh, I’m fine…"
    jk"{cps=25} I just want to finish this and make the culprit pay"
    jk"{cps=25} For what he did to Jenny and by framing me"
    mc"{cps=25} So far, our hunch is Justine"
    mc"{cps=25} She was the last person seen with Jenny during the party…"
    lg"{cps=25} One more… [mc] found a piece of paper containing a riddle creepy riddle."
    lg"{cps=25} Which says “we need to save jenny before blue moon”"
    jk"{cps=25} When is the blue moon?"
    mc"{cps=25} This coming weekend..."
    jk"{cps=25} Shit that day is near!"
    mc"{cps=25} I know we’ running out of time… We need your help on this try to remember"
    lg"{cps=25} Here… Do you remember this video?"
    jk"{cps=25} I think I can still remember this…"
    jk"{cps=25} Yeah, if I remember correctly there was someone in there with them… I can’t remember who."
    mc"{cps=25} That’s what we’re about to find out"
    mc"{cps=25} I have a plan; we’re going to break in Lucas’s house"
    lg"{cps=25} Wait! Isn’t that illegal?!"
    jk"{cps=25} ALRIGHT!!!"
    mc"{cps=25} Shh! Idiots keep your voices down!"
    lg"{cps=25} Says the person who shouted"
    mc"{cps=25} Let’s focus, shall we?"
    jk"{cps=25} You got my attention"
    mc"{cps=25} Okay, here’s the plan…"
    mc"{cps=25} Lucas’s house has lot of guards and surrounded by the police"
    mc"{cps=25} Laura will distract the guards"
    mc"{cps=25} Jake will watch my back while I check the security footage"
    jk"{cps=25} Why be the distraction?"
    mc"{cps=25} The police know you"
    lg"{cps=25} Do you want to go back to Jail that badly?"
    jk"{cps=25} Nope, I’m good food there tastes like shit"
    mc"{cps=25} I’ll talk to you guys when I finish the preparations"
    jk"{cps=25} JUST LIKE IN THE SPY MOVIES!!"
    lg"{cps=25} SSHH!!"
    mc"{cps=25} See you guys around"
    $ start_raid_ch1.available = True
    $ start2_raid_ch1.available = True
    #Buy usb
    #Buy ketchup
    return

label jaketalk_ch1:
    #If statement for item
    hide screen phone
    jk"{cps=25} What’s up?"
    mc"{cps=25} We’ll go during the evening let’s meet in Lucas’s House"
    jk"{cps=25} Alright! I’ll be there sharp"
    $ start2_raid_ch1.incProgress()
    #return
    #else
    return

label lauratalk_ch1:
    #If statement for item
    hide screen phone
    lg"{cps=25} Hmm?"
    mc"{cps=25} We’ll go during the evening let’s meet in Lucas’s House"
    lg"{cps=25} Okay this is kind of making me nervous"
    lg"{cps=25} I’ll see you then"
    $ start2_raid_ch1.incProgress()
    #return
    #else
    return
