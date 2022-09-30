import pygame
import math

factor = 1
pygame.init()
pygame.freetype.set_default_resolution(72*factor)

imgloader = {"copycat":"char1","all cooperate":"char2","all cheat":"char3","grudger":"char4","detective":"char5","copykitten":"char6","simpleton":"char7","rando":"char8"}

def end():
    pygame.quit()
    exit(1)

class Screen:
    def __init__(self,initial_size,minimum_size,logo_path,caption,color_name='black',navbar=[]):
        self.screen = pygame.display.set_mode(initial_size,pygame.RESIZABLE)
        self.size = list(initial_size)
        self.minimum_size = minimum_size
        pygame.display.set_icon(pygame.image.load(logo_path))
        pygame.display.set_caption(caption)
        self.fill_color = color_name
        self.hovering = -1
        self.active = -1
    def before(self):
        self.screen.fill(self.fill_color)        
    def after(self):
        pygame.display.flip()
    def event_handler(self,buttons,reloaders,refresher=0):
        def reloader():
            for f in reloaders:
                f()
        while 1:
            state_change = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end()
                elif event.type == pygame.VIDEORESIZE:
                    self.size = list(event.size)
                    if self.size[0]<self.minimum_size[0]:
                        self.size[0] = self.minimum_size[0]
                    if self.size[1]<self.minimum_size[1]:
                        self.size[1] = self.minimum_size[1]
                    self.screen = pygame.display.set_mode(self.size,pygame.RESIZABLE)
                    state_change = 1
                elif event.type == pygame.MOUSEMOTION:
                    if self.hovering!=-1:
                        if ((buttons[self.hovering][0]) and (not pygame.Rect((buttons[self.hovering][1][0]+self.subscreen_position[0],buttons[self.hovering][1][1]+self.subscreen_position[1],buttons[self.hovering][1][2],buttons[self.hovering][1][3])).collidepoint(pygame.mouse.get_pos()))):
                            buttons[self.hovering][0]=0
                            self.hovering = -1
                            reloader()
                            state_change = 1
                    else:
                        for i in range(len(buttons)):
                            if pygame.Rect((buttons[i][1][0]+self.subscreen_position[0],buttons[i][1][1]+self.subscreen_position[1],buttons[i][1][2],buttons[i][1][3])).collidepoint(pygame.mouse.get_pos()):
                                buttons[i][0]=1
                                self.hovering = i
                                reloader()
                                state_change = 1
                                break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.hovering!=-1:
                        if (buttons[self.hovering][0]==1):
                            buttons[self.hovering][0]=2
                            self.active = self.hovering
                            reloader()
                            state_change = 1
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.active!=-1:
                        if (buttons[self.active][0]==2 and self.active==self.hovering):
                            buttons[self.active][0]=0
                            reloader()
                            for f in buttons[self.active][8]:
                                f[0](*f[1:])
                            state_change = 1
            if refresher:
                for i in range(len(buttons)):
                    if pygame.Rect((buttons[i][1][0]+self.subscreen_position[0],buttons[i][1][1]+self.subscreen_position[1],buttons[i][1][2],buttons[i][1][3])).collidepoint(pygame.mouse.get_pos()):
                        buttons[i][0]=1
                        self.hovering = i
                        reloader()
                        state_change = 1
            if state_change:
                break
    def flush(self):
        self.hovering = -1
        self.active = -1
    def place_subscreen(self,subscreen):
        size_of_subscreen = subscreen.get_size()
        self.subscreen_position = ((self.size[0]-size_of_subscreen[0])/2,(self.size[1]-size_of_subscreen[1])/2)
        self.screen.blit(subscreen,self.subscreen_position)

class Section:
    def __init__(self,size,color_name,caption,initial_state=False):
        self.background = pygame.Surface(size)
        self.background.fill(color_name)
        self.background_color = color_name
        self.caption = caption
        self.enabled = initial_state
        self.labels = []
        self.buttons = []
        self.objects = []
        self.active_position = [0,0]
    #For new label, offset = 0; For new line offset = line gap in terms of font size; For continuation offset = -1; For horizontally centering single label, offset = -2
    def add_label(self,text,text_color,font_name,font_size,position,offset=-1,italic=False,bold=False,background_color="white"):
        font_object = pygame.freetype.SysFont(font_name,int(font_size/factor),bold=bold,italic=italic) 
        font_object.antialiased = True
        img = font_object.render(text,text_color,bgcolor=background_color)[0]
        if (offset==0):
            self.active_position= [position[0],position[1]]
        elif (offset==-2):
            self.active_position = [position[0]-(img.get_width()/2),position[1]]
        elif (offset!=-1):
            self.active_position= [position[0],self.active_position[1]+offset*font_size]        
        copy_position = (self.active_position[0],self.active_position[1])
        self.labels.append([img,copy_position,text])
        self.active_position[0]+=img.get_width()
    def remove_label(self,text):
        for label in self.labels:
            if label[2]==text:
                self.labels.remove(label)
    def add_button(self,text,text_color,font_name,font_size,rect,passive_bg,hover_bg,active_bg,border_color,funcset,border_width=1):
        font_object = pygame.freetype.SysFont(font_name,int(font_size/factor))
        font_object.antialiased = True
        self.buttons.append([0,rect,[text,text_color,font_object],passive_bg,hover_bg,active_bg,border_color,border_width,funcset])
        #First integer: 0=none, 1=hover, 2=active
    def remove_button(self,text):
        for button in self.buttons:
            if button[2][0]==text:
                self.buttons.remove(button)
                break
    def config_machine(self,rect,left,right,top,bottom,leftn=None,rightn=None,topn=None,bottomn=None,color="grey"):
        for obj in self.objects:
            if obj[2]=="machine":
                self.objects.remove(obj)
        mach = pygame.Surface((rect[2],rect[3]))
        mach.fill(color)
        backcolors = ["white","yellow"]
        #pygame.draw.polygon(mach,backcolors[top],[(125,20),(205,100),(125,180),(45,100)])
        pygame.draw.polygon(mach,backcolors[top],[(125,20),(165,60),(125,100),(85,60)])        
        pygame.draw.polygon(mach,backcolors[right],[(165,60),(205,100),(165,140),(125,100)])
        pygame.draw.polygon(mach,backcolors[bottom],[(125,100),(165,140),(125,180),(85,140)])
        pygame.draw.polygon(mach,backcolors[left],[(85,60),(125,100),(85,140),(45,100)])        
        pygame.draw.polygon(mach,"black",[(125,20),(205,100),(125,180),(45,100)],width=5)
        pygame.draw.lines(mach,"black",True,[(165,140),(85,60),(85,140),(165,60)],width=5)
        pygame.draw.line(mach,"black",(125,20),(125,180),width=5)
        capt_obj = pygame.freetype.SysFont("consolas",12)
        mach.blits(((capt_obj.render("you",fgcolor="black",rotation=45)[0],(35,60)),(capt_obj.render("cheat",fgcolor="black",rotation=45)[0],(40,65)),(capt_obj.render("you",fgcolor="black",rotation=45)[0],(75,20)),(capt_obj.render("cooperate",fgcolor="black",rotation=45)[0],(70,15)),(capt_obj.render("they",fgcolor="black",rotation=-45)[0],(150,10)),(capt_obj.render("cooperate",fgcolor="black",rotation=-45)[0],(130,10)),(capt_obj.render("they",fgcolor="black",rotation=-45)[0],(190,50)),(capt_obj.render("cheat",fgcolor="black",rotation=-45)[0],(180,60))))  
        num_obj = pygame.freetype.SysFont("bahnschrift",24)
        if (bottomn==None and bottom) or (bottomn):
            mach.blits(((num_obj.render("0")[0],(105,130)),(num_obj.render("0")[0],(135,130))))
        if (topn==None and top) or (topn):
            mach.blits(((num_obj.render("+2")[0],(97,50)),(num_obj.render("+2")[0],(129,50))))
        if (leftn==None and left) or (leftn):
            mach.blits(((num_obj.render("+3")[0],(57,90)),(num_obj.render("-1")[0],(90,90))))
        if (rightn==None and right) or (rightn):
            mach.blits(((num_obj.render("-1")[0],(138,90)),(num_obj.render("+3")[0],(169,90))))
        self.objects.append([mach,rect,"machine"])
    def add_player(self,character,position,dir=0):
        img = pygame.image.load(character+".png")
        if dir:
            img = pygame.transform.flip(img,1,0)
        self.objects.append([img,position,character])
    def config_circle(self,charlist,scorelist,radius,rect,highlight=-1,linecolor="black"):
        w,h = rect[2],rect[3]
        circlesurf = pygame.Surface((w,h))
        circlesurf.fill("white")
        n = len(charlist)
        theta = 2*math.pi/n
        points = []
        for i in range(n):
            points.append(((w/2)+radius*math.cos(i*theta),(h/2)+radius*math.sin(i*theta)))
        for i in range(n):
            for j in range(i+1,n):
                pygame.draw.aaline(circlesurf,linecolor,points[i],points[j])
        if highlight!=-1:
            for i in range(n):
                pygame.draw.aaline(circlesurf,"yellow",points[i],points[highlight],blend=2)
        font_object = pygame.freetype.SysFont("bahnschrift",16)
        for i in  range(n):
            img = font_object.render("%d"%scorelist[i])[0]
            circlesurf.blit(img,((w/2)+(radius+20)*math.cos(i*theta)-(img.get_width()/2),(h/2)+(radius+20)*math.sin(i*theta)-(img.get_height()/2)))
        for i in  range(n):
            img = pygame.transform.scale(pygame.image.load(imgloader[charlist[i]]+".png"),(30,35))
            circlesurf.blit(img,((w/2)+(radius+55)*math.cos(i*theta)-(img.get_width()/2),(h/2)+(radius+55)*math.sin(i*theta)-(img.get_height()/2)))
        self.objects.append([circlesurf,rect,"circle"])
    def ready_static(self):
        self.background.fill(self.background_color)
        for label in self.labels:
            self.background.blit(label[0],label[1])
    def ready_dynamic(self):
        for button in self.buttons:
            if button[0]==0:
                pygame.draw.rect(self.background,button[3],button[1],border_radius=int(button[1][1]/2))
                text_img = button[2][2].render(button[2][0],button[2][1],bgcolor=button[3])[0]
            elif button[0]==1:
                pygame.draw.rect(self.background,button[4],button[1],border_radius=int(button[1][1]/2))
                text_img = button[2][2].render(button[2][0],button[2][1],bgcolor=button[4])[0]
            elif button[0]==2:
                pygame.draw.rect(self.background,button[5],button[1],border_radius=int(button[1][1]/2))
                text_img = button[2][2].render(button[2][0],button[2][1],bgcolor=button[5])[0] 
            pygame.draw.rect(self.background,button[6],button[1],width=button[7],border_radius=int(button[1][1]/2))         
            self.background.blit(text_img,(button[1][0]+((button[1][2]-text_img.get_width())/2),button[1][1]+((button[1][3]-text_img.get_height())/2)))
    def ready_objects(self):
        for obj in self.objects:
            self.background.blit(obj[0],obj[1])
    def flush(self):
        self.objects=[]
        self.labels=[]
        self.buttons=[]
    def reset(self):
        pass
    def return_subscreen(self):
        return self.background

class TempValues:
    def __init__(self):
        pass