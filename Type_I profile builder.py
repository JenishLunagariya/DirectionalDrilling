import math
import matplotlib.pyplot as plt
import numpy as np

print('first, you need to input all required data for calculation')
Ns=float(input('enter tha surface North:'))
Es=float(input('enter the surface East:'))
Nt=float(input('enter the target North:'))
Et=float(input('enter the target East:'))
Vt=float(input('enter tha TVD of target:'))
Vb=float(input('enter the TVD of KOP:'))
Phi=float(input('enter the Build-up rate(Phi):'))

MDb=Vb

#Horizontal Displacement Ht
HT=((Nt-Ns)**2+(Et-Es)**2)
Ht=math.sqrt(HT)

#Target Bearing Beta
BETA=((Et-Es)/(Nt-Ns))
Beta=math.atan(BETA)

#Radius of Curvature R
R=18000/(3.1416*Phi)

# Maximum Inclination angle Alpha

X=((Ht-R)/(Vt-Vb))
x=math.atan(X)

Y=((R*math.cos(x))/(Vt-Vb))
y=math.asin(Y)

Alpha=(x+y)

# At point C
Vc=Vb+R*math.sin(Alpha)
Hc=R*(1-math.cos(Alpha))
MDc=MDb + 100*(Alpha*180/3.1416)/Phi

#At point T

MDt=MDc + (Vt-Vc)/math.cos(Alpha)

# printing the Values
print('\n')
print('Here, all the Distances are in ft')
print('Horizontal Displacement(Ht):', Ht)
print('Target Bearing(Beta):', Beta)
print('Radius of Curvature(R):', R)
print('x(degree):', x * 180 / 3.1416)
print('y(degree):', y * 180 / 3.1416)
print('Angle Alpha(degree):', Alpha * 180 / 3.1416)
print('\n')
print('At point C:-')
print('\tTVD of Point C(Vc):', Vc)
print('\tHorizontal Distance of point C(Hc):', Hc)
print('\tMeasured depth of point C(MDc):', MDc)
print('At point T:-')
print('\tMeasured Depth of target(MDt):', MDt)



'''Below Code is for Plotting it using matplotlib(2D)'''
# Vertical Section
x0=[0,0]
y0=[0,-Vb]
plt.xlabel('Horizontal distance From Well(ft)')
plt.ylabel('Depth(ft)')
plt.plot(x0,y0)

# Build-Up section from KOP=(0,Vb) to (Hc,Vc)
# Equation of circlr: (x-R)^2 + (y-Vb)^2 = R^2

y2=np.linspace(-Vb,-Vc,100)
Y=np.linspace(Vb,Vc,100)
x2=-np.sqrt(R**2-(Y-Vb)**2)+R
plt.plot(x2,y2)

# Tengential Section
y3=[-Vc,-Vt]
x3=[Hc,Ht]
plt.plot(x3,y3)

plt.show()