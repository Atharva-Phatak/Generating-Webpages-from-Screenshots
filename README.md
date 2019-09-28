# Generating-Webpages-from-Screenshots


# Introduction

The 21st century has seen the rise of Machine learning , Deep Learning ,etc to automate a myriad of tasks. Deep Learning systems have given state of art performance on Computer vision and other related tasks. In 2017 an interesting paper called [Pix2Code](https://arxiv.org/pdf/1705.07962.pdf) was published by Tony Beltramelli which tackled the problem of converting the UI design mockups to code. The concept used in this paper is very simple yet elegant , it treated the problem of converting the screenshots to code as a image captioning task( Image Captioning refers to the process of generating textual description from an image) and deep learning systems are being used to perform image captioning.

This project focuses on just converting the webpage screenshots to corresponding HTML/Bootstrap code and everything is implemented using PyTorch.

# How does it work ?

## Dataset

The author of the paper "Pix2Code" paper was kind enough to make the dataset open for use. The dataset consists of the screenshot and its corresponding DSL code(Domain Specific code).

Here's how it looks..

**Screenshots and Codes**

![ss](https://github.com/Atharva-Phatak/Generating-Webpages-from-Screenshots/blob/master/Images/ss.JPG)





So we are only interested in the  GUI Layout , the various components(button , etc) and their relationship and hence actual value of text label can be ignored. The DSL consists of 18 vocabulary token. The pix2code datasaet consists of 3500 images and DSL code pairs.

## The Model

The image captioning model consists of an encoder and decodee type of architecture. We are dealing with images so the first candidate that comes in mind is CNN which is used to extract features from images and similarly for the language based modelling RNN's come to mind. The architecutre consists of a ResNet-152 as an encoder. This a deep resiudual network which has shown increased accuracy at image classification based on extreme depth of the network. The decoder is a Long Short Term Memory(LSTM) which takes in the expected target for the screenshot and features extracted from the encoder. The source and target sequences along with features are used to train the LSTM's.

Here's how the architecture looks..

![model](https://github.com/Atharva-Phatak/Generating-Webpages-from-Screenshots/blob/master/Images/model.JPG)

Before passing the images to the encoder they are resiszed to 224 x 224 and the extracted features are passed to LSTM for decoding and prediciting the tokens.

## Evaluation 

To quantify the results , Bilingual Evaluation understudy Scores(BLEU) are used , which is common for image captioning models. The scores give the value between 0.0 to 1.0 indicating how similiar are the two sequences of tokens.

# Refernces

* Author's Implementation : https://github.com/tonybeltramelli/pix2code
* Pix2Code Paper : https://arxiv.org/pdf/1705.07962.pdf
* Image Captioning Tutorial(PyTorch) : https://github.com/yunjey/pytorch-tutorial/tree/master/tutorials/03-advanced/image_captioning
* Emil Wallners awesome blog : https://medium.com/@emilwallner/how-you-can-train-an-ai-to-convert-your-design-mockups-into-html-and-css-cc7afd82fed4
* Image Captioning(Analytic's Vidhya) : https://www.analyticsvidhya.com/blog/2018/04/solving-an-image-captioning-task-using-deep-learning/
* Show , Attend , Tell : https://arxiv.org/pdf/1502.03044.pdf

# Dependencies
* NLTK
* PyTorch
* Numpy
* Python 3.6




