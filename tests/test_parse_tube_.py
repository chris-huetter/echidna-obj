import unittest
import os
import math
import scipy.spatial
from parse_tube_ import Obj_tube


class Test_Obj_tube(unittest.TestCase):
    def test_get_file(self):
        # test if the input is an existing path
        self.file = os.path.dirname('/Users/christianerhuetter/Desktop/BIOE19/06_BSC_SS19/BSC_Thesis/Programming/echidna_obj/testfiles/nanotube.obj')
        assert os.path.exists(self.file), 'Did not find the file at the chosen path, ' + str(
             self.file) + ', please try again.'

    def test_material_properties(self):
        # test if the file contains material properties
        # as those are necessary for correct parsing
        self.file = ('./testfiles/nanotube.obj')
        with open(self.file, 'r') as f:
            self.file = f.readlines()
        lines = [line.rstrip('\n') for line in self.file]
        for line in lines:
            split = line.split()
            assert split[0:] != 'usemtl'

    def test_get_count(self):
        # test of count is not one object
        # as one mesh would refer to be a wireframe model or wrong export settings
        obj = Obj_tube('./testfiles/nanotube.obj')
        obj_count = obj.get_count()
        self.assertIsNot(obj_count, 1)

    def test_get_vertices(self):
        # test if the file contains vertices by detecting parameter 'v'
        self.file = ('./testfiles/nanotube.obj')
        with open(self.file, 'r') as f:
            self.file = f.readlines()
        lines = [line.rstrip('\n') for line in self.file]
        for line in lines:
            split = line.split()
            assert split[0:] != 'v', 'File does not contain vertices. Please check file.'

    def test_calc_edgelength(self):
        obj = Obj_tube('./testfiles/nanotube.obj')
        obj_edge = obj.calc_edgelength()[0]
        test_center_one = [-1.87648827, -30.27291727,   0]
        test_center_two = [-1.87648827, -30.27291727, 200.]
        test_edge = scipy.spatial.distance.euclidean(test_center_one, test_center_two)
        self.assertEqual(obj_edge, test_edge)

    def test_calc_bplength(self):
        # compare bplength division to manual setup
        obj = Obj_tube('./testfiles/nanotube.obj')
        obj_bp = obj.calc_bplength()[0]
        test_edge_length = 200.0
        test_bp = math.floor(test_edge_length / 0.34)
        self.assertEqual(obj_bp, test_bp)

    def test_get_direction(self):
        obj = Obj_tube('./testfiles/nanotube.obj')
        obj_dir_norm = obj.get_direction()[0]
        test_segm = (-1.87648827, -30.27291727, 200.0), (-1.87648827, -30.27291727, 0.0)
        test_x, test_y, test_z = (test_segm[1][0] - test_segm[0][0]), (test_segm[1][1] - test_segm[0][1]), (test_segm[1][2] - test_segm[0][2])
        test_vector = math.sqrt(test_x**2+test_y**2+test_z**2)
        test_x_norm = test_x / test_vector
        test_y_norm = test_y / test_vector
        test_z_norm = test_z / test_vector
        test_dir_norm = [test_x_norm, test_y_norm, test_z_norm]
        self.assertEqual(obj_dir_norm, test_dir_norm)


if __name__ == '__main_':
    unittest.main()
