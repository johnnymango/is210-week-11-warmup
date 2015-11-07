#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Classes and Instances"""


import produce


TOMATO = produce.Produce()

EGGPLANT = produce.Produce.arrival = 1311210802

TOMATO_ARRIVAL = TOMATO.arrival

EGGPLANT = produce.Produce()
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
