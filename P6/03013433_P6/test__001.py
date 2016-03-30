# coding=gbk
import xlrd
'''
Created on 2016��3��8��

@author: 1
'''
def mean(sample_list):#�����ֵ
    sum=0
    for i in sample_list:
        sum+=i
    mean_value=float(sum)/len(sample_list)
    return mean_value

def s_deviation(sample_list):#���㷽��
    mean_value=mean(sample_list)
    s_deviation_value=0
    for i in range(len(sample_list)):
        sum1=((sample_list[i]-mean_value)**2)
        s_deviation_value+=sum1
    s_deviation_value=float(s_deviation_value)/len(sample_list)
    return s_deviation_value 
    
def linear_b(list_x,list_y):#�������ϵ��b
    x_mean=mean(list_x)
    y_mean=mean(list_y)
    if len(list_x)!=len(list_y):
        print ("error")
    total=0
    total_=0
    for i in range(len(list_x)):
        sum1=list_x[i]*list_y[i]
        total+=sum1
        sum2=list_x[i]**2
        total_+=sum2
    s_xy=(float(total)/len(list_x))-(x_mean*y_mean)
    s_xx=(float(total_)/len(list_x))-x_mean
    return s_xy/s_xx

def linear_a(b,x_mean,y_mean):#�������ϵ��a
    a=y_mean-b*x_mean     
    return a

data = xlrd.open_workbook('demo.xlsx')
table = data.sheets()[0]
ncols = table.ncols
a=table.col_values(0)
b=table.col_values(1)
c=table.col_values(2)
d=table.col_values(3)
print('��һ�еľ�ֵ' , mean(a))
print('�ڶ��еľ�ֵ' , mean(b))
print('�����еľ�ֵ' , mean(c))
print('�����еľ�ֵ' , mean(d))
print('��һ�еķ���' , s_deviation(a))
print('�ڶ��еķ���' , s_deviation(b))
print('�����еķ���' , s_deviation(c))
print('�����еķ���' , s_deviation(d))
b1=linear_b(a, b)
a1=linear_a(b1, mean(a), mean(b))
print('��һ�������Իع���',a1,b1)
b2=linear_b(a,c)
a2=linear_a(b2,mean(a),mean(c))
print('��һ�������Իع���',a2,b2)
b3=linear_b(a,d)
a3=linear_a(b3,mean(a),mean(d))
print('��һ�������Իع���',a3,b3)
import numpy as np
import pylab as pl
x1=[0,-a1/b1]
y1=[a1,0]
pl.plot(x1,y1,'r')
pl.plot(a, b,'go')
pl.title('FIGURE1')
pl.show()
import pylab as pl_
x2=[0,-a2/b2]
y2=[a2,0]
pl_.plot(x2,y2,'r')
pl_.plot(a, c,'go')
pl_.title('FIGURE2')
pl_.show()
import pylab as pl__
x3=[0,-a3/b3]
y3=[a3,0]
pl__.plot(x3,y3,'r')
pl__.plot(a, d,'go')
pl__.title('FIGURE3')
pl__.show()