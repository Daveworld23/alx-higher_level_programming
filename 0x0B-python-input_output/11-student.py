#!/usr/bin/python3
"""Defines a class Student."""
class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student.
        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """
        Gets dictionary representation of the student."""
        if attrs is None:
            return self.__dict__
        else:
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
    def reload_from_json(self, json):
        """Replaces all attrivutes of student."""
        for b, c in json.item():
            setattr(self, b, c)
