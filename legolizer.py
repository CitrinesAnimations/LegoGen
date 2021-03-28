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
                "h" : -3
            },
            "2" : {
                "s" : 1,
                "h" : -3
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

def fabo(yep, base):
    if base == True:
        base = yep
    return base

def pobo(yep, base):
    if yep == True:
        base = False
    return base
    

voxelc = {}

voxels = {}

#Get voxel data from voxels.txt and use it
with open('voxels.txt') as json_file:
    data = json.load(json_file)
    voxels = data
    voxelc = data

def checkSide(vx, vy, vz, wx, wy, wz, s, da, sett):
    for bi in da:
        if wy == (vy + s[bi]["h"]):
            if s[bi]["s"] != 0:
                if (wx == (vx + s[bi]["s"])) and (wz == vz):
                    da[bi]["px"] = sett
                if (wx == (vx - s[bi]["s"])) and (wz == vz):
                    da[bi]["nx"] = sett
                if (wz == (vz + s[bi]["s"])) and (wx == vx):
                    da[bi]["pz"] = sett
                if (wz == (vz - s[bi]["s"])) and (wx == vx):
                    da[bi]["nz"] = sett
    return da


def makeSlope(slopeType):
    #Go through each brick to make slopes
    for v in voxels:
        #Make sure brick is a 1x1 not a slope
        if voxels[v]["part"] == "3005":
            #1Brick position
            vcords = voxels[v]["position"]
            
            bg = {
                "px" : False,
                "nx" : False,
                "pz" : False,
                "nz" : False
            }

            bgs = {
                "px" : True,
                "nx" : True,
                "pz" : True,
                "nz" : True
            }

            checkbrick = {}

            checkempty = {}


            ofset = slopeList[slopeType]

            for bi in ofset["brick"]:
                checkbrick[bi] = bg
            for ni in ofset["empty"]:
                checkempty[ni] = bgs

            for w in voxels:
                wcords = voxels[w]["position"]
                if voxels[w]["part"] != "air":
                    posi = checkSide(vcords["x"], vcords["y"], vcords["z"], wcords["x"], wcords["y"], wcords["z"], slopeList[slopeType]["brick"], checkbrick, True)
                    checkbrick = posi
                posis = checkSide(vcords["x"], vcords["y"], vcords["z"], wcords["x"], wcords["y"], wcords["z"], slopeList[slopeType]["empty"], checkempty, False)
                checkempty = posis

            
            px = True

            nx = True

            pz = True

            nz = True
            
            for cg in checkbrick:

                if checkbrick[cg]["px"] == False:
                    px = False
                if checkbrick[cg]["nx"] == False:
                    nx = False
                if checkbrick[cg]["pz"] == False:
                    pz = False
                if checkbrick[cg]["nz"] == False:
                    nz = False


            for cgi in checkempty:

                if checkempty[cgi]["px"] == False:
                    px = False
                if checkempty[cgi]["nx"] == False:
                    nx = False
                if checkempty[cgi]["pz"] == False:
                    pz = False
                if checkempty[cgi]["nz"] == False:
                    nz = False
            
            ava = []

            chos = ""

            if px == True:
                ava.append("px")
            if nx == True:
                ava.append("nx")
            if pz == True:
                ava.append("pz")
            if nz == True:
                ava.append("nz")


            if len(ava) != 0:
                chos = random.choice(ava)
                if chos == "px":
                    countt = str(random.randrange(5000, 10000))
                    
                    iposition = {}

                    iposition["x"] = vcords["x"] + 1

                    iposition["y"] = vcords["y"]

                    iposition["z"] = vcords["z"]
                    
                    idata = {}

                    idata["part"] = "air"
                    idata["position"] = iposition

                    voxels[countt] = idata


                    voxels[v]["part"] = "3040"
                    voxels[v]["rotation"] = "0 0 -1 0 1 0 1 0 0"
                if chos == "nx":
                    voxels[v]["part"] = "3040"
                    voxels[v]["rotation"] = "0 0 1 0 1 0 -1 0 0"
                if chos == "nz":
                    voxels[v]["part"] = "3040"
                    voxels[v]["rotation"] = "1 0 0 0 1 0 0 0 1"
                if chos == "pz":
                    voxels[v]["part"] = "3040"
                    voxels[v]["rotation"] = "-1 0 0 0 1 0 0 0 -1"

        
            


            
            
            



makeSlope("3040")

#Basic function to create a 1x1 for every voxel.
for v in voxels:
    rot = "0.0 0.0 -1.0 0.0 1.0 0.0 1.0 0.0 0.0"
    if voxels[v].get("rotation") is not None:
        rot = voxels[v]["rotation"]
    
    textOutput += placePart(voxels[v]["part"], 4, voxels[v]["position"]["x"], voxels[v]["position"]["y"], voxels[v]["position"]["z"], rot)
    
    

print("done")
ldrOutput.write(textOutput)