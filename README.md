# Electrical Signals Databases

> **Citation:**
>
> @online{DatabaseRTE, 
> author = {Presvôts, Corentin},  
> title = {Database of Voltage and Current Samples Values from the French Electricity Transmission Grid, Réseau de Transport d'Electricité (RTE), France},
> url = {https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS},
> year = {2024},
> }
> 

# Voltages and Current Database, DATA_S

This database comprises 12066 measured voltage and current waveform signals (phase-ground) on high voltage lines of the French electricity transmission grid during various faults. 


## Signal Characteristics
All signals are stored in a list DATA_S of shape (12066, 6, 21000)

Where 12066  represents the number of observed faults

6 is the number of signals per observed fault (v1, v2, v3, i1, i2, i3)

21000 is the number of samples per signal

The nominal frequency of the network is 50 Hz

The nominal voltage is 90 kV


## Sample Characteristics
The sampling frequency is 6400 Hz

The number of bits to encode a sample is 19 bits

Quantization levels range from -32767 to 32767, or 19 bits

The quantization step size for voltage signals is 18.310550000000003V per level

The quantization step size for current signals is 4.3140030000000005A per level

## Examples of Observed Voltage and Current Signals

### Signal 1 
![Figure 2024-03-28 151843](https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/707b2a46-0d82-4682-8038-a871d2904120)
![Figure 2024-03-28 151848](https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/4a006b14-e3d1-44e0-9221-fc79b8168607)
### Signal 2 
![Figure 2024-03-28 151720](https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/281f124b-3976-4048-9c48-01226a7c291a)
![Figure 2024-03-28 151727](https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/697742c5-aaef-48da-a524-c2eeea8c22e1)
### Signal 3 
![Figure 2024-03-28 132920](https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/ebfea83c-2ada-4dc0-89ed-a6ee5585e4c5)
![Figure 2024-03-28 132927](https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/d3b8d152-09ca-4851-a213-67cf47b71fdd)

# Transient Signals Databases, DATA_u and DATA_i

The lists DATA_u and DATA_i are two databases of voltage and current signals respectively obtained from DATA_S.

DATA_u and DATA_i contain 30000 signals of size 128 samples, corresponding to one period of the nominal frequency of the network at 50 Hz.

To obtain DATA_u and DATA_i, a scan of all signals in DATA_S is performed. For each voltage signal in DATA_S, a temporal segmentation is performed, dividing each voltage signal into signals of size 128 samples.

A transient selection criterion is applied to each 128-sample signal.

The window is kept if:

- the standard deviation of the signal is greater than 100 times the quantization step (to remove windows where the signal amplitude changes little)
- if the mean absolute value of the signal is greater than 2000 V (to remove all periodic signals such as harmonics)

If the 128 voltage samples are retained, the 128 current samples are also retained.
DATA_u[k] and DATA_i[k] are therefore derived from the observation of the same conductor.

## Examples of Recovered Transient Voltage Signals

<table>
  <tr>
    <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/07f4098b-52aa-4f8e-9853-fd0682fd5d61" alt="Image1" width="200"></td>
    <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/42db26ee-cd6c-434f-996a-a063e7b4ae02" alt="Image2" width="200"></td>
    <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/5d140e7c-8875-4b7c-9d5b-ad6eef07bb1b" alt="Image3" width="200"></td>
    <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/2e1996d8-5e97-4d94-a78a-b7e1f86b0fce" alt="Image4" width="200"></td>
    <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/521be535-9d22-4efd-8604-fd4c8ac2269a" alt="Image5" width="200"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/3945924e-46f2-491b-8194-2705ded99cac" alt="Image4" width="200"></td>
    <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/9ba41826-f494-48c2-b44e-6fcf61e13682" alt="Image6" width="200"></td>
    <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/fdf4bbec-93ed-4b3c-99e9-a6e73e8e0c6a" alt="Image7" width="200"></td>
    <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/287a2b8a-47ad-4fff-bf34-b2e5e03c22ab" alt="Image8" width="200"></td>
    <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/138e2a04-2a7a-4e28-8e7e-ff95339ae1e9" alt="Image5" width="200"></td>
  </tr>
  <tr>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/24cbc12a-a2e0-4ab7-9976-9e10b7c3ef2a" alt="Image4" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/3324fb4e-c81d-451e-aeee-e43792299ce8" alt="Image6" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/3ae1e49f-b452-4812-bea1-22409525a4dd" alt="Image7" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/7bfd395c-0a41-4c68-b832-345bdd5f0b30" alt="Image8" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/ebd51acd-dbcb-4459-924e-5ce1cadcdd8a" alt="Image5" width="200"></td>
  </tr>
  <tr>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/abe2a86b-fb72-44d6-8cc2-3ee1350442a3" alt="Image4" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/dbaa119f-2479-45ba-a9c5-18743ea1a373" alt="Image6" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/385e5fdc-bbca-43ed-bc00-9c4558bed42c" alt="Image7" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/9feffb5d-67a0-4077-9882-2fd289212ad6" alt="Image8" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/3aafe378-d8b1-42e1-8d38-0cd735aa7a82" alt="Image5" width="200"></td>
  </tr>
  <tr>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/3cd01edd-cca7-4a6f-b086-618c7a7c59dd" alt="Image4" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/17738dd3-b859-441b-a743-d935cde72c7c" alt="Image6" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/4fcd78c1-cdd0-4847-8a6a-f64bf307243d" alt="Image7" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/99689b8f-830d-4473-a527-679a8ef7ec04" alt="Image8" width="200"></td>
  <td><img src="https://github.com/CorentinPresvots/DATABASE_ELECTRICAL_SIGNALS/assets/144250214/cd914add-ee09-418a-84e4-d9d77289ec39" alt="Image5" width="200"></td>
  </tr>
</table>

## Download DATA_u, DATA_i, and DATA_S Databases
Download the txt files DATA_S, DATA_u and DATA_i. 

Space required to download the databases :

DATA_S.txt : 7.9 GB 

DATA_u.txt : 20 MB

DATA_i.txt : 13 MB

then with python run


    DATA_S_load = np.loadtxt('DATA_S.txt').reshape((12066, 6, 21000)) # Load DATA_S from the text file 
    DATA_u_load = np.loadtxt('DATA_u.txt') #  Load DATA_u from the text file
    DATA_i_load = np.loadtxt('DATA_i.txt') # Load DATA_i from the text file


    ## test 
    print("DATA_S_load",np.shape(DATA_S_load))
    print("DATA_u_load",np.shape(DATA_u_load))
    print("DATA_i_load",np.shape(DATA_i_load))
  
    for k in range(10):
        fig=plt.figure(figsize=(15,5),dpi=100)
        for i in range(3):
            plt.plot(t,DATA_S_load[k][i]*18.310550000000003,lw=2,label='v{}'.format(i+1))
            plt.xlabel('t [s]')
            plt.ylabel('Voltage (V)')
            plt.grid( which='major', color='#666666', linestyle='-')
            plt.legend()
            plt.minorticks_on()
            
        fig=plt.figure(figsize=(15,5),dpi=100)
        for i in range(3):            
            plt.plot(t,DATA_S_load[k][i+3]4.3140030000000005,lw=2,label='i{}'.format(i+1))
            plt.xlabel('t [s]')
            plt.ylabel('Courrent (A)')
            plt.grid( which='major', color='#666666', linestyle='-')
            plt.legend()
            plt.minorticks_on()   
            
# Prerequisites

- numpy


- matplotlib.pyplot


