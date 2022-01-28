import os
import pygame

from config import config


def is_png_file(filename):
    return filename.split('.')[-1] == 'png'


class Assest:
    def __init__(self):
        self.assests = {'img': {}, 'sound': {}}
        self.load_images('assests/images/')

    def load_images(self, path):
        all_files = os.listdir(path)
        png_files = filter(is_png_file, all_files)

        for filename in png_files:
            full_path = path + filename
            img = self.load_img(full_path)
            img_name = filename.split('.')[0]
            self.assests['img'][img_name] = img

    def load_img(self, path):
        img = pygame.image.load(path)
        img.set_colorkey(config['images']['colorkey'])
        return img.copy()
