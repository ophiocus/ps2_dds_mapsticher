# Lets get some basic references and imports and stuff
import os, sys
from collections import defaultdict
from os import listdir
from os.path import isfile, join
from PIL import Image


# lets start by reading in the available files and matching them to continents
# Set of continent to look into
continents =[
  "Amerish",
  "Indar",
  "Esamir",
  "Hossin",
  "VR",
  "quickload",
  "Tutorial"
]

# Level of detail 
# Will affect the logic of the assembly
detail =[
  "LOD0",
  "LOD1",
  "LOD2",
  "LOD3"
]

# Parameters handling
params_default={
  "continent":"VR",
  "detail":"LOD2"
}

# Process params
process_params = {
  "continent":[x for x in sys.argv if x in continents],
  "detail":[x for x in sys.argv if x in detail]
}
# Pad process params with defaults
params_runtime={
  "continent": process_params["continent"][0] if process_params["continent"] else params_default["continent"],
  "detail":process_params["detail"][0] if process_params["detail"] else params_default["detail"]
}

# START
# Read files in local folder param_runtime["continent"]
# Let's get a clean slate
os.system("CLS")
map_parts = defaultdict(dict)
file_name = [fn for fn in os.listdir(str("./" + params_runtime["continent"] +"_Tile"))
              if fn.endswith(str(params_runtime["detail"] + ".dds")) ]

# Process file list
#
print("how many files " + str(len(file_name)))
print(params_runtime)

# Get coordinates from file names
for fn in sorted(file_name):
  item = fn[:fn.find(".")].split("_")
  map_parts[ int(item[2]) ][ int(item[3]) ] =  "./" + params_runtime["continent"] + "_Tile/" + fn
map_parts_axis = sorted(map_parts[0].keys())

# Get relative size
map_side = Image.open( map_parts[0][0] ).size[0] * len(map_parts_axis)
map_canvas = Image.new( 'RGB' , (map_side,map_side) )


for x in map_parts_axis:
  for y in map_parts_axis:
    
    # Coordinates Step
    x_coord = int(( ((map_parts_axis.index(x) + 1) * ((map_side / len(map_parts_axis)) ) )) - (map_side / len(map_parts_axis)) )
    y_coord = int(( ((map_parts_axis.index(y) + 1) * ((map_side / len(map_parts_axis)) ) )) - (map_side / len(map_parts_axis)) )
    
    # Paint me like one of your french girls
    part_img_file = Image.open(map_parts[x][y])
    map_canvas.paste(part_img_file,(x_coord,y_coord))

map_canvas.save("./"+ params_runtime["continent"] + "_Tile/" + params_runtime["continent"] +"_"+params_runtime["detail"]+".png")
map_canvas.close()

# Report items here
print(map_parts_axis)
print(sys.argv[0])
print(len(sys.argv))
print(str(sys.argv))
print("Params: \nContinent:"+ params_runtime["continent"] + "\nDetail: " + params_runtime["detail"])
# Program end
print("done! yay")
