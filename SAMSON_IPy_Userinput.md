 
# Input to SAMSON IPython Console  
 

#### How to use the ObjParser  in SAMSON to parse a 3D .obj file. 

### Install ECHIDNA 
using : $ pip install echidna_obj
     
To Parse an .obj file use SAMSON IPy (Nanotube example):
```python
# first import the application ADENITA and the python package ECHIDNA
# with the IPy Console in SAMSON
import SE_DDA2A078_1AB6_96BA_0D14_EE1717632D7A as adenita 
from echidna_obj.parse_tube_ import ObjTube
from echidna_obj.parse_wire_ import ObjWire

# Assign a model by choosing the file path
# Depending on model category (nanotube, wireframe)
# example shows "nanotube" category 
nanotube = ObjTube('C:/Users/.../filename.obj')

# assign parameters for transfer from ECHIDNA to ADENITA
directions = nanotube.get_direction() 
starts = nanotube.get_startvertices()
bpLengths = nanotube.calc_bpLength()
num_ds = len(bpLengths)

# create a new component with ADENITA and transfer the parsed data
part = adenita.createComponent()
for i in range(0, num_ds):
	bpLength = bpLengths[i]
	start = starts[i]
	direction = directions[i]
	adenita.addDoubleStrandToComponent(part, bpLength, start, direction)
	
# parse the model into SAMSON 
adenita.addComponentToActiveLayer(part)

```
After input the file is loaded into SAMSON.