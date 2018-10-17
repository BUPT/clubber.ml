---
title: demo驱动学习：Image_Caption
comments: true
mathjax: true
categories:
  - VQA
tags:
  - imageCaption
  
---

## Introduction to demo
Source Code:[image_captioning_with_attention](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/eager/python/examples/generative_examples/image_captioning_with_attention.ipynb)

### Related Papers
[Show, Attend and Tell: Neural Image Caption Generation with Visual Attention.](https://arxiv.org/pdf/1502.03044.pdf)

### Goal of this end2end model
1. Generate a caption, such as "a surfer riding on a wave", according to an image.
![](http://ww1.sinaimg.cn/mw690/ca26ff18ly1fun2xxvjt8j20hs0buamq.jpg)
2. Use an attention based model that enables us to see which parts of the image the model focuses on as it generates a caption.
![](http://ww1.sinaimg.cn/mw690/ca26ff18ly1fun2yatwwhj20zz0ehk1c.jpg)

### Dateset
**MS-COCO**:This dataset contains >82,000 images, each of which has been annotated with at least 5 different captions.

## Frame work of demo:
1. Download and prepare the MS-COCO dataset
2. Limit the size of the training set for faster training
3. Preprocess the images using InceptionV3: extract features from the last convolutional layer.
    1. Initialize InceptionV3 and load the pretrained Imagenet weights
    2. Caching the features extracted from InceptionV3

4. Preprocess and tokenize the captions
    1. First, tokenize the captions will give us a vocabulary of all the unique words in the data (e.g., "surfing", "football", etc).
    2. Next, limit the vocabulary size to the top 5,000 words to save memory. We'll replace all other words with the token "UNK" (for unknown).
    3. Finally, we create a word --> index mapping and vice-versa.
    4. We will then pad all sequences to the be same length as the longest one.

5.  create a tf.data dataset to use for training our model.


6.  Model
    1. extract the features from the lower convolutional layer of InceptionV3 giving us a vector of shape (8, 8, 2048).
    2. This vector is then passed through the CNN Encoder(which consists of a single Fully connected layer).
    3. The RNN(here GRU) attends over the image to predict the next word.

7. Training
    1. We extract the features stored in the respective .npy files and then pass those features through the encoder.
    2. The encoder output, hidden state(initialized to 0) and the decoder input (which is the start token) is passed to the decoder.
    3. The decoder returns the predictions and the decoder hidden state.
    4. The decoder hidden state is then passed back into the model and the predictions are used to calculate the loss.
    5. Use teacher forcing to decide the next input to the decoder.
    6. Teacher forcing is the technique where the target word is passed as the next input to the decoder.
    7. The final step is to calculate the gradients and apply it to the optimizer and backpropagate.

8. Caption
    1. The evaluate function is similar to the training loop, except we don't use teacher forcing here. The input to the decoder at each time step is its previous predictions along with the hidden state and the encoder output.
    2. Stop predicting when the model predicts the end token.
    3. And store the attention weights for every time step.




## Problems undesirable
### Version
- The code requires TensorFlow version **>=1.9**. 1.10.0 is better.
- `cudatoolkit`

### GPU lose connect


## Reference
1. https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/eager/python/examples/generative_examples/image_captioning_with_attention.ipynb