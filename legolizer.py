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
    },
    "3040" : {
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
            "1" : 0
        }
    }
}

slopeList = {
    "3040" : {
        "brick" : {
            "1" : {
                "s" : 0,
                "h" : -1
            },
            "2" : {
                "s" : 1,
                "h" : -1
            }
        },
        "empty" : {
            "1" : {
                "s" : 1,
                "h" : 0
            }
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

def fabo(inv):
    if inv == True:
        inv = False
    else:
        inv = False
    return inv

voxels = {}

#Get voxel data from voxels.txt and use it
with open('voxels.txt') as json_file:
    data = json.load(json_file)
    voxels = data

def checkSide(vx, vz, wx, wz, s):
    sp = []

    if wx == (vx + s):
        sp.append(s)
    if wx == (vx - s):
        sp.append(-s)
    if wz == (vz + s):
        sp.append(s)
    if wz == (vz - s):
        sp.append(-s)
    
    return sp


def makeSlope(slopeType):
    #Go through each brick to make slopes
    for v in voxels:
        #Make sure brick is a 1x1 not a slope
        if voxels[v]["part"] == "3005":
            #1Brick position
            vcords = voxels[v]["position"]

            bg = True

            for b in slopeList[slopeType]["brick"]:
                slopeList[slopeType]["brick"][b]
                for w in voxels:
                    if voxels[w]["part"] != "air":
                        wcords = voxels[w]["position"]
                        
                        if wcords["y"] == vcords["y"] + slopeList[slopeType]["brick"][b]["h"]:
                            posi = checkSide(vcords["x"], vcords["z"], wcords["x"], wcords["z"], slopeList[slopeType]["brick"][b]["s"])
                            print (posi)


makeSlope("3040")

#Basic function to create a 1x1 for every voxel.
#for v in voxels:
#    textOutput += placePart(voxels[v]["part"], 4, voxels[v]["position"]["x"], voxels[v]["position"]["y"], voxels[v]["position"]["z"], "0.0 0.0 -1.0 0.0 1.0 0.0 1.0 0.0 0.0")

#drOutput.write(textOutput)