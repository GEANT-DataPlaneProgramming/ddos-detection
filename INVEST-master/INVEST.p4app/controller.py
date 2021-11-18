# !/usr/bin/python
# -*- coding:utf-8 -*-
# ###########################

import subprocess
from datasketch import HyperLogLog
import numpy as np

# Only valid for Python2
def readRegister(register, thrift_port):
    p = subprocess.Popen(['docker', 'exec', '-i', 'hh', 'simple_switch_CLI', '--thrift-port', str(thrift_port)],
stdin=subprocess.PIPE, stdout=subprocess.PIPE,
     stderr=subprocess.PIPE)
    stdout, stderr = p.communicate(input="register_read %s" % (register))
    reg = list(stdout.strip().split("= ")[1].split("\n")[0].split(", "))
    reg = map(int, reg)
    return reg


hll_reg1 = readRegister("hll_register", 22222)
s1 = readRegister("tot_reg", 22222)
hll1 = HyperLogLog(p=11, reg=np.array(hll_reg1))
print "Cardinality estimation in S1(HLL):"
print hll1.count()
n1 = hll1.count()
print "S1"
print s1[0] 

hll_reg2 = readRegister("hll_register", 22223)
s2 = readRegister("tot_reg", 22223)
hll2 = HyperLogLog(p=11, reg=np.array(hll_reg2))
print "Cardinality estimation in S2(HLL):"
print hll2.count()
n2 = hll2.count()
print "S2"
print s2[0] 

hll_reg3 = readRegister("hll_register", 22224)
hll3 = HyperLogLog(p=11, reg=np.array(hll_reg3))
s3 = readRegister("tot_reg", 22224)
print "Cardinality estimation in S3(HLL):"
print hll3.count()
n3 = hll3.count()
print "S3"
print s3[0] 


hll_tot = HyperLogLog(p=11)
hll_tot.merge(hll1)
hll_tot.merge(hll2)
hll_tot.merge(hll3)
print "Network-wide Cardinality number:"
print hll_tot.count()

hll_reg = [hll1, hll2, hll3]
hll_top = HyperLogLog(p=11)
N = [n1, n2, n3]
N_t = N
S = [s1[0], s2[0], s3[0]]
I_top = []
k = 0
R_tot = 0
while hll_top.count() < hll_tot.count():
    n_max = max(N_t)
    i = N.index(n_max)    
    I_top.append(i)
    hll_top.merge(hll_reg[i])
    k = k + 1
    R_tot = R_tot + S[i]/N[i]
    N_t.remove(n_max)

R_tot = (1/k)*R_tot

print "Average flow packet size"
print R_tot

stot = R_tot * hll_tot.count() 
print "Network traffic volume estimation"
print stot
print "======================="
