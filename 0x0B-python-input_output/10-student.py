#!/usr/bin/python3
"""Definesa class Student."""
class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student.
        Args:
            first_name (str): first name of Student
            last_name (str): last nane of student
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """Gets dictionary representation of student."""
        if attrs is None:
            return self.__dict__
        else:
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
