# MEDICAL L2X MODEL TRAINING
Training L2X model on clinical heart failure data set.

- Ensure heart_dataset.csv saved in project 'Medical' folder
- install necessary libraries by running in console:
      'pip install tensorflow, pandas, numpy, keras, nltk'
- for python 3.0 or above:
      'pip3 install tensorflow, pandas, numpy, keras, nltk'


# CONTENTS

--- main.py contains code for
1. training and validation dataset generation
2. feature rank calculation
3. median ranks of selected features
4. Gumbel-Softmax variables and algorithm
5. Variational approximation
6. Calculation of Q from X_s
7. Batch Normalization
8. Training of model based on L2X
9. Parsing
10.Epoch-wise results

--- make_data.py contains code for
1. importing dataset/dataframe generation
2. response variable and input data definition


# HOW TO RUN

To train L2X on the data of heart failure records and generate median ranks of selected features by L2X.
Omit '--train' when using a trained model

----Run in terminal----

      python main.py --train --datatype 'heart'
