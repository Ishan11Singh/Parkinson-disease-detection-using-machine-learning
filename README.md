<p align="center">
  <img src="https://github.com/mmore21/parkinvision/blob/master/static/img/logo.png" width="300" />
</p>

<p align="center">
  Hand-drawn spiral prediction for Parkinson's disease.
</p>

<p align="center">
  <img src="https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/000/929/166/datas/original.png" />
  Home Page
</p>
<p align="center">
  <img src="https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/000/929/170/datas/original.png" />
  Negative prediction
</p>

</p>
<p align="center">
  <img src="https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/000/929/169/datas/original.png" />
  Positive prediction
</p>


<p align="center">
  <a href="https://devpost.com/software/parkinvision-79jpa8">Details</a>
</p>

## About

This project employs ML to analyze medical images for early Parkinson's Disease detection. Trained on historical data, ML models distinguish between healthy and PD-affected individuals, boosting diagnostic accuracy. Early detection enables timely intervention, enhancing patient care and outcomes in PD management.

## Technologies

* Python
* Tensorflow 2.0 / Keras
* scikit-learn
* OpenCV
* Flask
* Twilio API

## Machine Learning and Deep Learning Approach

Two different models were trained for this task (as a learning experience). Ultimately, the machine learning approach was chosen as the lack of data stunted the deep learning model's performance.

* The machine learning approach trained a Random Forest classifier using the scikit-learn and OpenCV libraries.
* The deep learning approach trained a standard Convolutional Neural Network using a Tensorflow 2.0 / Keras model with data augmentation.

## Acknowledgements

The data folder was downloaded from an article on [pyimagesearch](https://www.pyimagesearch.com/2019/04/29/detecting-parkinsons-disease-with-opencv-computer-vision-and-the-spiral-wave-test/) which provides the author's own approach to machine learning on this data set. Some of the computer vision techniques were derived from his post. Additionally, he mentioned the source of the data set, Adriano de Oliveira Andrade and Joao Paulo Folado from the NIATS of Federal University of Uberlândia. 
