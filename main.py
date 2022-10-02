def main():
    import back
    import random as r

    main_font = "bahnschrift"

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
        return int(not (0 in player_response_list))

    def detective(player_response_list,*useless_stuff):
        l = len(player_response_list)
        if l in [0,2,3]:
            return 1
        elif l==1:
            return 0
        else:
            if 0 in player_response_list[2:]:
                return player_response_list[l-1]
            else:
                return 0

    def copykitten(player_response_list,*useless_stuff):
        if len(player_response_list) < 3:
            return 1
        return (player_response_list[len(player_response_list)-1] or player_response_list[len(player_response_list)-2])

    def simpleton(player_response_list,bot_response_list,*useless_stuff):
        l = len(player_response_list)
        if l:
            return int(not (player_response_list[l-1]^bot_response_list[l-1]))
        else:
            return 1

    def rando(*useless_stuff):
        return r.choice([0,1])

    char_fun_dict = {"copycat":copycat,"all cooperate":all_cooperate,"all cheat":all_cheat,"grudger":grudger,"detective":detective,"copykitten":copykitten,"simpleton":simpleton,"random":rando}
    char_resp_list = [copycat,all_cooperate,all_cheat,grudger,detective,copykitten,simpleton,rando]
    character_color = {"copycat":"lightslateblue","all cooperate":"hotpink","all cheat":"red2","grudger":"yellow2","detective":"green","copykitten":"deeppink1","simpleton":"black","random":"brown"}
    character_names = list(character_color.keys())
    imgloader = {"copycat":"char1","all cooperate":"char2","all cheat":"char3","grudger":"char4","detective":"char5","copykitten":"char6","simpleton":"char7","random":"char8"}

    def computescores(playlist,botlist,givecoin=1,getcoin=3):
        scores = [0,0]
        for i in range(len(playlist)):
            if playlist[i]:
                scores[1]+=getcoin
                scores[0]-=givecoin
            if botlist[i]:
                scores[0]+=getcoin
                scores[1]-=givecoin
        return scores

    def godstep(godplays,botplays,botname,givecoin=1,getcoin=3,maxsteps=8):
        godplay = list(godplays)
        botplay = list(botplays)
        best = [0,0]
        firstmove = []
        currentplay = [godplay,botplay]
        maxv = givecoin+getcoin
        def descend(step):
            s = computescores(currentplay[0],currentplay[1],givecoin,getcoin)
            if step*maxv<best[1]-s[0]+s[1]:    #PRUNING
                return
            if step==0:
                if (s[0]-s[1])>best[1]:
                    best[1] = s[0]-s[1]
                    best[0]=len(firstmove)
                return
            currentplay[1].append(char_fun_dict[botname](currentplay[0],currentplay[1]))
            currentplay[0].append(0)
            descend(step-1)
            currentplay[0][len(currentplay[0])-1] = 1
            if step==maxsteps:
                firstmove.append(0)
            descend(step-1)
            currentplay[0] = currentplay[0][:len(currentplay[0])-1]
        descend(maxsteps)
        return best[0]

    def tourney(bot1,bot2,rounds,givecoins=1,getcoins=3):
        scores = [0,0]
        resplists = [[],[]]
        for i in range(rounds):
            r1 = char_fun_dict[bot1](resplists[1],resplists[0])
            r2 = char_fun_dict[bot2](resplists[0],resplists[1])
            resplists[0].append(r1)
            resplists[1].append(r2)
            if r1:
                scores[0]-=givecoins
                scores[1]+=getcoins
            if r2:
                scores[1]-=givecoins
                scores[0]+=getcoins
        return (scores,resplists)

    def multitourney(charlist,err=0,resplist=[],givecoins=1,getcoins=3):
        n=len(charlist)
        scorelist = [*[0]*n]
        if resplist==[]:
            rxc = [[[[],[]] for j in range(i+1,n)] for i in range(n)][:n-1]
            resplist.extend(rxc)
        for i in range(n-1):
            for j in range(i+1,n):
                r1 = errify(char_fun_dict[charlist[i]](resplist[j-i-1][i][1],resplist[j-i-1][i][0]),err)
                r2 = errify(char_fun_dict[charlist[j]](resplist[j-i-1][i][0],resplist[j-i-1][i][1]),err)
                if r1:
                    scorelist[i]-=givecoins
                    scorelist[j]+=getcoins
                if r2:
                    scorelist[j]-=givecoins
                    scorelist[i]+=getcoins
                resplist[j-i-1][i][0].append(r1)
                resplist[j-i-1][i][1].append(r2)
        return scorelist,resplist

    def errify(ans,percent):
        x = r.randint(1,100)
        if x<=percent:
            return 1-ans
        return ans

    def add_index(L,backbutton=0):
        L.flush()
        L.add_label("COPYCAT - Hello! I start with Cooperate,",character_color["copycat"],main_font,24,(180,50),0)
        L.add_label("and afterwards, I just copy whatever you",character_color["copycat"],main_font,24,(180,50),1.2)
        L.add_label("did in the last round. Meow",character_color["copycat"],main_font,24,(180,50),1.2)
        L.add_player("char1",(100,50))
        L.add_label("ALWAYS COOPERATE - Let's",character_color["all cooperate"],main_font,24,(780,50),0)
        L.add_label("be best friends! <3",character_color["all cooperate"],main_font,24,(780,50),1.2)
        L.add_player("char2",(700,50))
        L.add_label("ALWAYS CHEAT -",character_color["all cheat"],main_font,24,(180,200),0)
        L.add_label("the strong shall",character_color["all cheat"],main_font,24,(180,200),1.2)
        L.add_label("eat the weak",character_color["all cheat"],main_font,24,(180,200),1.2)
        L.add_player("char3",(100,200))
        L.add_label("GRUDGER - Listen, pardner. I'll start cooperatin', and keep",character_color["grudger"],main_font,24,(480,200),0)
        L.add_label("cooperatin', but if y'all ever cheat me, I'LL CHEAT YOU BACK",character_color["grudger"],main_font,24,(480,200),1.2)
        L.add_label("'TIL THE END OF TARNATION.",character_color["grudger"],main_font,24,(480,200),1.2)
        L.add_player("char4",(400,200))
        L.add_label("DETECTIVE - First: I analyze you. I start: Cooperate, Cheat, Cooperate, Cooperate. If you",character_color["detective"],main_font,24,(180,350),0)
        L.add_label("cheat back, I'll act like Copycat. If you never cheat back, I'll act like Always Cheat, to",character_color["detective"],main_font,24,(180,350),1.2)
        L.add_label("exploit you. Elementary, my dear Watson.",character_color["detective"],main_font,24,(180,350),1.2)
        L.add_player("char5",(100,350))
        if backbutton:
            L.add_button("<---","black","consolas",24,(1050,500,100,50),"white","yellow","green","black",[[L.flush],[L4init],[s.switch_section,L4,L4]])

    L0 = back.Section((1200,600),'white')
    L1 = back.Section((1200,600),'white',"Introduction")
    L2 = back.Section((1200,600),'white',"One Game")
    L3 = back.Section((1200,600),'white',"Repeated Game")
    L4 = back.Section((1200,600),'white',"Tournament")
    L5 = back.Section((1200,600),'white',"Making Mistaeks")
    L6 = back.Section((1200,600),'white',"Sandbox Mode")
    L7 = back.Section((1200,600),'white',"God Player")
    L8 = back.Section((1200,600),'white',"Conclusion")

    s = back.Screen((1400,700),(1300,700),"logo.png","The Evolution of Trust",L0,"cyan")
    s.Ls = [L0,L1,L2,L3,L4,L5,L6,L7,L8]

    def L0init():
        L0.flush()
        L0.add_label("The",'black','bahnschrift',90,(600,50),-2)
        L0.add_label("Evolution",'black','bahnschrift',90,(600,150),-2)
        L0.add_label("of",'black','bahnschrift',90,(600,250),-2)
        L0.add_label("Trust",'black','bahnschrift',90,(600,350),-2)
        L0.add_button("Play!",'black','bahnschrift',24,(500,500,200,50),"white","yellow","green","black",[[L1init],[s.switch_section,L0,L1]])

    def L1init():
        L1.flush()
        L1.add_label("During World War I, peace broke out.","black",main_font,24,(100,50),0)
        L1.add_label("It was Christmas 1914 on the Western Front. Despite strict orders not to chillax with the ","black",main_font,24,(100,0),2,background_color="white")
        L1.add_label("enemy, British and German soldiers left their trenches, crossed No Man's Land, and ","black",main_font,24,(100,0),1.2)
        L1.add_label("gathered to bury their dead, exchange gifts, and play games.","black",main_font,24,(100,0),1.2)
        L1.add_label("Meanwhile: it's 2022, the West has been at peace for decades, and wow, we suck at trust. ","black",main_font,24,(100,0),2)
        L1.add_label("Surveys show that, over the past forty years, fewer and fewer people say they trust each ","black",main_font,24,(100,0),1.2)
        L1.add_label("other. So here's our puzzle:","black",main_font,24,(100,0),1.2)
        L1.add_label("Why, even in peacetime, do friends become enemies?","green",main_font,24,(100,0),2,italic=True)
        L1.add_label("And why, even in wartime, do enemies become friends?","green",main_font,24,(100,0),1.2,italic=True)
        L1.add_label("I think ","black",main_font,24,(100,0),2)
        L1.add_label("game theory","red",main_font,24,(100,0))
        L1.add_label(" can help explain our epidemic of distrust - and how we can fix it! ","black",main_font,24,(100,0))
        L1.add_label("So, to understand all this...","black",main_font,24,(100,0),1.2)
        L1.add_button("...let's play a game.","black",main_font,24,(450,500,300,50),"white","yellow","green","black",[[L2init],[s.switch_section,L1,L2]])

    def L2init():
        L2.flush()
        L2.add_label("THE GAME OF TRUST","black",main_font,32,(600,50),-2)
        L2.add_label("You have one choice. In front of you is a machine: if you put a coin in the machine, the other","black",main_font,24,(100,100),0)
        L2.add_label("player gets three coins - and vice versa. You both can either choose to COOPERATE (put in coin),","black",main_font,24,(100,100),1.2)
        L2.add_label("or CHEAT (don't put in coin).","black",main_font,24,(100,100),1.2)
        L2.add_label("you","black",main_font,18,(280,220),-2)
        L2.add_label("other player","black",main_font,18,(890,220),-2)
        L2.config_machine((475,200,250,200),0,0,0,0)
        L2.add_player("char0",(280,330))
        L2.add_player("char1",(900,330),1)
        L2.add_label("Let's say the other player cheats, and doesn't put in a coin.","black",main_font,20,(600,430),-2)
        L2.add_label("What should you do?","black",main_font,20,(600,460),-2,italic=1)
        L2v = back.TempValues()
        L2v.stepnumber = 0
        def L2resp(resp):
            if L2v.stepnumber==0:
                L2.config_machine((475,200,250,200),0,1,0,1)
                L2v.stepnumber+=1
                L2.labels = []
                if resp:
                    L2.add_label("Alas, turning the other cheek just gets you slapped!","black",main_font,24,(600,70),-2)
                else:
                    L2.add_label("Exactly! Why let that moocher mooch off of you?","black",main_font,24,(600,70),-2)
                L2.add_label("If you cooperate & they cheat, you lose a coin while they gain three (score: -1 vs +3).","black",main_font,24,(600,100),-2)
                L2.add_label("However, if you both cheat, neither of you gain or lose anything (score: 0 vs 0).","black",main_font,24,(600,130),-2)
                L2.add_label("Therefore: you should CHEAT.","black",main_font,24,(600,160),-2,bold=1)
                L2.add_label("But let's say the other player cooperates, and puts in a coin.","black",main_font,20,(600,430),-2)
                L2.add_label("What should you do now?","black",main_font,20,(600,460),-2,italic=1)
            elif L2v.stepnumber==1:
                L2.config_machine((475,200,250,200),1,1,1,1)
                L2.labels = []
                if resp:
                    L2.add_label("Sure, seems like the right thing to do... OR IS IT??","black",main_font,24,(600,70),-2)
                else:
                    L2.add_label("Wow, that's mean... and also the correct answer!","black",main_font,24,(600,70),-2)
                L2.add_label("Because if you both cooperate, you both give up a coin to gain three (score: +2 vs +2).","black",main_font,24,(600,100),-2)
                L2.add_label("But if you cheat & they cooperate, you gain three coins at their cost of one (score: +3 vs -1).","black",main_font,24,(600,130),-2)
                L2.add_label('Therefore: you "should" still CHEAT.',"black",main_font,24,(600,160),-2,bold=1)
                L2.add_label("And that's our dilemma. Trust is nice, but it can let others take advantage of you - or shoot you as you come","black",main_font,20,(100,430),0)
                L2.add_label("unarmed out of a trench. Sometimes, distrust is rational! But now, what happens if we play this game...","black",main_font,20,(100,460),1.5)
                L2.buttons = []
                L2.add_button("...more than once?","black",main_font,24,(450,500,300,50),"white","yellow","green","black",[[L3init],[s.switch_section,L2,L3]])
        L2.add_button("COOPERATE","black",main_font,24,(350,500,200,50),"white","yellow","green","black",[[L2resp,1],[s.switch_section,L2,L2]])
        L2.add_button("CHEAT","black",main_font,24,(650,500,200,50),"white","yellow","green","black",[[L2resp,0],[s.switch_section,L2,L2]])

    def L3init():
        L3.flush()
        L3.add_label("Now, let's play for real. You'll be playing against 5 different opponents,","black",main_font,24,(600,40),-2)
        L3.add_label('each with their own game "strategy". With each opponent, you\'ll play',"black",main_font,24,(600,70),-2)
        L3.add_label("anywhere between 3 to 7 rounds (You won't know in advance when the","black",main_font,24,(600,100),-2)
        L3.add_label("last round is). Can you trust them? Or rather... can they trust you?","black",main_font,24,(600,130),-2)
        L3.add_label("Pick your first, real move.","black",main_font,20,(600,430),-2)
        L3.add_label("Choose wisely.","black",main_font,20,(600,460),-2,bold=1)
        L3.config_machine((475,200,250,200),0,0,0,0,1,1,1,1)
        L3.add_player("char1",(860,330),1)
        L3.add_player("char0",(280,330))
        L3v = back.TempValues()
        L3v.stepnumber = 0
        L3v.character = 0
        L3v.number_of_rounds = [5,4,4,5,7]
        L3v.current_prl = []
        L3v.current_brl = []
        L3v.current_score = 0
        L3v.step_score = [0,0]
        def L3index():
            L3.flush()
            L3.add_label("COPYCAT - Hello! I start with Cooperate,",character_color["copycat"],main_font,24,(180,50),0)
            L3.add_label("and afterwards, I just copy whatever you",character_color["copycat"],main_font,24,(180,50),1.2)
            L3.add_label("did in the last round. Meow",character_color["copycat"],main_font,24,(180,50),1.2)
            L3.add_player("char1",(100,50))
            L3.add_label("ALWAYS COOPERATE - Let's",character_color["all cooperate"],main_font,24,(780,50),0)
            L3.add_label("be best friends! <3",character_color["all cooperate"],main_font,24,(780,50),1.2)
            L3.add_player("char2",(700,50))
            L3.add_label("ALWAYS CHEAT -",character_color["all cheat"],main_font,24,(180,200),0)
            L3.add_label("the strong shall",character_color["all cheat"],main_font,24,(180,200),1.2)
            L3.add_label("eat the weak",character_color["all cheat"],main_font,24,(180,200),1.2)
            L3.add_player("char3",(100,200))
            L3.add_label("GRUDGER - Listen, pardner. I'll start cooperatin', and keep",character_color["grudger"],main_font,24,(480,200),0)
            L3.add_label("cooperatin', but if y'all ever cheat me, I'LL CHEAT YOU BACK",character_color["grudger"],main_font,24,(480,200),1.2)
            L3.add_label("'TIL THE END OF TARNATION.",character_color["grudger"],main_font,24,(480,200),1.2)
            L3.add_player("char4",(400,200))
            L3.add_label("DETECTIVE - First: I analyze you. I start: Cooperate, Cheat, Cooperate, Cooperate. If you",character_color["detective"],main_font,24,(180,350),0)
            L3.add_label("cheat back, I'll act like Copycat. If you never cheat back, I'll act like Always Cheat, to",character_color["detective"],main_font,24,(180,350),1.2)
            L3.add_label("exploit you. Elementary, my dear Watson.",character_color["detective"],main_font,24,(180,350),1.2)
            L3.add_player("char5",(100,350))
            L3.add_label("Now, what if these characters were to play...","black",main_font,24,(600,450),-2) 
            L3.add_button("...against each other?","black",main_font,24,(400,500,400,50),"white","yellow","green","black",[[L4init],[s.switch_section,L3,L4]])
        def L3resp(resp):
            botresp = char_resp_list[L3v.character](L3v.current_prl,L3v.current_brl)
            L3v.current_brl.append(botresp)
            L3v.current_prl.append(resp)
            lac = [0,0,0,0]
            if botresp and resp:
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
                L3.add_label("And your total score is...","black",main_font,24,(100,40),0)
                L3.add_label("%d"%L3v.current_score,"black",main_font,72,(100,40),0.4)
                if L3v.current_score>35:
                    L3.add_label("which is pretty good! (the lowest & highest possible","black",main_font,24,(180,70),0)
                elif L3v.current_score>20:
                    L3.add_label("which is not bad! (the lowest & highest possible","black",main_font,24,(180,70),0)
                else:
                    L3.add_label("which is okay! (the lowest & highest possible","black",main_font,24,(180,70),0)
                L3.add_label("scores are 7 and 49, respectively)","black",main_font,24,(180,70),1.2)
                L3.add_label("So who were these strange characters you just played against?","black",main_font,24,(100,200),0)
                L3.add_player("char1",(150,300),1)
                L3.add_player("char2",(360,300),1)
                L3.add_player("char3",(570,300),1)
                L3.add_player("char4",(780,300),1)
                L3.add_player("char5",(990,300),1)
                L3.add_button("Let's find out!","black",main_font,24,(450,500,300,50),"white","yellow","green","black",[[L3index],[s.switch_section,L3,L3]])
                return
            L3.add_label("opponent: %d of 5"%(L3v.character+1),"black",main_font,20,(600,50),-2)
            L3.add_label("your total score: %d"%(L3v.current_score),"black",main_font,20,(600,80),-2)
            L3.add_label("%d ~ %d"%tuple(L3v.step_score),"black",main_font,70,(600,120),-2)
        L3.add_button("COOPERATE","black",main_font,24,(350,500,200,50),"white","yellow","green","black",[[L3resp,1],[s.switch_section,L3,L3]])
        L3.add_button("CHEAT","black",main_font,24,(650,500,200,50),"white","yellow","green","black",[[L3resp,0],[s.switch_section,L3,L3]])

    def L4init():
        L4.flush()
        L4.add_label("It's tournament time! Each character will now","black",main_font,24,(600,40),0)
        L4.add_label("play against every other character: that's 10","black",main_font,24,(600,40),1.2)
        L4.add_label("paired matches, and 10 rounds per match.","black",main_font,24,(600,40),1.2)
        L4.add_label("Who do you think will get the ","black",main_font,24,(600,140),0)
        L4.add_label("highest total score?","black",main_font,24,(600,140),italic=1)
        L4.add_label("Think carefully about it... and then ","black",main_font,24,(600,140),1.2)
        L4.add_label("PLACE YOUR","red",main_font,24,(600,140))
        L4.add_label("BETS:","red",main_font,24,(600,140),1.2)
        L4v = back.TempValues()
        L4v.charlist = ["copycat","all cooperate","all cheat","grudger","detective"]
        L4v.charscores = [0,0,0,0,0]
        L4.config_circle(L4v.charlist,L4v.charscores,150,(50,50,500,500),linecolor="grey")
        L4v.stepno = 0
        def add_index1():
            L4.flush()
            L4.add_label("COPYCAT - Starts with Cooperate.",character_color["copycat"],main_font,24,(180,50),0)
            L4.add_label("Then, it simply repeats whatever",character_color["copycat"],main_font,24,(180,50),1.2)
            L4.add_label("YOU did in the last round.",character_color["copycat"],main_font,24,(180,50),1.2)
            L4.add_player("char1",(100,50))
            L4.add_label("ALL COOPERATE -",character_color["all cooperate"],main_font,24,(780,50),0)
            L4.add_label("Always cooperates.",character_color["all cooperate"],main_font,24,(780,50),1.2)
            L4.add_player("char2",(700,50))
            L4.add_label("ALL CHEAT -",character_color["all cheat"],main_font,24,(180,200),0)
            L4.add_label("Always cheats.",character_color["all cheat"],main_font,24,(180,200),1.2)
            L4.add_player("char3",(100,200))
            L4.add_label("GRUDGER - Starts with Cooperate, and keeps cooperating",character_color["grudger"],main_font,24,(480,200),0)
            L4.add_label("until you cheat it even once. Afterwards, it always plays",character_color["grudger"],main_font,24,(480,200),1.2)
            L4.add_label("Cheat.",character_color["grudger"],main_font,24,(480,200),1.2)
            L4.add_player("char4",(400,200))
            L4.add_label("DETECTIVE - Starts with: Cooperate, Cheat, Cooperate, Cooperate. Afterwards, if you",character_color["detective"],main_font,24,(180,350),0)
            L4.add_label("ever retaliate with a Cheat, it plays like a ",character_color["detective"],main_font,24,(180,350),1.2)
            L4.add_label("Copycat.",character_color["copycat"],main_font,24,(180,350))
            L4.add_label(" Otherwise, it plays like an ",character_color["detective"],main_font,24,(180,350))
            L4.add_label("All",character_color["all cheat"],main_font,24,(180,350))
            L4.add_label("Cheat.",character_color["all cheat"],main_font,24,(180,350),1.2)
            L4.add_player("char5",(100,350))
            L4.add_button("<---","black","consolas",24,(1050,500,100,50),"white","yellow","green","black",[[L4init],[s.switch_section,L4,L4]])
        def L4last(betc):
            L4.flush()
            L4.add_label("...and the winner is...","black",main_font,24,(600,40),0)
            L4.add_label("COPYCAT!",character_color["copycat"],main_font,48,(600,40),1.2)
            if betc=="copycat":
                L4.add_label("Congrats, you placed your bet on the right horse.","black",main_font,24,(600,160),0)
            else:
                L4.add_label("(Apologies to your bet, ","black",main_font,24,(600,160),0)
                L4.add_label("%s"%betc,character_color[betc],main_font,24,(600,160))
                L4.add_label(".)","black",main_font,24,(600,160))
            L4.config_circle(L4v.charlist,L4v.charscores,150,(50,50,500,500),linecolor="grey")
            L4.add_label("Copycat",character_color["copycat"],main_font,24,(600,220),0)
            L4.add_label(" goes by many names. The Golden Rule,","black",main_font,24,(600,220))
            L4.add_label("reciprocal altruism, tit for tat, or... ","black",main_font,24,(600,220),1.2)
            L4.add_label("live and let live.","black",main_font,24,(600,220),bold=1)
            L4.add_label("That's why \"peace\" could emerge in the trenches","black",main_font,24,(600,220),1.2)
            L4.add_label("of World War I: when you're forced to play the same","black",main_font,24,(600,220),1.2)
            L4.add_label("game with the same specific people (not just the","black",main_font,24,(600,220),1.2)
            L4.add_label("same generic \"enemy\") over and over again --","black",main_font,24,(600,220),1.2)
            L4.add_label("Copycat",character_color["copycat"],main_font,24,(600,220),1.2)
            L4.add_label(" doesn't just win the battle, it wins the war.","black",main_font,24,(600,220))
            L4.add_button("NEXT","black",main_font,24,(700,500,300,50),"white","yellow","green","black",[[L5init],[s.switch_section,L4,L5]])
        def L4step(betc):
            L4.flush()
            for i in range(L4v.stepno+1,5):
                res = tourney(L4v.charlist[i],L4v.charlist[L4v.stepno],10)[0]
                L4v.charscores[i]+=res[0]
                L4v.charscores[L4v.stepno]+=res[1]
            L4.config_circle(L4v.charlist,L4v.charscores,150,(50,50,500,500),linecolor="grey",highlight=L4v.stepno)
            if L4v.stepno<3:
                L4.add_button("STEP","black",main_font,24,(700,250,300,50),"white","yellow","green","black",[[L4step,betc],[s.switch_section,L4,L4]])
            else:
                L4.add_button("(drumrolls...)","black",main_font,24,(700,250,300,50),"white","yellow","green","black",[[L4last,betc],[s.switch_section,L4,L4]])
            L4v.stepno+=1
        def L4resp(resp):
            L4.flush()
            L4.add_label("Alright, you placed your bet on ","black",main_font,24,(600,40),0)
            L4.add_label("%s!"%resp,character_color[resp],main_font,24,(600,40))
            L4.add_label("Let's go through the matches one by one, and","black",main_font,24,(600,40),2)
            L4.add_label("see how the tournament plays out...","black",main_font,24,(600,40),1.2)
            L4.config_circle(["copycat","all cooperate","all cheat","grudger","detective"],L4v.charscores,150,(50,50,500,500),linecolor="grey")
            L4.add_button("START","black",main_font,24,(700,250,300,50),"white","yellow","green","black",[[L4step,resp],[s.switch_section,L4,L4]])
        L4.add_button("copycat","black",main_font,20,(650,250,200,50),character_color["copycat"],"white",character_color["copycat"],"black",[[L4resp,"copycat"],[s.switch_section,L4,L4]])
        L4.add_button("all cooperate","black",main_font,20,(900,250,200,50),character_color["all cooperate"],"white",character_color["all cooperate"],"black",[[L4resp,"all cooperate"],[s.switch_section,L4,L4]])
        L4.add_button("all cheat","black",main_font,20,(650,350,200,50),character_color["all cheat"],"white",character_color["all cheat"],"black",[[L4resp,"all cheat"],[s.switch_section,L4,L4]])
        L4.add_button("grudger","black",main_font,20,(900,350,200,50),character_color["grudger"],"white",character_color["grudger"],"black",[[L4resp,"grudger"],[s.switch_section,L4,L4]])
        L4.add_button("detective","black",main_font,20,(775,450,200,50),character_color["detective"],"white",character_color["detective"],"black",[[L4resp,"detective"],[s.switch_section,L4,L4]])
        L4.add_button("?","black",main_font,24,(1050,500,100,50),"white","yellow","green","black",[[add_index1],[s.switch_section,L4,L4]])

    def L5init():
        L5v = back.TempValues()
        L5v.stepno = 0        
        def L5next():
            L5.flush()
            L5v.stepno+=1
            if L5v.stepno==1:
                L5.add_label("And normally, they'd just pay back each others' kindness and sing Kumbaya","black",main_font,24,(600,70),-2)
                L5.add_label("until the end of time.","black",main_font,24,(600,100),-2)
                L5.config_machine((475,200,250,200),0,0,1,0,1,1,1,1)
                L5.add_player("char1",(280,330))
                L5.add_player("char1",(900,330),1)
                L5.add_label("But what if, while trying to reciprocate goodness...","black",main_font,24,(600,450),-2)
                L5.add_button("...the first copycat makes a mistake?","black",main_font,24,(350,500,500,50),"white","yellow","green","black",[[L5next],[s.switch_section,L5,L5]])
            elif L5v.stepno==2:
                L5.add_label("OH NO","black",main_font,24,(600,50),-2,bold=1)
                L5.add_label("Mistakes, miscommunication, misinterpretations -- accidents happen","black",main_font,24,(600,100),-2)
                L5.add_label("all the time in real life.","black",main_font,24,(600,130),-2)
                L5.config_machine((475,180,250,200),1,0,0,0,1,1,1,1)
                L5.add_player("char1",(280,310))
                L5.add_player("char1",(900,310),1)
                L5.add_label("But if the other person doesn't think it was an accident...","black",main_font,24,(600,450),-2)
                L5.add_button("...they would retaliate.","black",main_font,24,(400,500,400,50),"white","yellow","green","black",[[L5next],[s.switch_section,L5,L5]])
            elif L5v.stepno==3:
                L5.add_label("OH NO TIMES TWO","black",main_font,24,(600,50),-2,bold=1)
                L5.add_label("The other player, being a ","black",main_font,24,(100,100),0)
                L5.add_label("Copycat",character_color["copycat"],main_font,24,(100,100))
                L5.add_label(", had to retaliate... and you, being a ","black",main_font,24,(100,100))
                L5.add_label("Copycat",character_color["copycat"],main_font,24,(100,130))
                L5.add_label(" as well, will also","black",main_font,24,(100,130))
                L5.add_label("have to retaliate...","black",main_font,24,(100,130),1.2)
                L5.config_machine((475,180,250,200),1,1,0,0,1,1,1,1)
                L5.add_player("char1",(280,310))
                L5.add_player("char1",(900,310),1)
                L5.add_label("Thus, like the Hatfields and McCoys, these two Copycats will spiral into an endless cycle of","black",main_font,24,(100,410),0)
                L5.add_label("vengeance... that started over a single mistake, long ago.","black",main_font,24,(100,130),1.2)
                L5.add_label("Tragic. But now, are there other types of players who can...","black",main_font,24,(100,130),2)
                L5.add_button("...deal with mistakes?","black",main_font,24,(400,520,400,50),"white","yellow","green","black",[[L5next],[s.switch_section,L5,L5]])
            elif L5v.stepno==4:
                L5.add_label("Let's meet some new faces!","black",main_font,24,(600,50),-2,bold=1)
                L5.add_label("COPYKITTEN:",character_color["copykitten"],main_font,24,(300,95),0)
                L5.add_label("Hello! I'm like ",character_color["copykitten"],main_font,24,(300,120),1.5)
                L5.add_label("Copycat",character_color["copycat"],main_font,24,(300,120))
                L5.add_label(", except I Cheat back only after you Cheat me",character_color["copykitten"],main_font,24,(300,120))
                L5.add_label("twice in a row. After all, the first one could be a mistake! Purrrrr",character_color["copykitten"],main_font,24,(300,120),1.2)
                L5.add_player("char6",(165,95))
                L5.add_label("SIMPLETON:",character_color["simpleton"],main_font,24,(100,120),2)
                L5.add_label("hi i try start cooperate. if you cooperate back, i do same thing as last",character_color["simpleton"],main_font,24,(100,120),1.5)
                L5.add_label("move, even if it mistake. if you cheat back, i do opposite thing as last",character_color["simpleton"],main_font,24,(100,120),1.2)
                L5.add_label("move, even if it mistake.",character_color["simpleton"],main_font,24,(100,120),1.2)
                L5.add_player("char7",(900,235),1)
                L5.add_label("RANDOM:",character_color["random"],main_font,24,(300,120),2)
                L5.add_label("Monkey robot! Ninja pizza tacos! lol i'm so random",character_color["random"],main_font,24,(300,120),1.5)
                L5.add_label("(Just plays Cheat or Cooperate randomly with a 50/50 chance)",character_color["random"],main_font,24,(300,120),1.2)
                L5.add_player("char8",(165,355))
                L5.add_label("Alright, let's see how well these peeps do when they...","black",main_font,24,(600,455),-2)
                L5.add_button("..play in a tournament.","black",main_font,24,(400,500,400,50),"white","yellow","green","black",[[L6init],[s.switch_section,L5,L6]])
        L5.flush()
        L5.add_label("As cool as Copycat is, it has a huge, fatal weakness I haven't mentioned","black",main_font,24,(600,70),-2)
        L5.add_label("yet. To understand the problem, let's say two Copycats are playing against","black",main_font,24,(600,100),-2)
        L5.add_label("each other:","black",main_font,24,(600,130),-2)
        L5.config_machine((475,200,250,200),0,0,0,0,1,1,1,1)
        L5.add_player("char1",(280,330))
        L5.add_player("char1",(900,330),1)
        L5.add_label("Being \"nice\" players, both their first moves will be: COOPERATE","black",main_font,24,(600,450),-2)
        L5.add_button("NEXT","black",main_font,24,(500,500,200,50),"white","yellow","green","black",[[L5next],[s.switch_section,L5,L5]])

    def L6init():
        L6.flush()
        L6v = back.TempValues()
        L6v.numbers = [5,5,5,5,5,0,0,0]
        L6v.charlist = [*[character_names[0]]*L6v.numbers[0],*[character_names[1]]*L6v.numbers[1],*[character_names[2]]*L6v.numbers[2],*[character_names[3]]*L6v.numbers[3],*[character_names[4]]*L6v.numbers[4],*[character_names[5]]*L6v.numbers[5],*[character_names[6]]*L6v.numbers[6],*[character_names[7]]*L6v.numbers[7]]
        L6v.scorelist = [*[0]*25]
        L6v.active_tab = 0
        L6v.rounds = 10
        L6v.eln = 5
        L6v.err = 5
        L6v.give_coin = 1
        L6v.get_coin = 3
        L6v.playlist = []
        L6v.playactive = 1
        def L6reset():
            L6v.scorelist = [*[0]*len(L6v.charlist)]
            L6v.playlist = []
        def L6inc(factor,id):
            if (10<=sum(L6v.numbers)+factor<=25) and ((L6v.numbers[id]+factor)>=0):
                L6v.numbers[id]+=factor
                L6v.charlist = [*[character_names[0]]*L6v.numbers[0],*[character_names[1]]*L6v.numbers[1],*[character_names[2]]*L6v.numbers[2],*[character_names[3]]*L6v.numbers[3],*[character_names[4]]*L6v.numbers[4],*[character_names[5]]*L6v.numbers[5],*[character_names[6]]*L6v.numbers[6],*[character_names[7]]*L6v.numbers[7]]
                L6v.scorelist = [*[0]*len(L6v.charlist)]
                L6v.playactive = 1
                L6v.eln = int(len(L6v.charlist)/4)
        def rinc(factor):
            if (3<=L6v.rounds+factor<=20):
                L6v.rounds+=factor
        def elninc(factor):
            if (2<=L6v.eln+factor<=len(L6v.scorelist)/4):
                L6v.eln+=factor
        def errinc(factor):
            if (0<=L6v.err+factor<=50):
                L6v.err+=factor
        def ginc(gg,factor):
            if gg==0:
                if (1<=L6v.give_coin+factor<=5):
                    L6v.give_coin+=factor
            elif gg==1:
                if (1<=L6v.get_coin+factor<=5):
                    L6v.get_coin+=factor
        def L6step():
            Scores,L6v.playlist = multitourney(L6v.charlist,L6v.err,L6v.playlist,L6v.give_coin,L6v.get_coin)
            L6v.scorelist = [sum(i) for i in zip(L6v.scorelist,Scores)]
        def L6play():
            for i in range(L6v.rounds):
                L6step()
            L6v.playactive = 0
        def L6replace():
            for i in range(L6v.eln):
                ix = L6v.scorelist.index(min(L6v.scorelist))
                L6v.scorelist.remove(L6v.scorelist[ix])
                L6v.charlist.remove(L6v.charlist[ix])
                iy = 0
                for i in range(len(L6v.numbers)):
                    iy+=L6v.numbers[i]
                    if iy>ix:
                        L6v.numbers[i]-=1
                        break
            adders = [0,0,0,0,0,0,0,0]
            for i in range(L6v.eln):
                ix = L6v.scorelist.index(max(L6v.scorelist))
                L6v.scorelist.remove(L6v.scorelist[ix])
                L6v.charlist.remove(L6v.charlist[ix])
                iy = 0
                for i in range(len(L6v.numbers)):
                    iy+=L6v.numbers[i]
                    if iy>ix:
                        L6v.numbers[i]-=1
                        adders[i]+=1
                        break
            L6v.numbers = [sum(i) for i in zip([2*i for i in adders],L6v.numbers)]
            L6v.charlist = [*[character_names[0]]*L6v.numbers[0],*[character_names[1]]*L6v.numbers[1],*[character_names[2]]*L6v.numbers[2],*[character_names[3]]*L6v.numbers[3],*[character_names[4]]*L6v.numbers[4],*[character_names[5]]*L6v.numbers[5],*[character_names[6]]*L6v.numbers[6],*[character_names[7]]*L6v.numbers[7]]
            L6v.scorelist = [*[0]*sum(L6v.scorelist)]
            L6v.playactive = 1
        def change_tab(tab):
            L6v.active_tab = tab
            L6.flush()
            if tab==0:
                L6.add_label("Start off with this distribution of players:","black",main_font,24,(650,120),0)
                L6.add_label("%s: %d"%(character_names[0],L6v.numbers[0]),character_color[character_names[0]],main_font,24,(650,160),0)
                L6.add_label("%s: %d"%(character_names[1],L6v.numbers[1]),character_color[character_names[1]],main_font,24,(950,160),0)
                L6.add_label("%s: %d"%(character_names[2],L6v.numbers[2]),character_color[character_names[2]],main_font,24,(650,250),0)
                L6.add_label("%s: %d"%(character_names[3],L6v.numbers[3]),character_color[character_names[3]],main_font,24,(950,250),0)
                L6.add_label("%s: %d"%(character_names[4],L6v.numbers[4]),character_color[character_names[4]],main_font,24,(650,340),0)
                L6.add_label("%s: %d"%(character_names[5],L6v.numbers[5]),character_color[character_names[5]],main_font,24,(950,340),0)
                L6.add_label("%s: %d"%(character_names[6],L6v.numbers[6]),character_color[character_names[6]],main_font,24,(650,430),0)
                L6.add_label("%s: %d"%(character_names[7],L6v.numbers[7]),character_color[character_names[7]],main_font,24,(950,430),0)
                L6.add_button("+","black",main_font,24,(700,190,40,40),"white","yellow","green","black",[[L6inc,+1,0],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(750,190,40,40),"white","yellow","green","black",[[L6inc,-1,0],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("+","black",main_font,24,(1000,190,40,40),"white","yellow","green","black",[[L6inc,+1,1],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(1050,190,40,40),"white","yellow","green","black",[[L6inc,-1,1],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("+","black",main_font,24,(700,280,40,40),"white","yellow","green","black",[[L6inc,+1,2],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(750,280,40,40),"white","yellow","green","black",[[L6inc,-1,2],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("+","black",main_font,24,(1000,280,40,40),"white","yellow","green","black",[[L6inc,+1,3],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(1050,280,40,40),"white","yellow","green","black",[[L6inc,-1,3],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("+","black",main_font,24,(700,370,40,40),"white","yellow","green","black",[[L6inc,+1,4],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(750,370,40,40),"white","yellow","green","black",[[L6inc,-1,4],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("+","black",main_font,24,(1000,370,40,40),"white","yellow","green","black",[[L6inc,+1,5],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(1050,370,40,40),"white","yellow","green","black",[[L6inc,-1,5],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("+","black",main_font,24,(700,460,40,40),"white","yellow","green","black",[[L6inc,+1,6],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(750,460,40,40),"white","yellow","green","black",[[L6inc,-1,6],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("+","black",main_font,24,(1000,460,40,40),"white","yellow","green","black",[[L6inc,+1,7],[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(1050,460,40,40),"white","yellow","green","black",[[L6inc,-1,7],[change_tab,0],[s.switch_section,L6,L6]])  
                L6.add_button("POPULATION","black",main_font,24,(600,50,200,50),"green","yellow","white","black",[[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("PAYOFFS","black",main_font,24,(820,50,150,50),"white","yellow","green","black",[[change_tab,1],[s.switch_section,L6,L6]])
                L6.add_button("RULES","black",main_font,24,(990,50,100,50),"white","yellow","green","black",[[change_tab,2],[s.switch_section,L6,L6]])    
            elif tab==1:
                L6.add_label("The payoffs in a one-on-one game are: ","black",main_font,24,(650,120),0)
                L6.add_label("When you cooperate, you give %d coins"%L6v.give_coin,"black",main_font,24,(650,160),0)
                L6.add_label("When your opponent cooperates, you get %d coins"%L6v.get_coin,"black",main_font,24,(650,280),0)
                L6.add_button("+","black",main_font,24,(840,200,40,40),"white","yellow","green","black",[[ginc,0,1],[change_tab,1],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(920,200,40,40),"white","yellow","green","black",[[ginc,0,-1],[change_tab,1],[s.switch_section,L6,L6]])
                L6.add_button("+","black",main_font,24,(840,320,40,40),"white","yellow","green","black",[[ginc,1,1],[change_tab,1],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(920,320,40,40),"white","yellow","green","black",[[ginc,1,-1],[change_tab,1],[s.switch_section,L6,L6]])
                L6.add_button("POPULATION","black",main_font,24,(600,50,200,50),"white","yellow","green","black",[[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("PAYOFFS","black",main_font,24,(820,50,150,50),"green","yellow","white","black",[[change_tab,1],[s.switch_section,L6,L6]])
                L6.add_button("RULES","black",main_font,24,(990,50,100,50),"white","yellow","green","black",[[change_tab,2],[s.switch_section,L6,L6]])
            elif tab==2:
                L6.add_label("Play %d rounds per match"%L6v.rounds,"black",main_font,24,(650,120),0)
                L6.add_label("After each tournament, eliminate the bottom","black",main_font,24,(650,220),0)
                L6.add_label("%d players and reproduce the top %d players"%(L6v.eln,L6v.eln),"black",main_font,24,(650,220),1.2)
                L6.add_label("During each round, there is a {}% chance".format(L6v.err),"black",main_font,24,(650,360),0)
                L6.add_label("a player makes a mistake","black",main_font,24,(650,360),1.2) 
                L6.add_button("+","black",main_font,24,(840,160,40,40),"white","yellow","green","black",[[rinc,1],[change_tab,2],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(920,160,40,40),"white","yellow","green","black",[[rinc,-1],[change_tab,2],[s.switch_section,L6,L6]])
                L6.add_button("+","black",main_font,24,(840,290,40,40),"white","yellow","green","black",[[elninc,1],[change_tab,2],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(920,290,40,40),"white","yellow","green","black",[[elninc,-1],[change_tab,2],[s.switch_section,L6,L6]])
                L6.add_button("+","black",main_font,24,(840,430,40,40),"white","yellow","green","black",[[errinc,1],[change_tab,2],[s.switch_section,L6,L6]])
                L6.add_button("-","black",main_font,24,(920,430,40,40),"white","yellow","green","black",[[errinc,-1],[change_tab,2],[s.switch_section,L6,L6]])
                L6.add_button("POPULATION","black",main_font,24,(600,50,200,50),"white","yellow","green","black",[[change_tab,0],[s.switch_section,L6,L6]])
                L6.add_button("PAYOFFS","black",main_font,24,(820,50,150,50),"white","yellow","green","black",[[change_tab,1],[s.switch_section,L6,L6]])
                L6.add_button("RULES","black",main_font,24,(990,50,100,50),"green","yellow","white","black",[[change_tab,2],[s.switch_section,L6,L6]])
            L6.config_circle(L6v.charlist,L6v.scorelist,150,(25,25,500,500),highlight=-1,linecolor="grey")
            if L6v.playactive:
                L6.add_button("PLAY","black",main_font,18,(225,220,100,30),"white","yellow","green","black",[[L6play],[change_tab,L6v.active_tab],[s.switch_section,L6,L6]])
            else:
                L6.add_button("REPLACE","black",main_font,18,(225,220,100,30),"white","yellow","green","black",[[L6replace],[change_tab,L6v.active_tab],[s.switch_section,L6,L6]])
            L6.add_button("STEP","black",main_font,18,(225,260,100,30),"white","yellow","green","black",[[L6step],[change_tab,L6v.active_tab],[s.switch_section,L6,L6]])
            L6.add_button("RESET","black",main_font,18,(225,300,100,30),"white","yellow","green","black",[[L6reset],[change_tab,L6v.active_tab],[s.switch_section,L6,L6]])
            L6.add_label("NOTE: Sandbox Mode is totally optional.","black",main_font,24,(50,525),0,bold=1)
            L6.add_label("Feel free to skip it, or play around! Once you're done, let's...","black",main_font,24,(50,525),1.2)
            L6.add_button("...proceed","black",main_font,24,(800,525,200,50),"white","yellow","green","black",[[L7init],[s.switch_section,L6,L7]])
        change_tab(L6v.active_tab)

    def L7init():
        L7v = back.TempValues()
        L7v.activeplayer = "copycat"
        L7v.steplist = [[],[]]
        L7v.scorelist = [0,0]
        def L7step():
            r1 = godstep(tuple(L7v.steplist[0]),tuple(L7v.steplist[1]),L7v.activeplayer)
            r2 = char_fun_dict[L7v.activeplayer](L7v.steplist[0],L7v.steplist[1])
            L7v.steplist[0].append(r1)
            L7v.steplist[1].append(r2)
            if r1:
                L7v.scorelist[0]-=1
                L7v.scorelist[1]+=3
            if r2:
                L7v.scorelist[1]-=1
                L7v.scorelist[0]+=3
            L7.flush()
            L7.add_label("Introducing... the God player!","black",main_font,24,(600,50),-2)
            L7.add_player("char9",(200,265))
            L7.add_player(imgloader[L7v.activeplayer],(400,265),1)
            L7.add_label("God's moves","black",main_font,24,(600,100),0,bold=1)
            for i in L7v.steplist[0]:
                if i:
                    L7.add_label("Cooperate","black",main_font,24,(600,100),1.2)
                else:
                    L7.add_label("Cheat","black",main_font,24,(600,100),1.2)
            L7.add_label("%s's moves"%L7v.activeplayer,"black",main_font,24,(900,100),0,bold=1)
            for i in L7v.steplist[1]:
                if i:
                    L7.add_label("Cooperate","black",main_font,24,(900,100),1.2)
                else:
                    L7.add_label("Cheat","black",main_font,24,(900,100),1.2)
            L7.add_button("STEP","black",main_font,24,(200,500,200,50),"white","yellow","green","black",[[L7step],[s.switch_section,L7,L7]])
            L7.add_button("RESET","black",main_font,24,(500,500,200,50),"white","yellow","green","black",[[L7reset],[s.switch_section,L7,L7]])
            L7.add_button("Conclude","black",main_font,24,(800,500,200,50),"white","yellow","green","black",[[L8init],[s.switch_section,L7,L8]])
        def L7reset(setplayer=None):
            L7.flush()
            L7v.steplist = [[],[]]
            L7v.scorelist = [0,0]
            if setplayer:
                L7v.activeplayer = setplayer
            L7.add_label("Introducing... the God player!","black",main_font,24,(600,50),-2)
            L7.add_player("char9",(200,265))
            L7.add_player(imgloader[L7v.activeplayer],(400,265),1)
            L7.add_button("copycat","black",main_font,24,(700,100,150,50),character_color["copycat"],"white",character_color["copycat"],"black",[[L7reset,"copycat"],[s.switch_section,L7,L7]])
            L7.add_button("all cooperate","black",main_font,24,(900,100,150,50),character_color["all cooperate"],"white",character_color["all cooperate"],"black",[[L7reset,"all cooperate"],[s.switch_section,L7,L7]])
            L7.add_button("all cheat","black",main_font,24,(700,200,150,50),character_color["all cheat"],"white",character_color["all cheat"],"black",[[L7reset,"all cheat"],[s.switch_section,L7,L7]])
            L7.add_button("grudger","black",main_font,24,(900,200,150,50),character_color["grudger"],"white",character_color["grudger"],"black",[[L7reset,"grudger"],[s.switch_section,L7,L7]])
            L7.add_button("detective","black",main_font,24,(700,300,150,50),character_color["detective"],"white",character_color["detective"],"black",[[L7reset,"detective"],[s.switch_section,L7,L7]])
            L7.add_button("copykitten","black",main_font,24,(900,300,150,50),character_color["copykitten"],"white",character_color["copykitten"],"black",[[L7reset,"copykitten"],[s.switch_section,L7,L7]])
            L7.add_button("simpleton","black",main_font,24,(700,400,150,50),"gray","white","gray","black",[[L7reset,"simpleton"],[s.switch_section,L7,L7]])
            L7.add_button("random","black",main_font,24,(900,400,150,50),character_color["random"],"white",character_color["random"],"black",[[L7reset,"random"],[s.switch_section,L7,L7]])
            L7.add_button("STEP","black",main_font,24,(200,500,200,50),"white","yellow","green","black",[[L7step],[s.switch_section,L7,L7]])
            L7.add_button("RESET","black",main_font,24,(500,500,200,50),"white","yellow","green","black",[[L7reset],[s.switch_section,L7,L7]])
            L7.add_button("Conclude","black",main_font,24,(800,500,200,50),"white","yellow","green","black",[[L8init],[s.switch_section,L7,L8]])
        L7reset()

    def L8init():
        L8.flush()
        def L8next():
            L8.flush()
            L8.add_label("If there's one big takeaway from ","black",main_font,24,(100,50),0)
            L8.add_label("all","black",main_font,24,(100,50),italic=1)
            L8.add_label(" of game theory, it's this:","black",main_font,24,(100,50))
            L8.add_label("What the game is, defines what the players do. Our problem today isn't just that people are","black",main_font,24,(100,0),2)
            L8.add_label("losing trust, it's that our environment acts against the evolution of trust.","black",main_font,24,(100,0),1.2)
            L8.add_label("That may seem cynical or naive -- that we're \"merely\" products of our environment -- but","black",main_font,24,(100,0),2)
            L8.add_label("as game theory reminds us, we are each others' environment. In the short run, the game","black",main_font,24,(100,0),1.2)
            L8.add_label("defines the players. But in the long run, it's us players who define the game.","black",main_font,24,(100,0),1.2)
            L8.add_label("So, do what you can do, to create the conditions necessary to evolve trust. Build relationships.","black",main_font,24,(100,0),2)
            L8.add_label("Find win-wins. Communicate clearly. Maybe then, we can stop firing at each other, get out of","black",main_font,24,(100,0),1.2)
            L8.add_label("our own trenches, cross No Man's Land to come together...","black",main_font,24,(100,0),1.2)
            L8.add_label("...and all learn...","black",main_font,36,(600,420),-2)
            L8.add_label("...to live and let live.","black",main_font,48,(600,500),-2)
        L8.add_label("Game theory has shown us the three things we need for the evolution of trust:","black",main_font,24,(100,50),0)
        L8.add_label("1. REPEAT INTERACTIONS","lightslateblue",main_font,48,(130,100),0)
        L8.add_label("Trust keeps a relationship going, but you need the knowledge of possible future","black",main_font,24,(130,160),0)
        L8.add_label("repeat interactions before trust can evolve.","black",main_font,24,(130,160),1.2)
        L8.add_label("2. POSSIBLE WIN-WINS","green",main_font,48,(130,240),0)
        L8.add_label("You must be playing a non-zero-sum game, a game where it's at least possible","black",main_font,24,(130,300),0)
        L8.add_label("that both players can be better off - a win-win.","black",main_font,24,(130,300),1.2)
        L8.add_label("3. LOW MISCOMMUNICATION","red2",main_font,48,(130,380),0)
        L8.add_label("If the level of miscommunication is too high, trust breaks down. But when there's a","black",main_font,24,(130,440),0)
        L8.add_label("little bit of miscommunication, it pays to be more forgiving.","black",main_font,24,(130,440),1.2)
        L8.add_label("Of course, real-world trust is affected by much more","black",main_font,18,(100,520),0)
        L8.add_label("than this. There's reputation, shared values, contracts,","black",main_font,18,(100,520),1.2)
        L8.add_label("cultural markers, blah blah blah. And let's not forget...","black",main_font,18,(100,520),1.2)
        L8.add_button("...the biggest lesson.","black",main_font,24,(600,525,400,50),"white","yellow","green","black",[[L8next],[s.switch_section,L8,L8]])

    L0init()
    s.switch_section(0,L0)

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
        while L8.enabled:
            s.before()
            s.place_subscreen(L8.return_subscreen())
            s.after()
            s.event_handler(L8.buttons,[L8.ready_objects,L8.ready_dynamic])

if __name__ == "__main__":
    main()