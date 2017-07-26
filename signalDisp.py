import re
import matplotlib.pyplot as plt
import numpy as np
# Convert 16bit complement to true form
# Input type should be a str
# Exp:
# 0000101100010011 -> 0001000000101011
# 1111111101100100 -> 0001011010101110
def BinC2BinT(num_bin):
    firstBit = re.compile(r"\d")
    match = firstBit.match(num_bin)
    if match and match.group() is "1":
        num = -(~int(num_bin,base=2)+2**16+1)
        # num = -num
    else:
        num = int(num_bin,base=2)
    return num

# Input file:signalq.vh
# assign i[0	]= 16'b0000101100010011;
# assign i[1	]= 16'b1111111101100100;
# assign i[2	]= 16'b1111010011010101;
# assign i[3	]= 16'b1110101111101000;
# ************
def getSeq():
    reviseNum=[]
    pattern = re.compile(r".+16'b(\d+)")
    f_signal_i = open("signalq.vh","r")
    for i, line in enumerate(f_signal_i):
        plt.figure(1)
        match = pattern.match(line)
        if match:
            num = match.group(1)
            print(num)
            reviseNum.append(BinC2BinT(num))
        else:
            print "no result"
    f_signal_i.close()
    return reviseNum
def FFT(wave):
    tran = np.fft.fft(wave)
    return tran

if __name__ == '__main__':
    signal = getSeq()
    n=123
    plt.plot(signal[n+1:n+200])
    fs = FFT(signal)
    # plt.plot(fs[1:1000])
    plt.show()
