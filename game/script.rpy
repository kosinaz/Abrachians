# The script of the game goes in this file.

# Declare characters used by this game.

define r = Character("Ruby Ray")

define p = Character("Phil Phaser")

define a = Character("Arthur")

define b = Character("Ben")

define c = Character("Cindy")

define d = Character("Duke")

define e = Character("Erika")

define m = Character("Monster")

# Display the character's sprite on the n-th place of the screen.

transform place (n):

  xalign 1.0 / 6.0 * n

  yalign 1.0

# Define the flipped version of the room image to use during investigations.

image bg room flip = im.Flip("bg room.png", horizontal = True)

# Set the variable that shows the player's target on the given night.

default target1 = "Arthur"

default target2 = "Arthur"

# The game starts here.

label start:

  # Show a background.

  scene bg outside

  # Show the player's character sprite.

  show ruby outside at left

  # Show both the background and the sprite with a fade-in transition.

  with fade

  # Display a dialogue of the already declared character.

  r "Oh, hello, beautiful Ganymede! We just came to find out why nobody is responding to our calls from your City X. I hope you don't mind."

  show phil outside at right

  p "Yeah, keep joking, but I still have a bad feeling about this. Look, there is no traffic around the city and no movement at all."

  r "Ok, you are right, that's odd. Let's check what's going on here."

  scene bg lobby

  with fade

  "They found nobody on the streets, so they decided to enter the first building they saw, the Hotel Quantum."
  
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

  with fade

  r "Hmm. Let's see who should I check tonight?"

  menu:

    "Arthur":

      $ target1 = "Arthur"

    "Ben":

      $ target1 = "Ben"

    "Cindy":

      $ target1 = "Cindy"

    "Duke":

      $ target1 = "Duke"

    "Erika":

      $ target1 = "Erika"

  scene bg room flip

  show ruby inside at left

  with fade

  r "[target1] left and didn't even lock the door. Let's have a quick look around! Maybe I can find something interesting."

  if target1 == "Arthur":

    r "A top secret document hidden under the bed about the Zeta-7 crystal locator optimized for locating Abrachian shrink ray crystals. Weird."

  if target1 == "Ben":

    r "A few strange crystals behind the toilet. They are covered with a special casing that makes them suitable for loading into a ray gun. Ben is up to no good!"

  if target1 == "Cindy":

    r "A few strange crystals behind the toilet. They are covered with a special casing that makes them suitable for loading into a ray gun. Cindy is up to no good!"

  if target1 == "Duke":

    r "A set of chemical apparatus hidden behind the mirror. They are still wet. He must have used it not long ago. But for what?"

  if target1 == "Erika":

    r "The key to the front door hidden under the door mat! How original!? So Erika was the thief!"

  scene bg room

  show ruby inside at left

  with fade

  r "Woah, this was close. I'm glad that nobody saw me. Maybe I should get some sleep then continue the investigation tomorrow."

  scene bg room

  show ruby inside at left

  with fade

  r "Oh, a message from Arthur that we should all meet in the lobby."

  scene bg lobby

  show ruby inside at left

  show erika at place (5)

  show cindy at place (2)

  show ben at place (4)

  show arthur at place(3)

  show phil inside at right

  with fade

  c "Where is Duke?"

  a "Stop playing! We already know you are the monster! You got rid of Duke, but still had the courage to come here and continue to play your part. Don't even try to attack us, we outnumber you, and you didn't even bring your gun."

  c "Who? M-me? Arthur what are you talking about? You think I'm a monster?"

  p "She isn't. She was with me. Almost the whole day."

  c "What? You were the one who kidnapped and interrogated me? But why?"

  p "I wanted to know if you are clean. And now it seems you definitely are."

  a "Then why did I found shrink ray crystals in your room?"

  c "I don't even know what you are talking about."

  r "What has the crystals got to do with the monster?"

  a "The shapeshifting monsters are not killing anybody, but they are using shrink ray guns to kidnap and enslave people."

  p "Then maybe the monster tried to frame Cindy, but luckily I took care of her."

  a "Either that or you are also lying. Maybe there are more than one monsters in this hotel. Unfortunately we cannot know for sure. Unless someone else saw something."

  if target1 == "Ben":

    menu:

      "Ben also has some crystals.":
        
        jump ben_revealed

      "Nothing.":

        jump day2

  if target1 == "Erika":

    menu:

      "Erika has the key to the front door!":

        jump erika_revealed

      "Nothing.":

        jump day2

  jump day2

label day2:

  a "Nothing? Well, then once again I ask you to stay in your rooms. If Duke had taken my advice, he might still be with us. Enough said. Back to your rooms!"

  scene bg room

  show ruby inside at left

  with fade

  r "Wow, so we do have a monster! I have to find it before more people disappear. But who could it be?"

  menu:

    "Arthur":

      $ target2 = "Arthur"

    "Ben":

      $ target2 = "Ben"

    "Cindy":

      $ target2 = "Cindy"

    "Erika":

      $ target2 = "Erika"

  scene bg room flip

  show ruby inside at left

  with fade

  if target2 == "Arthur":

    if target1 == "Arthur":

      r "Nothing new, just the document about the locator. I bet he has this locator and he used it to find the crystals in Cindy's room."

    else:

      r "A top secret document hidden under the bed about the Zeta-7 crystal locator optimized for locating Abrachian shrink ray crystals. I bet he has this locator and he used it to find the crystals in Cindy's room."

  if target2 == "Ben":

    if target1 == "Ben":

      r "Just the same crystals behind the toilet, but this time a lot less, than last time. This can't be good!"

    else: 

      r "A few strange crystals behind the toilet. They are covered with a special casing that makes them suitable for loading into a ray gun. Ben is up to no good!"

  if target2 == "Cindy":

    if target1 == "Cindy":

      r "Just the crystals, nothing else that would prove that she wasn't framed."

    else:

      r "Here they are, the crystals Arthur was talking about, but nothing else that would prove that she wasn't framed."

  if target2 == "Erika":

    if target1 == "Erika":

      r "She still has the key, but no crystals that would show that she might be a monster."

    else:

      r "The key to the front door hidden under the door mat! How original!? So Erika was the thief!"

  scene bg room

  show ruby inside at left

  with fade

  r "Ok, another successful night without being caught, but I think I get some rest now."

  scene bg room

  show ruby inside at left

  with fade

  r "A message from Cindy, that we should meet in the lobby again."

  scene bg lobby

  show ruby inside at left

  show erika at place (5)

  show cindy at place (2)

  show ben at place (4)

  show phil inside at right

  with fade

  c "Arthur is gone! The monster caught him for sure. What should we do now? It can be any of us!"

  p "No, not any of us. It's not you or me, because we were busy on the first night and Duke still disappeared. And it's also not Ben, because last night I kept him occupied."

  b "Yes, it wasn't a pleasant experience I would say."

  p "So it's Erika."

  e "Puny human, I should have taken care of you instead of Arthur. Whatever, you will never catch me!"

  hide erika

  p "Stop!"

  hide phil

  if target1 == "Ben" or target2 == "Ben":

    r "Ben, come, let's help Phil! Cindy will be ok. Right Cindy?"

    c "Sure, I guess."

    b "O-ok."

  else:

    r "Ben, stay with Cindy, we'll take care of the monster."

  scene bg room flip

  show ruby inside at left

  show phil inside at right

  if target1 == "Ben" or target2 == "Ben":

    show ben at place (1)

  with fade

  r "Did you catch her?"

  p "Yes, she ran straight to her room. I used my gun to neutralize her. She won't cause any more trouble."

  if target1 == "Ben" or target2 == "Ben":

    jump ben_revealed2

  r "Great, but we still need to find the others. They must be somewhere here in the hotel. I don't think Erika risked taking them outside."

  p "Yes, but unfortunately, we can't ask her anymore."

  r "Then let's not waste more time. I'll look for them in the rooms upstairs, you start downstairs."

  scene bg room

  show ruby inside at left

  with fade

  r "I can't belive we couldn't find them. We checked all the rooms."

  if target1 == "Cindy" or target2 == "Cindy":

    jump ben_revealed3

  scene bg room

  show ruby inside at left

  with fade

label ben_revealed:

  b "I... I also got framed."

  a "Great! And I bet you didn't stay in your room either."

  b "Oh, yes, um... I was with Erika."

  e "Hah, in your dreams, honey!"

  a "Ben, or whatever you are, stand back, you know you have no chance against all of us."

  b "But... but I'm not a monster! How could I prove it to you?"

  p "Well, if you are a monster, we have to make sure that you can't hurt anyone else. I have a ray gun with which I can neutralize you for a week. If you are innocent, you are good to go afterwards. But if nobody else disappers..."

  b "I see. Well, let it be then."

  p "Good choice, buddy."

  scene bg lobby

  show ruby inside at left

  show erika at place (5)

  show cindy at place (2)

  show arthur at place(3)

  show phil inside at right

  with fade

  a "So, our main suspect is gone, but that doesn't mean we found the monster for sure. Once again I ask you to stay in your rooms. If Duke had taken my advice, he might still be with us. Enough said. Back to your rooms!"

  scene bg room

  show ruby inside at left

  with fade

  r "Wow, I'm glad that I shared my findings about Ben. Even if he is not a monster, Phil made sure we won't have to worry about him anymore. But Arthur was right, we may not be safe yet. So let's see who should I check tonight."

  menu:

    "Arthur":

      $ target = "Arthur"

    "Cindy":

      $ target = "Cindy"

    "Erika":

      $ target = "Erika"

  scene bg room flip

  show ruby inside at left

  with fade

  r "Another open door and another empty room. Let's have a quick look around!"

  if target == "Arthur":

    r "A top secret document hidden under the bed about the Zeta-7 crystal locator optimized for locating Abrachian shrink ray crystals. Weird."

  elif target == "Cindy":

    r "Just the crystals, nothing else that would prove that she wasn't framed."

  elif target == "Erika":

    r "The key to the front door hidden under the door mat! How original!? So Erika was the thief!"

  scene bg room

  show ruby inside at left

  show monster at right

  with fade

  m "You left your door open. What a pity!"

  r "Wait!"

  scene black

  with fade

  "The End"

  # This ends the game.

  return

label ben_revealed2:

  b "Oh, no! What have you done with her, dumb human?"

  r "Hah, when I saw the crystals in you room, I knew that you are dirty. I'm glad that I brought you here."

  p "Ok, buddy, where is Arthur and Duke? Talk, if you don't want to get to Erika's fate!"

  b "You... you will shoot me down anyway, don't you?"

  r "We are not monsters. If you tell us everything we want to know, maybe we'll accidentally throw you out on Callisto when we head home."

  b "All right. Where should I start?"

  r "In the beginning. How could you open the front door?"

  b "We didn't. Ben and Erika gave up and decided to leave the hotel, the city, the moon. They stole Arthur's key, then left. We caught them a few minutes later. Our friends took them with them. They must be in one of our underground mines since then."
  
  b "The hotel's name was on the key, so we decided to take their place. We closed the door behind us, then saw you talking with Arthur. We had only one gun, so stood no chance against the three of you, so we went to our rooms instead."

  b "The first night I put some crystal in Cindy's room, just in case. It almost worked, but Phil messed it up for us. In the meantime, Erika shrank Duke, and locked him in the basement."
  
  b "The second night I couldn't do anything, again, because of Phil. And it seems Erika chose the wrong target. Arthur is also in the basement now. Here's the key. So... we are good?"

  p "We are good, buddy. Now stay still, the next time you wake up, you will be on the spectacular Callisto."

  b "Wait!"

  scene bg lobby

  show ruby inside at left

  show duke at place (4)

  show cindy at place (2)

  show arthur at place(3)

  show phil inside at right

  with fade

  a "Thank you very much for your help. I hope you will reach your rocket, before the monsters notice you. You are our only hope."

  r "Don't worry Arthur! We are back with the army in a few days. The invasion will be stopped. See you soon!"

  scene black

  with fade

  "The End"

  # This ends the game.

  return

label ben_revealed3:

  r "The only room I didn't check is Ben's. I have to give it a try."

  scene bg room flip

  show ruby inside at left

  with fade

  r "He is not here, maybe he is still with Cindy. I guess he won't mind if I look around a little."

  r "Wait, he also has some crystals. Did Erika frame him too? Or is he a monster too? Well, if he is, I don't want to face him alone. I have to get Phil first."

  scene bg room flip

  show ruby inside at left

  with fade

  r "Phil, are you in here? Your door was wide open."

  r "His clothes are on the floor but he is nowhere. So Ben is a monster! And he got him. Luckily, I know where Phil hides his gun."

  r "There we go. Now, let's get Cindy, before it's too late."

  scene bg room flip

  show ruby inside at left

  show cindy at right

  with fade

  c "Ruby! What a nice surprise!"

  r "Lock the door! I'll stay with you tonight. Ben is also a monster and got rid of Phil, but he doesn't know that we already know this. Tomorrow we'll take care of him."

  c "O-ok."

  scene bg lobby

  show ruby inside at left

  show cindy at right

  show ben at place(3)

  with fade

  r "Good morning, Ben!"

  b "Good morning, ladies."

  r "Ok, this was fun. Look, you forgot this gun in Phil's room, after you shot him. What a pity."

  b "Oh... ooooh."

  r "So talk, if you don't want to get to Erika's fate!"

  b "You... you will shoot me down anyway, don't you?"

  r "We are not monsters. If you tell us everything we want to know, maybe we'll accidentally throw you out on Callisto when we head home."

  b "All right. Where should I start?"

  r "In the beginning. How could you open the front door?"

  b "We didn't. Ben and Erika gave up and decided to leave the hotel, the city, the moon. They stole Arthur's key, then left. We caught them a few minutes later. Our friends took them with them. They must be in one of our underground mines since then."
  
  b "The hotel's name was on the key, so we decided to take their place. We closed the door behind us, then saw you talking with Arthur. We had only one gun, so stood no chance against the three of you, so we went to our rooms instead."

  b "The first night I put some crystal in Cindy's room, just in case. It almost worked, but Phil messed it up for us. In the meantime, Erika shrank Duke, and locked him in the basement."
  
  b "The second night I couldn't do anything, again, because of Phil. And it seems Erika chose the wrong target. Arthur is also in the basement now."
  
  b "Then after Phil neutralized Erika, I took her shrink ray gun, and shrank Phil too. He joined the others in the basement. Here's the key. So... we are good?"

  r "We are good. Now stay still, the next time you wake up, you will be on the spectacular Callisto."

  b "Wait!"

  scene bg lobby

  show ruby inside at left

  show duke at place (4)

  show cindy at place (2)

  show arthur at place(3)

  show phil inside at right

  with fade

  a "Thank you very much for your help. I hope you will reach your rocket, before the monsters notice you. You are our only hope."

  r "Don't worry Arthur! We are back with the army in a few days. The invasion will be stopped. See you soon!"

  scene black

  with fade

  "The End"

  # This ends the game.

  return
