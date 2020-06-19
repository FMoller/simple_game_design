#I, Frederico Möller, am not the author of this template
#BUT I CAN NOT REMEMBER EXACTLY WHERE I FOUND IT.
#So, if anyone knows the source, tell me, then I can give the proper credit.

# import the pygame module, so you can use it
import pygame
import draw_aux
import math

W_SIZE = (640,480)
P_SIZE = (64,64)

# define a main function
def main():
    r = 0
    g = 0
    clock = pygame.time.Clock()
    
    # initialize the pygame module
    pygame.init()
    # Carrega imagens que serão usadas por esse script
    logo = pygame.image.load("imagens/icon.png")
    
    pygame.display.set_icon(logo)
    pygame.display.set_caption("licao2")
    # Inicializa a superfície do display
    screen = pygame.display.set_mode(W_SIZE)

    
    # Sobrescreve os blocos de informação com a imagem
    #screen.blit(bg_img,(0,0))
    #screen.blit(pl_img_rt[0],pl_pos_rt)
    # Envia os dados a serem desenhados para o driver de video
    pygame.display.flip()
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        screen.fill((0,0,0))
        # leitura de comandos do jogador:
        ms_pos = pygame.mouse.get_pos()
        # processamento das ações do jogador
        g = math.floor(ms_pos[0]/640*255)
        r = math.floor(ms_pos[1]/480*255)
        cor=(r,g,0)
        print(cor)
        screen.fill(cor) 
        pygame.display.flip()
        clock.tick(60)
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
##                 change the value to False, to exit the main loop
                running = False
    pygame.quit()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
