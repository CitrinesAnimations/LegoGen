import json
import math
import os
import random

#Open the file which we are going to write to.
ldrOutput = open("Output.ldr", "w+")

#Store text in this string to be written on the file.
textOutput = ""

#Info about parts, part id: dimensions: x,y,z. offset: x,y,z. studs:.
partList = {
    "3004" : {
        "size" : {
            "x" : 2,
            "y" : 3,
            "z" : 1
        },
        "offset" : {
            "x" : 0.5,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0,
            "2" : 1
        }
    },
    "3010" : {
        "size" : {
            "x" : 4,
            "y" : 3,
            "h" : 1
        },
        "offset" : {
            "x" : 1.5,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0
        }
    },
    "3005" : {
        "size" : {
            "x" : 1,
            "y" : 3,
            "z" : 1
        },
        "offset" : {
            "x" : 0.0,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0
        }
    },
    "3622" : {
        "size" : {
            "x" : 3,
            "y" : 3,
            "z" : 1
        },
        "offset" : {
            "x" : 1.0,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0
        }
    },
    "3069" : {
        "size" : {
            "x" : 2,
            "y" : 1,
            "z" : 1
        },
        "offset" : {
            "x" : 0.5,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0,
            "2" : 1
        }
    },
    "2431" : {
        "size" : {
            "x" : 4,
            "y" : 1,
            "z" : 1
        },
        "offset" : {
            "x" : 1.5,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0
        }
    },
    "3070" : {
        "size" : {
            "x" : 1,
            "y" : 1,
            "z" : 1
        },
        "offset" : {
            "x" : 0.0,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0
        }
    },
    "63864" : {
        "size" : {
            "x" : 3,
            "y" : 1,
            "z" : 1
        },
        "offset" : {
            "x" : 1.0,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0
        }
    },
    "3001" : {
        "size" : {
            "x" : 4,
            "y" : 3,
            "z" : 2
        },
        "offset" : {
            "x" : 1.5,
            "y" : 0.0,
            "z" : 0.5
        },
        "studs" : {
            "1" : 0,
            "2" : 1
        }
    },
    "3024" : {
        "size" : {
            "x" : 1,
            "y" : 1,
            "z" : 1
        },
        "offset" : {
            "x" : 0.0,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0,
            "2" : 1
        }
    },
    "2454" : {
        "size" : {
            "x" : 2,
            "y" : 15,
            "z" : 1
        },
        "offset" : {
            "x" : 0.5,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0,
            "2" : 1
        }
    },
    "3754" : {
        "size" : {
            "x" : 6,
            "y" : 15,
            "z" : 1
        },
        "offset" : {
            "x" : 2.5,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0,
            "2" : 1
        }
    },
    "3245" : {
        "size" : {
            "x" : 2,
            "y" : 6,
            "z" : 1
        },
        "offset" : {
            "x" : 0.5,
            "y" : 0.0,
            "z" : 0.0
        },
        "studs" : {
            "1" : 0,
            "2" : 1
        }
    },
    "4032" : {
        "size" : {
            "x" : 2,
            "y" : 1,
            "z" : 2
        },
        "offset" : {
            "x" : 1.0,
            "y" : 0.0,
            "z" : 1.0
        },
        "studs" : {
            "1" : 0,
            "2" : 1
        }
    },
    "14769" : {
        "size" : {
            "x" : 2,
            "y" : 1,
            "z" : 2
        },
        "offset" : {
            "x" : 1.0,
            "y" : 0.0,
            "z" : 1.0
        },
        "studs" : {
            "1" : 0,
            "2" : 1
        }
    },
    "98138" : {
        "size" : {
            "x" : 1,
            "y" : 1,
            "z" : 1
        },
        "offset" : {
            "x" : 0.5,
            "y" : 0.0,
            "z" : 0.5
        },
        "studs" : {
            "1" : 0,
            "2" : 1
        }
    },
    "4073" : {
        "size" : {
            "x" : 1,
            "y" : 1,
            "z" : 1
        },
        "offset" : {
            "x" : 0.5,
            "y" : 0.0,
            "z" : 0.5
        },
        "studs" : {
            "1" : 0,
            "2" : 1
        }
    }
}

#Basic function to place a part and output the line.
def placePart(p, c, x, y, z, m):
    #Part id, colour id, x, y, z, matrix ^^
    #1 + colour id + x + y + z + matrix + part id
    outputText = "1 " + str(c) + " " + str(x * 20) + " " + str(-y * 8) + " " + str(z * 20) + " " + m + " " + p + ".dat" + "\n"
    return outputText

def inbo(inv):
    if inv == True:
        inv = False
    else:
        inv = True
    return inv

voxels = {
    "1" : {
        "part" : "3005",
        "position" : {
            "x" : 0,
            "y" : 0,
            "z" : 0
        }
        
    },
    "2" : {
        "part" : "3005",
        "position" : {
            "x" : 1,
            "y" : 0,
            "z" : 0
        }
    },
    "3" : {
        "part" : "3005",
        "position" : {
            "x" : 0,
            "y" : 3,
            "z" : 0
        }
    }
}

def makeSlope():
    for v in voxels:
        vcords = voxels[v]["position"]
        
        down = False

        side = False
        
        for w in voxels:
            wcords = voxels[w]["position"]

            if wcords["x"] == vcords["x"] and wcords["y"] == vcords["y"] - 3 and wcords["z"] == vcords["z"]:
                down = inbo(down)
            elif wcords["x"] == vcords["x"] + 1 and wcords["y"] == vcords["y"] - 3 and wcords["z"] == vcords["z"]:
                side = inbo(side)
            
            if down and side == True:
                voxels[v]["part"] = "3040"

makeSlope()

#Basic function to create a 1x1 for every voxel.
for v in voxels:
    textOutput += placePart(voxels[v]["part"], 4, voxels[v]["position"]["x"], voxels[v]["position"]["y"], voxels[v]["position"]["z"], "0.0 0.0 -1.0 0.0 1.0 0.0 1.0 0.0 0.0")

ldrOutput.write(textOutput)