import subprocess
import time
results = subprocess.check_output(["netsh", "wlan", "show", "all"])
dd=[s.strip() for s in results.splitlines()]
k=1
m=1
n=1
for i in dd:
    if "34:97:f6:3c:94:1e" in i:
        m=k
    if "00:14:bf:0f:c5:33" in i:
        n=k
    k=k+1

#Assigning keys
if m==1:
    key1="offline"
    pkey1="offline"
else:
    key1=dd[m-5]
    key1=key1[9:]
    pkey1=dd[m]
    pkey1=pkey1[20:24]
if n==1:
    key2="offline"
    pkey2="offline"
else:

    key2=dd[n-5]
    key2=key2[9:]
    pkey2=dd[n]
    pkey2=pkey2[20:24]

#printing
print ""
print ">",(time.strftime("%H:%M:%S"))
print "..............."
print key1
print pkey1
print key2
print pkey2
