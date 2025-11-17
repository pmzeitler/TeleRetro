import os
import pygame as pg

from datetime import datetime

pg.init()

UPDATE_FPS = 240
DISPLAY_FPS = 60
FPS_DIVIDER = UPDATE_FPS / DISPLAY_FPS
divider_count = 0

elapsed_ms = 0

update_clock = pg.time.Clock()
main_dir = os.path.split(os.path.abspath(__file__))[0]

font_md = pg.font.Font(os.path.join(main_dir, "chevy_picory.ttf"), 24)
font_lg = pg.font.Font(os.path.join(main_dir, "chevy_picory.ttf"), 48)

windowflags = pg.SHOWN | pg.HWSURFACE;

(width, height) = (640, 480)
#pg.display.set_icon(window_icon)
pg.display.set_caption("TeleRetro")
screen = pg.display.set_mode((width, height), windowflags)

background_colour = (0,0,155)
screen.fill(background_colour)
pg.display.flip()

def get_rendered_length(font, text):
  tmp_surf = font.render(text, True, (0,0,0))
  rsize = tmp_surf.get_rect()
  return (rsize.w, rsize.h)

def render_shadow_text(screen, font, text, position_x, position_y):
  if (screen == None):
    return False
  shadow_surface = font.render(text, True, (0,0,0))
  screen.blit(shadow_surface, (position_x + 3, position_y + 3))
  text_surface = font.render(text, True, (255,255,255))
  screen.blit(text_surface, (position_x, position_y))

running = True
show_colon = True
while running:
  update_clock.tick(UPDATE_FPS)
  elapsed_ms += update_clock.get_time()

  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False

  divider_count += 1

  if (divider_count >= FPS_DIVIDER):
    #update display    
    divider_count = 0
    if (elapsed_ms >= 1000):
      elapsed_ms = 0
      show_colon = not show_colon

    pg.draw.rect(screen, (255,0,0), pg.Rect(0,0,640,80))
    
    pg.draw.rect(screen, (0,255,0), pg.Rect(0,400,640,80))
    
    now = datetime.now()
    format_str = "%H %M"
    if (show_colon):
      format_str = "%H:%M"
      
    formatted_time = now.strftime(format_str)
    tsize = get_rendered_length(font_lg, formatted_time)
    render_shadow_text(screen, font_lg, formatted_time, 635-tsize[0], 5)
    tsize = get_rendered_length(font_lg, "Testing Second Line")
    render_shadow_text(screen, font_lg, "Testing Second Line", 635-tsize[0], 75-tsize[1])
    
    pg.display.flip()
	

