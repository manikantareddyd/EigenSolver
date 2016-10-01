
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
if method == 1:
    import DirectPower
elif method == 2:
    import InversePower
elif method == 3:
    import ShiftedPower
elif method == 4:
    import QR
else:
    print "Wrong Choice"
