# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Ruby Ray")

define p = Character("Phil Phaser")

define a = Character("Arthur")

define b = Character("Ben")

define c = Character("Cindy")

define d = Character("Duke")

define e = Character("Erica")

transform place (n):
    xalign 1.0 / 6.0 * n
    yalign 1.0

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

    show erica at place (5)

    show cindy at place (2)

    show ben at place (4)

    show arthur at place(3)

    show phil inside at right

    with fade

    a "Let’s quickly get past introducing each other. The new guests there are Ruby and Phil, and the old ones here are Erica and Ben on my left and Cindy and Duke on my right. Now that everyone knows each other, let me explain why I called you here."

    a "One of you stole my key, opened the door, let these in, then locked it again. I don't know if this was supposed to be a bad joke, or a horrible act of a madman, but I highly doubt you would reveal yourself. Still, I give it a try."

    a "Silence? That's what I expected. So now we are here, not knowing what happened, and there is a chance that a monster also sneaked in and pretends to be one of us."

    a "Since I can't expect you to stay together until we figure out if we need to be afraid of each other, I ask you to do the opposite. Go back to your room, stay there, and don't open your door for anyone until I tell you that it's safe to come out."

    e "But what if you are the monster."

    a "That's the point. It can be any of us, and you won't know until it's too late. So I think the best is to stay away from everybody. We just need to sit still until the militia comes and rescues us. But if you have a better idea, feel free to share it."

    e "I don't."

    a "Then what are you waiting for? Back to your rooms!"

    hide duke

    hide erica

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

    r "Nice try, Phil. But a shapeshifting monster is far from enough to let you sleep in my room."

    p "Fine. You didn't want to sleep anyway, did you? So who do you want to check first?"

    # This ends the game.

    return
