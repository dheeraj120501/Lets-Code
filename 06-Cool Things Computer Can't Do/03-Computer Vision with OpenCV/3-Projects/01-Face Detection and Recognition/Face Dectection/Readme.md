## Different Face Detection Methods

- Face detection with Haar cascades
  - Extremely fast but prone to false-positives and in general less accurate than deep learning-based face detectors
- Face detection with OpenCV’s “hidden” pre-trained deep learning face detector
  - This model is a good balance of both speed and accuracy.
  - This method uses deep learning, in particular a Single Shot Detector (SSD) with ResNet as base network architecture.
- Face detection with dlib (HOG and CNN)
  - HOG is more accurate than Haar cascades but computationally more expensive.
  - Dlib’s CNN face detector is the most accurate of the bunch but cannot run in real-time without a GPU.
- Multi-task Cascaded Convolutional Networks (MTCNNs)
  - Very accurate deep learning-based face detector.
  - Easily compatible with both Keras and TensorFlow.
