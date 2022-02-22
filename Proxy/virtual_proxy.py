class Bitmap:

    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image {self.filename}')

    def draw(self):
        print(f'Drawing  image {self.filename}')


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image):
    print('About drawing image')
    image.draw()
    print(f'Done drawing.')


image = LazyBitmap('palm.jpg')
draw_image(image)
