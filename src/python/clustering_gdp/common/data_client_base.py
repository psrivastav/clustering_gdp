#!/usr/bin/env python

from abc import ABCMeta, abstractmethod


class DataClientBase(object):
    """
        The abstract base class to represent the API for all data client objects
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, config):
        self.config = config
