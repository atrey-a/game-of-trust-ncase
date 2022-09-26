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
    def before(self):
        self.screen.fill(self.fill_color)
    def after(self):
        pygame.display.flip()
    def event_handler(self):
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
                    state_change = 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    state_change = 1
                elif event.type == pygame.MOUSEBUTTONUP:
                    state_change = 1
            if state_change==1:
                break
    def place_subscreen(self,subscreen):
        size_of_subscreen = subscreen.get_size()
        position = ((self.size[0]-size_of_subscreen[0])/2,(self.size[1]-size_of_subscreen[1])/2)
        self.screen.blit(subscreen,position)

class Section:
    def __init__(self,size,color_name,initial_state=False):
        self.background = pygame.Surface(size)
        self.background.fill(pygame.Color(color_name))
        self.enabled = initial_state
        self.labels = []
        self.buttons = []
        self.objects = []
    #Check for invalid/unavailable fonts
    def add_labels(self,*lables): #(text,color_name,font_name,font_size,position(strictly tuple),line_break)
        self.active_position = list(lables[0][4])
        for label in lables:
            font_object = pygame.font.Font(pygame.font.match_font(label[2]),label[3])
            if label[5]:
                self.active_position[0] = lables[0][4][0]
                self.active_position[1] += label[3]*1.5
                print(lables[0][4][0])
            img = font_object.render(label[0],1,pygame.Color(label[1]))
            copy_position = (self.active_position[0],self.active_position[1])
            self.labels.append([img,copy_position])
            self.active_position[0]+=img.get_width()
    def ready_subscreen(self):
        for label in self.labels:
            print(label[1])
            self.background.blit(label[0],label[1])
    def return_subscreen(self):
        return self.background