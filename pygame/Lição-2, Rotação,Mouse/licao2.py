#I, Frederico Möller, am not the author of this template
#BUT I CAN NOT REMEMBER EXACTLY WHERE I FOUND IT.
#So, if anyone knows the source, tell me, then I can give the proper credit.

# import the pygame module, so you can use it
import pygame
import draw_aux

W_SIZE = (640,480)
P_SIZE = (64,64)
# define a main function
def main():
    clock = pygame.time.Clock()
     
    # initialize the pygame module
    pygame.init()
    # Carrega imagens que serão usadas por esse script
    logo = pygame.image.load("imagens/icon.png")
    bg_img = pygame.image.load("imagens/redsand1280.png")
    pl_img = pygame.image.load("imagens/player.png")
    
    pygame.display.set_icon(logo)
    pygame.display.set_caption("licao2")
    # Inicializa a superfície do display
    screen = pygame.display.set_mode(W_SIZE)

    #Redimensiona imagens
    pl_img = pygame.transform.scale(pl_img,P_SIZE)

    #Posição inicial de objetos
    pl_pos = (int(W_SIZE[0]/2)-(P_SIZE[0]/2),int(W_SIZE[1]/2)-(P_SIZE[1]/2))
    pl_angle = 0
    pl_img_rt = draw_aux.rotacionar(pl_img,pl_angle)
    pl_pos_rt = (pl_pos[0]+pl_img_rt[1][0],pl_pos[1]+pl_img_rt[1][1])

    
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
        # event handling, gets all event from the event queue:
        
        #Calcula o angulo de acordo com a posição do mouse e do player:
        ms_pos = pygame.mouse.get_pos()
        pl_angle = draw_aux.calcula_angulo(ms_pos,pl_pos)
        pl_img_rt = draw_aux.rotacionar(pl_img,pl_angle)
        pl_pos_rt = (pl_pos[0]+pl_img_rt[1][0],pl_pos[1]+pl_img_rt[1][1])

        screen.blit(bg_img,(0,0))
        screen.blit(pl_img_rt[0],pl_pos_rt)
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
