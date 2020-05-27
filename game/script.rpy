# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Ruby Ray")

define p = Character("Phil Phaser")

define a = Character("Arthur")

define b = Character("Ben")

define c = Character("Cindy")

define d = Character("Duke")

define e = Character("Erika")

transform place (n):
    xalign 1.0 / 6.0 * n
    yalign 1.0

image bg room flip = im.Flip("bg room.png", horizontal = True)

default target = "Arthur"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg outside

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ruby outside at left

    # These display lines of dialogue.

    r "Oh, hello, beautiful Ganymede! We just came to find out why nobody is responding to our calls from your City X. I hope you don't mind."

    show phil outside at right

    p "Yeah, keep joking, but I still have a bad feeling about this. Look, there is no traffic around the city and no movement at all."

    r "Ok, you are right, that's odd. Let's check what's going on here."

    scene bg lobby

    "They found nobody on the streets, so they decided to enter the first building they saw, Hotel Quantum."
    
    show phil inside at right

    p "Empty, just like the whole city."

    show ruby inside at left
    
    r "Wait! Someone is coming."

    show arthur at place(3)
    
    a "Oh! Intruders? Monsters or saviors?"

    p "She is Ruby Ray, and I'm Phil Phaser, space detectives. We are here to investigate why this city went silent. What kind of monsters are you talking about?"

    a "A bunch of shapeshifting monsters attacked the city a few days ago. The mayor ordered strict quarantine while the militia mitigates the problem. His last message was to close all doors and not let anyone in until his next instruction."

    r "The front door was wide open..."

    a "What? So you didn't break in? Wait! Someone stole my keys!"

    show cindy at place(2)

    c "Arthur! What happened? Who are these people? Are they members of the militia? Is the quarantine finally over?"

    a "No, Cindy, still no news from the mayor. It seems they are just two strangers who have wandered into our hotel. They say the front door was open. It seems someone took my keys and let them in."

    c "But the door is locked. I just went there to check it, just like I do every morning."

    a "Ok, that's enough! Call everyone here immediately, I want to talk with them!"

    scene bg lobby

    show ruby inside at left

    show duke at place (1)

    show erika at place (5)

    show cindy at place (2)

    show ben at place (4)

    show arthur at place(3)

    show phil inside at right

    with fade

    a "Let’s quickly get past introducing each other. The new guests there are Ruby and Phil, and the old ones here are Erika and Ben on my left and Cindy and Duke on my right. Now that everyone knows each other, let me explain why I called you here."

    a "One of you stole my key, opened the door, let these in, then locked it again. I don't know if this was supposed to be a bad joke, or a horrible act of a madman, but I highly doubt you would reveal yourself. Still, I give it a try."

    a "Silence? That's what I expected. So now we are here, not knowing what happened, and there is a chance that a monster also sneaked in and pretends to be one of us."

    a "Since I can't expect you to stay together until we figure out if we need to be afraid of each other, I ask you to do the opposite. Go back to your room, stay there, and don't open your door for anyone until I tell you that it's safe to come out."

    e "But what if you are the monster."

    a "That's the point. It can be any of us, and you won't know until it's too late. So I think the best is to stay away from everybody. We just need to sit still until the militia comes and rescues us. But if you have a better idea, feel free to share it."

    e "I don't."

    a "Then what are you waiting for? Back to your rooms!"

    hide duke

    hide erika

    hide cindy
    
    hide ben

    a "We still have two free rooms on the first floor. You can take those."

    r "Thank you."

    hide arthur

    p "What are you up to?"

    r "I just want to check the guest register. I think it will be useful to know who stays in which room."

    r "There you go. Now at least we have a chance to find out if any of these people hides something suspicious in their room. Maybe the key to the front door."

    p "Oh, Ruby, I knew you won't be able to stay sit. But let's go now, before someone accuses us being the monster."

    scene bg room

    show ruby inside at left

    show phil inside at right

    r "Nice try, Phil. But a shapeshifting monster is far from enough for me to let you sleep in my room."

    p "Fine. You didn't want to sleep anyway, did you? So who do you want to check first?"

    menu:

      "Arthur":

        $ target = "Arthur"

        jump reaction

      "Ben":

        $ target = "Ben"

        jump reaction

      "Cindy":

        $ target = "Cindy"

        jump reaction

      "Duke":

        $ target = "Duke"

        jump reaction

      "Erika":

        $ target = "Erika"

        jump reaction

    label reaction:

      if target == "Cindy":

        p "Ok, then I will check Duke."

      else:
 
        p "Ok, then I will check Cindy."

      scene bg room flip

      show ruby inside at left

      r "[target] left and didn't even lock the door. Let's have a quick look around! Maybe I can find something interesting."

      if target == "Arthur":

        r "A top secret document hidden under the bed about the Zeta-7 crystal locator optimized for locating Abrachian shrink ray crystals. Weird."

      elif target == "Ben":

        r "A few strange crystals behind the toilet. They are covered with a special casing that makes them suitable for loading into a ray gun. Ben is up to no good!"

      elif target == "Cindy":

        r "A few strange crystals behind the toilet. They are covered with a special casing that makes them suitable for loading into a ray gun. Cindy is up to no good!"

      elif target == "Duke":

        r "A set of chemical apparatus hidden behind the mirror. They are still wet. He must have used it not long ago. But for what?"

      elif target == "Erika":

        r "The key to the front door hidden under the door mat! How original!? So Erika was the thief!"

      scene bg room

      show ruby inside at left

      r "Woah, this was close. I'm glad that nobody saw me. Maybe I should get some sleep then continue the investigation tomorrow."

      scene bg room

      show ruby inside at left

      with fade

      "Oh, a message from Arthur, that we should all meet in the lobby. Let's what he has to say to us!"

      scene bg lobby

      show ruby inside at left

      show erika at place (5)

      show cindy at place (2)

      show ben at place (4)

      show arthur at place(3)

      show phil inside at right

      a "I have bad news and good news. Duke disappeared, but I think I found the culprit. Cindy, my dear, what have you done?"

      if target != "Cindy":

        p "She was with me. Almost the whole day."

        c "What? You were the one who kidnapped and interrogated me? But why?"

        p "I wanted to know if you are clean. And now it seems you definitely are."

        a "Then why did I found shrink ray crystals in your room?"

        c "I don't even know what you are talking about."

        r "What has the crystals got to do with the monster?"

        a "The shapeshifting monsters are not killing anybody, but they are using shrink ray guns to kidnap and enslave people."

        p "Then maybe the monster tried to frame Cindy, but luckily I took care of her."

        a "Either that or you are also lying. Maybe there are more than one monsters in this hotel. Unfortunately we cannot know for sure. Unless someone else saw something."

        if target == "Ben":

          menu:

            "Ben also has some crystals. He is either the framer or also got framed, but I find this quite unlikely.":
              
              jump benrevealed

            "Nothing.":

              jump benhidden

        elif target == "Erika":

          menu:

            "Erika has the key! She is either the monster or the one who let in the monster.":

              jump erikarevealed

            "Nothing.":

              jump erikahidden

      else:

        c "I did nothing! I have no idea where is Duke."

        a "Then why did I found shrink ray crystals in your room?"

        c "I don't even know what you are talking about."

        r "What has the crystals got to do with the monster?"

        a "The shapeshifting monsters are not killing anybody, but they are using shrink ray guns to kidnap and enslave people."

        p "Well, if Cindy is a monster, we have to make sure that she can't hurt anyone else. I have a ray gun with which I can neutralize her for a week. If she is innocent, she is good to go afterwards. But if nobody else disappers..."

        c "I see. I think that's the best I can do to prove my innocence."

        p "You are a brave girl, Cindy. I promise it won't hurt."

    # This ends the game.

    return
