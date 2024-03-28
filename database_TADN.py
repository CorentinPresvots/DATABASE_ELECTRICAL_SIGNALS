# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:04:56 2023

@author: presvotscor
"""
"""
# Ouvrir le fichier en mode lecture
with open('data_test.txt', 'r') as file:
    # Lire le contenu du fichier
    content = file.read()

# Extraire la liste à partir du contenu du fichier
# En supposant que la liste est toujours dans la forme indiquée
start = content.find('[')
end = content.find(']')
if start != -1 and end != -1:
    # Extraire la partie entre crochets et la diviser en éléments individuels
    list_str = content[start + 1:end]
    x_test_RTE = [float(item.strip()) for item in list_str.split(',')]

    # Maintenant, 'elements' contient la liste que vous souhaitez récupérer
    print(x_test_RTE[0:10])
"""

import numpy as np
import matplotlib.pyplot as plt


def get_RTE_signal():
    nom_fichier = "monFichier.txt"
    # Listes pour stocker les données
    v1=[]
    v2=[]
    v3=[]
    i1=[]
    i2=[]
    i3=[]
    
    # Lire les données depuis le fichier
    with open(nom_fichier, 'r') as file:
        lignes = file.readlines()
        for ligne in lignes:
            elements = ligne.strip().split(',')  # Divise la ligne en éléments en utilisant la virgule comme délimiteur
            if len(elements) >= 1:
                # Ajoute le premier élément (colonne 1) à la liste
                v1.append(float(elements[0]))
                v2.append(float(elements[1]))
                v3.append(float(elements[2]))
                i1.append(float(elements[3]))
                i2.append(float(elements[4]))
                i3.append(float(elements[5]))
    v1=np.array(v1)/290
    v2=np.array(v2)/290
    v3=np.array(v3)/290
    i1=np.array(i1)/290
    i2=np.array(i2)/290
    i3=np.array(i3)/290

    return v1,v2,v3,i1,i2,i3



def get_EPRI_signal(number):

    nom_fichier = "data/{}.csv".format(str(number))
    # Listes pour stocker les données
    v1=[]
    v2=[]
    v3=[]
    i1=[]
    i2=[]
    i3=[]
    
    file=open(nom_fichier, 'r')
    line = file.readlines()[3: :1]
    
    for element in line :
        v1.append(float(element.split(',')[1]))
        v2.append(float(element.split(',')[2]))
        v3.append(float(element.split(',')[3]))
        i1.append(float(element.split(',')[4]))
        i2.append(float(element.split(',')[5]))
        i3.append(float(element.split(',')[6]))

    v1=np.array(v1)
    v2=np.array(v2)
    v3=np.array(v3)
    i1=np.array(i1)
    i2=np.array(i2)
    i3=np.array(i3)
    
    return v1,v2,v3,i1,i2,i3
    #file = open("dataset/{}.csv".format(str(number)), "r")
    


def get_RTE_TADN_signal(path):
    
    nom_fichier_CFG = "{}.cfg".format(str(name))
    with open(nom_fichier_CFG, 'r') as file:
        lignes = file.readlines()
        
        #print("lignes",lignes)
                
        # pas de quantification tension
        Deltav1 = 1000*float(lignes[2].strip().split(',')[5])/float(lignes[2].strip().split(',')[10])
        Deltav2 = 1000*float(lignes[3].strip().split(',')[5])/float(lignes[3].strip().split(',')[10])
        Deltav3 = 1000*float(lignes[4].strip().split(',')[5])/float(lignes[4].strip().split(',')[10])
        
        # pas de quantification courant
        Deltai1 = 1000*float(lignes[5].strip().split(',')[5])/float(lignes[5].strip().split(',')[10])
        Deltai2 = 1000*float(lignes[6].strip().split(',')[5])/float(lignes[6].strip().split(',')[10])
        Deltai3 = 1000*float(lignes[7].strip().split(',')[5])/float(lignes[6].strip().split(',')[10])  
        
        
        Delta=[Deltav1 ,Deltav2 ,Deltav3,Deltai1 ,Deltai2 ,Deltai3 ]
        #print("Delta", Delta)
        
        # Nombre de bits max
        Rv1=int(np.ceil(np.log2(1+2*float(lignes[2].strip().split(',')[9]))))
        Rv2=int(np.ceil(np.log2(1+2*float(lignes[3].strip().split(',')[9]))))
        Rv3=int(np.ceil(np.log2(1+2*float(lignes[4].strip().split(',')[9]))))
        
        
        Ri1=int(np.ceil(np.log2(1+2*float(lignes[5].strip().split(',')[9]))))
        Ri2=int(np.ceil(np.log2(1+2*float(lignes[6].strip().split(',')[9]))))
        Ri3=int(np.ceil(np.log2(1+2*float(lignes[7].strip().split(',')[9]))))    
        
        R=[Rv1 ,Rv2 ,Rv3,Ri1 ,Ri2 ,Ri3]
        

       # print(kv1)
        #print(kv2)
        #print(kv3)
            
        #print(ki1)
        #print(ki2)
        #print(ki3)            
            
          
    nom_fichier = "{}.dat".format(str(name))
    # Listes pour stocker les données
    t=[]
    v1=[]
    v2=[]
    v3=[]
    i1=[]
    i2=[]
    i3=[]
    

    try:
        with open(nom_fichier, 'r') as file:
            lignes = file.readlines()
           
    except UnicodeDecodeError:
        print("Une erreur de décodage Unicode s'est produite. Impossible de lire le fichier.")
        lignes = []  # ou une autre action que vous souhaitez effectuer en cas d'erreur de décodage
        S=[v1,v2,v3,i1,i2,i3]        
        return 0,0,0,0,0   
    cpt=0   
    for ligne in lignes[:-1]:
        
        cpt+=1
        if cpt>21000:
            break
        elements = ligne.strip().split(',')  # Divise la ligne en éléments en utilisant la virgule comme délimiteur    
        #print(1,len(elements),elements)
        if len(elements)!=24:
            print("La longeur de la chaîne", elements, "n'est pas égale à 24.")
            print("nom",nom_fichier)
            return 0,0,0,0,0
        
        try : 
            t.append(float(elements[1]))
            v1.append(float(elements[2]))
            v2.append(float(elements[3]))
            v3.append(float(elements[4]))
            i1.append(float(elements[5]))
            i2.append(float(elements[6]))
            i3.append(float(elements[7]))
        except ValueError:
            print("La chaîne", elements, "ne peut être convertie en un nombre flottant.")
            return 0,0,0,0,0

            
            
    fs=int(1/(t[-1]*10**(-6)/len(v1)))
    #print("fs",fs)
    t=np.array(t)*10**(-6)
    v1=np.array(v1)#*Deltav1
    v2=np.array(v2)#*Deltav2
    v3=np.array(v3)#*Deltav3
    i1=np.array(i1)#*Deltai1
    i2=np.array(i2)#*Deltai2
    i3=np.array(i3)#*Deltai3
    
    S=[v1,v2,v3,i1,i2,i3]
    
    return t,S,fs,Delta,R



def w_faults(S,size_window,std_signal,Delta):
    DATA_u=[]
    DATA_i=[] 

    Threshold=0*0.1 
    
    Threshold_noise=1*100
    Threshold_mean=2000
    N=len(S[0])
    
    for phase in range(3):
        for k in range(int(N/size_window)):
            signal_w=np.array(S[phase][k*size_window:(k+1)*size_window])*Delta[phase]
            
            std_signal_w=np.std(signal_w)
            mean_signal_w=np.mean(signal_w)
          
            if (std_signal_w<(1-Threshold)*std_signal or std_signal_w>(1+Threshold)*std_signal) and (std_signal_w>Threshold_noise*Delta[phase] and np.abs(mean_signal_w)>Threshold_mean):
                DATA_u.append(S[phase][k*size_window:(k+1)*size_window])
                DATA_i.append(S[phase+3][k*size_window:(k+1)*size_window])
                
                
                
                
    return DATA_u,DATA_i
                
                





# Programme principal
if __name__ == "__main__":
    """
    v1,v2,v3,i1,i2,i3=get_RTE_signal()
    fs=6400 # samples frequency
     
    t=np.linspace(0,(len(v1)-1)*(1/fs),len(v1))  # vecteur temps\n",
    
    fig=plt.figure(figsize=(10,5),dpi=100)
    plt.plot(t,v1/1000,lw=2)
    plt.plot(t,v2/1000,lw=2)
    plt.plot(t,v3/1000,lw=2)
    plt.xlabel('t [s]')
    plt.ylabel('Voltage (kV)')
    plt.title('voltages RTE')
    plt.grid( which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    
    
    fig=plt.figure(figsize=(10,5),dpi=100)
    plt.plot(t,i1/1000,lw=2)
    plt.plot(t,i2/1000,lw=2)
    plt.plot(t,i3/1000,lw=2)
    plt.xlabel('t [s]')
    plt.ylabel('Current (kA)')
    plt.title('Currents RTE')
    plt.grid( which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    """



    """

    v1,v2,v3,i1,i2,i3=get_EPRI_signal(21834)
    fs=15384.6 # samples frequency
     
    t=np.linspace(0,(len(v1)-1)*(1/fs),len(v1))  # vecteur temps\n",
    
    fig=plt.figure(figsize=(10,5),dpi=100)
    plt.plot(t,v1/1000,lw=2)
    plt.plot(t,v2/1000,lw=2)
    plt.plot(t,v3/1000,lw=2)
    plt.xlabel('t [s]')
    plt.ylabel('Voltage (kV)')
    plt.title('voltages RTE')
    plt.grid( which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    
    
    fig=plt.figure(figsize=(10,5),dpi=100)
    plt.plot(t,i1/1000,lw=2)
    plt.plot(t,i2/1000,lw=2)
    plt.plot(t,i3/1000,lw=2)
    plt.xlabel('t [s]')
    plt.ylabel('Current (kA)')
    plt.title('Currents RTE')
    plt.grid( which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    
    """
    import os
    
    # Chemin complet du répertoire contenant les fichiers à lire
    directory_path = r'D:\Users\presvotscor\Database_TADN'
    
    # Liste des noms de fichiers dans le répertoire
    file_names = os.listdir(directory_path)
    print("file_names",file_names)
    
    

    # Lire chaque fichier
    DATA_S=[]
    
    DATA_u=[]
    DATA_i=[]
    
    cpt_file=0

    for file_name in file_names:
        
        # Liste des noms de fichiers dans le répertoire
        # Chemin complet du fichier
        file_path_names = os.path.join(directory_path, file_name)
        
        
    
        files = os.listdir(file_path_names)
        

        
        print("files {}".format(cpt_file),file_name)
        

        
        
        
        
        if cpt_file>np.infty:
            break
        cpt_file+=1
        
        
        cpt=0
        for file in files:
    
            # Chemin complet du fichier
            file_path = os.path.join(file_path_names, file)
            
            # Séparer le nom de base et l'extension du fichier
            file_base, file_extension = os.path.splitext(file_path)
            #print("file_base",file_base)
            #print('file_base',bad_name[0])
            #print(file_extension)
            #ezfzefezfzefezf
            
            
            if file_extension==".DAT" or file_extension==".dat":
                
                #if cpt==50:
                #    break
         
            
            
                #name="20211003-145748-L31HAGET-00466"
                #name="20200721-012934-L31LUSSA-00080"
                name=file_base
                t,S,fs,Delta,R=get_RTE_TADN_signal(name)
                if fs!=0 and fs<6300:
                    print("fs={:.0f} Hz".format(fs),Delta,"Nb samples={}".format(len(t)))
                if  fs>6300 and (len(t)<=20000):
                    print("La longueur de la liste len(t)={}<20000".format(len(t)))
             
                if fs>6300 and np.max(S[0])*Delta[0]<500:
                    print("L'amplitude max ={}<500 V".format(np.max(S[0])*Delta[0]))
                 
                    
                if fs>6300 and len(t)>20000 and np.max(S[0])*Delta[0]>500:
                    
                    if cpt>20:
                        break
                    cpt+=1
                    
                    
                    
                    #print("shape_S",np.shape(np.array(S)))
                    DATA_S.append(np.array(S))
                    #print("shape DATA_S",np.shape(DATA_S))
                            
                    data_u,data_i=w_faults(S,128,63000,Delta)
                    #print(np.shape(data_u))
                    DATA_u.extend(data_u)
                    #print(np.shape(DATA_u))
                    
                    DATA_i.extend(data_i)
                    

                

    shuffle=np.array([i for i in range(len(DATA_u))])

    np.random.shuffle(DATA_u) 
    np.random.shuffle(DATA_i)   
    
    
    shuffle=np.array([i for i in range(len(DATA_S))])
    np.random.shuffle(DATA_S) 
   
    
    print('shape(DATA_S)', np.shape(DATA_S))  
    print('shape(DATA_u)', np.shape(DATA_u))   
    print('shape(DATA_i)', np.shape(DATA_i))
    for k in range(20):
        fig=plt.figure(figsize=(8,5),dpi=100)
        plt.plot(t[0:128],DATA_u[k]*Delta[0],lw=2,label='v{}'.format(k))
        plt.xlabel('t [s]')
        plt.ylabel('Voltage (V)')
        plt.title('base de données, mean = {:.0f} V, std = {:.0f} V'.format(np.mean(DATA_u[k]*Delta[0]),np.std(DATA_u[k]*Delta[0])))
        plt.grid( which='major', color='#666666', linestyle='-')
        plt.legend()
        plt.minorticks_on()
    
    

 
 
    # Sauvegarder DATA_S dans un fichier texte
    np.savetxt('DATA_S.txt', np.array(DATA_S).flatten(),fmt='%d')
    np.savetxt('DATA_u.txt', np.array(DATA_u),fmt='%d')     
    np.savetxt('DATA_i.txt', np.array(DATA_i),fmt='%d')               
    
    # Charger DATA_S à partir du fichier texte
    DATA_S_load = np.loadtxt('DATA_S.txt').reshape((len(DATA_S), 6, 21000))
    print("DATA_S_load",np.shape(DATA_S_load))
    # Charger DATA_u à partir du fichier texte
    DATA_u_load = np.loadtxt('DATA_u.txt')
    DATA_i_load = np.loadtxt('DATA_i.txt')
    print("DATA_u_load",np.shape(DATA_u_load))
    print("DATA_i_load",np.shape(DATA_i_load))
    
    
    
    min_=0
    max_=10000
    for k in range(20):
        fig=plt.figure(figsize=(15,5),dpi=100)
        for i in range(3):
            plt.plot(t[min_:max_],DATA_S_load[k][i][min_:max_]*Delta[i],lw=2,label='v{}'.format(i+1))
            plt.xlabel('t [s]')
            plt.ylabel('Voltage (V)')
            plt.title('fs = {:.0f} Hz, R = {:.0f} bits, Delta = {:.2f} V'.format(fs,R[i],Delta[i]))
            plt.grid( which='major', color='#666666', linestyle='-')
            plt.legend()
            plt.minorticks_on()
            
        fig=plt.figure(figsize=(15,5),dpi=100)
        for i in range(3):            
            plt.plot(t[min_:max_],DATA_S_load[k][i+3][min_:max_]*Delta[i+3],lw=2,label='i{}'.format(i+1))
            plt.xlabel('t [s]')
            plt.ylabel('Courrent (A)')
            plt.title('fs = {} Hz, R = {} bits, Delta = {:.2f} A'.format(fs,R[i+3],Delta[i+3]))
            plt.grid( which='major', color='#666666', linestyle='-')
            plt.legend()
            plt.minorticks_on()        