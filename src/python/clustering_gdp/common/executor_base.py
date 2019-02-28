#!/usr/bin/env python

from abc import ABCMeta, abstractmethod


class ExecutorBase(object):
    """
        The abstract base class to represent the API for all executor objects
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def execute(self):
        pass
