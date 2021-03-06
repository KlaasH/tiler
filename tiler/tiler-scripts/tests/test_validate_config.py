import unittest
import sys, os
import shutil

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Insanity for getting parent folder in path
from validate_config import *

class TestValidateConfig(unittest.TestCase):

    def test_create_mbtiles(self):
        CONFIG_NAME = "example"
        config_path = "/tiler-data/test-data/configs/" + CONFIG_NAME + ".tiler.json"
        is_valid = validate_config(config_path)
        self.assertTrue(is_valid)

    def test_invalid_config(self):
        config_path = "/tiler-data/test-data/configs/invalid.tiler.json"
        self.assertTrue(os.path.isfile(config_path))

        with self.assertRaises(TypeError):
            validate_config(config_path)

if __name__ == '__main__':
    unittest.main()