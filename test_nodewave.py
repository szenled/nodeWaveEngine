# test_nodewave.py
"""
Tests for nodeWave module.
"""

import unittest
from nodewave import nodeWave

class TestnodeWave(unittest.TestCase):
    """Test cases for nodeWave class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = nodeWave()
        self.assertIsInstance(instance, nodeWave)
        
    def test_run_method(self):
        """Test the run method."""
        instance = nodeWave()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
