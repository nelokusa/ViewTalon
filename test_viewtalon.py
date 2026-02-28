# test_viewtalon.py
"""
Tests for ViewTalon module.
"""

import unittest
from viewtalon import ViewTalon

class TestViewTalon(unittest.TestCase):
    """Test cases for ViewTalon class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ViewTalon()
        self.assertIsInstance(instance, ViewTalon)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ViewTalon()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
