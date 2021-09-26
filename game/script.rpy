define pov = Character("[povname]")
default povname = "Bababooie"
define c = Character("Coordinator")
define l = Character("Lup")
define a = Character ("Alle")
define p = Character ("Paca")

default dates = 0
default lupDate = 0
default alleDate = 0
default pacaDate = 0

label start:

    scene bg club
    with fade
    play music "BlippyTrance.mp3"

    show coord wave
    with dissolve

    c "Ah, you must be our last guest for this afternoon's speed date!"

    $ povname = renpy.input("Please sign in:")
    $ povname = povname.strip()

    if not povname:
     $povname = "Bababooie"

     pov "My name is [povname]!"

    hide coord wave

    show coord normal

    c "Thanks, [povname].  Is this your first time speed dating?"

    menu:
        "Um yeah, is it that obvious?":
            jump explanation

        "No, I know my way around weird dating strategies.":
            c "Wonderful, then you already know the process!"
            jump meet_the_dates

    label explanation:
    c "Don't be nervous, it's easy!"
    c "The process is really simple.  Inside, there are 3 other singles looking for a fun date."
    c "You'll go in and introduce yourself and then you'll have a few minutes to strike up a conversation with one."
    c "When the timer goes off, rotate partners!  That way you meet several people quickly."
    c "At the end of the session you and the person you had the highest compatibility with can go on a date."

    pov "{i}Wow that sounds... kinda scary I think.  No! I won't get discouraged, being single sucks! :({/i}"
    pov "I'm gonna do my best to make a good connection!"

    menu:
        "Go in there!":
            jump meet_the_dates

    label meet_the_dates:

    hide coord normal
    with fade

    pov "{i}Through the doors is an open and sunny room.  Three figures are seated around a small round table."
    pov "{i}An awkward but excited vibe fills the space."
    pov "{i}The other prospective dates look up and offer me various little waves in greeting."

    show lup normal at left

    pov "{i}A tall and outgoing grey wolf."

    show alle normal

    pov "{i}An even taller moose who has a shy smile."

    show paca normal at right

    pov "{i}And very buff elephant who gives me a confident and pleasant smile."

    hide lup normal
    hide alle normal
    hide paca normal
    with fade
    show coord wave

    c "Alright, please choose your first conversation partner!"

    hide coord normal
    hide coord wave

    label convo_round1:

    menu:
        "The wolf seems fun.":
            $ dates = dates +1
            jump lup_convo1
        "The moose seems nice.":
            $ dates = dates +1
            jump alle_convo1
        "The elephant seems confident.":
            $ dates = dates +1
            jump paca_convo1
############################CHOOSE 1st DATE#####################################

    label lup_convo1:

    hide coord normal
    hide coord wave
    show lup normal

    l "Whoa! Nice!"

    pov "Hi, I'm [povname]."

    l "Wow, I like that name a lot!  I'm Lup.  I'm a line cook!"
    l "I'm training to be a real chef though!  What do you do?"

    menu:
        "I do gamedev, its hard but a lot of fun.":
            jump lup_convo1A
        "I want to learn how to make video games!":
            jump lup_convo1A

    label lup_convo1A:

    l "WOW."
    l "I LOVE GAMES!"
    l "What kind of games do you make?"
    l "Could you make a game about cooking??"

    pov "{i}I can't help but laugh a little at their enthusiasm."
    pov "Yeah, probably! You could race against the clock to get tasks done or something."

    hide lup normal
    show lup heh

    pov "{i}I should probably ask them about themselves, too."
    pov "What kinds of food do you want to make as a chef?"

    l "ALL KINDS!"
    l "But not chocolate!"
    l "Chocolate is super overrated!"

    pov "{i}I open my mouth to ask more but just then the timer goes off."

    hide lup heh
    show coord wave

    if dates == 3:
        jump ending

    c "Time to rotate partners!"

    pov "{i} Lup and I wave an enthusiastic goodbye at each other and change seats."

    $ lupDate = 1

    if dates == 1:
        menu:
            "The moose seems nice.":
                $ dates = dates +1
                hide coord wave
                jump alle_convo1

            "The elephant seems confident.":
                $ dates = dates +1
                hide coord wave
                jump paca_convo1

    elif alleDate == 1:
        menu:
            "The elephant seems confident.":
                $ dates = dates +1
                hide coord wave
                jump paca_convo1

    else:
        menu:
            "The moose seems nice.":
                $ dates = dates +1
                hide coord wave
                jump alle_convo1
###############################LUP CONVO#########################

    label alle_convo1:
        hide coord wave
        show alle normal

    a "Oh jeez... Sorry, I'm super nervous."
    a "I'm Alle.  I'm a counselor.  Like a therapist, not a school counselor."
    a "What's your name?"

    pov "Nice to meet you, Alle.  I'm [povname].  Right now I do gamedev."
    pov "But wow, conunseling.  You must have done a lot of schooling."

    hide alle normal
    show alle blush

    a "eheheh yeah kind of.  But I like helping people."
    a "Especially since times are kinda tough for everyone right now."

    hide alle blush
    show alle normal

    a "But you make games?  I love video games, though I play a lot less than I used to."

    pov "That's awesome, what kind of games do you like?"
    pov "{i}Alle gets a little sheepish grin on their face.  Its actually pretty cute."

    hide alle normal
    show alle blush

    a "I really like horror games.  Sometimes I stream them."

    pov "Hold up, you seriously-"

    menu:
        "play horror games?  Like the super scary ones?":
            jump alle_convo1A
        "stream??  Do you have a lot of viewers?":
            jump alle_convo1B

    label alle_convo1A:

    pov "{i}Alle gets a sparkle in their eye, they look pumped."

    a "Yeah! I love that one with the ghosts and the mansion and the camera ITS SO SCARY!!"
    jump alle_wrapup

    label alle_convo1B:

    pov "{i}Alle looks a little embarrassed but pleased."

    a "Not tons but my viewers are really nice and I like interacting with them a lot."
    a "I consider them my friends even if we've never met UvU."
    jump alle_wrapup

    label alle_wrapup:
    pov "{i} Honestly, its not what I expected but Alle is surprisingly cool."
    pov "{i} I start to ask another question but the timer on the table rings loudly."

    hide alle blush
    show coord wave

    if dates == 3:
        jump ending

    c "Time to rotate partners!"

    pov "{i} Alle gives me a shy but happy wave that I return with a smile."

    $ alleDate = 1

    if dates == 1:
        menu:
            "The wolf seems fun.":
                $ dates = dates +1
                jump lup_convo1

            "The elephant seems confident.":
                $ dates = dates +1
                hide coord wave
                jump paca_convo1

    elif lupDate == 1:
        menu:
            "The elephant seems confident.":
                $ dates = dates +1
                hide coord wave
                jump paca_convo1

    else:
        menu:
            "The wolf seems fun.":
                $ dates = dates +1
                jump lup_convo1
##########################################ALLE CONVO ##########################

    label paca_convo1:

    hide coord wave
    show paca normal

    pov "{i}The elephant stands to greet me, shaking my hand firmly but earnestly."

    p "It's nice to meet you, I'm Paca."
    p "This is my first time trying out speed dating."

    pov "It's nice to meet you too.  I'm [povname]."
    pov "What made you want to try out speed dating?  It's kind of unusual."
    pov "{i} Paca smiles a little self consciously."

    p "Honestly, I just want to meet more people.  My friend circle is quite small."
    p "My job demands a lot of my time."

    pov "Oh, do you-"

    menu:
        "have to travel a lot?":
            jump paca_convo1A
        "have trouble maintaining relationships because of it?":
            jump paca_convo1B

    label paca_convo1A:

    pov "{i} Paca nods and scratches their chin a little."

    p "Yeah.  I'm a marine biologist and I go on research trips once or twice a year."
    p "I'm gone for a month or two at a time so I do a lot of remote activities with friends."

    label paca_convo1B:

    hide paca normal
    show paca huh

    p "I guess you could say that.  I travel a lot."
    p "I do a lot of remote activities to try and stay connected with people."

    pov "Like what?"

    p "I really like movies so we watch them together online."
    p "Actually, that reminds me of something.  So I like to ask people this question..."
    p "Because my ex and I got into a huge fight over it so I like to see what others think."

    pov "Okay..."

    p "Do you think Star Wars is science {i}fiction{/i} or science {i}fantasy{/i}??"

    pov "UM"

    menu:
        "Oh my god, is there a difference??":
            jump paca_convo1C
        "Science Fantasy, it doesn't have a lot of classic scifi themes.":
            jump paca_convo1D
        "Science fiction, it takes place in space, doesn't it??":
            jump paca_convo1E

    label paca_convo1C:

    p "APPARENTLY.  We argued about it for weeks. ;_; "
    jump paca_wrapup

    label paca_convo1D:

    p "THAT'S WHAT I SAID!!"
    jump paca_wrapup

    label paca_convo1E:

    p "I see your point but if typical genre benchmarks don't apply, even if popular opinion considers-"

    label paca_wrapup:

    hide paca huh
    hide paca normal

    pov "{i}The timer on the table goes off.  Its time to switch partners."

    if dates == 3:
        jump ending

    pov "{i}I thank Paca for their time and switch seats."

    hide paca huh
    hide paca normal

    $ pacaDate = 1

    if dates == 1:
        menu:
            "The wolf seems fun.":
                $ dates = dates +1
                jump lup_convo1

            "The moose seems nice.":
                $ dates = dates +1
                hide coord wave
                jump alle_convo1

    elif alleDate == 1:
        menu:
            "The wolf seems fun.":
                $ dates = dates +1
                jump lup_convo1
    else:
        menu:
            "The moose seems nice.":
                $ dates = dates +1
                hide coord wave
                jump alle_convo1
#####################################PACA CONVO################################

    label ending:
        hide coord wave
        hide coord normal

        pov "And that was everyone."
        pov "Now the awkward part. =_="
        pov "Choosing who to go on a date with."

        pov "{i}I should consider this carefully..."

        show coord normal
        c "Okay! What did you think?  Were there any sparks?"

        hide coord normal
        hide coord wave

        menu:
            "Lup.  They're energy is too cute.":
                jump lup_ending
            "I really liked Alle, I'd like to get to know them more.":
                jump alle_ending
            "I think Paca and I would have a lot of fun together.":
                jump paca_ending

    label lup_ending:

        show lup heh

        l "Wow!  I'm excited!  I though you seemed pretty fun too!"
        l "Where do you wanna go first!??"

        hide lup heh

        jump thank_you

    label alle_ending:
        show alle blush

        a "T-Thanks!  I was so nervous coming here but I'm glad I did!"
        a "Should w-we... go get something to eat?"

        hide alle blush

        jump thank_you

    label paca_ending:
        show paca normal

        p "Wow, I'm actually really surprised!  And flattered!"
        p "Most people are really put off by my work demands."
        p "But I hope we get to be good friends"

        hide paca normal

    jump thank_you

    label thank_you:

    scene bg ending
    with fade

    pause 2.0

    return
