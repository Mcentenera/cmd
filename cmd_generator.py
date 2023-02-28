import numpy as np
from scipy.integrate import quad
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.path as mpath
from datetime import datetime #To calculate the time of execution
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import os

#This parameter to calculate the time of execution
time_ini = datetime.now()
seed = 1234
rng = np.random.default_rng(seed)

#-------------------------------------------------------------------------------

#Get the variables of magnitude from the file
V,m=np.loadtxt("cmd_Nalto.txt",skiprows=1,usecols=(6,8),unpack=True)

fig,ax=plt.subplots()

ax.plot(V-m,m,'ok',ms=0.1)
ax.annotate('AGB',(3.5,-2.1),(3.5,0),arrowprops=dict(),color='blue')
ax.annotate('RGB',(1,1),(2.2,1),arrowprops=dict(),color='blue')
ax.annotate('HB',(1.2,-0.5),(0.5,-3),arrowprops=dict(),color='blue')
ax.annotate('MS',(0,1),(-0.5,3),arrowprops=dict(),color='blue')
ax.annotate('BL',(0.7,-6),(0.7,-8),arrowprops=dict(),color='blue')
ax.annotate('RC',(1.3,-1),(1.4,-4),arrowprops=dict(),color='blue')
ax.annotate('Punto de giro',(0.7,2.8),(3,2.8),arrowprops=dict(),color='blue')

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

ax.tick_params(which='major', axis='x', direction='in', length=10, top=True)
ax.tick_params(which='major', axis='y', direction='in', length=10, right=True)
ax.tick_params(which='minor', axis='x', direction='in', length=6, top=True)
ax.tick_params(which='minor', axis='y', direction='in', length=6, right=True)

ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

plt.title ('Diagrama color-magnitud',fontsize = 15)
plt.xlabel ('Color V-I', fontsize=15)
plt.ylabel ('Magnitud aparente', fontsize=15)
ax.invert_yaxis()
plt.show
plt.savefig('Diagrama color-magnitud.png')

#Get the variables of magnitude from the file
V,m,t=np.loadtxt("cmd_16035.txt",skiprows=1,usecols=(16,18,10),unpack=True)
magV1=[]
magI1=[]
magV2=[]
magI2=[]
magV3=[]
magI3=[]
magV4=[]
magI4=[]
magV5=[]
magI5=[]
magV6=[]
magI6=[]
magV7=[]
magI7=[]

#Create a loop to divide the data in seven ranges of time
fig,ax=plt.subplots()
for i in range(0,len(t)):
    age=t[i]/1E9
    if age<=0.1:
        magV1.append(V[i])
        magI1.append(m[i])
        
    elif (age>0.1) and (age<=0.4):
        magV2.append(V[i])
        magI2.append(m[i])
        
    elif (age>0.4) and (age<=1):
        magV3.append(V[i])
        magI3.append(m[i])
        
    elif (age>1) and (age<=3):
        magV4.append(V[i])
        magI4.append(m[i])
        
    elif (age>3) and (age<=6):
        magV5.append(V[i])
        magI5.append(m[i])
        
    elif (age>6) and (age<=10):
        magV6.append(V[i])
        magI6.append(m[i])
        
    elif (age>10) and (age<=13):
        magV7.append(V[i])
        magI7.append(m[i])

ax.plot(np.array(magV1)-np.array(magI1),magI1,'ob',ms=0.1,label='$t\leq0.1$')
ax.plot(np.array(magV2)-np.array(magI2),magI2,'oy',ms=0.1,label='$0.1<t\leq0.4$')
ax.plot(np.array(magV3)-np.array(magI3),magI3,'og',ms=0.1,label='$0.4<t\leq1$')
ax.plot(np.array(magV4)-np.array(magI4),magI4,'om',ms=0.1,label='$1<t\leq3$')
ax.plot(np.array(magV5)-np.array(magI5),magI5,'oc',ms=0.1,label='$3<t\leq6$')
ax.plot(np.array(magV6)-np.array(magI6),magI6,'or',ms=0.1,label='$6<t\leq10$')
ax.plot(np.array(magV7)-np.array(magI7),magI7,'ok',ms=0.1,label='$10<t\leq13$')

ax.annotate('AGB',(3.5,-2.1),(3.5,0),arrowprops=dict(),color='blue')
ax.annotate('RGB',(1,1),(2.2,1),arrowprops=dict(),color='blue')
ax.annotate('HB',(1.2,-0.5),(0.5,-3),arrowprops=dict(),color='blue')
ax.annotate('MS',(0,1),(-0.5,3),arrowprops=dict(),color='blue')
ax.annotate('BL',(0.7,-6),(0.7,-7),arrowprops=dict(),color='blue')
ax.annotate('RC',(1.3,-1),(1.4,-4),arrowprops=dict(),color='blue')
ax.annotate('Punto de giro',(0.7,2.8),(3,2.8),arrowprops=dict(),color='blue')
plt.title ('Diagrama color-magnitud',fontsize = 15)
plt.xlabel ('Color V-I', fontsize=15)
plt.ylabel ('Magnitud aparente', fontsize=15)
lgnd = plt.legend(loc="upper right", numpoints=1, fontsize=8, bbox_to_anchor = (1.11, 0.55))

#lgnd.legendHandles[0]._legmarker.set_markersize(6)
#lgnd.legendHandles[1]._legmarker.set_markersize(6)
#lgnd.legendHandles[2]._legmarker.set_markersize(6)
#lgnd.legendHandles[3]._legmarker.set_markersize(6)
#lgnd.legendHandles[4]._legmarker.set_markersize(6)
#lgnd.legendHandles[5]._legmarker.set_markersize(6)
#lgnd.legendHandles[6]._legmarker.set_markersize(6)
ax.xaxis.set_minor_locator(AutoMinorLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))


ax.tick_params(which='major', axis='x', direction='in', length=10, top=True)
ax.tick_params(which='major', axis='y', direction='in', length=10, right=True)
ax.tick_params(which='minor', axis='x', direction='in', length=6, top=True)
ax.tick_params(which='minor', axis='y', direction='in', length=6, right=True)

ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

ax.invert_yaxis()
plt.show
plt.savefig('Diagrama color-magnitud IAC.png')

#-------------------------------------------------------------------------------

#Now we are going to plot one example of isocrone of our cmd

#Get the variables of magnitude from the file
V,m=np.loadtxt("cmd_Nalto.txt",skiprows=1,usecols=(6,8),unpack=True)

fig,ax=plt.subplots()

ax.plot(V-m,m,'ok',ms=0.1)

#Get the variables of magnitude from the file
V,m,t=np.loadtxt("cmd_21032.txt",skiprows=1,usecols=(16,18,10),unpack=True)
magV1=[]
magI1=[]
magV2=[]
magI2=[]
magV3=[]
magI3=[]
magV4=[]
magI4=[]
magV5=[]
magI5=[]
magV6=[]
magI6=[]
magV7=[]
magI7=[]

for i in range(0,len(t)):
    age=t[i]/1E9
    if age<=0.1:
        magV1.append(V[i])
        magI1.append(m[i])
                
    elif (age>0.1) and (age<=0.4):
        magV2.append(V[i])
        magI2.append(m[i])
                
    elif (age>0.4) and (age<=1):
        magV3.append(V[i])
        magI3.append(m[i])
                
    elif (age>1) and (age<=3):
        magV4.append(V[i])
        magI4.append(m[i])
                
    elif (age>3) and (age<=6):
        magV5.append(V[i])
        magI5.append(m[i])
                
    elif (age>6) and (age<=10):
        magV6.append(V[i])
        magI6.append(m[i])
                
    elif (age>10) and (age<=13):
        magV7.append(V[i])
        magI7.append(m[i])

ax.plot(np.array(magV1)-np.array(magI1),magI1,'ob',ms=0.1,label='$t\leq0.1$')
ax.plot(np.array(magV2)-np.array(magI2),magI2,'oy',ms=0.1,label='$0.1<t\leq0.4$')
ax.plot(np.array(magV3)-np.array(magI3),magI3,'og',ms=0.1,label='$0.4<t\leq1$')
ax.plot(np.array(magV4)-np.array(magI4),magI4,'om',ms=0.1,label='$1<t\leq3$')
ax.plot(np.array(magV5)-np.array(magI5),magI5,'oc',ms=0.1,label='$3<t\leq6$')
ax.plot(np.array(magV6)-np.array(magI6),magI6,'or',ms=0.1,label='$6<t\leq10$')
ax.plot(np.array(magV7)-np.array(magI7),magI7,'om',ms=0.1,label='$10<t\leq13$')

ax.xaxis.set_minor_locator(AutoMinorLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))


ax.tick_params(which='major', axis='x', direction='in', length=10, top=True)
ax.tick_params(which='major', axis='y', direction='in', length=10, right=True)
ax.tick_params(which='minor', axis='x', direction='in', length=6, top=True)
ax.tick_params(which='minor', axis='y', direction='in', length=6, right=True)

ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

plt.title ('Diagrama color-magnitud',fontsize = 15)
plt.xlabel ('Color V-I', fontsize=15)
plt.ylabel ('Magnitud aparente', fontsize=15)

ax.invert_yaxis()
plt.show
plt.savefig('Isocrona.png')

#-------------------------------------------------------------------------------

#Create two plots comparation between cmd and synthetic cmd
        
#Get the variables of magnitude from the file
V,m=np.loadtxt("cmd_Nalto.txt",skiprows=1,usecols=(6,8),unpack=True)

fig,ax=plt.subplots(1,2)
fig.set_size_inches(15,6)


ax[0].plot(V-m,m,'ok',ms=0.1)
ax[0].plot([0,0.5],[3.2,0.8],'-b')
ax[0].plot([0.5,0],[0.8,-5],'-b')
ax[0].plot([0,-0.5],[-5,-5],'-b')
ax[0].plot([-0.5,0],[-5,3.2],'-b')

def f(x):
    return-4.8*x+3.2

def f4(x):
    return 11.6*x-5

def f7(y):
    return (5/(58))*y+(25)/(58)

def f6(x):
    return 16.4*x+3.2

def f5(y):
    return (1/(16.4))*y-8/(41)
            
def recta(y):
    return 0.086620689655172413793103448275*y+0.3922413793103448275862068965517

x1=np.linspace(-0.5,-0.033333333,25)
x2=np.linspace(-0.033333333,0.5,26)
x=np.linspace(-0.5,0.5,50)
y=np.linspace(-5,3.2,50)

numeroazulm=[]
for i in range(0,len(x1)):
    for j in range(0,len(y)):
        if f5(y[1])<=x1[0] and f5(y[0])<=x1[1]:
            if f(x1[0])>y[0] and f(x1[1])>y[1]:
                verts=np.array([[x1[0],x1[1],x1[1],x1[0]],[y[0],y[0],y[1],y[1]]]).T
                ax[0].plot([x1[0],x1[1]],[y[0],y[0]],'-m',linewidth=0.5)
                ax[0].plot([x1[1],x1[1]],[y[0],y[1]],'-m',linewidth=0.5)
                ax[0].plot([x1[1],x1[0]],[y[1],y[1]],'-m',linewidth=0.5)
                ax[0].plot([x1[0],x1[0]],[y[1],y[0]],'-m',linewidth=0.5)
                path = mpath.Path(verts)
                points = np.column_stack([V-m, m])
                points_inside = points[path.contains_points(points)]
                numeroazulm.append(len(points_inside))
                    
                if len(y)>2:
                    y=np.delete(y,(0))
            else:
                yf=[3,3]
                yf[0]=f(x1[0])
                yf[1]=f(x1[1])
                verts=np.array([[x1[0],x1[1],x1[1],x1[0]],[yf[0],yf[1],y[0],y[0]]]).T
                path = mpath.Path(verts)
                points = np.column_stack([V-m, m])
                points_inside = points[path.contains_points(points)]
                numeroazulm.append(len(points_inside))

                ax[0].plot([x1[0],x1[1]],[yf[0],yf[1]],'-m',linewidth=0.5)
                ax[0].plot([x1[1],x1[1]],[yf[1],y[0]],'-m',linewidth=0.5)
                ax[0].plot([x1[1],x1[0]],[y[0],y[0]],'-m',linewidth=0.5)
                ax[0].plot([x1[0],x1[0]],[y[0],yf[0]],'-m',linewidth=0.5)

                    
        else:
            yf=[3,3]
            yf[0]=f6(x1[0])
            yf[1]=f6(x1[1])
            verts=np.array([[x1[0],x1[1],x1[1],x1[0]],[yf[0],yf[1],y[0],y[0]]]).T
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numeroazulm.append(len(points_inside))

            ax[0].plot([x1[0],x1[1]],[yf[0],yf[1]],'-b',linewidth=0.5)
            ax[0].plot([x1[1],x1[1]],[yf[1],y[0]],'-b',linewidth=0.5)
            ax[0].plot([x1[1],x1[0]],[y[0],y[0]],'-b',linewidth=0.5)
            ax[0].plot([x1[0],x1[0]],[y[0],yf[0]],'-b',linewidth=0.5)
                    
                    
    y=np.linspace(-5,3.2,50)
    if len(x1)>2:
        x1=np.delete(x1,(0))

y=np.linspace(3.2,-5,50)
yy=np.linspace(3.2,-5,50)
for i in range(0,len(x2)):
    verdad=0
    for j in range(0,len(y)):
        if f7(y[0])>=x2[0] and f7(y[1])>=x2[1]:
            if f(x2[0])>y[0] and f(x2[1])>y[1]:
                verts=np.array([[x2[0],x2[1],x2[1],x2[0]],[y[0],y[0],y[1],y[1]]]).T
                ax[0].plot([x2[0],x2[1]],[y[0],y[0]],'-m',linewidth=0.5)
                ax[0].plot([x2[1],x2[1]],[y[0],y[1]],'-m',linewidth=0.5)
                ax[0].plot([x2[1],x2[0]],[y[1],y[1]],'-m',linewidth=0.5)
                ax[0].plot([x2[0],x2[0]],[y[1],y[0]],'-m',linewidth=0.5)
                path = mpath.Path(verts)
                points = np.column_stack([V-m, m])
                points_inside = points[path.contains_points(points)]
                numeroazulm.append(len(points_inside))

                if len(y)>2:
                    y=np.delete(y,(0))
            else:
                if len(y)>2:
                    y=np.delete(y,(0))
                    
        else:
            yf=[3,3]
            yf[1]=f4(x2[0])
            yf[0]=f4(x2[1])
            verts=np.array([[x2[0],x2[1],x2[1],x2[0]],[y[0],y[0],yf[0],yf[1]]]).T
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numeroazulm.append(len(points_inside))
            ax[0].plot([x2[0],x2[1]],[y[0],y[0]],'-m',linewidth=0.5)
            ax[0].plot([x2[1],x2[1]],[y[0],yf[0]],'-m',linewidth=0.5)
            ax[0].plot([x2[1],x2[0]],[yf[0],yf[1]],'-m',linewidth=0.5)
            ax[0].plot([x2[0],x2[0]],[yf[1],y[0]],'-m',linewidth=0.5)
                    
                    
    y=np.linspace(3.2,-5,50)
    if len(x2)>2:
        x2=np.delete(x2,(0))
                

ax[0].plot([1.8,5],[-1,-2],'-r')
ax[0].plot([5,5],[-2,-3],'-r')
ax[0].plot([5,1.8],[-3,-3],'-r')
ax[0].plot([1.8,1.8],[-3,-1],'-r')
x=np.linspace(5,1.8,10)
y=np.linspace(-3,-1,10)

def f3(x):
    return -0.3125*x-0.4375

numerorojom=[]
for i in range(0,len(x)):
    for j in range(0,len(y)):
        if f3(x[0])>y[0] and f3(x[1])>y[1]:
            verts=np.array([[x[0],x[1],x[1],x[0]],[y[0],y[0],y[1],y[1]]]).T
            ax[0].plot([x[0],x[1]],[y[0],y[0]],'-m',linewidth=0.5)
            ax[0].plot([x[1],x[1]],[y[0],y[1]],'-m',linewidth=0.5)
            ax[0].plot([x[1],x[0]],[y[1],y[1]],'-m',linewidth=0.5)
            ax[0].plot([x[0],x[0]],[y[1],y[0]],'-m',linewidth=0.5)
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numerorojom.append(len(points_inside))
                    
            if len(y)>2:
                y=np.delete(y,(0))
        else:
            yf=[3,3]
            yf[0]=f3(x[0])
            yf[1]=f3(x[1])
            verts=np.array([[x[0],x[1],x[1],x[0]],[yf[0],yf[1],y[0],y[0]]]).T
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numerorojom.append(len(points_inside))
            ax[0].plot([x[0],x[1]],[yf[0],yf[1]],'-m',linewidth=0.5)
            ax[0].plot([x[1],x[1]],[yf[1],y[0]],'-m',linewidth=0.5)
            ax[0].plot([x[1],x[0]],[y[0],y[0]],'-m',linewidth=0.5)
            ax[0].plot([x[0],x[0]],[y[0],yf[0]],'-m',linewidth=0.5)
                    
                    
    y=np.linspace(-3,-1,10)
    if len(x)>2:
        x=np.delete(x,(0))


def f2(x):
    return-4.333333333333333*x+4.766666666666666666666666666


ax[0].plot([0.8,1.1],[1.3,0],'-g')
ax[0].plot([1.1,1.1],[0,-4],'-g')
ax[0].plot([1.1,0.8],[-4,-4],'-g')
ax[0].plot([0.8,0.8],[-4,1.3],'-g')
x=np.linspace(0.8,1.1,16)
y=np.linspace(-4,1.3,16)

numeroverdem=[]
for i in range(0,len(x)):
    for j in range(0,len(y)):
        if f2(x[0])>y[0] and f2(x[1])>y[1]:
            verts=np.array([[x[0],x[1],x[1],x[0]],[y[0],y[0],y[1],y[1]]]).T
            ax[0].plot([x[0],x[1]],[y[0],y[0]],'-m',linewidth=0.5)
            ax[0].plot([x[1],x[1]],[y[0],y[1]],'-m',linewidth=0.5)
            ax[0].plot([x[1],x[0]],[y[1],y[1]],'-m',linewidth=0.5)
            ax[0].plot([x[0],x[0]],[y[1],y[0]],'-m',linewidth=0.5)
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numeroverdem.append(len(points_inside))
                    
            if len(y)>2:
                y=np.delete(y,(0))
        else:
            yf=[3,3]
            yf[0]=f2(x[0])
            yf[1]=f2(x[1])
            verts=np.array([[x[0],x[1],x[1],x[0]],[yf[0],yf[1],y[1],y[1]]]).T
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numeroverdem.append(len(points_inside))
            ax[0].plot([x[0],x[1]],[yf[0],yf[1]],'-m',linewidth=0.5)
            ax[0].plot([x[1],x[1]],[yf[1],y[0]],'-m',linewidth=0.5)
            ax[0].plot([x[1],x[0]],[y[0],y[0]],'-m',linewidth=0.5)
            ax[0].plot([x[0],x[0]],[y[0],yf[0]],'-m',linewidth=0.5)
                    
                    
    y=np.linspace(-4,1.3,16)
    if len(x)>2:
        x=np.delete(x,(0))
                

ax[0].plot([0.5,1],[3,3],'-c')
ax[0].plot([1,1],[3,2],'-c')
ax[0].plot([1,0.5],[2,2],'-c')
ax[0].plot([0.5,0.5],[2,3],'-c')
x=np.linspace(0.5,1,64)
y=np.linspace(3,2,64)

numerocianm=[]
for i in range(0,len(x)):
    for j in range(0,len(y)):
        verts=np.array([[x[0],x[1],x[1],x[0]],[y[0],y[0],y[1],y[1]]]).T
        ax[0].plot([x[0],x[1]],[y[0],y[0]],'-m',linewidth=0.5)
        ax[0].plot([x[1],x[1]],[y[0],y[1]],'-m',linewidth=0.5)
        ax[0].plot([x[1],x[0]],[y[1],y[1]],'-m',linewidth=0.5)
        ax[0].plot([x[0],x[0]],[y[1],y[0]],'-m',linewidth=0.5)
        path = mpath.Path(verts)
        points = np.column_stack([V-m, m])
        points_inside = points[path.contains_points(points)]
        numerocianm.append(len(points_inside))
            
        if len(y)>2:
            y=np.delete(y,(0))
                    
    y=np.linspace(3,2,64)
    if len(x)>2:
        x=np.delete(x,(0))

            
ax[0].xaxis.set_minor_locator(AutoMinorLocator(10))
ax[0].yaxis.set_minor_locator(AutoMinorLocator(10))


ax[0].tick_params(which='major', axis='x', direction='in', length=10, top=True)
ax[0].tick_params(which='major', axis='y', direction='in', length=10, right=True)
ax[0].tick_params(which='minor', axis='x', direction='in', length=6, top=True)
ax[0].tick_params(which='minor', axis='y', direction='in', length=6, right=True)

ax[0].invert_yaxis()
ax[0].set_xlabel ('Color V-I', fontsize=15)
ax[0].set_ylabel ('Magnitud aparente', fontsize=15)
ax[0].grid(which='minor', alpha=0.2)
ax[0].grid(which='major', alpha=0.5)


V,m,t=np.loadtxt("cmd_16035.txt",skiprows=1,usecols=(16,18,10),unpack=True)

ax[1].plot(V-m,m,'ok',ms=0.1)
ax[1].plot([0,0.5],[3.2,0.8],'-b')
ax[1].plot([0.5,0],[0.8,-5],'-b')
ax[1].plot([0,-0.5],[-5,-5],'-b')
ax[1].plot([-0.5,0],[-5,3.2],'-b')

def f(x):
    return-4.8*x+3.2

def f4(x):
    return 11.6*x-5

def f7(y):
    return (5/(58))*y+(25)/(58)

def f6(x):
    return 16.4*x+3.2

def f5(y):
    return (1/(16.4))*y-8/(41)
            
def recta(y):
    return 0.086620689655172413793103448275*y+0.3922413793103448275862068965517

x1=np.linspace(-0.5,-0.033333333,25)
x2=np.linspace(-0.033333333,0.5,26)
x=np.linspace(-0.5,0.5,50)
y=np.linspace(-5,3.2,50)
Xb=[]

numeroazuls=[]
for i in range(0,len(x1)):
    for j in range(0,len(y)):
        if f5(y[1])<=x1[0] and f5(y[0])<=x1[1]:
            if f(x1[0])>y[0] and f(x1[1])>y[1]:
                verts=np.array([[x1[0],x1[1],x1[1],x1[0]],[y[0],y[0],y[1],y[1]]]).T
                ax[1].plot([x1[0],x1[1]],[y[0],y[0]],'-m',linewidth=0.5)
                ax[1].plot([x1[1],x1[1]],[y[0],y[1]],'-m',linewidth=0.5)
                ax[1].plot([x1[1],x1[0]],[y[1],y[1]],'-m',linewidth=0.5)
                ax[1].plot([x1[0],x1[0]],[y[1],y[0]],'-m',linewidth=0.5)
                path = mpath.Path(verts)
                points = np.column_stack([V-m, m])
                points_inside = points[path.contains_points(points)]
                numeroazuls.append(len(points_inside))
                    
                if len(y)>2:
                    y=np.delete(y,(0))
            else:
                yf=[3,3]
                yf[0]=f(x1[0])
                yf[1]=f(x1[1])
                verts=np.array([[x1[0],x1[1],x1[1],x1[0]],[yf[0],yf[1],y[0],y[0]]]).T
                path = mpath.Path(verts)
                points = np.column_stack([V-m, m])
                points_inside = points[path.contains_points(points)]
                numeroazuls.append(len(points_inside))
                ax[1].plot([x1[0],x1[1]],[yf[0],yf[1]],'-m',linewidth=0.5)
                ax[1].plot([x1[1],x1[1]],[yf[1],y[0]],'-m',linewidth=0.5)
                ax[1].plot([x1[1],x1[0]],[y[0],y[0]],'-m',linewidth=0.5)
                ax[1].plot([x1[0],x1[0]],[y[0],yf[0]],'-m',linewidth=0.5)

                    
        else:
            yf=[3,3]
            yf[0]=f6(x1[0])
            yf[1]=f6(x1[1])
            verts=np.array([[x1[0],x1[1],x1[1],x1[0]],[yf[0],yf[1],y[0],y[0]]]).T
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numeroazuls.append(len(points_inside))
            ax[1].plot([x1[0],x1[1]],[yf[0],yf[1]],'-m',linewidth=0.5)
            ax[1].plot([x1[1],x1[1]],[yf[1],y[0]],'-m',linewidth=0.5)
            ax[1].plot([x1[1],x1[0]],[y[0],y[0]],'-m',linewidth=0.5)
            ax[1].plot([x1[0],x1[0]],[y[0],yf[0]],'-m',linewidth=0.5)
                    
                    
    y=np.linspace(-5,3.2,50)
    if len(x1)>2:
        x1=np.delete(x1,(0))

y=np.linspace(3.2,-5,50)
yy=np.linspace(3.2,-5,50)
for i in range(0,len(x2)):
    verdad=0
    for j in range(0,len(y)):
        if f7(y[0])>=x2[0] and f7(y[1])>=x2[1]:
            if f(x2[0])>y[0] and f(x2[1])>y[1]:
                verts=np.array([[x2[0],x2[1],x2[1],x2[0]],[y[0],y[0],y[1],y[1]]]).T
                ax[1].plot([x2[0],x2[1]],[y[0],y[0]],'-m',linewidth=0.5)
                ax[1].plot([x2[1],x2[1]],[y[0],y[1]],'-m',linewidth=0.5)
                ax[1].plot([x2[1],x2[0]],[y[1],y[1]],'-m',linewidth=0.5)
                ax[1].plot([x2[0],x2[0]],[y[1],y[0]],'-m',linewidth=0.5)
                path = mpath.Path(verts)
                points = np.column_stack([V-m, m])
                points_inside = points[path.contains_points(points)]
                numeroazuls.append(len(points_inside))
                if len(y)>2:
                    y=np.delete(y,(0))
            else:
                if len(y)>2:
                    y=np.delete(y,(0))
                    
        else:
            yf=[3,3]
            yf[1]=f4(x2[0])
            yf[0]=f4(x2[1])
            verts=np.array([[x2[0],x2[1],x2[1],x2[0]],[y[0],y[0],yf[0],yf[1]]]).T
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numeroazuls.append(len(points_inside))
            ax[1].plot([x2[0],x2[1]],[y[0],y[0]],'-m',linewidth=0.5)
            ax[1].plot([x2[1],x2[1]],[y[0],yf[0]],'-m',linewidth=0.5)
            ax[1].plot([x2[1],x2[0]],[yf[0],yf[1]],'-m',linewidth=0.5)
            ax[1].plot([x2[0],x2[0]],[yf[1],y[0]],'-m',linewidth=0.5)
                    
                    
    y=np.linspace(3.2,-5,50)
    if len(x2)>2:
        x2=np.delete(x2,(0))

ax[1].plot([1.8,5],[-1,-2],'-r')
ax[1].plot([5,5],[-2,-3],'-r')
ax[1].plot([5,1.8],[-3,-3],'-r')
ax[1].plot([1.8,1.8],[-3,-1],'-r')
x=np.linspace(5,1.8,10)
y=np.linspace(-3,-1,10)

def f3(x):
    return -0.3125*x-0.4375

numerorojos=[]
for i in range(0,len(x)):
    for j in range(0,len(y)):
        if f3(x[0])>y[0] and f3(x[1])>y[1]:
            verts=np.array([[x[0],x[1],x[1],x[0]],[y[0],y[0],y[1],y[1]]]).T
            ax[1].plot([x[0],x[1]],[y[0],y[0]],'-m',linewidth=0.5)
            ax[1].plot([x[1],x[1]],[y[0],y[1]],'-m',linewidth=0.5)
            ax[1].plot([x[1],x[0]],[y[1],y[1]],'-m',linewidth=0.5)
            ax[1].plot([x[0],x[0]],[y[1],y[0]],'-m',linewidth=0.5)
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numerorojos.append(len(points_inside))
                    
            if len(y)>2:
                y=np.delete(y,(0))
        else:
            yf=[3,3]
            yf[0]=f3(x[0])
            yf[1]=f3(x[1])
            verts=np.array([[x[0],x[1],x[1],x[0]],[yf[0],yf[1],y[0],y[0]]]).T
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numerorojos.append(len(points_inside))
            ax[1].plot([x[0],x[1]],[yf[0],yf[1]],'-m',linewidth=0.5)
            ax[1].plot([x[1],x[1]],[yf[1],y[0]],'-m',linewidth=0.5)
            ax[1].plot([x[1],x[0]],[y[0],y[0]],'-m',linewidth=0.5)
            ax[1].plot([x[0],x[0]],[y[0],yf[0]],'-m',linewidth=0.5)
                    
                    
    y=np.linspace(-3,-1,10)
    if len(x)>2:
        x=np.delete(x,(0))

def f2(x):
    return-4.333333333333333*x+4.766666666666666666666666666

ax[1].plot([0.8,1.1],[1.3,0],'-g')
ax[1].plot([1.1,1.1],[0,-4],'-g')
ax[1].plot([1.1,0.8],[-4,-4],'-g')
ax[1].plot([0.8,0.8],[-4,1.3],'-g')
x=np.linspace(0.8,1.1,16)
y=np.linspace(-4,1.3,16)

numeroverdes=[]
for i in range(0,len(x)):
    for j in range(0,len(y)):
        if f2(x[0])>y[0] and f2(x[1])>y[1]:
            verts=np.array([[x[0],x[1],x[1],x[0]],[y[0],y[0],y[1],y[1]]]).T
            ax[1].plot([x[0],x[1]],[y[0],y[0]],'-m',linewidth=0.5)
            ax[1].plot([x[1],x[1]],[y[0],y[1]],'-m',linewidth=0.5)
            ax[1].plot([x[1],x[0]],[y[1],y[1]],'-m',linewidth=0.5)
            ax[1].plot([x[0],x[0]],[y[1],y[0]],'-m',linewidth=0.5)
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numeroverdes.append(len(points_inside))
                    
            if len(y)>2:
                y=np.delete(y,(0))
        else:
            yf=[3,3]
            yf[0]=f2(x[0])
            yf[1]=f2(x[1])
            verts=np.array([[x[0],x[1],x[1],x[0]],[yf[0],yf[1],y[1],y[1]]]).T
            path = mpath.Path(verts)
            points = np.column_stack([V-m, m])
            points_inside = points[path.contains_points(points)]
            numeroverdes.append(len(points_inside))
            ax[1].plot([x[0],x[1]],[yf[0],yf[1]],'-m',linewidth=0.5)
            ax[1].plot([x[1],x[1]],[yf[1],y[0]],'-m',linewidth=0.5)
            ax[1].plot([x[1],x[0]],[y[0],y[0]],'-m',linewidth=0.5)
            ax[1].plot([x[0],x[0]],[y[0],yf[0]],'-m',linewidth=0.5)
                    
                    
    y=np.linspace(-4,1.3,16)
    if len(x)>2:
        x=np.delete(x,(0))


ax[1].plot([0.5,1],[3,3],'-c')
ax[1].plot([1,1],[3,2],'-c')
ax[1].plot([1,0.5],[2,2],'-c')
ax[1].plot([0.5,0.5],[2,3],'-c')
x=np.linspace(0.5,1,64)
y=np.linspace(3,2,64)

numerocians=[]
for i in range(0,len(x)):
    for j in range(0,len(y)):
        verts=np.array([[x[0],x[1],x[1],x[0]],[y[0],y[0],y[1],y[1]]]).T
        ax[1].plot([x[0],x[1]],[y[0],y[0]],'-m',linewidth=0.5)
        ax[1].plot([x[1],x[1]],[y[0],y[1]],'-m',linewidth=0.5)
        ax[1].plot([x[1],x[0]],[y[1],y[1]],'-m',linewidth=0.5)
        ax[1].plot([x[0],x[0]],[y[1],y[0]],'-m',linewidth=0.5)
        path = mpath.Path(verts)
        points = np.column_stack([V-m, m])
        points_inside = points[path.contains_points(points)]
        numerocians.append(len(points_inside))
        if len(y)>2:
            y=np.delete(y,(0))
                    
    y=np.linspace(3,2,64)
    if len(x)>2:
        x=np.delete(x,(0))


            
ax[1].xaxis.set_minor_locator(AutoMinorLocator(10))
ax[1].yaxis.set_minor_locator(AutoMinorLocator(10))


ax[1].tick_params(which='major', axis='x', direction='in', length=10, top=True)
ax[1].tick_params(which='major', axis='y', direction='in', length=10, right=True)
ax[1].tick_params(which='minor', axis='x', direction='in', length=6, top=True)
ax[1].tick_params(which='minor', axis='y', direction='in', length=6, right=True)


ax[1].invert_yaxis()
ax[1].set_xlabel ('Color V-I', fontsize=15)
ax[1].set_ylabel ('Magnitud aparente', fontsize=15)
ax[1].grid(which='minor', alpha=0.2)
ax[1].grid(which='major', alpha=0.5)


Xr=[]
Xb=[]
Xc=[]
Xg=[]

for i in range(0,len(numerorojom)):
    xr=(numerorojom[i]+min(numerorojom[i],1)-numerorojos[i])**2/(numerorojom[i]+1)
    Xr.append(xr)
for j in range(0,len(numerocianm)):
    xc=(numerocianm[j]+min(numerocianm[j],1)-numerocians[j])**2/(numerocianm[j]+1)
    Xc.append(xc)
for k in range(0,len(numeroverdem)):
    xg=(numeroverdem[k]+min(numeroverdem[k],1)-numeroverdes[k])**2/(numeroverdem[k]+1)
    Xg.append(xg)
for l in range(0,len(numeroazulm)):
    xb=(numeroazulm[l]+min(numeroazulm[l],1)-numeroazuls[l])**2/(numeroazulm[l]+1)
    Xb.append(xb)
            
n=len(numerocians)+len(numerorojos)+len(numeroverdes)+len(numeroazuls)
XR=sum(Xr)
XB=sum(Xb)
XG=sum(Xg)
XC=sum(Xc)
valores=[]
valores.append(XR)
valores.append(XB)
valores.append(XC)
valores.append(XG)
X=sum(valores)/(n-1)
print(f'El valor de la función de correlación es {X}')
fig.suptitle("Diagramas color magnitud")
plt.savefig('Conteo.png')
plt.show()
   
#-------------------------------------------------------------------------------

#Generate a plot with the resisual from the synthetic cmd
        
age=[0,0.1,0.1,11,11,12,12,13,13]
SFR=[0,0,1,1,0,0,4,4,0]
plt.plot(age,SFR,'-b')
plt.xlabel ('t (Gyr)', fontsize=15)
plt.ylabel ('SFR ($10^{-3}$ M$_{\odot}$yr$^{-1}$kpc$^{-2}$)', fontsize=15)

plt.show
plt.savefig('SFR.png')

V,m=np.loadtxt("cmd_Nalto.txt",skiprows=1,usecols=(6,8),unpack=True)
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))

x=np.linspace(-1,5,60)
y=np.linspace(5,-6,60)
numerom=[]
numeros=[]

for i in range(0,len(x)):
    for j in range(0,len(y)):
        verts=np.array([[x[0],x[1],x[1],x[0]],[y[0],y[0],y[1],y[1]]]).T
        path = mpath.Path(verts)
        points = np.column_stack([V-m, m])
        points_inside = points[path.contains_points(points)]
        numerom.append(len(points_inside))
        if len(y)>2:
            y=np.delete(y,(0))
                    
    y=np.linspace(5,-6,60)
    if len(x)>2:
        x=np.delete(x,(0))

V,m,t=np.loadtxt("cmd_16035.txt",skiprows=1,usecols=(16,18,10),unpack=True)
x=np.linspace(-1,5,60)
Residuox1=[]
Residuoy1=[]
COLOR=[]


for i in range(0,len(x)):
    for j in range(0,len(y)):
        verts=np.array([[x[0],x[1],x[1],x[0]],[y[0],y[0],y[1],y[1]]]).T
        path = mpath.Path(verts)
        points = np.column_stack([V-m, m])
        points_inside = points[path.contains_points(points)]
        numeros.append(len(points_inside))
        xr=((numerom[j]+min(numerom[j],1)-len(points_inside)**2)/(numerom[j]+1))/3600
        if not xr==0:
            Residuox1.append((x[0]+x[1])/2)
            Residuoy1.append((y[0]+y[1])/2)
            t=np.log(-xr)
            COLOR.append(t)

        if len(y)>2:
            y=np.delete(y,(0))
                    
    y=np.linspace(5,-6,60)
    if len(x)>2:
        x=np.delete(x,(0))
#print('El máximo de COLOR es:', max(COLOR))
#print('El mínimo de COLOR es:', min(COLOR))
plt.scatter(Residuox1,Residuoy1,marker='s',c=COLOR,cmap='gray')
ax.invert_yaxis()

plt.clim(-8.1886891244442, 11.811813317492671)
plt.colorbar()


ax.xaxis.set_minor_locator(AutoMinorLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))


ax.tick_params(which='major', axis='x', direction='in', length=10, top=True)
ax.tick_params(which='major', axis='y', direction='in', length=10, right=True)
ax.tick_params(which='minor', axis='x', direction='in', length=6, top=True)
ax.tick_params(which='minor', axis='y', direction='in', length=6, right=True)

ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
plt.title ('Residuos CMD sintético',fontsize = 15)
plt.xlabel ('Color V-I', fontsize=15)
plt.ylabel ('Magnitud aparente', fontsize=15)

plt.show
plt.savefig('Residuossin.png')

time_end = datetime.now()
print(f"Initial time...: {time_ini}")
print(f"Final time.....: {time_end}")
print(f"Excecution time: {time_end-time_ini}")
