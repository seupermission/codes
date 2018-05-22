import numpy as np
import matplotlib.pyplot as plt
from  statistics import mean,stdev,variance

class Group:

    def __init__(self,X,Y,j):
        self.X = np.array(X)
        self.Y = np.array(Y)
        self.X1 = X
        self.Y1 = Y
        self.j = j 
        self.person_r = np.corrcoef(self.X1,self.Y1)[0, 1]  #Pearson correlation 
        

    def indicators(self):
        x={}
        y={}
       
        x['x_avg'] = mean(self.X)
        x['x_std'] = stdev(self.X)
        x['x_pstd'] = stdev(self.X)*10/11
        x['x_var'] = variance(self.X)
        x['x_pvar'] = variance(self.X)*10/11
        y['y_avg'] = mean(self.Y)
        y['y_std'] = stdev(self.Y)
        y['y_pstd'] = stdev(self.Y)*10/11
        y['y_var'] = variance(self.Y)
        y['y_pvar'] = variance(self.Y)*10/11
        return x,y,self.person_r

    
    def rSquared(self,measured, predicted):
        # RSS: residual sum of squares
        estimateError = ((predicted - measured)**2).sum()
        meanOfMeasured = measured.sum()/float(len(measured))
        
        # TSS: total sum of squares
        variability = ((measured - meanOfMeasured)**2).sum()
        return 1 - estimateError/variability
    

    
    def LinearRegression(self):
        measuredX = np.array(self.X)  
        measuredX.sort()
        measuredY = self.Y

        i=0
        a=[]
        R=[]
        predictedY = []
        while (i<1):
            a.append([0,0])
            R.append(None)
            predictedY.append(None)
            i=i+1
        
        i=0
        while (i<1):
            a[i][0-i:1] = np.polyfit(self.X, self.Y, i+1)
            predictedY[i] =(a[i][0]*measuredX + a[i][1])
            predictedY1 =( a[i][0]*self.X + a[i][1])
            R[i] = self.rSquared(measuredY, predictedY1)
            if (R[i]<0)or(R[i]>1):
                predictedY[i] =self.Y  
            i+=1
        return a,measuredX,predictedY,R
    

    
    def export(self,ax,j=5): 
        a,measuredX,predictedY,R = self.LinearRegression()
        ax.plot(self.X, self.Y, 'bo',label='Anscombe'+'%.0f' % (self.j+1)+'.jpg')
        for i in range(1):
            if j<5:
                i=j
            if i==0:
                if (R[i]<0)or(R[i]>1):
                    ax.plot(measuredX, predictedY[i], 'g:', 
                    label = 'linear fit x='+'%.2f' %(measuredX[0]))
                else :
                    ax.plot(measuredX, predictedY[i], 'g:', 
                    label = 'linear fit y='+'%.2f' % (a[i][1])+'x+'+'%.1f' % (a[i][0]))
            if j<5:
                break
                
        ax.set_title('Anscombe'+'%.0f' % (self.j+1)+'.txt')
        ax.legend(loc='best')
        ax.set_xlabel('X'+'%.0f' % (self.j+1))
        ax.set_ylabel('Y'+'%.0f' % (self.j+1))
        return ax
import xlrd



def read_datafile(filename):
    
    datafile = xlrd.open_workbook(filename)
    sheet = datafile.sheets()[0]
    col = sheet.ncols 
    row = sheet.nrows
    
    group = []
    x=[]
    y=[]
    
    i=0
    while (i < col):
        x.append(None)
        y.append(None)
        group.append(None)
        i=i+1
    
    i=0
    j=0
    while (i < col):
        x[i]=sheet.col_values(i)
        del x[i][0]
        y[i]=sheet.col_values(i+1)
        del y[i][0]
        group[j] = Group(x[i],y[i],j)
        j=j+1
        i=i+2
        
    return row,col,group


    
row,col,group = read_datafile('./data.xlsx')
row=row-1
a=int(col/2)
x=[]
y=[]
r=[]
fig = plt.figure(figsize=(12,10)) 

for i in range(a):
    ax = fig.add_subplot(2,2,i+1)
    group[i].export(ax)
    x.append(None)
    y.append(None)
    r.append(None)
    x[i],y[i],r[i]=group[i].indicators()
    
plt.show()

from prettytable import PrettyTable
table=PrettyTable(["data set","x-avg","x-std", "x-pstd", "x-var","x-pvar",
                   "y-avg","y-std", "y-pstd", "y-var","y-pvar","pearson_r"])  
table.align['data set']= "m" # middle align  
table.padding_width = 1 # One space between column edges and contents (default)  
for i in range(a):
    table.add_row([str(i),"%.1f" %x[i]['x_avg'],"%.3f" %x[i]['x_std'],
                   "%.3f" %x[i]['x_pstd'],"%.1f" %x[i]['x_var'],"%.1f" %x[i]['x_pvar'],
                   "%.3f" %y[i]['y_avg'],"%.3f" %y[i]['y_std'],"%.3f" %y[i]['y_pstd'],
                   "%.3f" %y[i]['y_var'],"%.3f" %y[i]['y_pvar'],"%.3f" %r[i]])     

print(table)