"""
DSC 20 Mid-Quarter Project
Name: Yutian Shi, Sha Lei
PID:  A16356870, A16344449
"""

# Part 1: RGB Image #
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
        self.pixels = pixels  # initialze the pixels list here
        self.num_rows = len(pixels[0])
        self.num_cols = len(pixels[0][0])
        self.red_idx=0
        self.green_idx=1
        self.blue_idx=2
        self.num_channels=3

    def size(self):
        """
        get the size of the image in the form of tuple by getting
        the length of second level list and length of third level
        list
        """

        return (self.num_rows, self.num_cols)

    def get_pixels(self):
        """
        get the element in the original 3d list copy into a
        new 3d list
        """
        pixels_deep_copy=\
[[list(row) for row in channel] for channel in self.pixels]
        return pixels_deep_copy

    def copy(self):
        """
        get the copy pixel's RGBImage instance
        """
        # YOUR CODE GOES HERE #
        new_instance=RGBImage(self.get_pixels())
        return new_instance

    def get_pixel(self, row, col):
        """
        Get the element that has same row index
        and column index in the outer three list
        """

        if (not isinstance(row, int)) or (not isinstance(col, int)):
            raise TypeError()
        elif row<0 or col<0 or row>=self.num_rows or col>=self.num_cols:
            raise ValueError()
        else:
            return (self.pixels[self.red_idx][row][col], \
                    self.pixels[self.green_idx][row][col], \
                    self.pixels[self.blue_idx][row][col])

    def set_pixel(self, row, col, new_color):
        """
        update the color of pixel at particular position with
        the data in new_color
        """

        if (not isinstance(row, int)) or (not isinstance(col, int)):
            raise TypeError()
        elif row<0 or col<0 or row>=self.num_rows or col>=self.num_cols:
            raise ValueError()
        else:
            num_of_colors=3
            for color_idx in range(num_of_colors):
                if new_color[color_idx]<0:
                    continue
                self.pixels[color_idx][row][col]=new_color[color_idx] 

# Part 2: Image Processing Methods #
class ImageProcessing:
    """
    A class that abstracts various methods to process image
    """

    @staticmethod
    def negate(image):
        """
        A method that inverts all pixel values in the input image
        """
        new_image=image.copy()
        negating=[new_image\
.set_pixel(row, col, tuple([255-c for c in image.get_pixel(row, col)])) \
for row in range(new_image.num_rows) for col in range(new_image.num_cols)]
        return new_image

    @staticmethod
    def tint(image, color):
        """
        A method that updates every pixel value in the input image with the \
        average of each previous pixel value and the new color.
        """
        new_image=image.copy()
        negating=[new_image\
.set_pixel(row, col, tuple([(color[i]+image.get_pixel(row, col)[i])//2 for i in range(new_image.num_channels)])) \
for row in range(new_image.num_rows) for col in range(new_image.num_cols)]
        return new_image

    @staticmethod
    def clear_channel(image, channel):
        """
        This method clears the given channel in the image, and returns the new
        image
        """
        new_image = image.copy()
        lst1 = [0 for j in range(new_image.num_cols)]
        lst2 = [lst1 for i in range(new_image.num_rows)]
        new_image.pixels[channel] = lst2
        return new_image




    @staticmethod
    def crop(image, tl_row, tl_col, target_size):
        """
        This method crops the image. It returns a new image with the top-left
        corner identifies by tl_row and tl_col, and the new image size would
        be the targeted_size represented in (n_rows, n_cols)
        """
        new_image = image.copy()
        br_row = tl_row + target_size[0] -1
        br_col = tl_col + target_size[1] -1
        if br_row + 1 <= new_image.num_rows and br_col + 1 <= new_image.num_cols:
            crop_row = [c[tl_row:(br_row + 1)] for c in new_image.pixels]
            crop_col = [[i[tl_col:(br_col+1)] for i in c] for c in crop_row]
            new_image.pixels = crop_col
        elif br_row + 1 > new_image.num_rows and br_col + 1 <= new_image.num_cols:
            crop_row = [c[tl_row:] for c in new_image.pixels]
            crop_col = [[i[tl_col:(br_col+1)] for i in c] for c in crop_row]
            new_image.pixels = crop_col
        elif br_row + 1 <= new_image.num_rows and br_col + 1 > new_image.num_cols:
            crop_row = [c[tl_row:(br_row + 1)] for c in new_image.pixels]
            crop_col = [[i[tl_col:] for i in c] for c in crop_row]
            new_image.pixels = crop_col
        elif br_row + 1 > new_image.num_rows and br_col + 1 > new_image.num_cols:
            crop_row = [c[tl_row:] for c in new_image.pixels]
            crop_col = [[i[tl_col:] for i in c] for c in crop_row]
            new_image.pixels = crop_col
        return new_image



    @staticmethod
    def chroma_key(chroma_image, background_image, color):
        """
        The methods replaces all pixels that have the input color in the
        chroma image with the corresponding pixels in the background_image
        """
        if (not isinstance(chroma_image, RGBImage)) or \
                (not isinstance(background_image, RGBImage)):
            raise TypeError()
        elif chroma_image.size() != background_image.size():
            raise ValueError()
        else:
            new_image = chroma_image.copy()
            for row in range(new_image.num_rows):
                for col in range(new_image.num_cols):
                    if new_image.get_pixel(row, col) == color:
                        new_image \
                            .set_pixel(row, col, background_image.get_pixel(row, col))
        return new_image

    # rotate_180 IS FOR EXTRA CREDIT (points undetermined)
    @staticmethod
    def rotate_180(image):
        """
        This method returns a new image that is rotated for 180 degrees
        """
        """
        new_image = image.copy()
        for c in range(new_image.num_channels):
            new_image.pixels[c] = new_image.pixels[c][::-1]
            for i in range(new_image.num_rows):
                new_image.pixels[c][i] = new_image.pixels[c][i][::-1]
        """
        new_image = image.copy()
        new_image.pixels = [new_image.pixels[c][::-1] for c in range(new_image.num_channels)]
        new_image.pixels = [[new_image.pixels[c][i][::-1] for i in range(new_image.num_rows)] \
                            for c in range(new_image.num_channels)]
        return new_image



# Part 3: Image KNN Classifier #
class ImageKNNClassifier:
    """
    Implementation of an image KNN Classifier
    """

    def __init__(self, n_neighbors):
        """
        Constructor of ImageKNNClassifier

        Parameters:
        n_neighbors(int): the number of neighbors the model need to find to
        make prediction
        data(list): a list to store data that is initially an empty list.
        """
        self.neighbor = n_neighbors
        self.data = []

    def fit(self, data):
        """
        This method completes the fitting process by storing the input data in
        the classifier instance. The input data is a list of tuples each with
        image and label. Image is a RGBImage instance and label is a string.
        """
        if len(data) <= self.n_neighbors:
            raise ValueError()
        elif self.data != []:
            raise ValueError()
        else:
            self.data = data



    @staticmethod
    def distance(image1, image2):
        """
        This method calculates the distance between two images by calulating
        the square root of the total sum of the squared difference between
        the every pair of values from the two image that have the same position
        (channel, row, column).
        """
        if not isinstance(image1,RGBImage) or not isinstance(image2,RGBImage):
            raise TypeError
        if image1.size() != image2.size():
            raise ValueError

        image1_lst = [j for c in image1.pixels for i in c for j in i]
        image2_lst = [j for c in image2.pixels for i in c for j in i]
        distance = sum([(image1_lst[i]-image2_lst[i])**2 for i in range(len(image1_lst))]) ** 0.5
        return distance

    @staticmethod
    def vote(candidates):
        """
        This method calculates the distance between two images by calulating
        the square root of the total sum of the squared difference between
        the every pair of values from the two image that have the same position
        (channel, row, column).
        """
        label = {}
        for i in candidates:
            if i not in label:
                label[i] = 1
            else:
                label[i] += 1
        biggest = max(label.values())
        for i in label:
            if label[i] == biggest:
                return i

    def predict(self, image):
        """
        The method predicts the label of the input image based on the KNN
        classification algorithm. The vote() method would be applied to find
        the most popular label among the nearest neighbors.
        """
        if self.data == []:
            raise ValueError
        dist = [(ImageKNNClassifier.distance(img[0],image),img[1]) for img in self.data]
        dist.sort(key=lambda x: x[0])
        neighbors = dist[0:self.neighbor]
        find_label = [i[1] for i in neighbors]
        return ImageKNNClassifier.vote(find_label)







