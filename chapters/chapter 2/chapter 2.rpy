label chapter_2:

  hide screen phone
  mc "{cps=25} There are lots of people in the party… Do you think janitors will recognize jenny?"
  show jake bragging with dissolve
  jk "{cps=25} This specific janitor knows Jenny. I heard he’s the head janitor in Lucas’s mansion."
  jk "{cps=25} And of course, he knows Jenny. She’s Lucas’s girlfriend. I also remember this. I heard him called Jenny. {p}I felt dizzy so I didn’t saw why? The next thing I knew, Jenny was gone from my sight."
  show laura neutral at left with moveinleft
  lg "{cps=25} We still don’t know when was the exact time she was last seen. Jake has a point. Janitors are always the last people to leave the place. Maybe Jenny was in the party until the end.."
  mc "{cps=25} So… are we going to find the janitor?"
  lg "{cps=25} why not? It won’t hurt to take a chance."
  jk "{cps=25} He must be in Lucas’s mansion."
  lg "{cps=25} If we went there… what are we gonna say to Lucas if he asks us? We cannot say that we went there for the janitor."
  mc "{cps=25} Why not?"
  lg "{cps=25} We are not close to him so why would we visit him? And it is better if we don’t tell Lucas about speculating Justine. At least not now… We do not have evidence…"
  jk "{cps=25} I agree with Laura. Lucas might think that I am only putting the blame to Justine"
  mc "{cps=25} So, what’s the plan?"
  lg "{cps=25} Jake… can you talk with Lucas?"
  jk "{cps=25} About what?"
  lg "{cps=25} Explain to him that it isn’t you. He still hopes that it is not really you…"
  jk "{cps=25} I-I’ll try…"
  lg "{cps=25} We can go there and say that we just came with Jake… And once he allowed you… We will leave you two and we’ll find the janitor."
  mc "{cps=25} Lucas’s mansion is huge. How can we find him right away…? Additionally, his mansion is surrounded with CCTV… "
  lg "{cps=25} They have maids around… We can ask them so we can find him... Let’s just hope that the janitor is in the first floor… We will be suspicious if we go to the second floor…"
  mc "{cps=25} What’s on your mind, Jake?"
  jk "{cps=25} I-I’m just thinking of what to tell Lucas when we talk."
  mc "{cps=25} First, let’s go the mall and buy something for Lucas… We can’t go there empty handed…"

#Go to the mall and buy anything~
#Lucas’s House~
#afternoon

  lg "{cps=25} Are we ready?"
  jk "{cps=25} I am.."
  mc "{cps=25} Let’s go… Call Lucas.."
  lg "{cps=25} (get the phone and call lucas) Hey, Lucas! How are you?"
  hide laura
  hide jake
  show lucas neutral with dissolve
  ln "{cps=25} (on the other line) Laura.. Still the same.. All is well.. Why?"
  ln "{cps=25} Where are you?{p} Home?"
  hide lucas 
  show laura neutral at left with dissolve
  show jake happy with dissolve
  lg "{cps=25} We’re outside of your house… Can you come out?"
  hide laura
  hide jake
  show lucas serious with dissolve
  ln "{cps=25} What are you doing there.. Wait for me in the living room…"
  hide lucas
  show laura neutral at left with moveinleft
  show jake happy with dissolve

  "(phone call ended)"

  mc "{cps=25} Let’s go…"
  hide laura neutral with moveoutleft
  hide jake bragging with moveoutright

  #lucas' living room

  show laura neutral at left with moveinleft
  show jake tired at right with moveinright
  lg "{cps=25} Lucas.."
  show lucas angry with moveinright
  ln" {cps=25} What is that son of a demon doing here, Laura?"
  jk" {cps=25} I just want-"
  ln"{cps=25} You son of a bitch! Where is Jenny? Where did you take her?"
  jk"{cps=25} It wasn’t me, dude…"
  ln"{cps=25} Liar!! Bring Jenny back! How dare that thick face of yours show in my house?"
  jk"{cps=25} Listen, Lucas.."
  ln"{cps=25} To what? To your excuses? To your nonsense stories?"
  show laura angry 
  lg"{cps=25} Calm down, Lucas…"
  ln"{cps=25} Why are you with him? Are you, his allies?  "

  menu:
    "Calm yourself down, Lucas. Listen first…":
      jump b1

    "We are not..":
      jump b2

  label b1:
    ln"{cps=25} How can I listen to someone who hid my girlfriend?"

  label b2:
    mc"{cps=25} we are not allies.. We are friends.."
    ln"{cps=25} it’s the same.. You are still friends with the person who hid my girlfriend.."

  lg"{cps=25} It is not Jake…"
  ln"{cps=25} Why are you covering him? He has my girlfriend! He has your friend…"
  lg"{cps=25} No.. Listen please.. Open your mind.. We all want to find jenny. We are on the same page… "
  mc"{cps=25} Listen to us first.. Listen to Jake.. He’ll help us find Jenny.."
  ln"{cps=25} That’s nonsense…"
  mc"{cps=25} Please, Lucas.. Just this once.. Listen.."
  ln"{cps=25} I can’t understand you two… I can’t understand why do you believe him… "
  jk"{cps=25} Listen to me.. I’ll explain everything.. I will answer all your questions if I can.."
  ln"{cps=25} Talk then… But I can’t promise if I can believe you.. As long as I can’t see Jenny.. You are still the suspect…"
  lg"{cps=25} We’ll leave you two… Lucas, listen to Jake.."
  hide laura with moveoutleft
  ln"{cps=25} …"
  hide lucas with moveoutleft
  mc"{cps=25} we’ll wait in the garden.."
  scene black
  with fade

  #~Lucas’s garden~

  hide jake  
  show laura neutral at left with moveinleft
  mc"{cps=25} Where are we going to start?"
  lg"{cps=25} No one’s here in the garden.. Where are the maids?"
  mc"{cps=25} I can’t see any guard too.."
  lg"{cps=25} Let’s go around…"

  #~Go anywhere in the house~
  #If they went to kitchen area… option talk to the maid will appear…
  #Else if they went to the bar they will find the janitor…

  #(If they went to kitchen)
  #lg"{cps=25} There’s a maid.."
  #mc"{cps=25} Let’s ask her?"
  #"(Approach the maid)"
  #lg"{cps=25} Hi, miss!"
  #maid"{cps=25} Yes, ma’am?"
  #lg"{cps=25} May I ask if you know this person?"
  #"(show the image)"
  #maid"{cps=25} Uhm… yes mam.. He’s the head janitor of the mansion, ma’am.."
  #mc"{cps=25} Is he here? "
  #maid"{cps=25} I think he’s in the bar ma’am…"
  #mc"{cps=25} Okay, thank you…"
  #maid"{cps=25} Do you want me to lead the way?" 
  #lg"{cps=25} No, thanks…"
  #mc"{cps=25} Let’s go?"
  #lg"{cps=25} Thank you.."

  #~go to the bar~
  #(if they went to bar first before going to the kitchen)
  lg"{cps=25} There he is…"
  mc"{cps=25} Let’s go!"
  lg"{cps=25} Hi, mister.. Good afternoon."
  show thomas neutral at right with moveinright
  init python:
    thomasChar = True
  mt "{cps=25} Hi, ma’am… Are you looking for sir Lucas?"
  mc"{cps=25} No.. He’s in the living room with our friend.. We just uhm… roam around and.. yeah.. here we are.."
  lg"{cps=25} What is your name sir?"
  mt"{cps=25} Thomas, ma’am… I am the head janitor of the mansion, ma’am… "
  lg"{cps=25} Nice to meet you, Sir Thomas… By the way, I haven’t seen Lucas’s parents.."
  mt"{cps=25} They are on a business trip ma’am.. They’ll be home by next week.."
  lg"{cps=25} Oh, really? Hmm… you’re the head janitor,, right?"
  mt"{cps=25} Yes, ma’am…"

  mc"{cps=25} Do you remember the party that was held here for Jenny?"
  mt"{cps=25} The… party, ma’am?"
  lg"{cps=25} yes.. the party.."
  mt"{cps=25} Y-yes, ma’am.. "
  mc"{cps=25} What time did the party ended?"
  mt"{cps=25} p-past 2:00 am..?"
  mc"{cps=25} You know jenny, right?"
  mt"{cps=25} y-yes.. she’s Sir Lucas' girlfriend.."
  lg"{cps=25} What time do you think she went home?"
  mt"{cps=25} I-I don’t know, m-ma’am.."
  lg"{cps=25} Are you sure?"
  mt"{cps=25} Uhm.. "
  ln"{cps=25} Thomas, can you clean the living room? There's a little mess…"
  mt"{cps=25} yes, sir!"
  hide thomas with moveoutright
  "(janitor went out)"  
  lg"{cps=25} Where is Jake?"
  show lucas serious at right with moveinright
  ln"{cps=25} He’s probably out…"
  mc"{cps=25} So… what happened?"
  show lucas sad
  ln"{cps=25} I can’t believe he fooled you… You really believed what he said?"
  show laura angry
  lg"{cps=25} He’s stating the fact, Lucas…"
  ln"{cps=25} I can’t believe him… I want to but I can’t… Find Jenny and bring her to me, then I’ll believe him…"
  show lucas neutral
  ln"{cps=25} I’m tired… Go home if you’re done here…"
  show laura neutral
  lg"{cps=25} okay.. but take this.. we bought this for you.. (gaved the item you bought)"
  ln"{cps=25} Just leave it there…"
  scene black
  with fade

  #~outside lucas’s house~

  show jake nervous
  show laura neutral at left with moveinleft
  mc"{cps=25} What happened?"
  show jake tired
  jk"{cps=25} As expected… he didn’t believe me… "
  lg"{cps=25} I understand him though… Just like us, he’s desperate to find jenny…"
  show jake nervous
  jk"{cps=25} Did you find the janitor? "
  mc"{cps=25} yeah.."
  lg"{cps=25} But we did not get any info…"
  show jake happy
  mc"{cps=25} He doesn’t know what happened to Jenny…"
  lg"{cps=25} Something is weird though.."
  mc"{cps=25} Why?"
  lg"{cps=25} He can talk fine at first… But he started stuttering when we asked him about the party… He can’t even look at us…"
  mc"{cps=25} I noticed it too… But I thought he’s just like that."
  jk"{cps=25} Maybe he knows something he cannot say…"
  lg"{cps=25} Can be.."
  show jake bragging
  jk"{cps=25} So, what’s the plan?"
  mc"{cps=25} Let’s go home first… I still have work later so you guys can think of the next step. Let’s meet at my place tomorrow.."
  hide laura 
  hide jake
  scene black
  with fade

  #~MC’s house~
  #~Evening~

  mc"{cps=25} The moon looks surreal… I want to stare at you all night but I still have work… "

  menu:
    "Take a shower":
      jump bath_2
    "Eat dinner":
      jump dinner_2

  label bath_2: 
    "TAKING A SHOWER"
    scene black
    with fade

  label dinner_2:
    mc"{cps=25} I can call Laura while eating"
    "(Calling Laura…)"
    #insert sound effect of calling
    lg"{cps=25} Hello?"
    mc"{cps=25} Laura… Have you thought of the plan?"
    lg"{cps=25} Uhm.. can I call you later?"
    mc"{cps=25} Why? Are you busy?"
    lg"{cps=25} Yeah.. kind of.. sorry"
    mc"{cps=25} Sure.. let’s just meet tomorrow.."
    lg"{cps=25} Yeah. Bye.."
    "(phone call ended)"
    mc"{cps=25} I think she’s so busy… I’ll just go to work…"

    #~GO TO WORK~
    
    #~AT HOME~
    #(Sleep)
    
    #~Morning~
    #~Living room
    show jake nervous at right with dissolve
    show laura neutral at left with dissolve
    mc"{cps=25} How are you both?"
    show jake happy
    jk"{cps=25} I met Justine when I was on the way here.."
    mc"{cps=25} And?"
    jk"{cps=25} He’s weird.."
    show laura angry
    lg"{cps=25} He’s always weird.."
    jk"{cps=25} I know.. but he’s weirder now.. He bumped me…"
    jk"{cps=25} I actually did not notice him… but normally, he will just passes through me… But when we cross our ways a while ago… he said something that made him weirder.."

    lg"{cps=25} What is it?"
    jk"{cps=25} He said “You better look around you”…"
    show laura chuckle
    lg"{cps=25} HAHAHAHAHAHA… you’re a real idiot! Of course, you bumped him!"
    mc"{cps=25} On the other hand.. it’s kinda sus… if we bumped to someone,"
    mc"{cps=25} we normally say “Watch, where you’re going” if we are not in a good shape. And the fact that we are suspecting him, it really feels off…"
    show laura neutral
    lg"{cps=25} You have a point…"
    jk"{cps=25} so, what’s the plan?"
    lg"{cps=25} We need to get the cctv footage during the party from every part of the house…"
    mc"{cps=25} But where can we get that?"
    jk"{cps=25} The records are automatically saved in his parents’ PC… And the PC is in their master bedroom located in the second floor of the house."
    lg"{cps=25} How did you know?"
    jk"{cps=25} I remember when I was drunk during the party..."
    jk"{cps=25} I lost track of where I was going. I just found myself in their master bedroom.. The PC was left open and I saw the footage of the party…"
    lg"{cps=25} So, we need to sneak in their master bedroom to get the footage.? How about their parents?"
    mc"{cps=25} His parents are on the business trip, remember? The janitor told us.."
    lg"{cps=25} ahh, yeah I remember.. Sorry.."
    jk"{cps=25} But we have another problem…"
    mc"{cps=25} What?"
    jk"{cps=25} their house is surrounded with CCTV.. "
    lg"{cps=25} What if we did not? What if we get caught?"
    
    menu: 
      "We won’t":
        jump c1
        
      "That’s possible":
        jump c2

    label c1:
      lg"{cps=25} How can you be so sure?"

      label c2:
        mc"{cps=25} But I have an idea, so it won’t happen.."
        lg"{cps=25} What is it?"

    mc"{cps=25} We have you.. "
    show laura surprised
    lg"{cps=25} What? What about me?"
    mc"{cps=25} You can call him and ask him where is he.. then we’ll just avoid him.. "
    show laura pissed
    lg"{cps=25} Are you putting me on the front line? This is like a suicide mission…"
    mc"{cps=25} You can do it… He can’t hate you…"
    show laura angry
    lg"{cps=25} I’m not sure…"
    jk"{cps=25} We are sure…"
    mc"{cps=25} So, Laura… Can you do it?"
    show laura angry
    lg"{cps=25} I don’t like the idea.. But do I have a choice?"
    mc"{cps=25} We know we can trust you in this one…"
    show laura neutral
    lg"{cps=25} I’ll try my best…"
    show jake nervous
    jk"{cps=25} We have another problem…"
    lg"{cps=25} What?"
    show jake happy
    jk"{cps=25} Does anyone of you have a flashdrive?"
    mc"{cps=25} nah.."
    lg"{cps=25} My flash drive is borrowed by my sister…"
    mc"{cps=25} We can just buy one…"
    scene black
    with fade

#~Go to the mall~
#~Buy a flash drive~
#~Go home~

    show laura neutral at left with moveinleft
    mc"{cps=25} Do we have everything we need?"
    show jake happy at right with moveinright
    jk"{cps=25} yeah.. I guess so.."
    lg"{cps=25} Should we go there now?"
    jk"{cps=25} Nah.. It’s too early.. The securities are probably on the stand… Let’s wait until, lunch time…"

    #~the user can use the day time feature to change the time to afternoon~
    #~afternoon~
    #~go to Lucas’s mansion~
    
    mc"{cps=25} Laura, call Lucas.. Ask him where he is…"
    lg"{cps=25} Sure.."
    "(phone rings then call answered)"
    hide jake with dissolve
    show lucas happy at right with moveinright
    lg"{cps=25} Hi, Lucas… Where are you?"
    ln"{cps=25} In the library, why?"
    lg"{cps=25} School library?"
    ln"{cps=25} No.. In our library.. In the mansion specifically.."
    lg"{cps=25} Ahhh okay.."
    ln"{cps=25} Why?"
    ln"{cps=25} Nothing.. I am in the mall.. I thought I saw you…"
    ln"{cps=25} nah.. I’m busy with our project.. "
    lg"{cps=25} Okay.. good luck!"
    ln"{cps=25} Thanks.. I gotta go.."
    lg"{cps=25} Sure.. bye,,"
    ln"{cps=25} Bye.."
    hide lucas with moveoutright
    "(phone call ended)"
    show jake happy at right with moveinright
    lg"{cps=25} he’s in the library.. "
    mc"{cps=25} Nice.. "
    jk"{cps=25} Let’s go.. the way is clear.. Guards might taking a lunch.. Let’s go…"
    hide laura with moveoutleft
    hide jake with moveoutright

    #~sneak to the master bedroom~
    #~master bedroom~

    show laura neutral at left with moveinleft
    show jake happy at right with moveinright
    mc"{cps=25} That was freaking crazy…"
    lg"{cps=25} Do they have hundreds of maids?! "
    jk"{cps=25} Not a surprise… this mansion is huge as fuck…"
    mc"{cps=25} There’s the PC…"
    jk"{cps=25} Shit! How many CCTv’s do they have?"
    mc"{cps=25} Wait.. Isn’t this his library?"
    jk"{cps=25} I guess so…"
    show laura surprised
    mc"{cps=25} Then, where is Lucas? I thought he’s in the library.."
    jk"{cps=25} I don’t know… He’s nowhere.."
    show laura neutral
    lg"{cps=25} Maybe he went out?"
    mc"{cps=25} possible."
    jk"{cps=25} Let’s see.. Is this the file?"
    mc"{cps=25} I think so.."
    lg"{cps=25} faster…"
    
    "(copy-paste-processing-done)"
    jk"{cps=25} Done.."
    mc"{cps=25} Let’s go.."
    jk"{cps=25} wait… Let me erase the footage when we went in and I’ll disconnect the system from the CCTV so we can escape."
    lg"{cps=25} Good…"
    jk"{cps=25} Done…"
    mc"{cps=25} Let’s Go"
    scene black
    with fade

    #~MC’s house~
    show laura chuckle at left with moveinleft
    lg"{cps=25} That was crazy…"
    show jake happy at right with moveinright
    jk"{cps=25} Ugh… let’s see what’s in here…"
    show laura neutral
    mc"{cps=25} Here… I have a laptop.."
    "(USB connected)"
    "(video playing)"
    #~after 2hrs~
    mc"{cps=25} Wait… look… "
    show laura surprised
    jk"{cps=25} This is jenny, Justine and I… "
    lg"{cps=25} So, Justine really took jenny?!!"
    mc"{cps=25} Where are they going?"
    jk"{cps=25} This is the last footage where jenny was last seen… and after 5 minutes,"
    jk"{cps=25} Justine went out alone… Then the janitor went in…"
    jk"{cps=25} After 30 mins, the janitor went out looking strange… the footage ended when the janitor went out…"
    show laura angry
    lg"{cps=25} Do you think it was the Janitor?"
    mc"{cps=25} Possible… But why would the janitor do that?"
    lg "{cps=25} I don’t know... No one knows…"
    show jake bragging
    jk"{cps=25} Justine is also a possible sus…"
    mc"{cps=25} If that is Justine? Why would he hide jenny? And how? "
    lg"{cps=25} Justine likes jenny, right? Maybe he hid her from Lucas?"
    jk"{cps=25} It makes sense… But still… Our conclusion is not enough… We must find evidence… "
    mc"{cps=25} Ughh… my head hurts already from these things…"
    lg"{cps=25} So, what’s the next plan?"
    jk"{cps=25} I think we should try to talk to janitor again... I know he knows something… I just wonder what’s stopping him from talking…"
    show laura neutral
    lg"{cps=25} What if he’s the culprit?"
    jk"{cps=25} We won’t ask him about it… We’ll ask him about what happened in the party… Not this specific thing…"
    mc "{cps=25} how?"
    jk"{cps=25} I’ll find a way... For now… let’s call it a day and take a rest… This was a long day for us…"
    lg"{cps=25} I agree.. Just talking to Lucas is already tiring.. Sneaking in and scaping is another story… I felt like I am a total criminal.."
    jk"{cps=25} At least you became a criminal for the good…"
    show laura pissed
    lg"{cps=25} And you’re a real idiot!"
    mc"{cps=25} Stop it, guys… "
    show laura neutral
    show jake happy
    jk"{cps=25} let’s go.. see you tomorrow…"
    mc"{cps=25} We have a class tomorrow…"
    jk"{cps=25} Then tomorrow in the afternoon?"
    mc"{cps=25} Sure…"
    show jake bragging
    jk"{cps=25} Should I take you home, laura?"
    lg"{cps=25} much better…"
    scene black
    with fade

    #~evening~
    #~go to work~
    #~go home~
    #~sleep~
    #~morning~
    #~School~
    mc"{cps=25} (thinking) laura might be in the room…"

    #~Go to the classroom~
    mc "{cps=25} (thinking) Laura isn’t here.. It’s almost time.. She might be in the library…"

    #~Go to the library~
    show laura neutral
    mc"{cps=25}There you are!"
    lg"{cps=25} What are you doing here?"

    menu:
      "you’re not in our room so I went here thinking you’re here.. And I am right..":
        jump d1
        
      "It’s almost time for our class":
        jump d2

    label d1:
      show laura neutral
      lg"{cps=25} Why are you looking for me then?"
      mc"{cps=25} It’s almost time for our class.."
      lg"{cps=25} We still have sometime before our P.E…"

    label d2:
      show laura neutral
      lg"{cps=25} Ugh! You’re right!  I lost track of time… let’s go!"

    show laura surprised
    lg"{cps=25} OMG!"
    mc"{cps=25} What?"
    show laura angry
    lg"{cps=25} Our morning class is PE… I did not brought my P.E. uniform.."
    mc"{cps=25} Life sucks bigtime huh?"
    lg"{cps=25} Shut up!"
    mc"{cps=25} I have extra uniform in my locker… But first, let’s go in our room.."
    scene black
    with fade

    #~go to the room~
    "Good morning, everyone! Today, you are tasked to play basketball and practice ball control… We are going to the gym with other sections.. Is that okay?"
    "Class: Yes sir.."
    "First, get a one-fourth sheet of pad paper.. write you name, age, cellphone number, and address… It will be collected and given to your adviser… I’m giving you five minutes to pass it… "
    mc"{cps=25} Laura, may I have one?"
    show laura neutral
    lg"{cps=25} sure…."
    
    #~gym~
    lg"{cps=25} Where’s your extra uniform.."
    mc"{cps=25} Locker.. wait, I’ll get it…"

    #~locker~
    mc"{cps=25} I think this will fit her…"

    #~show justine~
    menu:
      "Talk to Justine":
        jump e1
      "Leave him":
        jump e2

    label e1:
      hide laura
      mc"{cps=25} hey… P.E?"
      show justine happy with moveinright
      jr"{cps=25} yeah… (transition out that will pass through MC)"
      mc"{cps=25} He loves talking…"
      hide justine with dissolve
      jump e2

    label e2:
      #~gym~ 
      mc"{cps=25} here.."
      show laura neutral
      lg"{cps=25} thanks.. btw, you did not pass your paper?"
      mc"{cps=25} I did…"
      lg"{cps=25} then I guess it’s missing.. Write one again.."
      "Professor" "{cps=25} Let’s start in 10 mins."
      "--class started—"
      ##--user can time skipped to afternoon--


      #~afternoon
      #~MC’s home~
      show laura angry at left with moveinleft
      lg"{cps=25} How I hope that freaking basketball can help me in my career… I feel like my bones are broken.."
      show jake smiling at right with moveinright
      jk"{cps=25} How I hope it is real…"
      lg"{cps=25} Who cares about your thoughts?"
      jk"{cps=25} Then who cares about your feeling...."
      mc"{cps=25} Can you both stop? You’re so loud! Can’t you just be nice with each other?"
      show laura pissed
      show jake nervous
      "Laura & Jake" "{cps=25} NO WAY!"
      show laura neutral
      show jake happy
      mc"{cps=25} okay fine.. let’s proceed to the plan.. "
      jk"{cps=25} I went to lucas’s mansion last night… When the janitor went out, I overheard the guards…"
      jk"{cps=25} And if I am right… the janitor regularly went out at that time to check all the trashes…"
      lg"{cps=25} So the plan is-"
      show jake nervous
      jk"{cps=25} put you in the trashcan so you can talk with him…"
      show laura angry
      lg"{cps=25} What!?"
      jk"{cps=25} You look like a trash so you don’t have to disguise… effortless, right [mc]?"
      lg"{cps=25} You’re a freaking idiot, son of a demon!"

      menu:
        "Both of you.. shut up!":
          jump P1
          
        "That’s how my grandparents started… No one thought they’d get marry":
          jump P2

      label P1:
        lg"{cps=25} Just spill the plan.."
        return

      label P2:
        jk"{cps=25} You’re disgusting!"
        lg"{cps=25} Are you crazy?"

  show laura neutral
  show jake happy
  mc"{cps=25} let’s get back to the plan…"
  jk"{cps=25} so, I am thinking of going there later, sneak near the trashcan and find the right timing to talk to him…"
  lg"{cps=25} Let’s ask him again.. We are sure he somehow knows something… and that is what we need to know…"
  "(Phone rings)"
  lg"{cps=25} That’s not mine.."
  jk"{cps=25} Not mine…"
  "(looked at your phone)"
  mc"{cps=25} What is this?"
  jk"{cps=25} What?"
  mc"{cps=25} look…"
  show laura surprised
  lg"{cps=25} Isn’t it Sir Thomas? Look closely…"
  show jake nervous
  jk"{cps=25} Thomas?"
  mc"{cps=25} yes… the janitor…"
  show jake bragging
  show laura neutral
  jk"{cps=25} hmm.. It is him.. What is he doing?"
  mc"{cps=25} Who is with him?"
  show jake happy
  jk"{cps=25} The body built looks familiar…"
  show laura chuckle
  lg"{cps=25} You know a lot about body built huh… Didn’t know you’re interested with men.."
  show laura pissed
  jk"{cps=25} Why? Wanna learn from me? I can teach you my anatomy.. (smirk)"
  lg"{cps=25} you’re disgusting…"
  show laura neutral
  mc"{cps=25} looks like they are having a transaction… the man is giving a what? Money? To the janitor…"
  jk"{cps=25} Who sent you the image?"
  mc"{cps=25} it’s from unregistered number…"
  lg"{cps=25} Do you think it has something to do with jenny?"
  mc"{cps=25} I don’t know.."
  jk"{cps=25} That’s what we need to find out… We really need to talk to him.."
  mc"{cps=25} what time does he went out?"
  jk"{cps=25} 8pm.."
  mc"{cps=25} I have to go to work by 9pm… But I’ll go with you.."
  jk"{cps=25} Hey, tweety bird!"
  show laura angry
  lg"{cps=25} What!?"
  jk"{cps=25} You know you’re tweety bird huh… Are you coming with us?"
  show laura neutral
  lg"{cps=25} I can’t… We have a family dinner later… "
  mc"{cps=25} Okay.. I’ll call you then.."
  lg"{cps=25} Sure.."
  scene black
  with fade

#(time skipped to evening)
#~lucas’s house~

  mc"{cps=25} How many guards to they have?"
  show jake happy with moveinright
  jk"{cps=25} Three here outside… "
  mc"{cps=25} Is that how rich kid live?"
  jk"{cps=25} Possibly…"
  mc"{cps=25} It’s almost time.."
  jk"{cps=25} There he is.."
  mc"{cps=25} Sir Thomas!!"
  show thomas happy at right with moveinright
  mt"{cps=25} oh! What are you doing here?"
  jk"{cps=25} we need to ask you something.."
  mc"{cps=25} I know you know something about Jenny’s incident.. Whatever it is.. can you tell it to us?"
  show thomas neutral
  show jake tired
  mt"{cps=25} Sorry.. I know nothing about it…"
  jk"{cps=25} Please sir…"
  "(phone beeped)"
  "Phone""{cps=25} Sir Thomas.. Sir lucas is calling you… please proceed to the library…"
  mt" {cps=25} I have to go.."
  show jake happy
  mc"{cps=25} Sir, wait.. Here’s my number… please call me…"
  hide thomas with moveoutleft
  "(Thomas took the card and went away)"
  show jake tired at center with moveinright
  mc"{cps=25} What now?"
  jk"{cps=25} I don’t know…"
  mc"{cps=25} let’s go home.."
  jk"{cps=25} can I sleep in your place?"
  mc"{cps=25} sure…"
  scene black
  with fade
  
  #~MC’s home~
  show jake happy with moveinright
  mc"{cps=25} I’ll leave you here.. You can sleep in my room if you want…"
  jk"{cps=25} I can sleep anaywhere.."
  mc"{cps=25} Make yourself comfortable.. I have to go.. "
  jk"{cps=25} Sure.."
  mc"{cps=25} I’ll leave my phone here…"
  jk"{cps=25} No worries…"

  #~go to work~
  #~go home~
  
  mc"{cps=25} you’re still awake?"
  jk"{cps=25} yeah… the… janitor called…"
  mc"{cps=25} What? What did he said?"
  jk"{cps=25} Luckily, I recorded it…"
  mc"{cps=25} Where is it? Let me hear…"

  #AUDIO:
    
  jk"{cps=25} Hello?"
  mt"{cps=25} h-hello?"
  jk"{cps=25} Sorry but [mc] isn’t here…"
  mt"{cps=25} A-are you one of the men who are on the m-mansion a while ago?"
  jk"{cps=25} yes.. Is this sir Thomas?"
  mt"{cps=25} y-yess.. listen carefully… M-ma’am Jenny is alive.. She’s not badly hurt b-but"
  mt"{cps=25} she’s in d-danger.. p-please save her.. I-I am scared to death that I cant talk.. p-please don’t come near me a-again…"
  jk"{cps=25} you know the culprit? Where are you?"
  mt"{cps=25} y-yes save her from l- (gun shot)"
  jk"{cps=25} Sir? Sir what happened?"
  uk"{cps=25} I gave you chances… but you never learned.. I only had one command for you…"
  uk"{cps=25} yet you still failed to do… don’t worry.. you do not have to worry anymore.. you’re free from your conscience.. All is well for you.. All is well…"
  "(record ended)"




  
  