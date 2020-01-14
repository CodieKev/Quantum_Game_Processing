"""
Created on Wed Dec 18 02:14:18 2019.

@author: codie
"""
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer
import numpy as np


def Result(a,a1,b,b1,d,g,g1,h,h1,j):
    qc = QuantumCircuit()
    
    q = QuantumRegister(9, 'q')
    c = ClassicalRegister(2, 'c')
        
    qc.add_register(q)
    qc.add_register(c)
    
    qc.u3(a*np.pi, 0, 0, q[0])
    qc.u3((-1)*a1*a*np.pi, 0, 0, q[0])
    qc.u3(b*2, 0, 0, q[1])
    qc.u3(b1*b*(-2), 0, 0, q[1])
    qc.u3(d*2, 0, 0, q[2])
    qc.x(q[4])
    qc.u3(g*np.pi, 0, 0, q[5])
    qc.u3((-1)*g1*g*np.pi,0, 0, q[5])
    qc.u3(h*2, 0, 0, q[6])
    qc.u3(h1*h*(-2), 0, 0, q[6])
    qc.u3(j*2, 0, 0, q[7])
    qc.cx(q[1], q[3])
    qc.cx(q[6], q[8])
    qc.cx(q[2], q[3])
    qc.cx(q[7], q[8])
    qc.ccx(q[2], q[1], q[3])
    qc.ccx(q[7], q[6], q[8])
    qc.cswap(q[0], q[4], q[3])
    qc.cswap(q[5], q[4], q[8])
    qc.measure(q[8], c[1])
    qc.measure(q[3], c[0])
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend)
    job_result = job.result()
    data1 = int(job_result.get_counts(qc).get("11", "0"))+int(job_result.get_counts(qc).get("10", "0"))
    data2 = int(job_result.get_counts(qc).get("01", "0"))+int(job_result.get_counts(qc).get("11", "0"))
    print(job_result.get_counts(qc))
    return data1,data2
        
        
        
LB = b = b1 = d = h = h1 = j =A1 = G1 = 0

while LB==0:
    T = int(input("Use 0 for player 1 and 1 for player 2:-"))
    A = B = C = D = F = G = H = I = J = K = 0
    if T != 0:
        A = int(input("Use Knife(0 for No and 1 for YES):-"))
        A1= int(input("was he in range(1 for not 0 for yes):-"))
        if A == 0:
            B = int(input("Use Gun(0 for No and 1 for YES):-"))
            if B!= 0:   
                C = (1/(15-2*int(input("Type of bullet(Dammage ranked from 1,4):-"))))
                b1 = int(input("Did_it_hit(0 for hit 1 for not):-"))
                b=np.arcsin((((np.sin(b))**2)+C)**0.5)
                
            elif B ==0:           
                D = int(input("Use Granade(0 for No and 1 for YES):-"))
                if D!= 0:
                    F = 1/(2+int(input("Distance(0,2):-")))
                    
                    if F != 2:       
                        d=np.arcsin((((np.sin(d))**2)+F)**0.5)
    else:
        
                            
        G = int(input("Use Knife(0 for No and 1 for YES):-"))
        G1= int(input("was he in range(1 for not 0 for yes):-"))
        if G == 0:
            H = int(input("Use Gun(0 for No and 1 for YES):-"))
            if H!= 0:   
                I =(1/(15-2*int(input("Type of bullet(Dammage ranked from 1,4):-"))))
                h1 = int(input("Did_it_hit(0 for hit 1 for not):-"))
                h=np.arcsin((((np.sin(b))**2)+I)**0.5)
                
            elif H ==0:           
                J = int(input("Use Granade(0 for No and 1 for YES):-"))
                if J!= 0:
                    K = 1/(2+int(input("Distance(0,2):-")))
                    
                    if K != 2:       
                        j=np.arcsin((((np.sin(d))**2)+K)**0.5)

   
    
    
    D1,D2 =  Result(A,A1,b,b1,d,G,G1,h,h1,j)
    if D2<820:
        
        print("Life Of player 1 =",100-D2/8.2,"%")
    else:
        print("Life Of player 1 =",00,"%")
    if D1<820:
        
        print("Life Of player 2 =",100-D1/8.2,"%")
    else:
        print("Life Of player 2 =",00,"%")
    
    if D1 > 820:
        print("Player 1 Wins")
        LB = 1
    elif D2>820:
        print("Player 2 Wins")
        LB = 1
        
