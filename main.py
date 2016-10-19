
methods = """
1. Direct Power
2. Inverse Power
3. Shifted Power
4. QR Method
"""


methodNameMap = {
1: "Direct Power",
2: "Inverse Power",
3: "Shifted Power",
4: "QR Method"
}

for i in methodNameMap:
    print i,":",methodNameMap[i]

method = int(input())
import sys
sys.stdout = open("out","w")
if method == 1:
    print method, ":", methodNameMap[method],"\n"
    import DirectPower
elif method == 2:
    print method, ":", methodNameMap[method],"\n"
    import InversePower
elif method == 3:
    print method, ":", methodNameMap[method],"\n"
    import ShiftedPower
elif method == 4:
    print method, ":", methodNameMap[method],"\n"
    import QR
else:
    print "Wrong Choice"
