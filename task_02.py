#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""More Fun with Classes."""


import time


class Snapshot(object):
    """Object that stores Snapshot data"""

    def __init__(self):
        """Constructor for Snapshot class.

        Args:
            None

        Attributes:
            created (time) = Unix time
        """
        self.created = time.time()
