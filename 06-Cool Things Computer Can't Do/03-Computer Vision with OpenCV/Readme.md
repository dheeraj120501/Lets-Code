## Introduction

The goal of computer vision is to understand the story unfolding in a picture.

- As humans, this is quite simple. But for computers, the task is extremely difficult.

A image is an array/matrix of pixels in raster graphics.

- To get a specific pixel of an image we can do img[x, y] this will give the pixel at x, y co-ordinate of image.
- This pixel is represented as a tuple.

Pixels are the raw building blocks of an image. There is no finer granularity than the pixel.

- Most pixels are represented in two ways: grayscale and color.
- In a grayscale image, each pixel has a value between 0 and 255, where zero corresponds to “black” and 255 corresponds to “white”.
- Color pixels are normally represented in the RGB color space – one value for the Red component, one for Green, and one for Blue.

If we say a certain image or screen size is `w x h` it means it has w pixels along x axis and h pixels on y axis.

- HD is 1280x720 it means it has 1280 pixels along x axis and 720 pixels along y axis.

The more the pixels the better the image, video(a sequence of images).

Level of an image is the shade of black and white it support.

- Binary image is a black and white image that has only 2 levels 0(black) and 1(white).
- For grayscale image we use 256 lvl which mean we have 256 shades of black and white where 0(black) and 255(white). So a grayscale HD image is 1280 x 720 x 1 (width x height x channel).

For color image we have 3 Grayscale images presenting the intensity of Red, Green, Blue (RGB), Combining the 3 we get a colored image. So a colored HD image is 1280 x 720 x 3.

RGB image has 3 channels Red, Blue, Green.

Binary images can be achieved by thresholding.

## Computer Vision using Python

Let’s review some important Python packages that we’ll use for computer vision.

- **numpy and scipy**
  - NumPy is a library for the Python programming language that (among other things) provides support for large, multidimensional arrays.
  - Using NumPy, we can express images as multi-dimensional arrays.
  - Representing images as NumPy arrays is not only computationally and resource efficient, many other image processing and machine learning libraries use NumPy array representations as well.
  - Using NumPy’s built-in high-level mathematical functions, we can quickly and easily perform numerical analysis on an image.
  - SciPy adds further support for scientific and technical computing.
- **matplotlib**
  - matplotlib is a plotting library.
  - When analyzing images, we’ll make use of matplotlib.
  - Whether plotting image histograms or simply viewing the image itself, matplotlib is a great tool to have in your toolbox.
- **opencv**
  - The main goal of OpenCV is real-time image processing.
  - The library itself is written in C/C++, but Python bindings are provided when running the installer.
- **mahotas**
  - Much of the functionality implemented in Mahotas can be found in OpenCV, but in some cases, the Mahotas interface is just easier to use.
  - Mahotas, just like OpenCV, relies on NumPy arrays.
  - It is used to complement opencv.
- **scikit-learn**
  - scikit-learn isn’t an image processing or computer vision library – it’s a machine learning library.
  - One can’t have advanced computer vision techniques without some sort of machine learning, whether it be clustering, vector quantization, classification models, etc.
  - Scikit-learn also includes a handful of image feature extraction functions as well.
- **scikit-image**

  - The algorithms included in scikit-image follow closer to the state-of-the-art in computer vision.
  - New algorithms right from academic papers can be found in scikit-image.

In OpenCV the origin is at the top left corner of the screen, x axis is towards right and y axis is towards down. It increases as we move to the right and down.

OpenCV relies on NumPy arrays.

OpenCV represents RGB images as multi-dimensional NumPy arrays but in reverse order this means that images are actually represented in BGR order rather than RGB.

Even though we specify pixels in terms of (x, y)-coordinates, when it comes to writing code, we access the individual pixel values as image[y, x] as an image is defined as a matrix and we define a matrix in terms of number of rows and number of columns. So, to access an individual pixel located at (x, y), we first supply y, the row number, followed by x, the column number.

As image is a matrix/array of pixels so we can use NumPy’s built-in array slicing functionality to crop an image.

- eg. croppedImg = img[0:50, 100:300] # This mean that the image take the pixels from 0 till 50 in y axis and 100 till 300 in x axis.

- In slicing the height comes first.

Given that OpenCV interprets an image as a NumPy array, there is no reason why we can’t manually define the image ourselves.

- canvas = np.zeros((300, 300, 3), dtype = "uint8") # It is a Numpy array aka image of width 300, height 300 and channel 3 with all pixels having an initial value of 0 (complete black image).

OpenCV provides convenient, easy-to-use methods to draw shapes on an image.

Drawing on an image doesn’t allow us to visually understand the contents of an image using OpenCV, these operations allow us to draw Regions of Interest (ROIs) surrounding objects in an image.

- These drawing operations are therefore applied after the more complex computer vision operations used for image understanding.
- While OpenCV’s drawing functions may not have directly helped us locate, detect, or recognize an object in an image, they did allow us to visualize the results, which is still part of our image processing/computer vision pipeline.

Basic Image Processing Techniques

- Basic image transformations
  - Rotation
  - Translation
  - Scaling
  - Flipping
  - Cropping
- Image arithmetic
  - When working with images, we need to keep in mind the limits of our color space and data type.
  - There is a difference between OpenCV and NumPy addition. NumPy will perform **modulo arithmetic** and **wrap around**. OpenCV, on the other hand, will perform **clipping** and ensure pixel values never fall outside the range [0, 255]
- Bitwise operations
  - Bitwise operations operate in a binary manner and are represented as grayscale images.
  - A given pixel is turned “off” if it has a value of zero, and it is turned “on” if the pixel has a value greater than zero.
- Masking
  - For this we take the mask (array of all 1's) and do bitwise AND with the image.
  - The key point of masks is that they allow us to focus our computation only on regions of the image that interests us (ROI).
  - Using a mask allows us to focus only on the portions of the image that interests us.
- Splitting and Merging an image into its respective channels

The role of color spaces in image processing and computer vision is important, yet complicated at the same time.

- Some color spaces are:
  - RBG
  - HSV
  - L\*a\*b\*
