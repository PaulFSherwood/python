#!/usr/bin/env python

"""
Name:    002_display_fps_yipyip.py
Purpose: Display framerate and playtime
URL:     http://thepythongamebook.com/en:part2:pygame:step002
Author:  yipyip
Licence: gpl, see http://www.gnu.org/licenses/gpl.html
"""

####

import pygame 

####

class PygView(object):

  
    def __init__(self, width, fps):
        """Initialize pygame, window, background, font,...
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = width // 4
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF) # set screen size of game
        self.background = pygame.Surface(self.screen.get_size()).convert()                 # Create an empty pygame surface and convert
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', self.height // 7, bold=True)
        try:
            self.guage = pygame.image.load("gauge.bmp").convert()
        except:
            raise UserWarning, "Unable to find the image in the folder :-< "


    def run(self):
        """The mainloop
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0
            self.draw_text("FPS: %6.3f%sPLAYTIME: %6.3f SECONDS" %
                           (self.clock.get_fps(), " "*5, self.playtime))

            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.guage, (0, 0))
            
        pygame.quit()


    def draw_text(self, text):
        """Center text in window
        """
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))

####

if __name__ == '__main__':

    # call with width of window and fps
    PygView(600, 100).run()
