# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Ruby Ray")

define p = Character("Phil Phaser")

define a = Character("Arthur")

define c = Character("Cindy")

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

    r "Monsters? What monsters?"

    a "A bunch of shapeshifting monsters attacked the city a few days ago. The mayor ordered strict quarantine while the militia mitigates the problem. His last message was to close all doors and not let anyone in until his next instruction. I'm afraid you're not here to bring the long-awaited good news."

    r "The front door was wide open..."

    show cindy at place(2)

    c "Arthur! What happened? Who are these people? Are they members of the militia? Is the quarantine finally over?"

    a "No, Cindy, still no news from the mayor. It seems they are just two strangers who have wandered into our hotel. They say the front door was open."

    c "But it's locked. I just went there to check it."

    show duke at place (1)

    show erica at place (5)

    show cindy at place (2)

    show ben at place (4)

    show phil inside at right

    r "Nice..."

    # This ends the game.

    return
