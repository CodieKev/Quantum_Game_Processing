"""
Created on Wed Dec 18 02:14:18 2019

@author: codie
"""
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer
import numpy as np


def Result(a,b,d):
    qc = QuantumCircuit()
    
    q = QuantumRegister(7, 'q')
    c = ClassicalRegister(1, 'c')
        
    qc.add_register(q)
    qc.add_register(c)
    print("a,b,d",a,b,d) 
    qc.u3(a*np.pi, 0, 0, q[0])
    qc.u3(b*2, 0, 0, q[1])
    qc.u3(d*2, 0, 0, q[2])
    qc.cx(q[1], q[3])
    qc.cx(q[2], q[3])
    qc.ccx(q[2], q[1], q[3])
    qc.x(q[4])
    qc.cswap(q[0], q[4], q[3])
    qc.measure(q[3], c[0])
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend)
    job_result = job.result()
    data = job_result.get_counts(qc).get("1", "")
    print(job_result.get_counts(qc))
    return data
        
        
        
LB = 0
b = 0 
d = 0
while LB==0:
    A = B = C = D = F = 0
    A = int(input("Use Knife(0 for No and 1 for YES):-"))
    if A == 0:
        B = int(input("Use Gun(0 for No and 1 for YES):-"))
        if B!= 0:   
            C = (1/(15-2*int(input("Type of bullet(Dammage ranked from 1,4):-"))))
            b=np.arcsin((((np.sin(b))**2)+C)**0.5)
            
        elif B ==0:           
            D = int(input("Use Granade(0 for No and 1 for YES):-"))
            if D!= 0:
                F = 1/(2 + int(input("Distance(0,2):-")))
    
                if F != 2:       
                    d=np.arcsin((((np.sin(d))**2)+F)**0.5)
                    print(d)

    print("a,b,d",A,b,d) 
   
    
    
    data =  Result(A,b,d)
    print("Dammage_Delt =",data/8.2,"%")
    if data > 820:
        print("You_Got_Killed")
        LB = 1