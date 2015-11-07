#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Classes Task 4"""

### I don't understand this assignment.

import car


class CustomCar(car.Car):
    tires = 0


    def __init__(self, tires):

        if tires == 0:
            tires = [tire, tire, tire, tire]
            

class CustomTire(car.Tire):

  car.Tire._CustomTire__maximum_miles = 500
