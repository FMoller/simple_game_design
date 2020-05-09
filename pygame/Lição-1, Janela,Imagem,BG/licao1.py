#I, Frederico Möller, am not the author of this template
#BUT I CAN NOT REMEMBER EXACTLY WHERE I FOUND IT.
#So, if anyone knows the source, tell me, then I can give the proper credit.

# import the pygame module, so you can use it
import pygame

W_SIZE = (640,480)
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # Carrega imagens que serão usadas por esse script
    logo = pygame.image.load("imagens/icon.png")
    bg_img = pygame.image.load("imagens/redsand1280.png")
    
    pygame.display.set_icon(logo)
    pygame.display.set_caption("licao1")
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode(W_SIZE)
    # Sobrescreve os blocos de informação com a imagem
    screen.blit(bg_img,(-10,-10))
    # Envia os dados a serem desenhados para o driver de video
    pygame.display.flip()
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
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
