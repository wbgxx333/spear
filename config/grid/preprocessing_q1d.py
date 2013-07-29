#!/usr/bin/env python

# setup of the grid parameters

# default queue used for training
training_queue = { 'queue':'q1d', 'memfree':'8G'}
#training_queue = { 'queue':'q1d', 'memfree':'1G'}
# number of images that one job should preprocess
number_of_images_per_job = 200
preprocessing_queue = {'queue':'q1d', 'memfree':'1G'}

# number of features that one job should extract
number_of_features_per_job = 200
extraction_queue = {'queue':'q1d', 'memfree':'1G'}

# number of features that one job should project
number_of_projections_per_job = 50
projection_queue = {'queue':'q1d', 'memfree':'1G'}

# number of models that should be enroled by one enrol job
number_of_models_per_enrol_job = 50
enrol_queue = { 'queue':'q1d', 'memfree':'1G' }

# number of models that one score computation should use
number_of_models_per_score_job = 1
score_queue = { 'queue':'q1d', 'memfree':'1G' }