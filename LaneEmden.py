#!/usr/bin/env python
# coding: utf-8

# In[38]:


get_ipython().run_line_magic('pylab', 'inline')
import seaborn as sb
sb.set_palette("magma",7)


# In[55]:


dxi=0.01
N=1000 #We'll calculate from xi=0 to xi=0.01*1000=10

for n in range (7): #From n=0 to n=6
    
    xi=0.001 #Initial xi is not set to exactly zero to avoid singularity
    theta=1.0 #Initial theta at xi=0
    f=0.0
    
    s1=[] #theta's solution values will be saved in this array
    s2=[] #xi's values will be saved in this array
    
    #instead of integrating we'll do a summation with a step size=dxi=0.01
    
    for i in range (N):
        f += -xi**2*theta**(n)*dxi #First integral
        theta += f/xi**2*dxi #Second integral
        xi+=dxi #increasing xi by dxi with each iteration
        s1.append(theta)
        s2.append(xi)
        plot(s2,s1) #plotting

xlim(1,10)
ylim(-1,1)
axhline(y=0.0,c="black")
savefig('desktop\laneemden.png')
show()


# In[ ]:




