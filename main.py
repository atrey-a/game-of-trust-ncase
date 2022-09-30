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

    L0 = back.Section((1200,600),'white',"Caption")
    L1 = back.Section((1200,600),'white',"Caption")
    L2 = back.Section((1200,600),'white',"Caption")
    L3 = back.Section((1200,600),'white',"Caption")
    L4 = back.Section((1200,600),'white',"Caption")

    s = back.Screen((1400,700),(1300,700),"logo.png","The Evolution of Trust","grey",[L1,L2,L3])

    def switch_section(f,t):
        if f!=0:
            f.enabled = False
        t.enabled = True
        s.flush()
        t.ready_static()
        t.ready_dynamic()
        t.ready_objects()
        s.before()
        s.place_subscreen(t.return_subscreen())
        s.after()
        s.event_handler(t.buttons,[t.ready_dynamic,t.ready_objects],1)    

    L0.add_label("The",'black','bahnschrift',90,(600,50),-2)
    L0.add_label("Evolution",'black','bahnschrift',90,(600,150),-2)
    L0.add_label("of",'black','bahnschrift',90,(600,250),-2)
    L0.add_label("Trust",'black','bahnschrift',90,(600,350),-2)
    L0.add_button("Play!",'black','bahnschrift',24,(500,500,200,50),"white","yellow","green","black",[[switch_section,L0,L1]],border_width=1)

    L1.add_label("During World War I, peace broke out.","black","bahnschrift",24,(100,50),0,background="white")
    L1.add_label("It was Christmas 1914 on the Western Front. Despite strict orders not to chillax with the ","black","bahnschrift",24,(100,0),2,background="white")
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
    L1.add_button("...let's play a game.","black","bahnschrift",24,(450,500,300,50),"white","yellow","green","black",[[switch_section,L1,L2]])    

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
            L2.add_button("...more than once?","black","bahnschrift",24,(450,500,300,50),"white","yellow","green","black",[[switch_section,L2,L3]])
    L2.add_button("COOPERATE","black","bahnschrift",24,(350,500,200,50),"white","yellow","green","black",[[L2resp,1],[switch_section,L2,L2]])#[switch_section,L2,L3],
    L2.add_button("CHEAT","black","bahnschrift",24,(650,500,200,50),"white","yellow","green","black",[[L2resp,0],[switch_section,L2,L2]])    #[switch_section,L2,L3],
    
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
    L3v.number_of_rounds = [10 for i in range(5)]
    L3v.current_prl = []
    L3v.current_brl = []
    L3v.current_score = 0
    L3v.step_score = [0,0]
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
            L3.buttons=[]
            L3.add_button("Next","black","bahnschrift",24,(450,500,300,50),"white","yellow","green","black",[[switch_section,L3,L4]])
            return
        L3.add_label("opponent: %d of 5"%(L3v.character+1),"black","bahnschrift",20,(600,50),-2)
        L3.add_label("your total score: %d"%(L3v.current_score),"black","bahnschrift",20,(600,80),-2)        
        L3.add_label("%d ~ %d"%tuple(L3v.step_score),"black","bahnschrift",70,(600,120),-2)
    L3.add_button("COOPERATE","black","bahnschrift",24,(350,500,200,50),"white","yellow","green","black",[[L3resp,1],[switch_section,L3,L3]])
    L3.add_button("CHEAT","black","bahnschrift",24,(650,500,200,50),"white","yellow","green","black",[[L3resp,0],[switch_section,L3,L3]])

    L4.add_button("Go to L0","black","calibri",20,(500,500,200,50),"white","yellow","green","black",[[switch_section,L4,L0]])

    switch_section(0,L0)

    while 1:     
        while L0.enabled:
            s.before()
            s.place_subscreen(L0.return_subscreen())
            s.after()
            s.event_handler(L0.buttons,[L0.ready_dynamic])   
        while L1.enabled:
            s.before()
            s.place_subscreen(L1.return_subscreen())
            s.after()
            s.event_handler(L1.buttons,[L1.ready_dynamic])
        while L2.enabled:
            s.before()
            s.place_subscreen(L2.return_subscreen())
            s.after()
            s.event_handler(L2.buttons,[L2.ready_dynamic,L2.ready_objects])
        while L3.enabled:
            s.before()
            s.place_subscreen(L3.return_subscreen())
            s.after()
            s.event_handler(L3.buttons,[L3.ready_dynamic])
        while L4.enabled:
            s.before()
            s.place_subscreen(L4.return_subscreen())
            s.after()
            s.event_handler(L4.buttons,[L4.ready_dynamic])

if __name__ == "__main__":
    main()