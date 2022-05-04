def img_read(path):
    """
    Read the image with given `path` to a RGBImage instance.
    """
    mat = cv2.imread(path).transpose(2, 0, 1).tolist()
    mat.reverse()  # convert BGR (cv2 default behavior) to RGB
    return RGBImage(mat)


def img_save(path, image):
    """
    Save a RGBImage instance (`image`) as a image file with given `path`.
    """
    mat = np.stack(list(reversed(image.get_pixels()))).transpose(1, 2, 0)
    cv2.imwrite(path, mat)

class RGBImage:
    """
    This is a model that an image objects in the form of
    RGB color used
    """

    def __init__(self, pixels):
        """
        Initiates a pixel that is a 3-dimensional list that has c
        channels i rows and j columns
        """
        # YOUR CODE GOES HERE #
        #需要写assertioon吗？ 比如 pixels 里面数字的type, len(pixels)==3\
#要不要加 pixels 以外的 attribute? 例如 num_rows 写 size（）的时候可以直接用
        self.pixels = pixels  # initialze the pixels list here
        self.num_rows = len(pixels[0])
        self.num_cols = len(pixels[0][0])
        self.red_idx=0
        self.green_idx=1
        self.blue_idx=2
        self.num_channels=3

    def crop(image, tl_row, tl_col, target_size):
        """
        TODO: add description
        """
        new_image = image.copy()
        br_row = tl_row + target_size[0] -1
        br_col = tl_col + target_size[1] -1
        if br_row + 1 <= new_image.num_rows and br_col + 1 <= new_image.num_cols:
            crop_row = [c[tl_row:(br_row + 1)] for c in new_image.pixels]
            crop_col = [i[tl_col:(br_col+1)] for c in crop_row for i in c]
            new_image.pixels = crop_col
        """
        elif br_row + 1 > new_image.num_rows and br_col + 1 <= new_image.num_cols:
            crop_row = [c[tl_row:] for c in new_image.pixels]
            crop_col = [i[tl_col:(br_col + 1)] for c in crop_row for i in c]
            new_image.pixels = crop_col
        elif br_row + 1 <= new_image.num_rows and br_col + 1 > new_image.num_cols:
            crop_row = [c[tl_row:(br_row + 1)] for c in new_image.pixels]
            crop_col = [i[tl_col:] for c in crop_row for i in c]
            new_image.pixels = crop_col
        elif br_row + 1 > new_image.num_rows and br_col + 1 > new_image.num_cols:
            crop_row = [c[tl_row:] for c in new_image.pixels]
            crop_col = [i[tl_col:] for c in crop_row for i in c]
            new_image.pixels = crop_col
        """
        return new_image