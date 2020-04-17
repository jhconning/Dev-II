import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


Pc = 4
Pw = 8
c = 1/2
d = 1/2


def F(x,P=Pc,c=c):
    '''Cattle Profit Function'''
    return P*x - c*x**2

def AG(x, P=Pw):
    '''Wheat farm profit before crop damage'''
    return P*(x**0)   # to return an array of len(x)

def AGD(x,P=Pw,d=d):
    '''Wheat farm profit after damage'''
    return AG(x,P) - d*x**2

def copt(P=Pc,c=c):
    '''rancher private optimum'''
    return P/(2*c)

def topt(P=Pc,c=c, d=d):
    '''Social effient optimum'''
    return P/(2*(c+d))

CE, TE = copt(),topt()

def coaseplot1():
    xx = np.linspace(0,6,100)
    fig = plt.subplots(figsize=(12,8))
    plt.plot(xx, F(xx), label = 'Rancher Profit' )
    plt.plot(xx, AG(xx), '--', label = 'Farm w/ no cattle damage' )
    plt.plot(xx, AGD(xx), label = 'Farm w/ cattle damage')
    plt.plot(xx, F(xx) + AGD(xx),label='Sum of both activities')
    plt.scatter(copt(),F(copt()))
    plt.scatter(copt(), 0)
    plt.scatter(topt(),F(topt()) + AGD(topt()))
    plt.grid()
    plt.xlim(0,6)
    plt.ylim(0,14)
    plt.xlabel('x -- head of cattle', fontsize=18)
    plt.ylabel('Benefits/Profit', fontsize=18)
    plt.legend(fontsize=14);



def MC(x,c=1/2):
    '''Cattle MC'''
    return 2*c*x

def excost(x,d=1/2):
    return 2*d*x
    

def coaseplot2(Pw=Pw, Pc=Pc):
    xx = np.linspace(0,6,100)
    fig = plt.subplots(figsize=(12,9))
    plt.axhline(Pc);
    plt.plot(xx, MC(xx), label = 'Rancher PMC' )
    plt.plot(xx, MC(xx)+excost(xx), label = 'SMC')
    plt.fill_between(xx, MC(xx)+excost(xx),Pc*xx**0, where=((MC(xx)<=Pc*xx**0) & (xx>2)),
                     facecolor='green', alpha=0.2, label='DWL')

    plt.text(3,5,'DWL' , fontsize=15)
    plt.text(5,3.5,r'$SMB = P_C$', fontsize=15)
    plt.text(5,5.5, r'$PMC$', fontsize=15)
    plt.text(4.5,8.5, r'$SMC$', fontsize=15)
    #plt.scatter(topt(),G(topt()) + AGD(topt()))
    plt.grid()
    plt.xlim(0,6)
    plt.ylim(0,10)
    plt.yticks(np.arange(0, 10, 1)) 
    plt.xlabel('x -- head of cattle')
    plt.ylabel('Benefits/Profit')
    plt.legend();


# #### Code for land example


A=1

def FT(T, A=A):
    return A*np.sqrt(T)


def MVPT(P,T,A=A):
    return A*P/T**(1/2)

def LD(P,r,A=A):
    return (P*A/r)**2



A=1
Tbar  = 10  # Total land endowment
P = 5.5     # Price of output
cl = 3      # cost of clearing land


def req(P, cl, Tb=Tbar, N=2, A=A):
    '''equilibrium rental rate'''
    def landemand(r):
        return N*(A*P/r)**2 - Tb 
    return fsolve(landemand, 1)[0]
    


def mopt(P,cl,A=A):
    '''Optimum land use for each i at the P*MPT = max(cl,r)'''
    r = req(P,cl)
    ru = max(cl, r)
    return (A*P/ru)**2


mopt(P,cl), MVPT(P, mopt(P,cl) )


def landmarket(P, cl, title, A=A):
    t = np.linspace(0.1,Tbar-0.1, 2*Tbar)
    fig = plt.subplots(figsize=(12,8))
    x0 = mopt(P,cl,A=A)
    plt.ylim(0,5)
    #plt.axhline(cl,linestyle=':')
    plt.axhline(max(cl,req(P,cl,A=A)),linestyle='--')
    plt.axhline(cl,linestyle=':')
    plt.plot(t,MVPT(P,t))
    plt.text(8, MVPT(P,8),r'$P \cdot F_T(T)$', fontsize=18)
    plt.text(1, MVPT(P,Tbar-1),r'$P \cdot F_T(\bar T - T)$', fontsize=18)
    plt.xlabel('T -- land use', fontsize=18)
    plt.ylabel('MVPT', fontsize=18)

    plt.scatter(x0, MVPT(P,x0))
    plt.scatter(Tbar-mopt(P,cl),MVPT(P,x0))
    plt.plot([x0,x0],[0,MVPT(P,x0)],':')
    plt.plot([Tbar-x0,Tbar-x0],[0,MVPT(P,x0)],':')
    plt.plot(t,MVPT(P,Tbar - t))
    plt.plot(t,MVPT(P,Tbar-t))
    plt.title(title, fontsize=18)
    plt.xlim(0,Tbar);

