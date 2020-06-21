# Skin Cancer Image Classification application (Dermiscan)
According to the World Health Organization (WHO), The incidence of both non-melanoma and melanoma skin cancers has been increasing over the past decades. Currently, between 2 and 3 million non-melanoma skin cancers and 132,000 melanoma skin cancers occur globally each year. One in every three cancers diagnosed is a skin cancer and, according to Skin Cancer Foundation Statistics, one in every five Americans will develop skin cancer in their lifetime.

## Overview

This is an application that can make it easier for doctors and the general public to be able to predict skin diseases by taking pictures of the skin with a smartphone camera.

![Landing and Mobile App](web-mobile.PNG)

You can also predict via the website 
![Landing and Predict](web-predict.PNG)

### Dataset & Model

We provide a dataset bundled in this App: Final Project Model based on
Training data from Skin Cancer dataset : ISIC Dataset

```
https://www.isic-archive.com/#!/topWithHeader/onlyHeaderTop/gallery
```

For details of the dataset used, visit [this link](https://www.isic-archive.com).

Downloading, extracting, and placing the model in the assets folder is managed
automatically.

## Running Skin Cancer API Server

Dermiscan application link is http://dermiscan.co.id and mobile app link: https://github.com/simplephi/dermascan_application

Install the environtment

```
conda env create -f environment.yml
```

Get into the environtment
```
conda activate gpu-fp
```

run the app (make sure you are at the app root directory)
```
python server.py
```

### Installing (if you don't have python yet)

1. Install Python
```
[Python](https://www.python.org/downloads/)
```
2. Install Tensorflow
```
[Tensorflow](https://www.tensorflow.org/install)
```

3. Install Jupyter Notebook
```
[Jupyter](https://jupyter.org/install)
```

## Running the tests

How to run the automated tests for this system

1. Clone this repo
```
git clone https://github.com/SangsakaWira/SKIN-Cancer-FP-Bangkit.git
```
2. Enter to this folder repo
```
cd SKIN-Cancer-FP-Bangkit/
```

3. Running code on Jupyter Notebook
```
jupyter notebook
```

### Results

Based on the results from the test model, we get the value of accuracy.

Accuracy
```
 0.8123
```

### Techniques

We use CNN architecture and image augmentation to train models with an accuracy rate of up to 82%

## Requirements

*   Run it with [GoogleColab](https://colab.research.google.com/)

*   Or use Local machine with VGA Card embedded for best performance



## Authors

* **Indra Fransiskus Alam** - *cleverdarkness@gmail.com* - [Github](https://github.com/simplephi)
* **Sangsaka Wira** - *sangsakawira@gmail.com* - [Github](https://github.com/SangsakaWira)


## Acknowledgments

* Coursera Courses ([TensorFlow Specializations](https://www.coursera.org/specializations/tensorflow-in-practice))
* Machine Learning Crash Courses ([MLCC](https://developers.google.com/machine-learning/crash-course/))
* TensorFlow Lite ([TFlite](https://www.tensorflow.org/lite))
