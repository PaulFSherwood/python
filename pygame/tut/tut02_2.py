import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None 

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((350,350), pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load("images/myimage.jpg").convert()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(self._image_surf, (0, 0))
        self._display_surf.blit(self._image_surf, (2, 2),     ((118, 2), (115, 115)))
        self._display_surf.blit(self._image_surf, (117, 117), ((118, 2), (115, 115)))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
