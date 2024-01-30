#!/usr/bin/python3
""" Defines a Locked Class. """
class LockedClass:
""" Prevents the user from instantiating new LockedClass attributes
for anything but attributes called 'first_bame.' """
    def __init__(self, first_name):
        self.first_name = first_name
