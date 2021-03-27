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
    outputText = "1 " + str(c) + " " + str(x) + " " + str(y) + " " + str(z) + " " + m + " " + p + ".dat" + "\n"
    return outputText

