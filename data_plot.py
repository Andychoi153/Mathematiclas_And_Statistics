# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 23:24:09 2015

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator


f_name = "C:\\Users\\user\\Desktop\\scan\\graphene_3-3-C_200slit_0.2sec_5.1desity"#"C:\\Users\\user\\Downloads\\graphene_3-3-C_200slit_0.2sec_5.1desity"

Data_type1 = input("데이터가 시간 축 혹은 x (종속변수)값을 포함하고 있습니까? [Y/n]: ")# input 함수를 넣는다.
Data_type2 = input("데이터는 2d 형태 입니까? 3d 형태입니까? [2d/3d]:")

#f_name = input("for test :")


if Data_type2 == '3d' :
    Data_type3 = input("데이터는 vector form 입니까? grid-level form 입니까? [vector/level]: ")



if (Data_type1 == 'Y')|(Data_type1 == 'y') :#time
    Data = np.loadtxt(f_name, unpack = True)    
    x = Data[0]
    if Data.shape[0] > 2:
        Data = Data[1:-1]
        Data = np.append(Data, [Data[-1]],axis = 0)
        col_flag = 0
    else :
        Data = np.array([Data[1]])
        col_flag = 1
        
else :
    Data = np.loadtxt(f_name, unpack = True)
    col_flag = 0
    """if Data.shape[0] > 1:
        Data = Data[1:-1]
        Data = np.append(Data, [Data[-1]],axis = 0)
        col_flag = 0
    else :
        Data = np.array([Data[1]])
        col_flag = 1
"""

if Data_type2 == '2d' :#0
    Data = Data
elif (Data_type2 == '3d') & (Data_type3 == 'level') :#2
    Data = np.transpose(Data)
else :
    Data = np.loadtxt(f_name)
           

if col_flag == 1 :
    row = 1
    col = Data.shape[0]
else :
    try :
        row = Data.shape[0]#행의 갯수-2d 일때는 얘 가 함수 갯수/ 3d 일때는 얘가 y, 정의역의 갯수
        col = Data.shape[1] #열의 갯수-2d 일때는 예가 y값의 갯수, 정의역 개수, 치역의 개수 즉 x.size, y.size
    except :
        row = 1
        col = Data.shape[0]
        col_flag = 1

if Data_type2 == '2d' :#dim_graph0
    if (Data_type1 == 'Y')|(Data_type1 == 'y') :
        x = x
        f_count = row
    else :
        x_size = col
        f_count = row
        x = np.linspace(0,x_size-1,x_size)
        if col_flag == 1:
            Data = np.array([Data])
    for i in range(f_count) :
        plt.plot(x,Data[i])
        
    
elif Data_type2 == '3d' :
    if Data_type3 == 'vector' :
        x = Data[0]
        y = Data[1]
        z = Data[2]
        
        
    elif Data_type3 == 'level' :
        y, x = np.mgrid[slice(0,row),
                slice(0,col)]
        for i in range(row) :
            if i == 0 : 
                z = [Data[i]]
            else :
                z = np.append(z, [Data[i]],axis = 0)
        
        z_sort = np.sort(z,axis =None)
        minimum = int (z_sort.size*0.1)
        maximum = int (z_sort.size*0.9)
        z_sort = z_sort[minimum:maximum]
        z_max = np.mean(z_sort)+3*np.std(z_sort)
        z_min = np.mean(z_sort)-3*np.std(z_sort)
        levels = MaxNLocator(nbins=15).tick_values(z_min, z_max)#max와 min 기준 수정 요함
        cmap = plt.get_cmap('PiYG')
        norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

        im = plt.pcolormesh(x, y, z, cmap=cmap, norm=norm)
        plt.colorbar()
        # set the limits of the plot to the limits of the data
        plt.axis([x.min(), x.max(), y.min(), y.max()])
        plt.title('pcolormesh with levels')



plt.show()