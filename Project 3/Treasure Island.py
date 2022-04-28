print('''
                            ==(W{==========-      /===-                        
                              ||  (.--.)         /===-_---~~~~~~~~~------____  
                              | \_,|**|,__      |===-~___                _,-' `
                 -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~      
             ______-==|        /`\_. .__/\ \    | |  \\           _-~`         
       __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'             
    _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /               
  .'        /       |   \\      /~\___/~~\/  /' /        \   /'                
 /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'                  
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`                   
                  \_|      /        _) | ;  ),   __--~~                        
                    '~~--_/      _-~/- |/ \   '-~ \                            
                   {\__--_/}    / \\_>-|)<__\      \                           
                   /'   (_/  _-~  | |__>--<__|      |                          
                  |   _/) )-~     | |__>--<__|      |                          
                  / /~ ,_/       / /__>---<__/      |                          
                 o-o _//        /-~_>---<__-~      /                           
                 (^(~          /~_>---<__-      _-~                            
                ,/|           /__>--<__/     _-~                               
             ,//('(          |__>--<__|     /                  .----_          
            ( ( '))          |__>--<__|    |                 /' _---_~\        
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\      
        ,/,'//( (             \__>--<__\    \            /'  //        ||      
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'       
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/                  
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~                    
   ;'( ')/ ,)(                              ~~~~~~~~~~                         
  ' ') '( (/                                                                   
    '   '  ` ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
LorR = input('As you are exploring the island you discovered a crossroad. Where do you want to go> Type "Left" or "Right"').lower()

if LorR == "left":
    SorW = input(' You have come to a lake that water seems clear as day with no creature in sight. There is an island in the middle of the lake and a boat slowly drifting towards you but it is quite foggy so you can tell whether someone or something is on the boat. What will you do? Type "wait" to wait for the boat. Type "swim" to swim across. ').lower()
    if SorW == "wait":
        RorGorB = input('You arrive at the island unharmed. There is a house with 3 doors. One "red", one "green", and one "blue".').lower()
        if RorGorB == "green":
            print("You have entered the room and notice a tablet saying only the purest of sould would inherit this lords treasure. You are worth of my riches. The buildint shakes and the treasure appears. You win!")
        elif RorGorB == "red":
            print('You entered the room and seen a box full of gold and sprint directly for it. Little did you know the Lords Dragon was waiting for you and burned you alive once you touched the gold. Game Over')
        else:
            print("You entered a room filled with beast and met your end. Game Over!")
    elif SorW == "swim":
        print("The gatekeeper that was on the boat spots you and is furious that you infected his lords pure water with your filth and summons a army of sharks to devour you. Game Over.")
elif LorR == "right":
    print("You started walking down the right and fell in to a hole full of spikes. Game Over.")

