from base64 import encode
import numpy as np
from PIL import Image, ImageOps


class GrayscaleImage:
    """
    Grayscale Image class
    """

    def __init__(self, nrows, ncols) -> None:
        """
        Adds attributes to the object
        >>> gr = GrayscaleImage(100, 100)
        >>> print(gr.nrows)
        100
        """
        self.nrows = nrows
        self.ncols = ncols
        self.grid = np.zeros((nrows, ncols), dtype=int)
        self.start_code_dictionary = dict((i, [i]) for i in range(256))

    def width(self):
        """
        Returns the width of the image
        >>> gr = GrayscaleImage(100, 100)
        >>> print(gr.width())
        100
        """
        return self.ncols

    def height(self):
        """
        Returns the height of the image
        >>> gr = GrayscaleImage(100, 100)
        >>> print(gr.height())
        100
        """
        return self.nrows

    def clear(self, value):
        """
        Clears the image by assigning exact value to every pixel
        >>> gr = GrayscaleImage(100, 100)
        >>> gr.clear(30)
        >>> print(gr.grid[0, 1:3])
        [30, 30, 30]
        """
        for row in range(self.nrows):
            for col in range(self.ncols):
                self.grid[row, col] = value

    def getitem(self, row, col):
        """
        Get an exact pixel
        >>> gr = GrayscaleImage(100, 100)
        >>> print(gr.getitem(20,40))
        0
        """
        return self.grid[row, col]

    def setitem(self, row, col, value):
        """
        Sets an exact value ti exact pixel
        >>> gr = GrayscaleImage(100, 100)
        >>> gr.setitem(20,30,30)
        >>> print(gr.getitem(20,30))
        30
        """
        self.grid[row, col] = value

    def from_file(self, path):
        """
        Extrect image from file and creates grayscale
        """
        im1 = Image.open(path)
        im2 = ImageOps.grayscale(im1)
        self.grid = np.array(im2)
        self.nrows, self.ncols = im1.size[1], im1.size[0]

    def lzw_compression(self):
        """
        Compresses to lzw
        """
        size = 256
        im_code = self.start_code_dictionary
        start = []
        result = []
        list_grid = self.grid.tolist()
        for row in list_grid:
            for value in row:
                values_sequence = start.copy()
                values_sequence.append(value)
                if values_sequence in im_code.values():
                    start = values_sequence
                else:
                    val_list = list(im_code.values())
                    key_list = list(im_code.keys())
                    position = val_list.index(start)
                    result.append(key_list[position])
                    im_code[size] = values_sequence
                    size += 1
                    start = [values_sequence[-1]]
        if start:
            val_list = list(im_code.values())
            key_list = list(im_code.keys())
            position = val_list.index(start)
            result.append(key_list[position])
        return result

    def lzw_decompression(self, compressed=list):
        """
        Decompresses from lzw
        """
        size = 256
        im_code = self.start_code_dictionary
        start = [compressed.pop(0)]
        result = [start]
        for value in compressed:
            if value in im_code.keys():
                entry = im_code[value]
            elif value == size:
                entry = start + start[0]
            else:
                raise ValueError('Bad compressed k: %s' % value)
            result.append(entry)
            im_code[size] = start + [entry[0]]
            size += 1

            start = entry
        result2 = [j for i in result for j in i]
        arrr_list = []
        row_list = []
        for el in result2:
            if len(row_list) < self.ncols:
                row_list.append(el)
            elif len(row_list) == self.ncols:
                arrr_list.append(row_list)
                row_list = [el]
        img_array = np.array(arrr_list)
        new_img = Image.fromarray(img_array)
        new_img.show()
        return img_array


if __name__ == '__main__':
    gr = GrayscaleImage(100, 100)
    gr.from_file(
        "C:\\ucu\\pngtree-cure-starry-sky-night-sky-star-png-image_38228.jpg")
    print(gr.nrows, gr.ncols)
    print(gr.height())
    testtt = gr.lzw_compression()
    res = gr.lzw_decompression(testtt)
    com1 = res.tolist()
    com2 = gr.grid.tolist()
    print(com1[2])
    print(com2[2])
