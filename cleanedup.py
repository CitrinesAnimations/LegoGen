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

tA = []

#Basic function to place a part and output the line.
def placePart(p, c, x, y, z, m):
    #Part id, colour id, x, y, z, matrix ^^
    #1 + colour id + x + y + z + matrix + part id
    outputText = "1 " + str(c) + " " + str(x) + " " + str(y) + " " + str(z) + " " + m + " " + p + ".dat" + "\n"
    return outputText

def checkPlace(p, a, t, r, x, y, z, c):
    #Part id, area, taken area, percentage, x, y, z ^^
    outputText = ""
    
    #(area * percentage) / part x * part y * part z
    for u in range(0, int((a * (r * 0.1)) / (partList[p]["size"]["x"] * partList[p]["size"]["y"] * partList[p]["size"]["z"]))):
        print(u)
        #Bool: if True then continue.
        cP = False
        #Limit amount of tries to fit part in
        lT = 100
        while cP == False:
            cP = False
            lT -= 1
            if lT > 0:
                rX = random.randint(0, x)
                rY = random.randint(0, y)
                rZ = random.randint(0, z)
                #Bool: position allowence
                pS = True
                #Part x + 1 (to remove the 1 later)
                for i in range(0, partList[p]["size"]["x"]):
                    for o in range(0, partList[p]["size"]["y"]):
                        for q in range(0, partList[p]["size"]["z"]):
                            if pS == True:
                                if (rX + i, rY + o, rZ + q) not in t:
                                    pS = True
                                else:
                                    pS = False
                            else: 
                                pS = False
                if pS == True:
                    cP = True
                    outputText += (placePart(p, c, (rX + partList[p]["offset"]["x"])* 20, (rY + partList[p]["offset"]["y"]) * 8, (rZ + partList[p]["offset"]["z"]) * 20, "1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0"))
                    #add taken area of part to taken areas
                    for i in range(0, partList[p]["size"]["x"]):
                        for o in range(0, partList[p]["size"]["y"]):
                            for q in range(0, partList[p]["size"]["z"]):
                                t.append(((rX + i), (rY + o), (rZ + q)))
            else: cP = True
    return t, outputText

def remainPlace(p, x, y, z, t, c):
    forFinal = ""
    for i in range(0, x):
        for e in range(0, z + 1):
            for q in range(0, y):
                pS = True
                for h in range(0, partList[p]["size"]["y"]):
                    if pS == True:
                        if (i, q + h, e) not in t:
                            pS = True
                        else:
                            pS = False
                    else: 
                        pS = False
                if pS == True:
                    if (i, q, e) not in t:
                        forFinal += (placePart(p, c, (i + partList[p]["offset"]["x"])* 20, q * 8, e * 20, "1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0"))
                        for s in range(0, partList[p]["size"]["y"]):   
                            t.append((i, q + s, e))
    return t, forFinal

thick = 32

wide = 32

hight = 0

total = 1024

out = checkPlace("4032", total, tA, 3, thick, hight, wide, 72)

tA += out[0]

textOutput += out[1]

out = checkPlace("14769", total, tA, 1, thick, hight, wide, 71)

tA += out[0]

textOutput += out[1]

out = checkPlace("4073", total, tA, 0.5, thick, hight, wide, 71)

tA += out[0]

textOutput += out[1]

out = checkPlace("98138", total, tA, 1.5, thick, hight, wide, 72)

tA += out[0]

textOutput += out[1]

textOutput += placePart("3811", 72, 16 * 20, 8, 16 * 20, "1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0")

#out = remainPlace("3005", thick, hight, wide, tA, 2)

#tA += out[0]

#textOutput += out[1]






ldrOutput.write(textOutput)