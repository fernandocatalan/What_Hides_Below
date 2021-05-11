label third_location:
    $wenttolocation3 = True
    #this will be Maribel's folder where she can do whatever she wants.

#######Mary##########
# characters

    define d = Character("Detective [name]", color = "#230ac4")
    define A = Character("Ann", color = "#40E0D0")
    define O = Character("Officer", color = "#FF7F50")
    define c = Character("Mr Cruz", color = "#FFA500")
    define t = Character("Tom", color = "#880808")
    define v = Character("Victim", color = "#e6005c")
    image Ann = im.Scale("Ann.PNG", 550, 680, xalign=0.65, yalign=0.9)
    image mrCruz1 = im.Scale("mrCruz1.PNG", 650, 680, xalign=0.65, yalign=0.8)
    image Tom2 = im.Scale("tom2.PNG", 390, 680, xalign=0.65, yalign=0.8)
    image victim = im.Scale("victim.PNG", 200, 580, xalign=1.0, yalign=1.0)
# backgrounds
    image bg library = im.Scale("library1.jpg", 1920, 1080)
    image b5 = im.Scale("cruzhome.png", 1920, 1080)
    image b6 = im.Scale("objects/b6.png", 101, 84, xalign=0.73, yalign=0.70)
    image ob2 = im.Scale("objects/pic.png", 61, 84, xalign=0.80, yalign=0.70)
    image fd = im.Scale("fastdrive.jpg", 1920, 1080)
    image th = im.Scale("tomhome.jpg", 1500, 1080, xalign=0.5)
    image r2 = im.Scale("inside2.jpeg", 1920, 1080, xalign=0.5)
    image bm1 = im.Scale("basement1.jpg", 1500, 1080, xalign=0.5)
    image tom = im.Scale("tom.png", 1920, 1080, xalign=0.5)
    image bgEnd = im.Scale("end.png", 1920, 1080, xalign=0.5)
    image solved = im.Scale("case-solved.png", 1920, 1080, xalign=0.5,yalign=0.5)
    image bg locker = "locker_empty.png"
    stop sound
    $score = 1000
    $bookFound = 0

    show bg library
    d "{color=#3399ff}I'm in the library, It's very quiet here. Well, I guess I have to look for
      something odd."
    call talk from _call_talk
    call cruzhome from _call_cruzhome
    call tomhome from _call_tomhome
    scene
    return menu

label talk:

    d "{color=#3399ff}I need help, I see nothing but books in this whole section! let me ask the labrarian.
      I approached to her and I called her by her tag name."
    d "Excuse me Ann, I am detective [name]. I'm in an investigation related to this library. Is there any other section
       in this building?"
    show Ann
    A "Yes! There is a computer lab upstairs, the quiet place, and the basement that has been locked since I've known.
       An employee before me use to live in the basement for a long time. He quit and moved
       a few years ago."
    A  "He keeps coming, and seems to love the quiet room. We never talk to eachother,
       and actually, the quiet place is restricted."
    d "Can I take a look at the basement?"
    A "I am sorry detective, but I don't have the keys, but you can take a look at the quiet room.
       By the way, there are some missing items that I've been looking for detective [name], Can you
       find them for me? You will get compensated by Mr. Cruz"
    d "Okay Ann, I'll take a quick look. Don't worry about it"
    call quietRoom
    show bg library
    if bookFound == 1:
        d "{color=#3399ff}After a while of searching in the quiet room. I've found the missing items, and a blue
          book with a red X on it, and a note that says, "

        d "{color=#8b0000}'Congratulation, you have found my favorite place. How do you feel by standing on
          my collections? but don't get distracted.'"
        d "{color=#8b0000} 'You don't want to waste your time in here. I'm somewhere else enjoying
          the company. If you want to join us follow the X. You don't want to miss my wedding'"
        d "{color=#3399ff}I knew someone could be in danger, he has another victim! I am not only worried for how many
          others but the new life he's planning to take! What kind of collections is he talking
          about? In the past 3 months we have found 5 dead bodies in a plastic bag out of town."
        d "{color=#3399ff}I am horrified! All the dead bodies had the same missing finger, the ring finger. What kind of
          psychopath, is he? What kind of game is he playing? For the way he is giving me clues, I think he wants me to
          stop him. I just wish to stop him at once."
        d "{color=#3399ff}I went down stairs as fast as I could, then I got to the librarian and asked, where else can
          the keys possibly be"
    if bookFound == 0:
       d "{color=#3399ff}I couldn't find anything, I went downstairs as fast as I could, then I got
         to the librarian and asked. where else can the keys possibly be?"
    show Ann
    A "I have no idea where the keys are Sir you have to wait till tomorrow morning
       when the owner, Mr. Cruz is here"
    d "I don't have time for tomorrow. Can I get Mr. Cruz's address?"
    A "Sure detective, anything else I can help with"
    d "{color=#3399ff}She wrote the address on a paper note. The exact same note the suspect was using."
    A "Mr. Cruz lives a couple blocks from here detective [name]."
    d "thanks, let Mr. Cruz know I'm heading there"
    scene Ann
    return

label cruzhome:

    scene bg library
    show fd
    d "{color=#3399ff}I am driving as fast as I can to get to Mr. Cruz's house. My hands are sweating
       just by thinking of an innocent lady suffering right now by the hands
       of this psycho. I just remember some descriptions from the recent victims."
    d "{color=#3399ff}They were all College students, and I guess they were at the library studying.
       Poor innocent students, they had no idea what was comming for them."
    d  "{color=#3399ff}They had bruises all over their body as result for there punishment for fighting back. No
       signs of being tide, they show positive on many different drugs to make them weaker."
    d "{color=#3399ff}I believe he is keeping them in a place out of town. I just need a clue
       to where the suspect is located. The couple of minutes getting to the address feels
       like forever. I have arrived, I hope I can find something more than just a key."

    scene fd
    show b5
    d "I was about to knock on the door when Mr. Cruz opend it"
    show mrCruz1
    c "Hi detective!"
    d "Hello Mr. Cruz, I am detective [name]. I need to open the library's basement.
      I have to find out where Tom is right now. A life is in danger, and if i'm right he has taken out at least 5 lives"
    c "You are probably confusing Tom with someone else. The time he worked for me, I have never gotten
      any complain's. This must be a mistake. I can actually call my friend. I have known Tom for a very
      long time so that makes it difficult for me to believe he is a murderer."
    d "Unfortunately, it is true and there are lots of evidence against him. Now, please Mr. Cruzi'm losing time."
    c "well, I am sorry detective. I haven't seen those keys for a while. You can take a look at
      my office next room. It's the only place I haven't looked at."
    d "This is the last chance to look for those keys. If I can't find these keys in your office I'll have to
      use a warrant paper to open the basement Mr Cruz."
    c "Sure, Detective [name] no problem. I've been looking for some other stuff other than the keys
      if you find it I'll compensate you. There is no need to wait for the warrant paper. You can break
      the basement door if you have to."
    d "Thanks Mr. Cruz. Let me take a look, at your office real quick and don't worry about it I'll
      find everything. Give me a list."
    call homeoffice
    show b5
    show mrCruz1
    d "I found your stuff Mr. Cruz, but I couldn't find those keys. I also found a picture.
      Who else is with you in this picture?"
    show ob2
    c "It is Tom detective when he moved. He inherited that house after his grandmomther passed away. I helped him move."
    d "Where is this place exactly located Mr. Cruz? This must be the place where he keeps the victims against their will."
    c "It is out of town detective let me write you down the address"
    d "I'm going to head there right now. If you are in contact with him, for your security don't warn him."
    c "Of course not detective [name]. Anything else I can help. Well you know where I live so if you have a question come over."
    d "Thanks Mr Cruz. I have to go"
    scene
    scene
    show fd
    d "{color=#3399ff}I'm driving as fast as posible while calling the Sheriff. I am so close."
    d "Sheriff I know where the killer is. I need reinforments. I'll text you the address once
      I pull over."
    sheriff "You shouldn't go to that place alone. give me a few minutes [name]"
    d "Okay, I'll wait for the team there."

    return
label quietRoom:
    call variables2
    ##
    # The game starts here.
    $start = renpy.time.time()
    # this sets all the items back to not found
    $resetItems(locker_items)
    # which image set to use
    $hidden_files = "images/locker2_%s.png"
    # randomize the list and pick 5 items
    $hidden_items = renpy.random.sample(locker_items,5)
    # set number of hints
    $num_hints = 3
    # set number of extra clicks
    $num_clicks = 0
    $ score += 0
    $ bookFound = 0
    "Get ready to find the items!"
    $showitems = True
    scene Ann
    scene bg library
    play sound "audio/search.mp3"
    call screen hidden_object
    stop sound
    #scene bg locker
    $showitems = False
    show bg library
    $ elapsed = round(renpy.time.time() - start)
    $ bookFound = 1
    $ score = score - (((3 - num_hints) + (num_clicks))*50) + 100
    "Result: All Found! in [elapsed] seconds. Hints left [num_hints]. Extra clicks [num_clicks]"
    "congratulation detective [name]. You just earn your first clue 'the blue book'
    and 100 points earned. Current Score [score]"

    init python:

        class registerClick(Action):
            def __call__(self):
                global num_clicks
                global score
                num_clicks += 1
                renpy.restart_interaction()


        class getHint(Action):
            def __call__(self):
                global num_hints
                num_hints -= 1
                for index,i in enumerate(hidden_items):
                    if i.found == False and i.hint == False:
                        i.hint = True
                        break
                renpy.restart_interaction()

            def get_sensitive(self):
                global num_hints
                return num_hints > 0

        class SetItem(Action):

            def __init__(self, object, field, value):
                self.object = object
                self.field = field
                self.value = value

            def __call__(self):
                setattr(self.object, self.field, self.value)
                renpy.restart_interaction()

            def get_selected(self):
                return getattr(self.object, "hint") == True

        class Item:
            def __init__(self, name, x,y,w,h,hint=False):
                self.name = name
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.found = False
                self.hint = hint

        showitems = False
        def display_items_overlay():
            if showitems:
                ui.frame(id="obj_list")
                ui.vbox(id="display_vbox",spacing=10)
                ui.text("Hints: %d" % (num_hints))
                ui.text("Items:" )
                for index,i in enumerate(hidden_items):
                    inventory_prefix = ""
                    inventory_suffix = ""
                    item_name = i.name
                    item_state = i.found
                    if item_state == True:
                        inventory_prefix = "{s}"
                        inventory_suffix = "{/s}"
                    item_text = inventory_prefix+item_name+inventory_suffix
                    item_index = "object_%d" % (index)
                    ui.text(item_text,id=item_index)
                ui.close()
        config.overlay_functions.append(display_items_overlay)

        def is_all_found():
            for i in hidden_items:
                if i.found == False:
                    return False
            showitems = False
            return True

        def resetItems(in_items):
            for i in in_items:
                i.found = False

    screen hidden_object:
     tag hidden
     imagemap:
         auto hidden_files
         cache False
         imagebutton auto "empty_%s.png" action registerClick()
         textbutton "Hint" xalign 1.0 yalign 0.0 action getHint()

         for index, item in enumerate(hidden_items):
             hotspot (item.x,item.y,item.w,item.h) action If(hidden_items[index].found==False, SetItem(hidden_items[index],"found",True), None)
         if is_all_found():
             textbutton "Objects found!" xalign 0.5 yalign 0.5 action Return("All Found!")

    return
label homeoffice:
    call variables2
    ##
    # The game starts here.
    $start = renpy.time.time()
    # this sets all the items back to not found
    $resetItems(locker2_items)
    # which image set to use
    $hidden_files = "images/locker_%s.png"
    # randomize the list and pick 5 items
    $hidden_items = renpy.random.sample(locker2_items,5)
    # set number of hints
    $num_hints = 3
    # set number of extra clicks
    $num_clicks = 0
    $score += 0
    "Get ready to find the items!"
    $showitems = True
    scene Ann
    scene bg library
    play sound "audio/search.mp3"
    call screen hidden_object
    stop sound
    #scene bg locker
    $showitems = False
    show bg library
    $ elapsed = round(renpy.time.time() - start)
    $ score = score - (((3 - num_hints) + (num_clicks))*50) + 100

    "Result: All Found! in [elapsed] seconds"
    "Congratulation detective [name]. You just earn your second clue 'the picture', and 100
    points earned. Current score [score]"

    init python:

        class registerClick(Action):
            def __call__(self):
                global num_clicks
                num_clicks += 1
                renpy.restart_interaction()


        class getHint(Action):
            def __call__(self):
                global num_hints
                num_hints -= 1
                for index,i in enumerate(hidden_items):
                    if i.found == False and i.hint == False:
                        i.hint = True
                        break
                renpy.restart_interaction()

            def get_sensitive(self):
                global num_hints
                return num_hints > 0

        class SetItem(Action):

            def __init__(self, object, field, value):
                self.object = object
                self.field = field
                self.value = value

            def __call__(self):
                setattr(self.object, self.field, self.value)
                renpy.restart_interaction()

            def get_selected(self):
                return getattr(self.object, "hint") == True

        class Item:
            def __init__(self, name, x,y,w,h,hint=False):
                self.name = name
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.found = False
                self.hint = hint

        showitems = False
        def display_items_overlay():
            if showitems:
                ui.frame(id="obj_list")
                ui.vbox(id="display_vbox",spacing=10)
                ui.text("Hints: %d" % (num_hints))
                ui.text("Items:" )
                for index,i in enumerate(hidden_items):
                    inventory_prefix = ""
                    inventory_suffix = ""
                    item_name = i.name
                    item_state = i.found
                    if item_state == True:
                        inventory_prefix = "{s}"
                        inventory_suffix = "{/s}"
                    item_text = inventory_prefix+item_name+inventory_suffix
                    item_index = "object_%d" % (index)
                    ui.text(item_text,id=item_index)
                ui.close()
        config.overlay_functions.append(display_items_overlay)

        def is_all_found():
            for i in hidden_items:
                if i.found == False:
                    return False
            showitems = False
            return True

        def resetItems(in_items):
            for i in in_items:
                i.found = False
    screen hidden_object:
     tag hidden
     imagemap:
         auto hidden_files
         cache False
         imagebutton auto "empty_%s.png" action registerClick()
         textbutton "Hint" xalign 1.0 yalign 0.0 action getHint()
         for index, item in enumerate(hidden_items):
             hotspot (item.x,item.y,item.w,item.h) action If(hidden_items[index].found==False, SetItem(hidden_items[index],"found",True), None)
         if is_all_found():
             textbutton "Objects found!" xalign 0.5 yalign 0.5 action Return("All Found!")

    return

label tomhome:
    scene
    show th
    d "{color=#3399ff}I'm sorry but I can't wait. Every second counts"
    d "{color=#3399ff}seems like nobody is here. I have to break in"
    scene th
    show r2
    d "{color=#3399ff}It's too quiet in here."
    play sound "audio/screeming.mp3"
    d "{color=#3399ff}OMG I hear it now!"
    d "{color=#3399ff}The scream is coming from the floor. Tom has a particular attachement to basements.
      The entrance has to be from the outside."
    scene r2
    scene
    show bm1
    d "{color=#3399ff}I found it. I am walking carefully. I need to save her. Anyway the
      sheriff and the team must be here any moment now."
    scene r2
    scene bm1
    show tom
    d "raise your hands, you are under arrest."
    t "hahaha! wow detective you surprise me. You found me earlier than I've expected
      I had something else in mind."
    d "Turn arround carefully, and don't try anything stupid. on your knees
      and hands on your head"
    stop sound
    play sound "audio/police.mp3"
    scene tom
    show bgEnd
    show Tom2
    show victim
    $score += 500
    d "It's over Tom, there are lots of evidence agains you. Not only found from
      the library's basement where experts are taking out your mess. I can't
      believe there are more bodies there, and who knows where else. You better
      start talking Tom."
    d "{color=#3399ff} Tom stayed quiet while I handcuffed him while saying."
    d "You have the right to remain silent. Anything you say can and will be used
      against you in a court of law. You have the right to an attorney. If you cannot
      afford an attorney, one will be provided for you."
    v "Thank you so much"
    d "Stay there! The paramedicts will take care of you."
    sheriff "Good job [name]! we have lots to do. We have to identify those bodies,
            and make this psychopath speak up. This might lead us to solveing cases
            of many lost students."
    show solved
    "Congratulation detective [name], you solved this case, final score: [score]"
    stop sound
    return

label variables2:

    init python:
        locker_items = []
        locker_items.append(Item("angel",847,302,51,85))
        locker_items.append(Item("scroll",748,414,157,44))
        locker_items.append(Item("trophy",453,250,47,128))
        locker_items.append(Item("scissors",1544,575,93,48))
        locker_items.append(Item("pillow",1340,284,73,60))
        locker_items.append(Item("fish bowl",1101,304,73,58))
        locker_items.append(Item("coat stand",262,238,102,57))
        locker_items.append(Item("oil lamp",1617,386,44,87))
        locker_items.append(Item("candelbra",1352,372,50,98))
        locker_items.append(Item("spade",1251,609,119,50))


        locker2_items = []
        locker2_items.append(Item("owl",346,656,68,79))
        locker2_items.append(Item("chess piece",881,445,30,78))
        locker2_items.append(Item("tarantula",739,672,103,73))
        locker2_items.append(Item("music note",1019,560,60,32))
        locker2_items.append(Item("dogs",1334,549,181,110))
        locker2_items.append(Item("orange slice",1657,401,95,104))
        locker2_items.append(Item("comb",1268,963,109,112))
        locker2_items.append(Item("cat",0,969,165,109))
        locker2_items.append(Item("star",482,102,69,70))
        locker2_items.append(Item("tie",1055,370,56,106))
