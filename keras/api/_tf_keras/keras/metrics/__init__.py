"""DO NOT EDIT.

This file was autogenerated. Do not edit it by hand,
since your modifications would be overwritten.
"""

from keras.src.losses.losses import binary_crossentropy
from keras.src.losses.losses import binary_focal_crossentropy
from keras.src.losses.losses import categorical_crossentropy
from keras.src.losses.losses import categorical_focal_crossentropy
from keras.src.losses.losses import categorical_hinge
from keras.src.losses.losses import hinge
from keras.src.losses.losses import huber
from keras.src.losses.losses import kl_divergence as KLD
from keras.src.losses.losses import kl_divergence as kld
from keras.src.losses.losses import kl_divergence as kullback_leibler_divergence
from keras.src.losses.losses import log_cosh as logcosh
from keras.src.losses.losses import mean_absolute_error as MAE
from keras.src.losses.losses import mean_absolute_error as mae
from keras.src.losses.losses import mean_absolute_percentage_error as MAPE
from keras.src.losses.losses import mean_absolute_percentage_error as mape
from keras.src.losses.losses import mean_squared_error as MSE
from keras.src.losses.losses import mean_squared_error as mse
from keras.src.losses.losses import mean_squared_logarithmic_error as MSLE
from keras.src.losses.losses import mean_squared_logarithmic_error as msle
from keras.src.losses.losses import poisson
from keras.src.losses.losses import sparse_categorical_crossentropy
from keras.src.losses.losses import squared_hinge
from keras.src.metrics import deserialize
from keras.src.metrics import get
from keras.src.metrics import serialize
from keras.src.metrics.accuracy_metrics import Accuracy
from keras.src.metrics.accuracy_metrics import BinaryAccuracy
from keras.src.metrics.accuracy_metrics import CategoricalAccuracy
from keras.src.metrics.accuracy_metrics import SparseCategoricalAccuracy
from keras.src.metrics.accuracy_metrics import SparseTopKCategoricalAccuracy
from keras.src.metrics.accuracy_metrics import TopKCategoricalAccuracy
from keras.src.metrics.accuracy_metrics import binary_accuracy
from keras.src.metrics.accuracy_metrics import categorical_accuracy
from keras.src.metrics.accuracy_metrics import sparse_categorical_accuracy
from keras.src.metrics.accuracy_metrics import sparse_top_k_categorical_accuracy
from keras.src.metrics.accuracy_metrics import top_k_categorical_accuracy
from keras.src.metrics.confusion_metrics import AUC
from keras.src.metrics.confusion_metrics import FalseNegatives
from keras.src.metrics.confusion_metrics import FalsePositives
from keras.src.metrics.confusion_metrics import Precision
from keras.src.metrics.confusion_metrics import PrecisionAtRecall
from keras.src.metrics.confusion_metrics import Recall
from keras.src.metrics.confusion_metrics import RecallAtPrecision
from keras.src.metrics.confusion_metrics import SensitivityAtSpecificity
from keras.src.metrics.confusion_metrics import SpecificityAtSensitivity
from keras.src.metrics.confusion_metrics import TrueNegatives
from keras.src.metrics.confusion_metrics import TruePositives
from keras.src.metrics.correlation_metrics import ConcordanceCorrelation
from keras.src.metrics.correlation_metrics import PearsonCorrelation
from keras.src.metrics.correlation_metrics import concordance_correlation
from keras.src.metrics.correlation_metrics import pearson_correlation
from keras.src.metrics.f_score_metrics import F1Score
from keras.src.metrics.f_score_metrics import FBetaScore
from keras.src.metrics.hinge_metrics import CategoricalHinge
from keras.src.metrics.hinge_metrics import Hinge
from keras.src.metrics.hinge_metrics import SquaredHinge
from keras.src.metrics.iou_metrics import BinaryIoU
from keras.src.metrics.iou_metrics import IoU
from keras.src.metrics.iou_metrics import MeanIoU
from keras.src.metrics.iou_metrics import OneHotIoU
from keras.src.metrics.iou_metrics import OneHotMeanIoU
from keras.src.metrics.metric import Metric
from keras.src.metrics.probabilistic_metrics import BinaryCrossentropy
from keras.src.metrics.probabilistic_metrics import CategoricalCrossentropy
from keras.src.metrics.probabilistic_metrics import KLDivergence
from keras.src.metrics.probabilistic_metrics import Poisson
from keras.src.metrics.probabilistic_metrics import (
    SparseCategoricalCrossentropy,
)
from keras.src.metrics.reduction_metrics import Mean
from keras.src.metrics.reduction_metrics import MeanMetricWrapper
from keras.src.metrics.reduction_metrics import Sum
from keras.src.metrics.regression_metrics import CosineSimilarity
from keras.src.metrics.regression_metrics import LogCoshError
from keras.src.metrics.regression_metrics import MeanAbsoluteError
from keras.src.metrics.regression_metrics import MeanAbsolutePercentageError
from keras.src.metrics.regression_metrics import MeanSquaredError
from keras.src.metrics.regression_metrics import MeanSquaredLogarithmicError
from keras.src.metrics.regression_metrics import R2Score
from keras.src.metrics.regression_metrics import RootMeanSquaredError