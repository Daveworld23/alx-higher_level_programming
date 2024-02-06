#!/usr/bin/python3
"""Defines a class."""
class Student:
    """Represents a class called Student."""
    def _init__(self, first_name,last_name, age):
        """
        Initializes a new Student.
        Args:
            first_name (str): first name of student
            last_name (str): last nane of student
            age (int): age of student.
            """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """
        Returns the dictionary representation of the student.
        """
        return self.__dict__
