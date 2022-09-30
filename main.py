def main():
    import back   
    import random as r     

    def copycat(player_response_list,*useless_stuff):
        if len(player_response_list):
            return player_response_list[len(player_response_list)-1]
        else:
            return 1
    
    def all_cooperate(*useless_stuff):
        return 1
    
    def all_cheat(*useless_stuff):
        return 0
    
    def grudger(player_response_list,*useless_stuff):
        return (not (0 in player_response_list))

    def detective(player_response_list,*useless_stuff):
        l = len(player_response_list)
        if l in [1,3,4]:
            return 1
        elif l==2:
            return 0
        else:
            if 0 in player_response_list[4:]:
                return player_response_list[l-1]
            else:
                return 0

    def copykitten(player_response_list,*useless_stuff):
        return (player_response_list[len(player_response_list)-1] or player_response_list[len(player_response_list)-2])

    def simpleton(player_response_list,bot_response_list,*useless_stuff):
        l = len(player_response_list)
        if l:
            return not (player_response_list[l-1]^bot_response_list[l-1])
        else:
            return 1

    def rando(*useless_stuff):
        return r.choice([0,1])    

    char_resp_list = [copycat,all_cooperate,all_cheat,grudger,detective,copykitten,simpleton,rando]
    character_color = {"copycat":"lightslateblue","all cooperate":"hotpink","all cheat":"red2","grudger":"yellow2","detective":"green","copykitten":"","simpleton":"","rando":""}
    character_names = list(character_color.keys())

    def add_index(L,backbutton=0):
        L.flush()
        L.add_label("COPYCAT - Hello! I start with Cooperate,",character_color["copycat"],"bahnschrift",24,(180,50),0) 
        L.add_label("and afterwards, I just copy whatever you",character_color["copycat"],"bahnschrift",24,(180,50),1.2) 
        L.add_label("did in the last round. Meow",character_color["copycat"],"bahnschrift",24,(180,50),1.2) 
        L.add_player("char1",(100,50))
        L.add_label("ALWAYS COOPERATE - Let's",character_color["all cooperate"],"bahnschrift",24,(780,50),0)
        L.add_label("be best friends! <3",character_color["all cooperate"],"bahnschrift",24,(780,50),1.2)         
        L.add_player("char2",(700,50))
        L.add_label("ALWAYS CHEAT -",character_color["all cheat"],"bahnschrift",24,(180,200),0)
        L.add_label("the strong shall",character_color["all cheat"],"bahnschrift",24,(180,200),1.2)        
        L.add_label("eat the weak",character_color["all cheat"],"bahnschrift",24,(180,200),1.2)         
        L.add_player("char3",(100,200))
        L.add_label("GRUDGER - Listen, pardner. I'll start cooperatin', and keep",character_color["grudger"],"bahnschrift",24,(480,200),0) 
        L.add_label("cooperatin', but if y'all ever cheat me, I'LL CHEAT YOU BACK",character_color["grudger"],"bahnschrift",24,(480,200),1.2) 
        L.add_label("'TIL THE END OF TARNATION.",character_color["grudger"],"bahnschrift",24,(480,200),1.2)         
        L.add_player("char4",(400,200))
        L.add_label("DETECTIVE - First: I analyze you. I start: Cooperate, Cheat, Cooperate, Cooperate. If you",character_color["detective"],"bahnschrift",24,(180,350),0)
        L.add_label("cheat back, I'll act like Copycat. If you never cheat back, I'll act like Always Cheat, to",character_color["detective"],"bahnschrift",24,(180,350),1.2)         
        L.add_label("exploit you. Elementary, my dear Watson.",character_color["detective"],"bahnschrift",24,(180,350),1.2)
        L.add_player("char5",(100,350))        
        if backbutton:
            L.add_button("<---","black","consolas",24,(1050,500,100,50),"white","yellow","green","black",[[L.flush],[L4init],[switch_section,L4,L4]])

    L0 = back.Section((1200,600),'white',"Caption")
    L1 = back.Section((1200,600),'white',"Caption")
    L2 = back.Section((1200,600),'white',"Caption")
    L3 = back.Section((1200,600),'white',"Caption")
    L4 = back.Section((1200,600),'white',"Caption")
    L5 = back.Section((1200,600),'white',"Caption")
    L6 = back.Section((1200,600),'white',"Caption")
    L7 = back.Section((1200,600),'white',"Caption")
    

    s = back.Screen((1400,700),(1300,700),"logo.png","The Evolution of Trust","cyan",[L1,L2,L3])

    def switch_section(f,t):
        if f!=0:
            f.enabled = False
        t.enabled = True
        s.flush()
        t.ready_static()
        t.ready_objects()
        t.ready_dynamic()
        s.before()
        s.place_subscreen(t.return_subscreen())
        s.after()
        s.event_handler(t.buttons,[t.ready_objects,t.ready_dynamic],1)    

    def L0init():
        L0.flush()
        L0.add_label("The",'black','bahnschrift',90,(600,50),-2)
        L0.add_label("Evolution",'black','bahnschrift',90,(600,150),-2)
        L0.add_label("of",'black','bahnschrift',90,(600,250),-2)
        L0.add_label("Trust",'black','bahnschrift',90,(600,350),-2)
        L0.add_button("Play!",'black','bahnschrift',24,(500,500,200,50),"white","yellow","green","black",[[L1init],[switch_section,L0,L1]],border_width=1)

    def L1init():
        L1.flush()
        L1.add_label("During World War I, peace broke out.","black","bahnschrift",24,(100,50),0)
        L1.add_label("It was Christmas 1914 on the Western Front. Despite strict orders not to chillax with the ","black","bahnschrift",24,(100,0),2,background_color="white")
        L1.add_label("enemy, British and German soldiers left their trenches, crossed No Man's Land, and ","black","bahnschrift",24,(100,0),1.2)
        L1.add_label("gathered to bury their dead, exchange gifts, and play games.","black","bahnschrift",24,(100,0),1.2)
        L1.add_label("Meanwhile: it's 2022, the West has been at peace for decades, and wow, we suck at trust. ","black","bahnschrift",24,(100,0),2)
        L1.add_label("Surveys show that, over the past forty years, fewer and fewer people say they trust each ","black","bahnschrift",24,(100,0),1.2)
        L1.add_label("other. So here's our puzzle:","black","bahnschrift",24,(100,0),1.2)
        L1.add_label("Why, even in peacetime, do friends become enemies?","green","bahnschrift",24,(100,0),2,italic=True)
        L1.add_label("And why, even in wartime, do enemies become friends?","green","bahnschrift",24,(100,0),1.2,italic=True)
        L1.add_label("I think ","black","bahnschrift",24,(100,0),2)
        L1.add_label("game theory","red","bahnschrift",24,(100,0))
        L1.add_label(" can help explain our epidemic of distrust - and how we can fix it! ","black","bahnschrift",24,(100,0))
        L1.add_label("So, to understand all this...","black","bahnschrift",24,(100,0),1.2)
        L1.add_button("...let's play a game.","black","bahnschrift",24,(450,500,300,50),"white","yellow","green","black",[[L2init],[switch_section,L1,L2]])    

    def L2init():
        L2.flush()
        L2.add_label("THE GAME OF TRUST","black","bahnschrift",32,(600,50),-2)
        L2.add_label("You have one choice. In front of you is a machine: if you put a coin in the machine, the other","black","bahnschrift",24,(100,100),0)
        L2.add_label("player gets three coins - and vice versa. You both can either choose to COOPERATE (put in coin),","black","bahnschrift",24,(100,100),1.2)
        L2.add_label("or CHEAT (don't put in coin).","black","bahnschrift",24,(100,100),1.2)
        L2.add_label("you","black","bahnschrift",18,(280,220),-2)
        L2.add_label("other player","black","bahnschrift",18,(890,220),-2)
        L2.config_machine((475,200,250,200),0,0,0,0)
        L2.add_player("char0",(280,330))
        L2.add_player("char1",(900,330),1)
        L2.add_label("Let's say the other player cheats, and doesn't put in a coin.","black","bahnschrift",20,(600,430),-2)
        L2.add_label("What should you do?","black","bahnschrift",20,(600,460),-2,italic=1) 
        L2v = back.TempValues()
        L2v.stepnumber = 0
        def L2resp(resp):
            if L2v.stepnumber==0:
                L2.config_machine((475,200,250,200),0,1,0,1)
                L2v.stepnumber+=1
                L2.labels = []
                if resp:                
                    L2.add_label("Alas, turning the other cheek just gets you slapped!","black","bahnschrift",24,(600,70),-2)               
                else:
                    L2.add_label("Exactly! Why let that moocher mooch off of you?","black","bahnschrift",24,(600,70),-2)
                L2.add_label("If you cooperate & they cheat, you lose a coin while they gain three (score: -1 vs +3).","black","bahnschrift",24,(600,100),-2)
                L2.add_label("However, if you both cheat, neither of you gain or lose anything (score: 0 vs 0).","black","bahnschrift",24,(600,130),-2)
                L2.add_label("Therefore: you should CHEAT.","black","bahnschrift",24,(600,160),-2,bold=1) 
                L2.add_label("But let's say the other player cooperates, and puts in a coin.","black","bahnschrift",20,(600,430),-2)
                L2.add_label("What should you do now?","black","bahnschrift",20,(600,460),-2,italic=1) 
            elif L2v.stepnumber==1:
                L2.config_machine((475,200,250,200),1,1,1,1)
                L2.labels = []
                if resp:                
                    L2.add_label("Sure, seems like the right thing to do... OR IS IT??","black","bahnschrift",24,(600,70),-2)               
                else:
                    L2.add_label("Wow, that's mean... and also the correct answer!","black","bahnschrift",24,(600,70),-2)
                L2.add_label("Because if you both cooperate, you both give up a coin to gain three (score: +2 vs +2).","black","bahnschrift",24,(600,100),-2)
                L2.add_label("But if you cheat & they cooperate, you gain three coins at their cost of one (score: +3 vs -1).","black","bahnschrift",24,(600,130),-2)
                L2.add_label('Therefore: you "should" still CHEAT.',"black","bahnschrift",24,(600,160),-2,bold=1) 
                L2.add_label("And that's our dilemma. Trust is nice, but it can let others take advantage of you - or shoot you as you come","black","bahnschrift",20,(100,430),0)
                L2.add_label("unarmed out of a trench. Sometimes, distrust is rational! But now, what happens if we play this game...","black","bahnschrift",20,(100,460),1.5) 
                L2.buttons = []
                L2.add_button("...more than once?","black","bahnschrift",24,(450,500,300,50),"white","yellow","green","black",[[L3init],[switch_section,L2,L3]])
        L2.add_button("COOPERATE","black","bahnschrift",24,(350,500,200,50),"white","yellow","green","black",[[L2resp,1],[switch_section,L2,L2]])
        L2.add_button("CHEAT","black","bahnschrift",24,(650,500,200,50),"white","yellow","green","black",[[L2resp,0],[switch_section,L2,L2]])
        
    def L3init():
        L3.flush()
        L3.add_label("Now, let's play for real. You'll be playing against 5 different opponents,","black","bahnschrift",24,(600,40),-2) 
        L3.add_label('each with their own game "strategy". With each opponent, you\'ll play',"black","bahnschrift",24,(600,70),-2) 
        L3.add_label("anywhere between 3 to 7 rounds (You won't know in advance when the","black","bahnschrift",24,(600,100),-2) 
        L3.add_label("last round is). Can you trust them? Or rather... can they trust you?","black","bahnschrift",24,(600,130),-2) 
        L3.add_label("Pick your first, real move.","black","bahnschrift",20,(600,430),-2)
        L3.add_label("Choose wisely.","black","bahnschrift",20,(600,460),-2,bold=1)    
        L3.config_machine((475,200,250,200),0,0,0,0,1,1,1,1)
        L3.add_player("char1",(860,330),1)
        L3.add_player("char0",(280,330))    
        L3v = back.TempValues()
        L3v.stepnumber = 0
        L3v.character = 0
        #L3v.number_of_rounds = [r.randint(3,7) for i in range(5)]
        L3v.number_of_rounds = [5,4,4,5,7]
        L3v.current_prl = []
        L3v.current_brl = []
        L3v.current_score = 0
        L3v.step_score = [0,0]
        def L3index():
            L3.flush()
            add_index(L3)
            L3.add_label("Now, what if these characters were to play...","black","bahnschrift",24,(600,450),-2) 
            L3.add_button("...against each other?","black","bahnschrift",24,(400,500,400,50),"white","yellow","green","black",[[L4init],[switch_section,L3,L4]])
        def L3resp(resp):
            botresp = char_resp_list[L3v.character](L3v.current_prl,L3v.current_brl)
            L3v.current_brl.append(botresp)
            L3v.current_prl.append(resp)      
            lac = [0,0,0,0]
            if botresp+resp==2:
                lac[2]=1
                L3v.step_score[0]+=2
                L3v.current_score+=2
                L3v.step_score[1]+=2            
            elif botresp and not resp:
                lac[1]=1
                L3v.step_score[0]+=3
                L3v.current_score+=3
                L3v.step_score[1]-=1
            elif resp and not botresp:
                lac[0]=1
                L3v.step_score[0]-=1
                L3v.current_score-=1
                L3v.step_score[1]+=3 
            else:
                lac[3]=1
            L3.config_machine((475,200,250,200),*lac,1,1,1,1)  
            L3v.stepnumber+=1
            L3.labels = []
            if L3v.stepnumber==L3v.number_of_rounds[L3v.character]:
                L3v.character+=1
                L3v.stepnumber=0
                L3v.current_prl = []
                L3v.current_brl = []
                L3v.step_score = [0,0]
                L3.add_player("char%d"%(L3v.character+1),(860,330),1)
                L3.add_player("char0",(280,330))  
            if L3v.character==5:
                L3.flush()
                L3.add_label("And your total score is...","black","bahnschrift",24,(100,40),0) 
                L3.add_label("%d"%L3v.current_score,"black","bahnschrift",72,(100,40),0.4)
                if L3v.current_score>35:
                    L3.add_label("which is pretty good! The maximum and minimum scores are","black","bahnschrift",24,(100,40),1.2) 
                elif L3v.current_score>20:
                    L3.add_label("which is not bad! (the lowest & highest possible","black","bahnschrift",24,(100,40))
                else:
                    L3.add_label(" which is not bad! (the lowest & highest possible","black","bahnschrift",24,(100,40))
                L3.add_label("scores are 7 and 49, respectively)","black","bahnschrift",24,(100,40),1.2)
                L3.add_label("So who were these strange characters you just played against?","black","bahnschrift",24,(100,200),0) 
                #L3.add_label("%d"%L3v.current_score,"black","bahnschrift",48,(600,40),0.6)                                 
                L3.add_button("Let's find out!","black","bahnschrift",24,(450,500,300,50),"white","yellow","green","black",[[L3index],[switch_section,L3,L3]])
                return
            L3.add_label("opponent: %d of 5"%(L3v.character+1),"black","bahnschrift",20,(600,50),-2)
            L3.add_label("your total score: %d"%(L3v.current_score),"black","bahnschrift",20,(600,80),-2)        
            L3.add_label("%d ~ %d"%tuple(L3v.step_score),"black","bahnschrift",70,(600,120),-2)
        L3.add_button("COOPERATE","black","bahnschrift",24,(350,500,200,50),"white","yellow","green","black",[[L3resp,1],[switch_section,L3,L3]])
        L3.add_button("CHEAT","black","bahnschrift",24,(650,500,200,50),"white","yellow","green","black",[[L3resp,0],[switch_section,L3,L3]])

    def L4init():
        L4.flush()
        L4.add_label("It's tournament time! Each character will now","black","bahnschrift",24,(600,40),0)
        L4.add_label("play against every other character: that's 10","black","bahnschrift",24,(600,40),1.2)
        L4.add_label("paired matches, and 10 rounds per match.","black","bahnschrift",24,(600,40),1.2)
        L4.add_label("Who do you think will get the ","black","bahnschrift",24,(600,140),0)
        L4.add_label("highest total score?","black","bahnschrift",24,(600,140),italic=1)    
        L4.add_label("Think carefully about it... and then ","black","bahnschrift",24,(600,140),1.2)
        L4.add_label("PLACE YOUR","red","bahnschrift",24,(600,140))
        L4.add_label("BETS:","red","bahnschrift",24,(600,140),1.2)
        L4.add_button("copycat","black","bahnschrift",20,(650,250,200,50),character_color["copycat"],"white",character_color["copycat"],"black",[[switch_section,L4,L0]])
        L4.add_button("all cooperate","black","bahnschrift",20,(900,250,200,50),character_color["all cooperate"],"white",character_color["all cooperate"],"black",[[switch_section,L4,L0]])
        L4.add_button("all cheat","black","bahnschrift",20,(650,350,200,50),character_color["all cheat"],"white",character_color["all cheat"],"black",[[switch_section,L4,L0]])
        L4.add_button("grudger","black","bahnschrift",20,(900,350,200,50),character_color["grudger"],"white",character_color["grudger"],"black",[[switch_section,L4,L0]])
        L4.add_button("detective","black","bahnschrift",20,(775,450,200,50),character_color["detective"],"white",character_color["detective"],"black",[[switch_section,L4,L0]])
        L4.add_button("?","black","bahnschrift",24,(1050,500,100,50),"white","yellow","green","black",[[add_index,L4,1],[switch_section,L4,L4]])  

    def L5init():
        L5.flush()
        L5.add_label("As cool as Copycat is, it has a huge, fatal weakness I haven't mentioned","black","bahnschrift",24,(600,70),-2)
        L5.add_label("yet. To understand the problem, let's say two Copycats are playing against","black","bahnschrift",24,(600,100),-2)
        L5.add_label("each other:","black","bahnschrift",24,(600,130),-2)
        L5.config_machine((475,200,250,200),0,0,0,0,1,1,1,1)
        L5.add_player("char1",(280,330))
        L5.add_player("char1",(900,330),1)
        L5.add_label("Being \"nice\" players, both their first moves will be:","black","bahnschrift",24,(600,450),-2)
        L5.add_button("COOPERATE","black","bahnschrift",24,(500,500,200,50),"white","yellow","green","black",[[L0init],[switch_section,L5,L0]]) 

    def L6init():
        L6.flush()
        L6v = back.TempValues()
        L6v.charlist = [*[character_names[0]]*5,*[character_names[1]]*5,*[character_names[2]]*5,*[character_names[3]]*4]
        L6v.scorelist = [*[20]*19]
        L6.config_circle(L6v.charlist,L6v.scorelist,150,(100,50,500,500),highlight=-1,linecolor="grey")        
        L6.add_button("START","black","bahnschrift",18,(300,245,100,30),"white","yellow","green","black",[[L0init],[switch_section,L6,L0]])
        L6.add_button("STEP","black","bahnschrift",18,(300,285,100,30),"white","yellow","green","black",[[L0init],[switch_section,L6,L0]])
        L6.add_button("RESET","black","bahnschrift",18,(300,325,100,30),"white","yellow","green","black",[[L0init],[switch_section,L6,L0]])

    def L7init():
        L7.flush()
        #L7v = back.TempValues()
        def L7next():
            L7.flush()            
            L7.add_label("If there's one big takeaway from ","black","bahnschrift",24,(100,50),0)
            L7.add_label("all","black","bahnschrift",24,(100,50),italic=1)
            L7.add_label(" of game theory, it's this:","black","bahnschrift",24,(100,50))            
            L7.add_label("What the game is, defines what the players do. Our problem today isn't just that people are","black","bahnschrift",24,(100,0),2)
            L7.add_label("losing trust, it's that our environment acts against the evolution of trust.","black","bahnschrift",24,(100,0),1.2)
            L7.add_label("That may seem cynical or naive -- that we're \"merely\" products of our environment -- but","black","bahnschrift",24,(100,0),2)
            L7.add_label("as game theory reminds us, we are each others' environment. In the short run, the game","black","bahnschrift",24,(100,0),1.2)
            L7.add_label("defines the players. But in the long run, it's us players who define the game.","black","bahnschrift",24,(100,0),1.2)
            L7.add_label("So, do what you can do, to create the conditions necessary to evolve trust. Build relationships.","black","bahnschrift",24,(100,0),2)
            L7.add_label("Find win-wins. Communicate clearly. Maybe then, we can stop firing at each other, get out of","black","bahnschrift",24,(100,0),1.2)
            L7.add_label("our own trenches, cross No Man's Land to come together...","black","bahnschrift",24,(100,0),1.2)
            L7.add_label("and all learn...","black","bahnschrift",36,(600,420),-2)
            L7.add_label("...to live and let live.","black","bahnschrift",48,(600,500),-2)
            #L7.add_label("game theory","red","bahnschrift",24,(100,0))
            #L7.add_label(" can help explain our epidemic of distrust - and how we can fix it! ","black","bahnschrift",24,(100,0))
            #L7.add_label("So, to understand all this...","black","bahnschrift",24,(100,0),1.2)
        L7.add_label("Game theory has shown us the three things we need for the evolution of trust:","black","bahnschrift",24,(100,50),0)
        L7.add_label("1. REPEAT INTERACTIONS","lightslateblue","bahnschrift",48,(130,100),0)
        L7.add_label("Trust keeps a relationship going, but you need the knowledge of possible future","black","bahnschrift",24,(130,160),0)
        L7.add_label("repeat interactions before trust can evolve.","black","bahnschrift",24,(130,160),1.2)
        L7.add_label("2. POSSIBLE WIN-WINS","green","bahnschrift",48,(130,240),0)
        L7.add_label("You must be playing a non-zero-sum game, a game where it's at least possible","black","bahnschrift",24,(130,300),0)
        L7.add_label("that both players can be better off - a win-win.","black","bahnschrift",24,(130,300),1.2)
        L7.add_label("3. LOW MISCOMMUNICATION","red2","bahnschrift",48,(130,380),0)
        L7.add_label("If the level of miscommunication is too high, trust breaks down. But when there's a","black","bahnschrift",24,(130,440),0)
        L7.add_label("little bit of miscommunication, it pays to be more forgiving.","black","bahnschrift",24,(130,440),1.2)
        L7.add_label("Of course, real-world trust is affected by much more","black","bahnschrift",18,(100,520),0)
        L7.add_label("than this. There's reputation, shared values, contracts,","black","bahnschrift",18,(100,520),1.2)
        L7.add_label("cultural markers, blah blah blah. And let's not forget...","black","bahnschrift",18,(100,520),1.2)
        L7.add_button("...the biggest lesson.","black","bahnschrift",24,(600,525,400,50),"white","yellow","green","black",[[L7next],[switch_section,L7,L7]])
        
        #L7.add_label("Game theory has shown us the three things we need for the evolution of trust:","black","bahnschrift",24,(100,50),0)
        #L7.add_label("Game theory has shown us the three things we need for the evolution of trust:","black","bahnschrift",24,(100,50),0)
        
    L7init()
    switch_section(0,L7)

    while 1:     
        while L0.enabled:
            s.before()
            s.place_subscreen(L0.return_subscreen())
            s.after()
            s.event_handler(L0.buttons,[L0.ready_objects,L0.ready_dynamic])   
        while L1.enabled:
            s.before()
            s.place_subscreen(L1.return_subscreen())
            s.after()
            s.event_handler(L1.buttons,[L1.ready_objects,L1.ready_dynamic])
        while L2.enabled:
            s.before()
            s.place_subscreen(L2.return_subscreen())
            s.after()
            s.event_handler(L2.buttons,[L2.ready_objects,L2.ready_dynamic])
        while L3.enabled:
            s.before()
            s.place_subscreen(L3.return_subscreen())
            s.after()
            s.event_handler(L3.buttons,[L3.ready_objects,L3.ready_dynamic])
        while L4.enabled:
            s.before()
            s.place_subscreen(L4.return_subscreen())
            s.after()
            s.event_handler(L4.buttons,[L4.ready_objects,L4.ready_dynamic])
        while L5.enabled:
            s.before()
            s.place_subscreen(L5.return_subscreen())
            s.after()
            s.event_handler(L5.buttons,[L5.ready_objects,L5.ready_dynamic])
        while L6.enabled:
            s.before()
            s.place_subscreen(L6.return_subscreen())
            s.after()
            s.event_handler(L6.buttons,[L6.ready_objects,L6.ready_dynamic])
        while L7.enabled:
            s.before()
            s.place_subscreen(L7.return_subscreen())
            s.after()
            s.event_handler(L7.buttons,[L7.ready_objects,L7.ready_dynamic])
        

if __name__ == "__main__":
    main()