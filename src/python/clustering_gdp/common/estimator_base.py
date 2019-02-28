#!/usr/bin/env python

from abc import ABCMeta, abstractmethod


class EstimatorBase(object):
    """
        The abstract base class to represent the API for all estimator objects
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def fit(self):
        """

        This is the method that every child class should implement. This would encapsulate all and any logic
        to train and fit data using the particular Time Series modelling approach being used. Ideally this should
        return a model object obtained after training which can then be used to perform actual prediction.

        """
        pass
