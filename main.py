print('''
****************************************************************************************************************
         ___ . .  _                                                                                             
"T$$$P"   |  |_| |_                                                                                             
 :$$$     |  | | |_                                                                                             
 :$$$                                                      "T$$$$$$$b.                                          
 :$$$     .g$$$$$p.   T$$$$b.    T$$$$$bp.                   BUG    "Tb      T$b      T$P   .g$P^^T$$  ,gP^^T$$ 
  $$$    d^"     "^b   $$  "Tb    $$    "Tb    .s^s. :sssp   $$$     :$; T$$P $^b.     $   dP"     `T :$P    `T
  :$$   dP         Tb  $$   :$;   $$      Tb  d'   `b $      $$$     :$;  $$  $ `Tp    $  d$           Tbp.   
  :$$  :$;         :$; $$   :$;   $$      :$; T.   .P $^^    $$$    .dP   $$  $   ^b.  $ :$;            "T$$p.  
  $$$  :$;         :$; $$...dP    $$      :$;  `^s^' .$.     $$$...dP"    $$  $    `Tp $ :$;     "T$$      "T$b 
  $$$   Tb.       ,dP  $$"""Tb    $$      dP ""$""$" "$"$^^  $$$""T$b     $$  $      ^b$  T$       T$ ;      $$;
  $$$    Tp._   _,gP   $$   `Tb.  $$    ,dP    $  $...$ $..  $$$   T$b    :$  $       `$   Tb.     :$ T.    ,dP 
  $$$;    "^$$$$$^"   d$$     `T.d$$$$$P^"     $  $"""$ $"", $$$    T$b  d$$bd$b      d$b   "^TbsssP" 'T$bgd$P  
  $$$b.____.dP                                 $ .$. .$.$ss,d$$$b.   T$b.                                       
.d$$$$$$$$$$P                                                         `T$b.                                     
                                                                        "^^"                                    
****************************************************************************************************************
''')
print("Welcome to Gladden Fields.")
print("Your mission is to find the Ring.") 

d1 = input('''You're at a cross road. Where do you want to go? Type "Left" or "Right"\n''')
d1t = d1.lower()
if d1t == "left":
  d2 = input('''You came to a lake. There is a island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swin across.\n''')
  d2t = d2.lower()

  if d2t == "wait":
    d2 = input('''You arrive at Gladden Fields Village unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n''')
    d3t = d2.lower()


    if d3t == "yellow":
      print("Congrats!! You find the ring! But you have to destroy in the Mount Doom. Good Luck.")
    elif d3t == "blue":
      print("You have entered in a room full of beasts and they are hungry, you are the only food in the room. Game Over.")
    elif d3t == "red":
      print("You are in Narnia and can't go back, you have to find Aslan now. Good Luck.")
    else:
      print("Game Over")

  elif d2t == "swim":
    print('''
                   _.---._     .---.
          __...---' .---. `---'-.   `.
~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
  -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
   ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
      ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
       ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
          ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
              ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                  ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                       ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
''')
    print("The lake is full of crocodile. Game Over.")

elif d1t == "right":
  print('''
************************
        ,      ,
       /(.-""-.)\

   |\  \/      \/  /|
   | \ / =.  .= \ / |
   \( \   o\/o   / )/
    \_, '-/  \-' ,_/
      /   \__/   \

      \ \__/\__/ /
    ___\ \|--|/ /___
  /`    \      /    `\

 /       '----'       \ 
*************************
''')
  print("You find a goblin. Game Over.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
