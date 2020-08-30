# MedicalL2X
Using L2X (Learning to Explain) algorithm to train a model on clinical heart failure data set.

------IMPLEMENTATION OF L2X FOR MEDICAL HEART FAILURE DATASET-------

# Ensure heart_dataset.csv saved in project 'Medical' folder
# install necessary libraries by running in console:
      'pip install tensorflow, pandas, numpy, keras, nltk'
# for python 3.0 or above:
      'pip3 install tensorflow, pandas, numpy, keras, nltk'


------CONTENTS-------

# main.py contains code for
#    training and validation dataset generation
#    feature rank calculation
#    median ranks of selected features
#    Gumbel-Softmax variables and algorithm
#    output data shape
#    Variational approximation
#    Calculation of Q from X_s
#    Batch Normalization
#    Training of model based on L2X
#    Parsing
#    Epoch-wise results

# make_data.py contains code for
#    importing dataset/dataframe generation
#    response variable and input data definition


------HOW TO RUN-------

# To train L2X on the data of heart failure records and generate median ranks of selected features by L2X.
# Omit '--train' when using a trained model
# Run in terminal:

      python main.py --train --datatype 'heart'
