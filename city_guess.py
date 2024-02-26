from yandex_map.yandex_map import (
    show_map,
    get_map,
    get_coordinates,
    random_spn,
    del_map
)
import pygame
from random import shuffle


CITES = ['Великий Новгород', 'Москва', 'Санкт-Петербург', 'Псков', 'Ростов-на-Дону',
         'Токио', 'Лиссабон', 'Хельсинки', 'Стокгольм', 'Осло',
         'Калькутта', 'Рио-де_Жанейро', 'Денвер', 'Пекин', 'Исламабад',
         'Казань', 'Екатеринбург', 'Ставрополь', 'Южно-Сахалинск', 'Лос-Анджелес']

images = [get_map(get_coordinates(city), spn=random_spn(0.01, 0.25), map_format="sat") for city in CITES]
shuffle(images)


class Slider(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.count = 1
        sprites.add(self)

    def update(self):
        screen.fill("black")
        screen.blit(pygame.image.load(images[self.count - 1]), (0, 0))


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((600, 450))

    sprites = pygame.sprite.Group()

    slider = Slider()

    running = True
    while running:
        if slider.count == 20:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                slider.count += 1

        sprites.update()
        pygame.display.flip()
    pygame.quit()
    for img in images:
        del_map(img)