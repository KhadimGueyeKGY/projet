# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:09:47 2022

@author: Administrator
"""

import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
import matplotlib
import colorsys
ax = plt.subplot()

import pandas as pd
import xlrd
import numpy as np 
# plt.figure(figsize=(20,10), dpi=100)
xls = pd.ExcelFile('C:/Users/khgueye/OneDrive - Medical Research Council IRESSEF/Iressef_work/excel_data_base/Tableau resume des differents sequences de chaque batch 25072022.xlsx')
l  = xls.sheet_names
f = pd.read_excel(xls, l[0],header = None)
f = f.fillna(-1)
c= list(f[6])
del c[0]
a= list(f[7])
dp = [str(i).replace('-', '/') for i in list(f[12])]
ds = [str(i).replace('-', '/') for i in list(f[13])]
del a[0]
del dp[0]
del ds[0]
aa = [x for x in list(set(a)) if pd.isnull(x) == False]
#del aa [aa.index(-1)]
del aa [aa.index("None")]
aa.sort()

cc = [x for x in list(set(c)) if pd.isnull(x) == False]
del cc [cc.index("None")]
#del cc [cc.index(-1)]
#del cc [cc.index("Clade")]
mois_an = ["Dec-2020","Jan-2021","Feb-2021","March-2021","April-2021","May-2021","June-2021","July-2021","Aug-2021","Sept-2021","Oct-2021","Nov-2021","Dec-2021","Jan-2022","Feb-2022","March-2022","April-2022","May-2022","June-2021","July-2021"]


###############################evolution des clades CUMULE fig1cc

'''
matrix = []
cc.sort()
def fonc(an,mois):
    x = []
    for j in range(len(cc)):
        e = 0 
        for i in range(len(dp)) :
            if dp[i] == "/1"  :
                pass
            else :
                m = dp[i].split('/')
                if int(m[0]) == int(an):
                    if int(m[1]) == int(mois):
                            #print(m)
                            if c[i] == cc[j] :
                                e += 1
                        
        x.append(e)
    y = []
    y.append(float(x[0]*100/sum(x)))
    for i in range(1,len(x)):
        y.append(float(x[i]*100/sum(x))+y[i-1])
    matrix.append(y)

fonc("2020",'06')
fonc("2020",'08')
fonc("2020",'10')
fonc("2020",'11')
fonc("2020",'12')
fonc("2021",'01')
fonc("2021",'02')
fonc("2021",'03')
fonc("2021",'04')
fonc("2021",'05')
fonc("2021",'06')
fonc("2021",'07')
fonc("2021",'08')
fonc("2021",'09')
fonc("2021",'10')
fonc("2021",'11')
fonc("2021",'12')
fonc("2022",'01')
fonc("2022",'02')
fonc("2022",'03')
fonc("2022",'04')
fonc("2022",'05')
fonc("2022",'06')
fonc("2022","07")

mat = []
for i in range(len(matrix[0])):
    l = []
    for j in range(len(matrix)):
        l.append(matrix[j][i])
    mat.append(l)

#col= ["#76EEC6","#66CD00","#8B7355","cyan","#8A360F","#8B8378","#6F4242","darkgray","#B5A642","blue","#9F9F5F","#32CD99","#70DB93","#DBDB70","Turquoise","Khaki","#00FF7F","#4F2F4F","#00009C","#4D4DFF","#3299CC","navy","#9932CD","#9F5F9F","#8F8FBD","#38B0DE","#CDCDCD","#ADEAEA","#4E2F2F","#5C3317","#A62A2A","#A68064","#EAADEA","limegreen","#DB7093","#CC3299","#FF2400","#FFFF00","#D98719","black","#D19275","#EAEAAE","#D9D9F3","#2A4F2F","#e6e8ff","#D9A9F3","#F08080","#FFF0F5","#E0FFFF","#68838B","#ADD8E6"]
import matplotlib
import colorsys
col = list(matplotlib.colors.cnames.keys())
del col[0]
del col[3]
del col[3]
del col[3]
del col[15]
del col[42]
del col[45]
del col[44]
del col[14]

col[0] ="red"
col[1] ="#66CD00"
col[2] ="darkgray"
col[8] ="aqua"
col[12] ="yellow"
col[14] ="orange"
mois_an = ["June-2020","Aug-2020","Oct-2020","Nov-2020","Dec-2020","Jan-2021","Feb-2021","March-2021","April-2021","May-2021","June-2021","July-2021","Aug-2021","Sept-2021","Oct-2021","Nov-2021","Dec-2021","Jan-2022","Feb-2022","March-2022","April-2022","May-2022","June-2022","July-2022"]

for i in range(len(mois_an)-1, -1,-1):
    plt.axvline(x=i,color='gray',linestyle='--')
    
for i in range(len(cc)-1, -1,-1):
    plt.fill_between(range(len(mat[i])),mat[i],color = col[i],label =cc[i],alpha=1)


plt.legend(loc='upper left', bbox_to_anchor=(1.11,1),fontsize = 10, ncol=2, fancybox=True, shadow=True)
plt.text(24,105,'Nextstrain (Clades)',color = 'black',fontsize=12)
plt.xlim(0,20)
plt.ylim(0,100)
plt.xticks(range(len(mois_an)),mois_an,rotation = 90,fontsize=12)
plt.yticks(fontsize=16)
plt.ylabel("Percentage \n",fontsize=15)
plt.xlabel("\nEvolution over time",fontsize=15)
plt.text(1,60,'20A',color = 'black',fontsize=12)
plt.text(4.5,70,'20B',color = 'white',fontsize=12)
plt.text(6.8,85,'20I\n(Alpha)',color = 'black',fontsize=12)
plt.text(11,40,'21A \n(Delta)',color = 'black',fontsize=12)
plt.text(11,85,'21J \n(Delta)',color = 'black',fontsize=12)
plt.text(14,46,'21I \n(Delta)',color = 'black',fontsize=12)
plt.text(16,60,'21K \n(Omicron)',color = 'black',fontsize=12)
plt.text(18,75,'21L \n(Omicron)',color = 'black',fontsize=12)
plt.text(20,90,'recombinant',color = 'black',fontsize=12)
# plt.title("Distribution des différents variants d'intérêt par mois identifiés à IRESSEF\n au cours de la pandemis du SARS-Cov-2 au Sénégal\n\n",fontsize = 18)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

'''
###############################evolution des clades NON CUMULE fig3cnc

'''

matrix = []
cc.sort()
def fonc(an,mois):
    x = []
    for j in range(len(cc)):
        e = 0 
        for i in range(len(dp)) :
            if dp[i] == "/1"  :
                pass
            else :
                m = dp[i].split('/')
                if int(m[0]) == int(an):
                    if int(m[1]) == int(mois):
                            #print(m)
                            if c[i] == cc[j] :
                                e += 1
                        
        x.append(e)
    y = []
    y.append(float(x[0]*100/sum(x)))
    for i in range(1,len(x)):
        y.append(float(x[i]*100/sum(x)))
    matrix.append(y)

fonc("2020",'06')
fonc("2020",'08')
fonc("2020",'10')
fonc("2020",'11')
fonc("2020",'12')
fonc("2021",'01')
fonc("2021",'02')
fonc("2021",'03')
fonc("2021",'04')
fonc("2021",'05')
fonc("2021",'06')
fonc("2021",'07')
fonc("2021",'08')
fonc("2021",'09')
fonc("2021",'10')
fonc("2021",'11')
fonc("2021",'12')
fonc("2022",'01')
fonc("2022",'02')
fonc("2022",'03')
fonc("2022",'04')
fonc("2022",'05')
fonc("2022",'06')
fonc("2022",'07')
mat = []
for i in range(len(matrix[0])):
    l = []
    for j in range(len(matrix)):
        l.append(matrix[j][i])
    mat.append(l)

#col= ["#76EEC6","#66CD00","#8B7355","cyan","#8A360F","#8B8378","#6F4242","darkgray","#B5A642","blue","#9F9F5F","#32CD99","#70DB93","#DBDB70","Turquoise","Khaki","#00FF7F","#4F2F4F","#00009C","#4D4DFF","#3299CC","navy","#9932CD","#9F5F9F","#8F8FBD","#38B0DE","#CDCDCD","#ADEAEA","#4E2F2F","#5C3317","#A62A2A","#A68064","#EAADEA","limegreen","#DB7093","#CC3299","#FF2400","#FFFF00","#D98719","black","#D19275","#EAEAAE","#D9D9F3","#2A4F2F","#e6e8ff","#D9A9F3","#F08080","#FFF0F5","#E0FFFF","#68838B","#ADD8E6"]
import matplotlib
import colorsys
col = list(matplotlib.colors.cnames.keys())
del col[0]
del col[3]
del col[3]
del col[3]
del col[15]
del col[42]
del col[45]
del col[44]
del col[14]

col[0] ="red"
col[1] ="#66CD00"
col[2] ="darkgray"
col[8] ="aqua"
col[12] ="yellow"
col[14] ="orange"
col[cc.index("22C (Omicron)")]= "cyan"
mois_an = ["June-2020","Aug-2020","Oct-2020","Nov-2020","Dec-2020","Jan-2021","Feb-2021","March-2021","April-2021","May-2021","June-2021","July-2021","Aug-2021","Sept-2021","Oct-2021","Nov-2021","Dec-2021","Jan-2022","Feb-2022","March-2022","April-2022","May-2022","June-2022","July-2022"]

for i in range(len(mois_an)-1, -1,-1):
    plt.axvline(x=i,color='gray',linestyle='--')
    
for i in range(len(cc)-1, -1,-1):
    plt.fill_between(range(len(mat[i])),mat[i],color = col[i],label =cc[i],alpha=1)


plt.legend(loc='upper left', bbox_to_anchor=(1.11,1),fontsize = 10, ncol=2, fancybox=True, shadow=True)
plt.text(24,105,'Nextstrain (Clades)',color = 'black',fontsize=12)
plt.xlim(0,20)
plt.ylim(0,100)
plt.xticks(range(len(mois_an)),mois_an,rotation = 90,fontsize=12)
plt.yticks(fontsize=16)
plt.ylabel("Percentage \n",fontsize=15)
plt.xlabel("\nEvolution over time",fontsize=15)
plt.text(1,60,'20A',color = 'black',fontsize=12)
plt.text(4.5,70,'20B',color = 'white',fontsize=12)
plt.text(6.8,60,'20I\n(Alpha)',color = 'black',fontsize=12)
plt.text(11,40,'21A \n(Delta)',color = 'black',fontsize=12)
plt.text(14,46,'21I \n(Delta)',color = 'black',fontsize=12)
# plt.text(14,46,'21J \n(Delta)',color = 'black',fontsize=12)
plt.text(16,60,'21K \n(Omicron)',color = 'black',fontsize=12)
plt.text(18,75,'21L \n(Omicron)',color = 'black',fontsize=12)
# plt.text(20,90,'recombinant',color = 'black',fontsize=12)
# plt.title("Distribution des différents variants d'intérêt par mois identifiés à IRESSEF\n au cours de la pandemis du SARS-Cov-2 au Sénégal\n\n",fontsize = 18)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

'''

############################### evolution des linages CUMULE fig2lc
'''
matrix = []
def fonc(an,mois):
    x = []
    for j in range(len(aa)):
        e = 0 
        for i in range(len(dp)) :
            if dp[i] == "/1"  :
                pass
            elif str(dp[i]).find(an) != -1 :
                m = dp[i].split('/')
                print(m)
                if m[1] == mois:
                    if a[i] == aa[j] :
                        e += 1
        x.append(e)
    y = []
    y.append(float(x[0]*100/sum(x)))
    for i in range(1,len(x)):
        y.append(float(x[i]*100/sum(x))+y[i-1])
    matrix.append(y)

fonc("2020",'06')
fonc("2020",'08')
fonc("2020",'10')
fonc("2020",'11')
fonc("2020",'12')
fonc("2021",'01')
fonc("2021",'02')
fonc("2021",'03')
fonc("2021",'04')
fonc("2021",'05')
fonc("2021",'06')
fonc("2021",'07')
fonc("2021",'08')
fonc("2021",'09')
fonc("2021",'10')
fonc("2021",'11')
fonc("2021",'12')
fonc("2022",'01')
fonc("2022",'02')
fonc("2022",'03')
fonc("2022",'04')
fonc("2022",'05')
fonc("2022",'06')
fonc("2022",'07')
mat = []
for i in range(len(matrix[0])):
    l = []
    for j in range(len(matrix)):
        l.append(matrix[j][i])
    mat.append(l)
# col= ["Navy","Purple","DodgerBlue","BlueViolet","SkyBlue","DarkKhaki","Fuchsia","Turquoise","Khaki","Orange","cyan","DarkTurquoise","Yellow","Teal","Olive","PaleVioletRed","Pink","Maroon","Coral","black","YellowGreen","Indigo","Lavender","PeachPuff","PowderBlue","blue","#FF2400","#FFFF00","#D98719","#D19275","#EAEAAE","#D9D9F3","#e6e8ff","#4B0082"]
#col= ["#76EEC6","#8A360F","#8B7355","cyan","#0000CD","#66CD00","#8B8378","#6F4242","darkgray","#B5A642","blue","#9F9F5F","#32CD99","#70DB93","#DBDB70","Turquoise","Khaki","#00FF7F","#4F2F4F","#00009C","#4D4DFF","#3299CC","navy","#9932CD","#9F5F9F","#8F8FBD","#38B0DE","#CDCDCD","#ADEAEA","#4E2F2F","#5C3317","#A62A2A","#A68064","#EAADEA","limegreen","#DB7093","#CC3299","#FF2400","#FFFF00","#D98719","black","#D19275","#EAEAAE","#D9D9F3","#2A4F2F","#e6e8ff","#D9A9F3","#F08080","#FFF0F5","#E0FFFF","#68838B","#ADD8E6"]
import matplotlib
import colorsys
col = list(matplotlib.colors.cnames.keys())
del col[0]
del col[3]
del col[3]
del col[15]
del col[42]
del col[45]
del col[44]
col[aa.index("BA.5")]= "red"
col[aa.index("BA.4")]= "yellow"
for i in range(len(aa)-1, -1,-1):
    plt.fill_between(range(len(mat[i])),mat[i],color = col[i],label =aa[i],alpha=1)
    plt.axvline(x=i,color='gray',linestyle='--')

# mois_an = ["June-2020","Aug-2020","Oct-2020","Nov-2020","Dec-2020","Jan-2021","Feb-2021","March-2021","April-2021","May-2021","June-2021","July-2021","Aug-2021","Sept-2021","Oct-2021","Nov-2021","Dec-2021","Jan-2022","Feb-2022","March-2022"]
mois_an = ["June-2020","Aug-2020","Oct-2020","Nov-2020","Dec-2020","Jan-2021","Feb-2021","March-2021","April-2021","May-2021","June-2021","July-2021","Aug-2021","Sept-2021","Oct-2021","Nov-2021","Dec-2021","Jan-2022","Feb-2022","March-2022","April-2022","May-2022","June-2022","July-2022"]


plt.legend(loc='upper left', bbox_to_anchor=(1.1,1),fontsize = 10, ncol=4, fancybox=True, shadow=True)
plt.text(26,105,'Lineages',color = 'black',fontsize=12)
plt.xlim(0,len(mois_an)-1)
plt.ylim(0,100)
plt.xticks(range(len(mois_an)),mois_an,rotation = 90,fontsize=12)
plt.yticks(fontsize=16)
plt.ylabel("Percentage \n",fontsize=15)
plt.xlabel("\nEvolution over time",fontsize=15)
plt.text(4.2,48,'B.1.1.420',color = 'white',fontsize=12)
plt.text(5.2,20,'B.1',color = 'black',fontsize=12)
plt.text(9,70,'Eta',color = 'black',fontsize=12)
plt.text(9.2,85,'Delta \n(B.1.617.2)',color = 'black',fontsize=12)
plt.text(11,10,'AY.36',color = 'black',fontsize=12)
plt.text(6.2,60,'Alpha',color = 'black',fontsize=12)
#plt.text(6.8,74,'AY.4',color = 'black',fontsize=12)
plt.text(12.9,60,'AY.4',color = 'black',fontsize=12)
plt.text(4.3,85,'B.1.416',color = 'black',fontsize=12)
plt.text(14.5,30,'AY.26',color = 'black',fontsize=10)
#plt.text(11.2,55,'AY.87',color = 'black',fontsize=12)
plt.text(15.2,80,'Omicron',color = 'black',fontsize=12)
#plt.text(1.7,95,'B',color = 'black',fontsize=10)
#plt.text(3.2,70,'A.27',color = 'white',fontsize=10)
#plt.text(10.6,8,'AY.26',color = 'black',fontsize=10)

# plt.title("Distribution des différents variants d'intérêt par mois identifiés à IRESSEF\n au cours de la pandemis du SARS-Cov-2 au Sénégal\n\n",fontsize = 18)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# plt.savefig('C:/Users/Administrator/OneDrive - Medical Research Council IRESSEF/Iressef_work/projet/projet2/figure/evolution_of_variant_04102021.pdf',dpi=1)

'''



#################### evolution de chaque lineage NON CUMULE fig4lnc 

'''

matrix = []
def fonc(an,mois):
    x = []
    for j in range(len(aa)):
        e = 0 
        for i in range(len(dp)) :
            if dp[i] == "/1"  :
                pass
            elif str(dp[i]).find(an) != -1 :
                m = dp[i].split('/')
                print(m)
                if m[1] == mois:
                    if a[i] == aa[j] :
                        e += 1
        x.append(e)
    y = []
    y.append(float(x[0]*100/sum(x)))
    for i in range(1,len(x)):
        y.append(float(x[i]*100/sum(x)))
    matrix.append(y)

fonc("2020",'06')
fonc("2020",'08')
fonc("2020",'10')
fonc("2020",'11')
fonc("2020",'12')
fonc("2021",'01')
fonc("2021",'02')
fonc("2021",'03')
fonc("2021",'04')
fonc("2021",'05')
fonc("2021",'06')
fonc("2021",'07')
fonc("2021",'08')
fonc("2021",'09')
fonc("2021",'10')
fonc("2021",'11')
fonc("2021",'12')
fonc("2022",'01')
fonc("2022",'02')
fonc("2022",'03')
fonc("2022",'04')
fonc("2022",'05')
fonc("2022",'06')
fonc("2022",'07')
mat = []
for i in range(len(matrix[0])):
    l = []
    for j in range(len(matrix)):
        l.append(matrix[j][i])
    mat.append(l)
    
###Couleur 
import matplotlib
import colorsys
col = list(matplotlib.colors.cnames.keys())
del col[0]
del col[3]
del col[3]
del col[15]
del col[42]
del col[45]
del col[44]
col[aa.index("BA.2")]= "blue"
col[aa.index("BA.2.3")]= "Purple"
col[aa.index("BA.2.9")]= "DodgerBlue"
col[aa.index("BA.5")]= "red"
col[aa.index("BA.4")]= "yellow"

 # col= ["Navy","Purple","DodgerBlue","BlueViolet","SkyBlue","DarkKhaki","Fuchsia","Turquoise","Khaki","Orange","cyan","DarkTurquoise","Yellow","Teal","Olive","PaleVioletRed","Pink","Maroon","Coral","black","YellowGreen","Indigo","Lavender","PeachPuff","PowderBlue","blue","#FF2400","#FFFF00","#D98719","#D19275","#EAEAAE","#D9D9F3","#e6e8ff","#4B0082"]
#col= ["#0000EE","#8A360F","#8B7355","#0000CD","#66CD00","#8B8378","#6F4242","darkgray","#B5A642","blue","#9F9F5F","#32CD99","#70DB93","#DBDB70","Turquoise","Khaki","#00FF7F","#4F2F4F","cyan","#4D4DFF","#3299CC","navy","#9932CD","#9F5F9F","#8F8FBD","#38B0DE","#CDCDCD","#ADEAEA","#4E2F2F","#5C3317","#A62A2A","#A68064","#EAADEA","limegreen","#DB7093","#CC3299","#FF2400","#FFFF00","#D98719","black","#D19275","#EAEAAE","#D9D9F3","#2A4F2F","#e6e8ff","#D9A9F3","#F08080","#FFF0F5","#E0FFFF","#68838B","#ADD8E6"]

for i in range(len(aa)-1, -1,-1):
    plt.axvline(x=i,color='gray',linestyle='--',alpha=0.4)


for i in range(len(aa)-1, -1,-1):
    plt.fill_between(range(len(mat[i])),mat[i],color = col[i],label =aa[i],alpha=0.6)
    
    

mois_an = ["June-2020","Aug-2020","Oct-2020","Nov-2020","Dec-2020","Jan-2021","Feb-2021","March-2021","April-2021","May-2021","June-2021","July-2021","Aug-2021","Sept-2021","Oct-2021","Nov-2021","Dec-2021","Jan-2022","Feb-2022","March-2022","April-2022","May-2022","June-2022","July-2022"]

# mois_an = ["Nov-2021","Dec-2021","Jan-2022","Feb-2022","March-2022","April-2022"]

plt.legend(loc='upper left', bbox_to_anchor=(1.08,1), ncol=4, fancybox=True, shadow=True)
plt.text(len(mois_an) + 7,105,'Lineages',color = 'black',fontsize=12)
plt.xlim(0,len(mois_an)-1)
plt.ylim(0,100)
plt.xticks(range(len(mois_an)),mois_an,rotation = 90,fontsize=12)
plt.yticks(fontsize=12)
plt.ylabel("Percentage \n",fontsize=15)
#plt.xlabel("\nEvolution over time",fontsize=15)
plt.xlabel("\nMonth",fontsize=15)

plt.text(5.2,15,'B.1',color = 'white',fontsize=10)
plt.text(8.8,35,'Eta',color = 'black',fontsize=10)
plt.text(9.3,50,'     Delta \n(B.1.617.2)',color = 'black',fontsize=10)
plt.text(6.5,38,'Alpha',color = 'black',fontsize=10)
plt.text(12.9,40,'AY.4',color = 'black',fontsize=10)
# plt.text(14.7,90,'Omicron',color = 'black',fontsize=10)
# plt.text(16.7,95,'BA.2',color = 'red',fontsize=10)
# plt.annotate(s='', xy=(9.5,80), xytext=(9.99,27),c="red", arrowprops=dict(arrowstyle='<-'))
# plt.title("Distribution des différents variants d'intérêt par mois identifiés à IRESSEF\n au cours de la pandemis du SARS-Cov-2 au Sénégal\n\n",fontsize = 18)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.text(14.5,95,'BA.1',color = 'red',fontsize=12)
plt.text(17.5,95,'BA.2',color = 'red',fontsize=12)
plt.text(21,60,'BA.5',color = 'red',fontsize=12)
plt.text(22,30,'BA.2.9',color = 'blue',fontsize=12)
plt.annotate('', xy=(17,78), xytext=(14.8,94), arrowprops=dict(arrowstyle='->'))
plt.annotate('', xy=(18,80), xytext=(17.8,94), arrowprops=dict(arrowstyle='->'))
plt.annotate('', xy=(22,50), xytext=(22,58), arrowprops=dict(arrowstyle='->'))


'''

################################################# distribution des clades ou lineages du mois en cours fig5 and 6 


c= list(f[6])
del c[0]
a= list(f[7])
dp = [str(i).replace('-', '/') for i in list(f[12])]

del a[0]
del dp[0]
aa = [x for x in list(set(a)) if pd.isnull(x) == False]
#del aa [aa.index(-1)]
aa.sort()
cc = [x for x in list(set(c)) if pd.isnull(x) == False]
#del cc [cc.index(-1)]
#del cc [cc.index("Clade")]
cl = [] # clade
li = [] # lineage
def fonc(an,mois):
    for j in range(len(aa)):
        for i in range(len(dp)) :
            if dp[i] == "/1"  :
                pass
            elif str(dp[i]).find(an) != -1 :
                m = dp[i].split('/')
                print(m)
                if m[1] == mois:
                    cl.append(c[i])
                    li.append(a[i])

fonc("2022",'07')




cl = [x for x in cl if pd.isnull(x) == False]
li= [x for x in li if pd.isnull(x) == False]
cl_u = [x for x in list(set(cl)) if pd.isnull(x) == False]
li_u = [x for x in list(set(li)) if pd.isnull(x) == False]
del cl_u[cl_u.index('None')]
del li_u[li_u.index('None')]
#plt.suptitle("Distribution des différents variants identifiés à IRESSEF\n lors de la deuxième vague \n\n\n\n",fontsize=24)
#plt.subplot(1,3,1)



a  = cl
b = cl_u
l = []
for i in range(len(b)):
    l.append(a.count(b[i]))
###Couleur 
import matplotlib
import colorsys
col = list(matplotlib.colors.cnames.keys())
del col[0]
del col[3]
del col[4]
del col[3]
del col[15]
del col[42]
del col[45]
del col[44]
# col[aa.index("BA.2")]= "blue"
# col[aa.index("BA.2.3")]= "Purple"
# col[aa.index("BA.2.9")]= "DodgerBlue"
# col= ["#6F4242","#527F76","#2F4F2F","#238E23","#B5A642","#9F9F5F","#32CD99","#70DB93","#DBDB70","#00FF7F","#4F2F4F","#00009C","#4D4DFF","#3299CC","#9932CD","#9F5F9F","#8F8FBD","#38B0DE","#CDCDCD","#ADEAEA","#4E2F2F","#5C3317","#A62A2A","#A68064","#EAADEA","#DB7093","#CC3299","#FF2400","#FFFF00","#D98719","#D19275","#EAEAAE","#D9D9F3","#e6e8ff"]

############# clades fig5dc

# dic={}
# dic = {b[i]: l[i] for i in range(len(l))}
# dic1 = sorted(dic.items(), key=lambda t: t[1])# ll = [dic1[i][1] for i in range(len(dic1))]
# bb = [dic1[i][0] for i in range(len(dic1))]
# #plt.pie(ll, autopct='%.2f',colors=col,explode = [0, 0.2, 0, 0, 0])

# ex=[]
# for i in range(len(ll)):
#     if ll[i] > 250:
#         ex.append(0)
#     else:
#         ex.append(0)
# pr = [round(ll[i]/sum(ll)*100,2) for i in range(len(ll))]
# bb2 = [str(bb[i])+" ("+str(pr[i])+"%)" for i in range(len(bb))]
# plt.pie(ll,colors = col,explode = ex,autopct = lambda x: str(round(x, 2)) + '%',pctdistance = 1.17, labeldistance = 1.4,shadow = True)
# plt.legend(bb2,loc='upper left', bbox_to_anchor=(1.3,0.8), ncol=1, fancybox=True, shadow=True)
# # plt.suptitle("Distribution des différents variants identifiés à IRESSEF\n lors de la deuxième vague \n\n\n\n\n",fontsize=12)
# plt.title('Nextstrain (Clades) _ July 2022\n\n',fontsize = 18)


########lineages fig6dl

a  = li
b = li_u
l = []
for i in range(len(b)):
    l.append(a.count(b[i]))
dic={}
dic = {b[i]: l[i] for i in range(len(l))}
dic1 = sorted(dic.items(), key=lambda t: t[1])
ll = [dic1[i][1] for i in range(len(dic1))]
bb = [dic1[i][0] for i in range(len(dic1))]
#plt.pie(ll, autopct='%.2f',colors=col)
ex=[]
for i in range(len(ll)):
    if ll[i] > 250:
        ex.append(0)
    else:
        ex.append(0)
pr = [round(ll[i]/sum(ll)*100,2) for i in range(len(ll))]
bb2 = [str(bb[i])+" ("+str(pr[i])+"%)" for i in range(len(bb))]
plt.pie(ll,colors = col,explode = ex,autopct = lambda x: str(round(x, 2))+"%" ,pctdistance = 1.17,shadow = True)

#plt.legend(bb2,loc='upper left', bbox_to_anchor=(-0.4,0), ncol=3, fancybox=True, shadow=True)
plt.legend(bb2,loc='upper left', bbox_to_anchor=(1.3,0.8), ncol=2, fancybox=True, shadow=True)
plt.title('Pangolin (Lineages) _ July 2022\n\n',fontsize = 18)







