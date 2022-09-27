import pygame

pygame.init()

def end():
    pygame.quit()
    exit(1)

class Screen:
    def __init__(self,initial_size,minimum_size,logo_path,caption,color_name='black'):
        self.screen = pygame.display.set_mode(initial_size,pygame.RESIZABLE)
        self.size = list(initial_size)
        self.minimum_size = minimum_size
        pygame.display.set_icon(pygame.image.load(logo_path))
        pygame.display.set_caption(caption)
        self.fill_color = pygame.Color(color_name)
        self.hovering = -1
        self.active = -1
    def before(self):
        self.screen.fill(self.fill_color)
    def after(self):
        pygame.display.flip()
    def event_handler(self,buttons,reloader):
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
                            buttons[self.active][0]=3
                            reloader()
                            buttons[self.active][7][0](*buttons[self.active][7][1:])
                            state_change = 1
            if state_change==1:
                break
    def flush(self):
        self.hovering = -1
        self.active = -1
    def place_subscreen(self,subscreen):
        size_of_subscreen = subscreen.get_size()
        self.subscreen_position = ((self.size[0]-size_of_subscreen[0])/2,(self.size[1]-size_of_subscreen[1])/2)
        self.screen.blit(subscreen,self.subscreen_position)

class Section:
    def __init__(self,size,color_name,initial_state=False):
        self.background = pygame.Surface(size)
        self.background.fill(pygame.Color(color_name))
        self.enabled = initial_state
        self.labels = []
        self.buttons = []
        self.objects = []
        self.active_position = [0,0]
    #Check for invalid/unavailable fonts
    #For new label, offset = 0; For new line offset = line gap in terms of font size; For continuation leave undeclared
    def add_label(self,text,text_color,font_name,font_size,position,offset=-1):
        if (offset!=-1):
            self.active_position= [position[0],self.active_position[1]+offset*font_size]
        font_object = pygame.font.Font(pygame.font.match_font(font_name),font_size)
        img = font_object.render(text,1,pygame.Color(text_color))
        copy_position = (self.active_position[0],self.active_position[1])
        self.labels.append([img,copy_position])
        self.active_position[0]+=img.get_width()
    def add_button(self,text,text_color,font_name,font_size,rect,passive_bg,active_bg,passive_border,active_border,funcset):
        font_object = pygame.font.Font(pygame.font.match_font(font_name),font_size)
        text_img = font_object.render(text,1,pygame.Color(text_color))
        self.buttons.append([0,rect,text_img,pygame.Color(passive_bg),pygame.Color(active_bg),pygame.Color(passive_border),pygame.Color(active_border),funcset])
        #First integer: 0=none, 1=hover, 2=active, 3=done
    def ready_static(self):
        for label in self.labels:
            self.background.blit(label[0],label[1])
    def ready_dynamic(self):
        for button in self.buttons:
            if button[0]==0:
                pygame.draw.rect(self.background,button[3],button[1],border_radius=int(button[1][1]/2))
                pygame.draw.rect(self.background,button[5],button[1],width=2,border_radius=int(button[1][1]/2))
            elif button[0]==1:
                pygame.draw.rect(self.background,button[3],button[1],border_radius=int(button[1][1]/2))
                pygame.draw.rect(self.background,button[6],button[1],width=2,border_radius=int(button[1][1]/2))
            elif button[0]==2:
                pygame.draw.rect(self.background,button[4],button[1],border_radius=int(button[1][1]/2))
                pygame.draw.rect(self.background,button[6],button[1],width=2,border_radius=int(button[1][1]/2))
            elif button[0]==3:
                pygame.draw.rect(self.background,button[4],button[1],border_radius=int(button[1][1]/2))
                pygame.draw.rect(self.background,button[5],button[1],width=2,border_radius=int(button[1][1]/2))            
            self.background.blit(button[2],(button[1][0]+((button[1][2]-button[2].get_width())/2),button[1][1]+((button[1][3]-button[2].get_height())/2)))
    def flush(self):
        pass
    def return_subscreen(self):
        return self.background