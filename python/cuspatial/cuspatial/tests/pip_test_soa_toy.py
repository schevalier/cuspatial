"""
GPU-based pip demo using toy datasets(tests among three points and two polygons)  

Note: make sure cudf_dev conda environment is activated
"""

import numpy as np
from cudf.dataframe import columnops
import cuspatial.bindings.spatial as gis

pnt_x=columnops.as_column(np.array([0,-8,6],dtype=np.float64))
pnt_y=columnops.as_column(np.array([0,-8,6],dtype=np.float64))

ply_fpos=columnops.as_column(np.array([1, 2],dtype=np.int32))
ply_rpos=columnops.as_column(np.array([5, 10],dtype=np.int32))
ply_x=columnops.as_column(np.array([-10,   5, 5, -10, -10,  0, 10, 10,  0, 0],dtype=np.float64))
ply_y=columnops.as_column(np.array([-10, -10, 5,   5, -10,  0,  0, 10, 10, 0],dtype=np.float64))

bm=gis.cpp_pip_bm(pnt_x,pnt_y,ply_fpos,ply_rpos,ply_x,ply_y)
bma=bm.data.to_array()
#look into binary represenation in Python of the resulting bitmap
print(np.binary_repr(bma[0], width=ply_fpos.data.size))

