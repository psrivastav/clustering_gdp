#!/usr/bin/env python

from abc import ABCMeta, abstractmethod


class ModelBase(object):
    """
        The abstract base class to represent the API for all model objects
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def transform(self):
        """

        This is the method that every child of this class should implement. This would encapsulate all the logic
        to perform any and all prediction using the this model

        """
        pass
