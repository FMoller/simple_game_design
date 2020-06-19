import pygame
import numpy as np

def calcula_angulo(ms_pos,pl_pos,last_angle=0):
    pl_ms_dx = ms_pos[0]-pl_pos[0]
    pl_ms_dy = -ms_pos[1]+pl_pos[1]
    
    if pl_ms_dy == 0:
        if pl_ms_dx == 0:
            return last_angle
        elif pl_ms_dx > 0:
            return 0
        else:
            return 180
    elif pl_ms_dy > 0:
        if pl_ms_dx == 0:
            return 90
        elif pl_ms_dx > 0:
            return np.rad2deg(np.arctan(pl_ms_dy/pl_ms_dx))
        else:
            return 180+np.rad2deg(np.arctan(pl_ms_dy/pl_ms_dx))
    else:
        if pl_ms_dx == 0:
            return 270
        elif pl_ms_dx > 0:
            return 360+np.rad2deg(np.arctan(pl_ms_dy/pl_ms_dx))
        else:
            return 180+np.rad2deg(np.arctan(pl_ms_dy/pl_ms_dx))

#ref = https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
def rotacionar(imagem,angulo):
    centro = imagem.get_rect().center
    n_imagem = pygame.transform.rotate(imagem,angulo)
    n_rect = n_imagem.get_rect(center = centro)
    return(n_imagem,n_rect)
            
        
            
