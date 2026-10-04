#!/usr/bin/env python3
"""creating base parent class"""

class BaseGeometry:
    """foundational concept for geometric shapes. 
    It defines behavior that other shape classes will build upon"""
    def area(self):
        raise Exception("not implemented in this class.")
