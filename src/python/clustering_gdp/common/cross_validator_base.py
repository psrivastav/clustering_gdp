#!/usr/bin/env python

from abc import ABCMeta, abstractmethod


class CrossValidatorBase(object):
    """
        The abstract base class to represent the API for all cross validator objects
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def validate(self):
        """

        This is the method that every child class should implement for performing any or all cross validation logic.

        """
        pass
