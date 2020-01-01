import unittest
import os
import math
import scipy.spatial
from parse_wire_ import Obj_wire


class Test_Obj_wire(unittest.TestCase):
    def test_get_file(self):
        # test if the input is an existing path
        self.file = os.path.dirname("/Users/christianerhuetter/Desktop/BIOE19/06_BSC_SS19/BSC_Thesis/Programming/echidna_obj/testfiles/wireframe.obj")
        assert os.path.exists(self.file), "Did not find the file at the chosen path, " + str(
             self.file) + ", please try again."

    def test_get_vertices(self):
        # test if the file contains vertices by detecting parameter 'v'
        self.file = ("./testfiles/wireframe.obj")
        with open(self.file, 'r') as f:
            self.file = f.readlines()
        lines = [line.rstrip('\n') for line in self.file]
        for line in lines:
            split = line.split()
            assert split[0:] != 'v', 'File does not contain vertices. Please check file.'

    def test_get_faces(self):
        # test if the file contains faces by detecting parameter 'f'
        self.file = ("./testfiles/wireframe.obj")
        lines = [line.rstrip('\n') for line in self.file]
        for line in lines:
            split = line.split()
            assert split[0:] != 'f', 'File does not contain faces. Please check file.'

    def test_segments(self):
        # test if segments connection is valid
        # by comparing generated segment of testfile with manual creation
        obj = Obj_wire('./testfiles/wireframe.obj')
        obj_segment = obj.get_segments()[0]

        test_segment = (100.0, 100.0, 0.0), (100.0, 0.0, 0.0)
        self.assertEqual(obj_segment, test_segment)

    def test_calc_edgelength(self):
        # compare generated edge to manually calculated edge
        obj = Obj_wire('./testfiles/wireframe.obj')
        obj_length = obj.calc_edgelength()[0]

        test_vertex_one = (100.0, 100.0, 0.0)
        test_vertex_two = (100.0, 0.0, 0.0)
        test_length = scipy.spatial.distance.euclidean(test_vertex_one, test_vertex_two)
        self.assertEqual(obj_length, test_length)

    def test_calc_bplength(self):
        # compare bplength division to manual setup
        obj = Obj_wire('./testfiles/wireframe.obj')
        obj_bp = obj.calc_bplength()[0]

        test_edge_length = 100.0
        test_bp = math.floor(test_edge_length / 0.34)
        self.assertEqual(obj_bp, test_bp)

    def test_get_direction(self):
        # compare direction to manual set up
        obj = Obj_wire('./testfiles/wireframe.obj')
        obj_dir_norm = obj.get_direction()[0]
        test_segm = (100.0, 100.0, 0.0), (100.0, 0.0, 0.0)
        test_x, test_y, test_z = (test_segm[1][0] - test_segm[0][0]), (test_segm[1][1] - test_segm[0][1]), (test_segm[1][2] - test_segm[0][2])
        test_vector = math.sqrt(test_x**2+test_y**2+test_z**2)
        test_x_norm = test_x / test_vector
        test_y_norm = test_y / test_vector
        test_z_norm = test_z / test_vector
        test_dir_norm = [test_x_norm, test_y_norm, test_z_norm]
        self.assertEqual(obj_dir_norm, test_dir_norm)


if __name__ == '__main_':
    unittest.main()
