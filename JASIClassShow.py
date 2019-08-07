# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:19:34 2016

@author: Samuel Sellberg
"""
from  scipy import *
from  pylab import *

class JASI:
    def __init__(self,J,A,S,I,size=10,part=100):
        if not isinstance(J,(int,float)):
            raise TypeError("Inputs must be 'int' or 'float'.")
        if not isinstance(A,(int,float)):
            raise TypeError("Inputs must be 'int' or 'float'.")
        if not isinstance(S,(int,float)):
            raise TypeError("Inputs must be 'int' or 'float'.")
        if not isinstance(I,(int,float)):
            raise TypeError("Inputs must be 'int' or 'float'.")
        if not isinstance(size,(int,float)):
            raise TypeError("Inputs must be 'int' or 'float'.")
        if not isinstance(part,(int,float)):
            raise TypeError("Inputs must be 'int' or 'float'.")
        if not allclose((J+A+S+I),1):
            raise ValueError("J, A, S and I must add up to 1")
        self.J=J
        self.A=A
        self.S=S
        self.I=I
        self.__size__=size
        self.part=part
        self.nJ=(1-self.J)*self.__size__
        self.nA=(1-self.A)*self.__size__
        self.nS=(1-self.S)*self.__size__
        self.nI=(1-self.I)*self.__size__
    def arousal(self):
        return 1-self.I
    def valence(self,neg):
        if not isinstance(neg,(int,float)):
            raise TypeError("Negative barrier must be of type 'int' or 'float'.")
        if neg>1:
            raise ValueError("Negative barrier must smaller than 1.")
        return neg-self.J
    def importance(self):
        if self.S==0 and self.A==0:
            return 0.0
        return (self.S-self.A)/(self.S+self.A)
    def num(self,size=None):
        if size==None:
            size=self.__size__
        self.nJ=(1-self.J)*size
        self.nA=(1-self.A)*size
        self.nS=(1-self.S)*size
        self.nI=(1-self.I)*size
        return 'J = %s, A = %s, S = %s, I = %s, size = %s' %(self.nJ,self.nA,self.nS,self.nI,size)
    def __add__(self,feeling,times=1):
        if not isinstance(feeling,JASI):
            raise TypeError("Can only add forwards a defined feeling.")
    def addJ(self,times):
        if not isinstance(times,int):
            raise TypeError("The number of times must be of type 'int'.")
        P=1-self.J
        for n in range(times):
            self.J+=(1-self.J)/self.part
        a=self.A/P
        s=self.S/P
        i=self.I/P
        self.A=(1-self.J)*a
        self.S=(1-self.J)*s
        self.I=(1-self.J)*i
        if not allclose((self.J+self.A+self.S+self.I),1):
            raise ValueError("Something went wrong when adding percentages.")
        self.nJ=(1-self.J)*self.__size__
        self.nA=(1-self.A)*self.__size__
        self.nS=(1-self.S)*self.__size__
        self.nI=(1-self.I)*self.__size__
        return self.J
    def addA(self,times):
        if not isinstance(times,int):
            raise TypeError("The number of times must be of type 'int'.")
        P=1-self.A
        for n in range(times):
            self.A+=(1-self.A)/self.part
        j=self.J/P
        s=self.S/P
        i=self.I/P
        self.J=(1-self.A)*j
        self.S=(1-self.A)*s
        self.I=(1-self.A)*i
        if not allclose((self.J+self.A+self.S+self.I),1):
            raise ValueError("Something went wrong when adding percentages.")
        self.nJ=(1-self.J)*self.__size__
        self.nA=(1-self.A)*self.__size__
        self.nS=(1-self.S)*self.__size__
        self.nI=(1-self.I)*self.__size__
        return self.A
    def addS(self,times):
        if not isinstance(times,int):
            raise TypeError("The number of times must be of type 'int'.")
        P=1-self.S
        for n in range(times):
            self.S+=(1-self.S)/self.part
        j=self.J/P
        a=self.A/P
        i=self.I/P
        self.J=(1-self.S)*j
        self.A=(1-self.S)*a
        self.I=(1-self.S)*i
        if not allclose((self.J+self.A+self.S+self.I),1):
            raise ValueError("Something went wrong when adding percentages.")
        self.nJ=(1-self.J)*self.__size__
        self.nA=(1-self.A)*self.__size__
        self.nS=(1-self.S)*self.__size__
        self.nI=(1-self.I)*self.__size__
        return self.S
    def addI(self,times):
        if not isinstance(times,int):
            raise TypeError("The number of times must be of type 'int'.")
        P=1-self.I
        for n in range(times):
            self.I+=(1-self.I)/self.part
        j=self.J/P
        a=self.A/P
        s=self.S/P
        self.J=(1-self.I)*j
        self.A=(1-self.I)*a
        self.S=(1-self.I)*s
        if not allclose((self.J+self.A+self.S+self.I),1):
            raise ValueError("Something went wrong when adding percentages.")
        self.nJ=(1-self.J)*self.__size__
        self.nA=(1-self.A)*self.__size__
        self.nS=(1-self.S)*self.__size__
        self.nI=(1-self.I)*self.__size__
        return self.I
    def subJ(self,times):
        if not isinstance(times,int):
            raise TypeError("The number of times must be of type 'int'.")
        P=1-self.J
        for n in range(times):
            self.J-=self.J/self.part
        a=self.A/P
        s=self.S/P
        i=self.I/P
        self.A=(1-self.J)*a
        self.S=(1-self.J)*s
        self.I=(1-self.J)*i
        if not allclose((self.J+self.A+self.S+self.I),1):
            raise ValueError("Something went wrong when adding percentages.")
        self.nJ=(1-self.J)*self.__size__
        self.nA=(1-self.A)*self.__size__
        self.nS=(1-self.S)*self.__size__
        self.nI=(1-self.I)*self.__size__
        return self.J
    def subA(self,times):
        if not isinstance(times,int):
            raise TypeError("The number of times must be of type 'int'.")
        P=1-self.A
        for n in range(times):
            self.A-=self.A/self.part
        j=self.J/P
        s=self.S/P
        i=self.I/P
        self.J=(1-self.A)*j
        self.S=(1-self.A)*s
        self.I=(1-self.A)*i
        if not allclose((self.J+self.A+self.S+self.I),1):
            raise ValueError("Something went wrong when adding percentages.")
        self.nJ=(1-self.J)*self.__size__
        self.nA=(1-self.A)*self.__size__
        self.nS=(1-self.S)*self.__size__
        self.nI=(1-self.I)*self.__size__
        return self.A
    def subS(self,times):
        if not isinstance(times,int):
            raise TypeError("The number of times must be of type 'int'.")
        P=1-self.S
        for n in range(times):
            self.S-=self.S/self.part
        j=self.J/P
        a=self.A/P
        i=self.I/P
        self.J=(1-self.S)*j
        self.A=(1-self.S)*a
        self.I=(1-self.S)*i
        if not allclose((self.J+self.A+self.S+self.I),1):
            raise ValueError("Something went wrong when adding percentages.")
        self.nJ=(1-self.J)*self.__size__
        self.nA=(1-self.A)*self.__size__
        self.nS=(1-self.S)*self.__size__
        self.nI=(1-self.I)*self.__size__
        return self.S
    def subI(self,times):
        if not isinstance(times,int):
            raise TypeError("The number of times must be of type 'int'.")
        P=1-self.I
        for n in range(times):
            self.I-=self.I/self.part
        j=self.J/P
        a=self.A/P
        s=self.S/P
        self.J=(1-self.I)*j
        self.A=(1-self.I)*a
        self.S=(1-self.I)*s
        if not allclose((self.J+self.A+self.S+self.I),1):
            raise ValueError("Something went wrong when adding percentages.")
        self.nJ=(1-self.J)*self.__size__
        self.nA=(1-self.A)*self.__size__
        self.nS=(1-self.S)*self.__size__
        self.nI=(1-self.I)*self.__size__
        return self.I
    def to(self,emotion,times,j=1,a=2,s=3,i=4):
        if not isinstance(emotion,JASI):
            raise TypeError("Current JASI-value needs to advance toward another JASI-value.")
        if not isinstance(times,int):
            raise TypeError("The number of times must be of type 'int'.")
        if not j==1 and not j==2 and not j==3 and not j==4:
            raise ValueError("'j','a','s' and 'i' must be in a range from 1 to 4.")
        if not a==1 and not a==2 and not a==3 and not a==4:
            raise ValueError("'j','a','s' and 'i' must be in a range from 1 to 4.")
        if not s==1 and not s==2 and not s==3 and not s==4:
            raise ValueError("'j','a','s' and 'i' must be in a range from 1 to 4.")
        if not i==1 and not i==2 and not i==3 and not i==4:
            raise ValueError("'j','a','s' and 'i' must be in a range from 1 to 4.")
        if not j+a+s+i==10:
            raise ValueError("'j','a','s' and 'i' must be in a range from 1 to 4.")
        for k in range(times):
            for t in range(1,5):
                if t==j:
                    if self.J<emotion.J:
                        self.addJ(1)
                if t==a:
                    if self.A<emotion.A:
                        self.addA(1)
                if t==s:
                    if self.S<emotion.S:
                        self.addS(1)
                if t==i:
                    if self.I<emotion.I:
                        self.addI(1)
        return self
    def check(self,dic,prio=None):
        if not isinstance(dic,dict):
            raise TypeError("'check' needs a dictionary to check.")
        keys=list(dic.keys())
        match=[]
        priolist=[]
        for i in range(len(keys)):
            if keys[i].check(self)==True:
                match.append(keys[i])
                priolist.append(keys[i].prio)
        if match==[]:
            raise Exception("No fields were found.")
        if prio==None:
            prio=max(priolist)
        if not priolist.count(prio)==1:
            raise Exception("More than one fields occupy the same volume and priority.")
        ind=priolist.index(prio)
        return dic[match[ind]]
    def visualize(self,siderot=-60,toprot=30,slide=-0.45,straightup=False):
        if not isinstance(siderot,(int,float)) or not isinstance(toprot,(int,float)):
            raise TypeError("Degrees must be 'int' or 'float'.")
        if not isinstance(slide,(int,float)):
            raise TypeError("Slide must be 'int' or 'float'.")
        if not -360<siderot<360 or not -360<siderot<360:
            raise ValueError("Degrees must be in interval -360 < x < 360.")
        if not -1<=slide<=1:
            raise ValueError("Slide must be in interval -1 < x < 1.")
        if straightup==True:
            siderot,toprot,slide=(90,90,1)
        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt
        fig=plt.figure()
        ax=fig.gca(projection='3d')
        ax._axis3don=False
        ax.view_init(elev=toprot,azim=siderot)
        ax.set_aspect("equal")
        a=slide
        b=(1/3)*(3-(sqrt(3)*sqrt((a-3)**2)))
        c=(1/3)*(3-(sqrt(3)*sqrt((a+3)**2)))
        L=(2*sqrt(a**3+3))/(sqrt(3))
        d=1-(L*sqrt(2/3))
        i=(b+c+1)/3
        j=a/3
        ax.plot3D((b,1,c,i,b,c),(-1,a,1,j,-1,1),(1,1,1,d,1,1),color="black")
        ax.plot3D((1,i),(a,j),(1,d),color="black")
        ax.plot3D((b,b),(-1,-1),(1,1),marker='o',color="g")
        ax.text(b,-1,1.15,"J",color='g')
        ax.plot3D((c,c),(1,1),(1,1),marker='o',color="r")
        ax.text(c,1,1.1,"A",color='r')
        ax.plot3D((1,1),(a,a),(1,1),marker='o',color="b")
        ax.text(1,a,1.1,"S",color='b')
        ax.plot3D((i,i),(j,j),(d,d),marker='o',color="white")
        ax.text(i,j,d-0.25,"I",color='gray')
        x=self.J*b+self.A*c+self.S+self.I*i
        y=-self.J+self.A+self.S*a+self.I*j
        z=1-self.I*(L*sqrt(2/3))   # Same as (self.J+self.A+self.S+self.I*d)
        ax.plot3D((x,x),(y,y),(z,z),marker='o',color="black")
        ax.text2D(0.05,1,"J.A.S.I.-modula",transform=ax.transAxes)
    def __repr__(self):
        return 'J = %s, A = %s, S = %s, I = %s' %(self.J,self.A,self.S,self.I)

class JASIfield:
    def __init__(self,j,J,a,A,s,S,i,I,imp=None,IMP=None,prio=0,colour='gray'):
        if not isinstance(j,(int,float)) or not isinstance(J,(int,float)) or not isinstance(a,(int,float)) or not isinstance(A,(int,float)) or not isinstance(s,(int,float)) or not isinstance(S,(int,float)) or not isinstance(i,(int,float)) or not isinstance(I,(int,float)):
            raise TypeError("JASI-values must be 'int' or 'float'.")
        if not isinstance(prio,int):
            raise TypeError("prio must be of type 'int'.")
        if not isinstance(colour,str):
            raise TypeError("colour must be of type 'str'.")
        if j>1 or J>1 or a>1 or A>1 or s>1 or S>1 or i>1 or I>1:
            raise ValueError("JASI-values can't be greater than 1.")
        if j>J or a>A or s>S or i>I:
            raise ValueError("The lowercase JASI-value must be smaller that the uppercase JASI-values.")
        if not imp==None:
            if not isinstance(imp,(int,float)) and isinstance(IMP,(int,float)):
                raise TypeError("None or both imp-arguments must be given as 'int' or 'float'.")
            elif not -1<=imp<=1 or not -1<=IMP<=1:
                raise ValueError("The imp-arguments must be in interval -1 < x < 1.")
            elif imp>IMP:
                raise ValueError("'imp' must be smaller than 'IMP'.")
            self.imp=imp
            self.IMP=IMP
        else:
            self.imp=None
        self.j=j
        self.J=J
        self.a=a
        self.A=A
        self.s=s
        self.S=S
        self.i=i
        self.I=I
        self.prio=prio
        self.colour=colour
        if not (self.j+self.a+self.s+self.i)<1<=(self.J+self.A+self.S+self.I):
            raise Exception("The given field does not exist.")
    def change(self,j=None,J=None,a=None,A=None,s=None,S=None,i=None,I=None,prio=None,colour=None,imp=None,IMP=None):
        if j==None:
            j=self.j
        if J==None:
            J=self.J
        if a==None:
            a=self.a
        if A==None:
            A=self.A
        if s==None:
            s=self.s
        if S==None:
            S=self.S
        if i==None:
            i=self.i
        if I==None:
            I=self.I
        if prio==None:
            prio=self.prio
        if colour==None:
            colour=self.colour
        if imp==None:
            if not self.imp==None:
                imp=self.imp
        if IMP==None:
            if not self.imp==None:
                IMP=self.IMP
        return self.__init__(j,J,a,A,s,S,i,I,imp,IMP,prio,colour)
    def organize(self,dictionary,name):
        if not isinstance(dictionary,dict):
            raise TypeError("Can only add to a dictionary.")
        if not isinstance(name,str):
            raise TypeError("name must be of type 'str'.")
        dictionary[self]=name
    def check(self,emotion,give=False,info=False):
        if not isinstance(emotion,JASI):
            raise TypeError("Can only check for a 'JASI' within 'JASIfield'.")
        if not self.imp==None:
            if self.imp<emotion.importance()<=self.IMP:
                importance=True
        else:
            importance=True
        if self.j<emotion.J<=self.J and self.a<emotion.A<=self.A and self.s<emotion.S<=self.S and self.i<emotion.I<=self.I and importance==True:
            if give==True:
                return self
            elif info==True:
                return True, '%s<%s<=%s, %s<%s<=%s, %s<%s<=%s, %s<%s<=%s, Prio = %s' %(self.j,emotion.J,self.J,self.a,emotion.A,self.A,self.s,emotion.S,self.S,self.i,emotion.I,self.I,self.prio)
            else:
                return True
        else:
            return False
    def visualize(self,siderot=-60,toprot=30,slide=-0.45,straightup=False,check=None):
        if not isinstance(siderot,(int,float)) or not isinstance(toprot,(int,float)):
            raise TypeError("Degrees must be 'int' or 'float'.")
        if not isinstance(slide,(int,float)):
            raise TypeError("Slide must be 'int' or 'float'.")
        if not -360<siderot<360 or not -360<siderot<360:
            raise ValueError("Degrees must be in interval -360 < x < 360.")
        if not -1<=slide<=1:
            raise ValueError("Slide must be in interval -1 < x < 1.")
        if straightup==True:
            siderot,toprot,slide=(90,90,1)
        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt
        fig=plt.figure()
        ax=fig.gca(projection='3d')
        ax._axis3don=False
        ax.view_init(elev=toprot,azim=siderot)
        ax.set_aspect("equal")
        a=slide
        b=(1/3)*(3-(sqrt(3)*sqrt((a-3)**2)))
        c=(1/3)*(3-(sqrt(3)*sqrt((a+3)**2)))
        L=(2*sqrt(a**3+3))/(sqrt(3))
        d=1-(L*sqrt(2/3))
        i=(b+c+1)/3
        j=a/3
        ax.plot3D((b,1,c,i,b,c),(-1,a,1,j,-1,1),(1,1,1,d,1,1),color="black")
        ax.plot3D((1,i),(a,j),(1,d),color="black")
        ax.plot3D((b,b),(-1,-1),(1,1),marker='o',color="magenta")
        ax.text(b,-1,1.15,"J",color='magenta')
        ax.plot3D((c,c),(1,1),(1,1),marker='o',color="cyan")
        ax.text(c,1,1.1,"A",color='cyan')
        ax.plot3D((1,1),(a,a),(1,1),marker='o',color="yellow")
        ax.text(1,a,1.1,"S",color='yellow')
        ax.plot3D((i,i),(j,j),(d,d),marker='o',color="white")
        ax.text(i,j,d-0.25,"I",color='gray')
        arg=[self.j,self.J,self.a,self.A,self.s,self.S,self.i,self.I]
        sequence=[(0,2,4,6,7),(0,2,5,6,7),(0,2,6,4,5),(0,2,7,4,5),(0,3,4,6,7),(0,3,5,6,7),(0,3,6,4,5),(0,3,7,4,5),(0,4,6,2,3),(0,4,7,2,3),(0,5,6,2,3),(0,5,7,2,3),(1,2,4,6,7),(1,2,5,6,7),(1,2,6,4,5),(1,2,7,4,5),
                  (1,3,4,6,7),(1,3,5,6,7),(1,3,6,4,5),(1,3,7,4,5),(1,4,6,2,3),(1,4,7,2,3),(1,5,6,2,3),(1,5,7,2,3),(2,4,6,0,1),(2,4,7,0,1),(2,5,6,0,1),(2,5,7,0,1),(3,4,6,0,1),(3,4,7,0,1),(3,5,6,0,1),(3,5,7,0,1)]
        frame=[]
        coord=[]
        for A,B,C,low,high in sequence:
            mid=1-(arg[A]+arg[B]+arg[C])
            if arg[low]<=mid<=arg[high]:
                if high==1:
                    frame.append((mid,arg[A],arg[B],arg[C]))
                elif high==3:
                    frame.append((arg[A],mid,arg[B],arg[C]))
                elif high==5:
                    frame.append((arg[A],arg[B],mid,arg[C]))
                elif high==7:
                    frame.append((arg[A],arg[B],arg[C],mid))
        if not self.imp==None:
            impframe=[]
            for m in range(len(frame)):
                tes=JASI(frame[m][0],frame[m][1],frame[m][2],frame[m][3])
                if self.imp<=tes.importance()<=self.IMP:
                    impframe.append(frame[m])
                elif self.imp>tes.importance():
                    for n in range(len(frame)):
                        if not m==n:
                            val=frame[m]
                            nes=JASI(frame[n][0],frame[n][1],frame[n][2],frame[n][3])
                            if self.imp<=nes.importance():
                                if val[0]==frame[n][0] and val[1]==frame[n][1]:
                                    Jimp,Aimp=val[0],val[1]
                                    Simp=-(Aimp*(self.imp+1))/(self.imp-1)
                                    Iimp=1-(Jimp+Aimp+Simp)
                                    impframe.append((Jimp,Aimp,Simp,Iimp,0))
                                if val[0]==frame[n][0] and val[2]==frame[n][2]:
                                    Jimp,Simp=val[0],val[2]
                                    Aimp=(Simp-self.imp*Simp)/(self.imp+1)
                                    Iimp=1-(Jimp+Aimp+Simp)
                                    impframe.append((Jimp,Aimp,Simp,Iimp,0))
                                if val[0]==frame[n][0] and val[3]==frame[n][3]:
                                    Jimp,Iimp=val[0],val[3]
                                    Aimp=((self.imp-1)*(Iimp+Jimp-1))/2
                                    Simp=1-(Jimp+Aimp+Iimp)
                                    impframe.append((Jimp,Aimp,Simp,Iimp,0))
                                if val[1]==frame[n][1] and val[3]==frame[n][3]:
                                    Aimp,Iimp=val[1],val[3]
                                    Jimp=(2*Aimp-Iimp*self.imp+Iimp+self.imp-1)/(self.imp-1)
                                    Simp=1-(Jimp+Aimp+Iimp)
                                    impframe.append((Jimp,Aimp,Simp,Iimp,0))
                                if val[2]==frame[n][2] and val[3]==frame[n][3]:
                                    Simp,Iimp=val[2],val[3]
                                    Jimp=(-Iimp*(self.imp+1)+self.imp-2*Simp+1)/(self.imp+1)
                                    Aimp=1-(Jimp+Simp+Iimp)
                                    impframe.append((Jimp,Aimp,Simp,Iimp,0))
                elif self.IMP<tes.importance():
                    for n in range(len(frame)):
                        if not m==n:
                            val=frame[m]
                            nes=JASI(frame[n][0],frame[n][1],frame[n][2],frame[n][3])
                            if self.IMP>=nes.importance():
                                if val[0]==frame[n][0] and val[1]==frame[n][1]:
                                    Jimp,Aimp=val[0],val[1]
                                    Simp=-(Aimp*(self.IMP+1))/(self.IMP-1)
                                    Iimp=1-(Jimp+Aimp+Simp)
                                    impframe.append((Jimp,Aimp,Simp,Iimp,1))
                                if val[0]==frame[n][0] and val[2]==frame[n][2]:
                                    Jimp,Simp=val[0],val[2]
                                    Aimp=(Simp-self.IMP*Simp)/(self.IMP+1)
                                    Iimp=1-(Jimp+Aimp+Simp)
                                    impframe.append((Jimp,Aimp,Simp,Iimp,1))
                                if val[0]==frame[n][0] and val[3]==frame[n][3]:
                                    Jimp,Iimp=val[0],val[3]
                                    Aimp=((self.IMP-1)*(Iimp+Jimp-1))/2
                                    Simp=1-(Jimp+Aimp+Iimp)
                                    impframe.append((Jimp,Aimp,Simp,Iimp,1))
                                if val[1]==frame[n][1] and val[3]==frame[n][3]:
                                    Aimp,Iimp=val[1],val[3]
                                    Jimp=(2*Aimp-Iimp*self.IMP+Iimp+self.IMP-1)/(self.IMP-1)
                                    Simp=1-(Jimp+Aimp+Iimp)
                                    impframe.append((Jimp,Aimp,Simp,Iimp,1))
                                if val[2]==frame[n][2] and val[3]==frame[n][3]:
                                    Simp,Iimp=val[2],val[3]
                                    Jimp=(-Iimp*(self.IMP+1)+self.IMP-2*Simp+1)/(self.IMP+1)
                                    Aimp=1-(Jimp+Simp+Iimp)
                                    impframe.append((Jimp,Aimp,Simp,Iimp,1))
            frame=impframe
        for k in range(len(frame)):
            x=frame[k][0]*b+frame[k][1]*c+frame[k][2]+frame[k][3]*i
            y=-frame[k][0]+frame[k][1]+frame[k][2]*a+frame[k][3]*j
            z=1-frame[k][3]*(L*sqrt(2/3))
            coord.append((x,y,z))
        for t in range(len(frame)):
            for s in range(len(frame)):
                if not t==s:
                    val=frame[t]
                    if val[0]==frame[s][0] and val[1]==frame[s][1] or val[0]==frame[s][0] and val[2]==frame[s][2] or val[0]==frame[s][0] and val[3]==frame[s][3] or val[1]==frame[s][1] and val[2]==frame[s][2] or val[1]==frame[s][1] and val[3]==frame[s][3] or val[2]==frame[s][2] and val[3]==frame[s][3]:
                        ax.plot3D((coord[t][0],coord[s][0]),(coord[t][1],coord[s][1]),(coord[t][2],coord[s][2]),color=self.colour)
                    elif len(val)==5 and len(frame[s])==5:
                        if val[4]==frame[s][4] and val[0]==frame[s][0] or val[4]==frame[s][4] and val[1]==frame[s][1] or val[4]==frame[s][4] and val[2]==frame[s][2] or val[4]==frame[s][4] and val[3]==frame[s][3]:
                            ax.plot3D((coord[t][0],coord[s][0]),(coord[t][1],coord[s][1]),(coord[t][2],coord[s][2]),color=self.colour)
        if not check==None:
            if not isinstance(check,JASI):
                raise TypeError("Can only check for a 'JASI' within 'JASIfield'.")
            x=check.J*b+check.A*c+check.S+check.I*i
            y=-check.J+check.A+check.S*a+check.I*j
            z=1-check.I*(L*sqrt(2/3))
            ax.plot3D((x,x),(y,y),(z,z),marker='o',color="black")
            ax.text2D(0.05,1,"J.A.S.I.-modula",transform=ax.transAxes)
            return self.check(check)
        ax.text2D(0.05,1,"J.A.S.I.-modula",transform=ax.transAxes)
    def __repr__(self):
        if not self.imp==None:
            return '%s<J<=%s, %s<A<=%s, %s<S<=%s, %s<I<=%s, %s<Importance<=%s, Prio = %s' %(self.j,self.J,self.a,self.A,self.s,self.S,self.i,self.I,self.imp,self.IMP,self.prio)
        else:
            return '%s<J<=%s, %s<A<=%s, %s<S<=%s, %s<I<=%s, Prio = %s' %(self.j,self.J,self.a,self.A,self.s,self.S,self.i,self.I,self.prio)
        




emotions={1:'Happy',2:'Sad',3:'Angry',4:'Melancholic',5:'Fearsome',6:'Passionated',7:'Calm'}
show=JASI(.4,.2,.05,.35)
showto=JASI(.15,.1,.3,.45)
emotion=JASI(.12,.10,.14,.64,10)
emotion2=JASI(.69,.10,.14,.07)
emotion3=JASI(.25,.25,.25,.25)
happy=JASIfield(0.6,1,0,0.8,0,0.8,0,0.8,colour="#5201FA")
extreme=JASIfield(0.2,0.5,0.1,0.2,0,0.3,0.2,1,colour="crimson")
angry=JASIfield(0,0.8,0.61,1,0,0.8,0,0.8,colour="#00E86E")
prio1=JASIfield(0.1,0.67,0.15,0.66,0.03,0.59,0.07,0.42,colour="#374018")
prio2=JASIfield(0.2,0.57,0.15,0.36,0.03,0.19,0.2,0.42,colour="#7A8E35")
joy=JASIfield(0.2,1,0,0.8,0,0.8,0,0.8,colour="greenyellow")
tester=JASIfield(0.25,0.5,0,0.25,0,0.25,0,1,colour="turquoise")