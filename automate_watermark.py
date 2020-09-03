import os
from os.path import isfile, join

from PIL import Image


class WatermarkAutomation:
    def __init__(self):
        self.file_extensions = ('.jpg', '.png', '.jpeg')
        self.in_directory = f"{os.path.dirname(os.path.abspath(__file__))}/{'pre_photos'}"
        self.out_directory = f"{os.path.dirname(os.path.abspath(__file__))}/{'post_photos'}"

        self.watermark = Image.open('watermark.png')
        self.watermark_width = self.watermark.width
        self.watermark_heigth = self.watermark.height

    def run(self):
        pictures = self.get_files_from_in_directory()
        self.put_watermark_on_multiple_files(pictures)
        self.delete_images_from_directory(pictures)

    def put_watermark_on_multiple_files(self, pictures):
        for picture in pictures:
            self.put_watermark_on_single_file(picture)

    def get_files_from_in_directory(self):
        onlyfiles = [f for f in os.listdir(
            self.in_directory) if isfile(join(self.in_directory, f))]
        return [f for f in onlyfiles if f.endswith(self.file_extensions)]

    def delete_images_from_directory(self, images):
        for image in images:
            os.remove(f'{self.in_directory}/{image}')

    def put_watermark_on_single_file(self, image_name):
        image = Image.open(f'{self.in_directory}/{image_name}')
        image_width = image.width
        image_height = image.height
        image.paste(self.watermark,
                    (int((image_width - self.watermark_width) / 2), int((image_height - self.watermark_heigth) / 2)),
                    self.watermark)
        image.save(f'{self.out_directory}/marked_{image_name}')


def main():
    automate = WatermarkAutomation()
    automate.run()


if __name__ == '__main__':
    main()
