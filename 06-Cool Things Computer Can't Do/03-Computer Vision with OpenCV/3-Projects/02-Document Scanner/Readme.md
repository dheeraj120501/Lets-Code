- Document scanning can be broken down into three distinct and simple steps.

  - The first step is to apply edge detection.

  - The second step is to find the contours in the image that represent the document we want to scan.

  - The final step is to apply a perspective transform to obtain a top-down, 90-degree view of the image, just as if we scanned the document.

  - Optionally, you can also apply thresholding to obtain a nice, clean black and white feel to the piece of paper.
