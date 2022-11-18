ghost = str(' .-.' + '\n' + 
        '(o o) boo!'+'\n' + 
        '| O \ '+ '\n' + 
         ' \   \ '+ '\n' + 
          '  `~~~')
filler = 16
air = 3
import tkinter as tk
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from srim import TRIM, Ion, Layer, Target







class MP35N():
    side1 = [Layer({
    'Ni': {'stoich':35}, 'Co': {'stoich':35}, 'Cr': {'stoich':20}, 'Mo':{'stoich':10}
    }, density = 8.43, width = 9.0e7)]
    side2 = [Layer({
    'Ni': {'stoich':35}, 'Co': {'stoich':35}, 'Cr': {'stoich':20}, 'Mo':{'stoich':10}
    }, density = 8.43, width = 9.0e7)]
    
    def plot_hist(self, canvas, ax):        
        ax.clear()
        ytemp, xtemp, _ = ax.hist(GUI.x[0], bins = 100)
        for i in range(0, len(GUI.x)):
            ax.hist(GUI.x[i], bins = 100, label = str(GUI.En[i].get()) + 'MeV/c')
        ax.set_xlabel('Muon Penetration Depth (mm)')
        ax.set_ylabel('Number of Muons at Given Depth')
        mp1 = [9+air]*10 
        sample = [15+air]*10
        mp2 = [24+air]*10
        line1 = np.linspace(0, max(ytemp), 10)
        ax.fill_betweenx(line1, mp1,air, color = 'skyblue', label = 'MP35N')
        ax.fill_betweenx(line1, sample, mp1, color = 'lightgrey', label = 'sample ')
        ax.fill_betweenx(line1, mp2, sample, color = 'skyblue')
        box = ax.get_position()
        ax.legend()
        canvas.draw()
        
    def plot_scatt(self, canvas, ax):
        ax.clear()
        theta = np.linspace(0,2*np.pi, 150)
        r1 = 3
        r2 = 12
        a1 = r1*np.cos(theta) + filler
        b1 = r1*np.sin(theta)
        a2 = r2*np.cos(theta)+filler
        b2 = r2*np.sin(theta)
        ax.plot(a1, b1, color = 'red')
        ax.axis('equal')
        ax.plot(a2, b2, color = 'red', label = 'Pressure Cell Boundary')
        for i in range(0, len(GUI.x)):
            ax.scatter(GUI.x[i], GUI.z[i], s = 2, label = str(GUI.En[i].get()) + 'MeV/c')
        box = ax.get_position()
        ax.legend()
        ax.set_xlim(0, 30)
        ax.set_ylim(-15, 15)
        ax.set_xlabel('X-position of Stopped Muons (mm)')
        ax.set_ylabel('Z-position of Stopped Muons (mm)')
        canvas.draw()

class CUBE_MP():
    side1 = [Layer({
    'Ni': {'stoich':35}, 'Co': {'stoich':35}, 'Cr': {'stoich':20}, 'Mo':{'stoich':10}
    }, density = 8.43, width = 6.0e7), Layer({
    'Be': {'stoich':3}, 'Cu': {'stoich':97}
    }, density = 8.25, width = 3.0e7)]
    side2 = [Layer({
    'Be': {'stoich':3}, 'Cu': {'stoich':97}
    }, density = 8.25, width = 3.0e7) , Layer({
    'Ni': {'stoich':35}, 'Co': {'stoich':35}, 'Cr': {'stoich':20}, 'Mo':{'stoich':10}
    }, density = 8.43, width = 6.0e7)]
    def plot_hist(self, canvas, ax):
        ax.clear()
        ytemp, xtemp, _ = ax.hist(GUI.x[0], bins = 100)
        for i in range(0, len(GUI.x)):
            ax.hist(GUI.x[i], bins = 100, label = str(GUI.En[i].get()) + 'MeV/c')
        ax.set_xlabel('Muon Penetration Depth (mm)')
        ax.set_ylabel('Number of Muons at Given Depth')
        PC1 = [6+air]*10 
        PC2 = [9+air]*10
        sample = [15+air]*10
        PC3 = [18+air]*10
        PC4 = [24+air]*10
        line1 = np.linspace(0, max(ytemp), 10)
        ax.fill_betweenx(line1, PC1,air, color = 'skyblue', label = 'MP35N')
        ax.fill_betweenx(line1, PC2, PC1, color = 'lightgreen', label = 'CuBe')
        ax.fill_betweenx(line1, sample, PC2, color = 'lightgrey', label = 'sample')
        ax.fill_betweenx(line1, PC3, sample, color = 'lightgreen')
        ax.fill_betweenx(line1, PC4, PC3, color = 'skyblue')
        box = ax.get_position()
        ax.legend()
        canvas.draw()
    def plot_scatt(self, canvas, ax):
        ax.clear()
        theta = np.linspace(0,2*np.pi, 150)
        r1 = 3
        r2 = 12
        r3 = 6
        a1 = r1*np.cos(theta) + filler
        b1 = r1*np.sin(theta) 
        a2 = r2*np.cos(theta) + filler
        b2 = r2*np.sin(theta)
        a3 = r3*np.cos(theta) + filler
        b3 = r3*np.sin(theta)
        ax.plot(a1, b1, color = 'orange')
        ax.axis('equal')

        ax.plot(a2, b2, color = 'red', label = 'MP35N')
        ax.plot(a3, b3, color = 'orange', label = 'CuBe')
        for i in range(0, len(GUI.x)):
            ax.scatter(GUI.x[i], GUI.z[i], s = 2, label = str(GUI.En[i].get()) + 'MeV/c')
        box = ax.get_position()
        ax.legend()
        ax.set_xlim(0, 30)
        ax.set_ylim(-15, 15)
        ax.set_xlabel('X-position of Stopped Muons (mm)')
        ax.set_ylabel('Z-position of Stopped Muons (mm)')
        
        canvas.draw()
class CUBE():
    side1 = [Layer({
    'Be': {'stoich':3}, 'Cu': {'stoich':97}
    }, density = 8.25, width = 9.0e7)]
    side2 = [Layer({
    'Be': {'stoich':3}, 'Cu': {'stoich':97}
    }, density = 8.25, width = 9.0e7)]
    
    def plot_hist(self, canvas, ax):        
        ax.clear()
        ytemp, xtemp, _ = ax.hist(GUI.x[0], bins = 100)
        for i in range(0, len(GUI.x)):
            ax.hist(GUI.x[i], bins = 100, label = str(GUI.En[i].get()) + 'MeV/c')
        ax.set_xlabel('Muon Penetration Depth (mm)')
        ax.set_ylabel('Number of Muons at Given Depth')
        cb1 = [9+air]*10 
        sample = [15+air]*10
        cb2 = [24+air]*10
        line1 = np.linspace(0, max(ytemp), 10)
        ax.fill_betweenx(line1, cb1,air, color = 'lightgreen', label = 'CuBe')
        ax.fill_betweenx(line1, sample, cb1, color = 'lightgrey', label = 'sample ')
        ax.fill_betweenx(line1, cb2, sample, color = 'lightgreen')
        box = ax.get_position()
        ax.legend()
        canvas.draw()
        
    def plot_scatt(self, canvas, ax):
        ax.clear()
        theta = np.linspace(0,2*np.pi, 150)
        r1 = 3
        r2 = 12
        a1 = r1*np.cos(theta) + filler
        b1 = r1*np.sin(theta) 
        a2 = r2*np.cos(theta) + filler
        b2 = r2*np.sin(theta)
        ax.plot(a1, b1, color = 'red')
        ax.axis('equal')
        ax.plot(a2, b2, color = 'red', label = 'Pressure Cell Boundary')
        for i in range(0, len(GUI.x)):
            ax.scatter(GUI.x[i], GUI.z[i], s = 2, label = str(GUI.En[i].get()) + 'MeV/c')
        box = ax.get_position()
        ax.legend()
        ax.set_xlim(0, 30)
        ax.set_ylim(-15, 15)
        ax.set_xlabel('X-position of Stopped Muons (mm)')
        ax.set_ylabel('Z-position of Stopped Muons (mm)')
        canvas.draw()


class GUI():
    
    layers = []
    x,y,z = [], [], []
    
    entry_PC =  list
    exit_PC = list
    
    PC_Choices = {"MP35N" : MP35N,
        "CUBE_MP" : CUBE_MP, 
        "CUBE" : CUBE
        }
    PC_Choice = None 
    PC_In_Use = 'MP35N'
    
    PC_Values = {
        "MP35N" : True,
        "CUBE" : False
        }
    
    
    En = []
    HalfMax = str
    NumSim = str
    directory = str
    fig_direc = str
    fig_name = str
    
    NumElements = int
    ChemEl = []
    Stoich = []
    density = int
    
    NumEnergies = int
    
    error_message = str
    
    
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Pressure Cell')
        self.window.geometry('1100x800')
        self.button_Run()
        self.pressure_cell_choice()
        self.make_canvas()
        self.enter_NumEnergies()
        self.enter_FWHMax()
        self.enter_noSim()
        self.enter_Direc()
        self.enter_Num_elements()
        self.enter_Density()
        self.Dynamic_widget_Elements()
        self.Dynamic_widget_Energies()
        self.button_refresh_chem()
        self.button_refresh_En()
        self.OutPut_Stopping_Percentage()
        self.print_results()
        self.enter_fig_direc()
        self.enter_fig_name()
        self.OutPut_Error()

    def run(self):
        while True: 
            self.window.update_idletasks()
            self.window.update()

    def make_canvas(self):
        f = plt.figure(figsize = (10,5))
        ax1 = f.add_subplot(121)
        ax2 = f.add_subplot(122)
        
        canvas = FigureCanvasTkAgg(f, self.window)
        canvas.get_tk_widget().grid(row = 13, column = 0, columnspan = 5, rowspan = 5)
        
        self.plot_hist_button(self.PC_Choice, canvas, ax1)
        self.plot_scatt_button(self.PC_Choice, canvas, ax2)
        self.save_button(ax1)
        
    def plot_hist_button(self, class_name, canvas, ax1):
        buttonHist = tk.Button(self.window, text = 'Plot Histogram', command = lambda: self.PC_Choice.plot_hist(canvas, ax1))
        buttonHist.grid(row = 11, column= 0)
    
    def plot_scatt_button(self, class_name, canvas, ax2):
        buttonHist = tk.Button(self.window, text = 'Plot Scatter', command = lambda: self.PC_Choice.plot_scatt(canvas, ax2))
        buttonHist.grid(row = 12, column= 0)
             
    def button_Run(self):
        
        button = tk.Button(self.window, text = 'Run', command = lambda: self.Run_sim(Process, self.PC_Choice))
        button.grid(row = 12, column = 1)

    def enter_NumEnergies(self):
        tk.Label(self.window, text = 'Number of Momentums').grid(row=0, column = 0)
        
        self.NumEnergies = tk.StringVar(self.window, value = '2')
        NumEnEntry = tk.Entry(self.window, textvariable = self.NumEnergies)
        NumEnEntry.grid(row = 0, column = 1)
    
    def Dynamic_widget_Energies(self):
        tk.Label(self.window, text = 'Momentums (MeV/c)').grid(row = 0, column = 3)
        
        self.En.clear()
        for j in range(0, int(self.NumEnergies.get())):
            entEn = tk.Entry(self.window)
            self.En.append(entEn)
        for k in range(0, int(self.NumEnergies.get())):
            self.En[k].grid(row = k+1, column = 3)
    

    def enter_FWHMax(self):
        tk.Label(self.window, text = 'Full Width Half Maximum Percentage' + '\n' + '(3% at GPD)').grid(row=6, column = 0)
        self.HalfMax = tk.StringVar(self.window, value = '3')
        HalfEntry = tk.Entry(self.window, textvariable = self.HalfMax)
        HalfEntry.grid(row = 6, column = 1)
    
    def enter_noSim(self):
        tk.Label(self.window, text = 'Number of Simulations').grid(row=4, column = 0)
        self.NumSim = tk.StringVar(self.window, value = '100')
        SimEntry = tk.Entry(self.window, textvariable = self.NumSim)
        SimEntry.grid(row = 4, column = 1)
        
    def enter_Direc(self):
        tk.Label(self.window, text = 'SRIM Directory').grid(row=1, column = 6)
        self.directory = tk.StringVar(self.window, value = r'C:/Users/name/...')
        DirecEntry = tk.Entry(self.window, textvariable = self.directory)
        DirecEntry.grid(row = 1, column = 7)
    
    def enter_Num_elements(self):
        tk.Label(self.window, text = 'Number of Elements').grid(row=2, column = 0)
        
        self.NumElements = tk.StringVar(self.window, value = '2')
        ElEntry = tk.Entry(self.window, textvariable = self.NumElements)
        ElEntry.grid(row = 2, column = 1)
    
    def enter_fig_direc(self):
        tk.Label(self.window, text = 'Enter Saving Directory').grid(row = 2, column = 6)
        self.fig_direc = tk.StringVar(self.window, value = r'C:/Users/name/...')
        figentry = tk.Entry(self.window, textvariable = self.fig_direc)
        figentry.grid(row = 2, column = 7)
        
    def enter_fig_name(self):
        tk.Label(self.window, text = 'Enter Saving Name').grid(row = 3, column = 6)
        self.fig_name = tk.StringVar(self.window, value = 'stopping')
        figentry = tk.Entry(self.window, textvariable = self.fig_name)
        figentry.grid(row = 3, column = 7)
    
    def enter_Density(self):
        tk.Label(self.window, text = 'Density (g/cm3)').grid(row=7, column = 0)
        
        self.density = tk.StringVar(self.window, value = '8.43')
        DenEntry = tk.Entry(self.window, textvariable = self.density)
        DenEntry.grid(row = 7, column = 1)
        

    def Dynamic_widget_Elements(self):
        tk.Label(self.window, text = 'Atomic Element').grid(row = 0, column = 4)
        tk.Label(self.window, text = 'Stoichimotry').grid(row = 0, column = 5)
        for j in range(0, int(self.NumElements.get())):
            entChem = tk.Entry(self.window)
            entStoi = tk.Entry(self.window)
            self.ChemEl.append(entChem)
            self.Stoich.append(entStoi)
        for k in range(0, int(self.NumElements.get())):
            self.ChemEl[k].grid(row = k+1, column = 4)
            self.Stoich[k].grid(row = k+1, column = 5)
    
    def refresh(self, list_input):
        #Have to enter as a list!
        for element in list_input:
            for i in range(0, len(element)):
                element[i].grid_forget()
            element.clear()
        print('working')
    
    def button_refresh_chem(self):
        list_in = [self.ChemEl, self.Stoich]
        button = tk.Button(self.window, text = 'Refresh Number of elements', command = lambda: [self.refresh(list_in), self.Dynamic_widget_Elements()] )
        button.grid(row = 3, column= 0)
    def button_refresh_En(self):
        button = tk.Button(self.window, text = 'Refresh Number of Momentums', command = lambda: [self.refresh([self.En]), self.Dynamic_widget_Energies()] )
        button.grid(row = 1, column= 0)
    
    def insamp(self, x, y, z):
        count1 = 0
        g = 0
        while g < len(x):
            x_new = abs(x[g] - filler)
            z_new = abs(z[g])
            r = 3
            if np.sqrt(pow(x_new,2) + pow(z_new,2)) <= r:
                if -6 < y[g] < 6:
                    count1+=1
            g+=1
        return (count1/float(self.NumSim.get())) * 100
    
    def OutPut_Stopping_Percentage(self):
        Output = tk.Text(self.window, bg = 'light cyan', height = 10)
        txt = ''
        for i in range(0, len(self.x)):
            txt += 'Momentum = '+ str(self.En[i].get()) + 'MeV/c, % in sample = '+ str(self.insamp(self.x[i], self.y[i], self.z[i]))+ '%' + "\n"
        for k in range(0, len(self.x)):
            txt += '\n \n \n \n \n \n'
            txt += 'At Momentum = ' + str(self.En[k].get()) + 'MeV/c'+'\n'
            txt += 'x' + '\t' + 'y' + '\t' + 'z' + '\n' 
            for j in range(0, len(self.x[k])):
                txt += str(self.x[k][j]  - filler)+ '\t' + str(self.y[k][j]) + '\t' + str(self.z[k][j]) + '\n' 
            print(k)
        Output.insert(tk.END, txt)        
                
        Output.grid(row = 24, column = 0, columnspan =4, rowspan = 10)
    
    def OutPut_Error(self):
        Output = tk.Text(self.window, bg = 'red', height = 2)
        Output.insert(tk.END, self.error_message)
        Output.grid(row = 24, column = 4, columnspan = 5, rowspan = 2)
        
    
    def save_fig(self, direc, name, ax):
        ax.figure.savefig(str(direc) + str(name) + '.png', dpi = 300)
    
    def save_button(self, ax1):
        buttonscatt = tk.Button(self.window, text = 'Save Figure', command = lambda: self.save_fig(self.fig_direc.get(), self.fig_name.get() , ax1))
        buttonscatt.grid(row = 12, column= 3)
    
    def print_results(self):
        button = tk.Button(self.window, text = 'Print Results', command = lambda: self.OutPut_Stopping_Percentage())
        button.grid(row = 10, column = 1)
        
    def set_label_value(self, text):
        self.PC_Choice = self.PC_Choices[text]()
        self.PC_In_Use = text
        tk.Label(self.window, text = 'Pressure cell in use : ' + str(self.PC_In_Use)).grid(row=9, column = 1, columnspan = 2)
        
    def pressure_cell_choice(self):
        R1 = tk.Button(self.window, text = 'MP35N', command = lambda: self.set_label_value('MP35N'))
        R1.grid(row = 8, column= 0)
        R2 = tk.Button(self.window, text = 'CuBe x MP35N', command = lambda: self.set_label_value('CUBE_MP'))
        R2.grid(row = 9, column= 0)
        R3 = tk.Button(self.window, text = 'CuBe', command = lambda: self.set_label_value('CUBE'))
        R3.grid(row = 10, column= 0)
               
    def Run_sim(self, run_klass, PC_klass):
        self.x.clear()
        self.y.clear()
        self.z.clear()
        layer_dictionary = {}
        for i in range(len(self.ChemEl)):
            layer_dictionary[self.ChemEl[i].get()] = {'stoich' : self.Stoich[i].get()} 
        layers = []
        
        #Variox
        Cop1 = Layer({
            'Cu':{'stoich':1}
            }, density = 8.96, width = 8.0e6)
        N2Sheild =  Layer({
            'Al':{'stoich':1}
            }, density = 2.7, width = 2.0e6)
        Mylar = Layer({
            'Al':{'stoich':1}
            }, density = 2.7, width = 1e6)
        Vacuum = Layer({
            'N':{'stoich':1}
            }, density = 10e-20, width = 1e7)
        

        Brass = Layer({
            'Cu':{'stoich':66}, 'Zn':{'stoich':33}
            }, density = 8.73, width = 1.9e7)
        
        
        try:
            sample = Layer(layer_dictionary
                           , density =  float(self.density.get()), width = 6.0e7)
        except ValueError:
            self.error_message = 'Please Check Your Elements :)'
            self.OutPut_Error()
            raise
        #this represents the crystat - pressure cell - sample - pressure cell setup at GPD
        layers.append(Mylar)
        layers.append(N2Sheild)
        layers.append(Cop1)
        layers.append(Vacuum)
        layers.append(Brass)
        
        try:
            for element in PC_klass.side1:
                layers.append(element)
        except AttributeError:
            self.error_message = 'Please Select a Pressure Cell First :)'
            self.OutPut_Error()
            print(self.error_message)
            raise
        
        layers.append(sample)
        
        for element in PC_klass.side2:
            layers.append(element)
        
        for element in self.En:
            xtemp, ytemp, ztemp = [],[],[]
            try:
                run_klass.MeanP = float(element.get()) * 1e6
            except ValueError:
                self.error_message = 'Please Check Your Momentums :) ' + '\n' + ghost 
                self.OutPut_Error()
                raise
            run_klass.Half_Max_Perc = float(self.HalfMax.get())
            run_klass.Peak_No_Sims = int(self.NumSim.get())
            run_klass.target_layer = layers
            run_klass.srim_direc = self.directory.get()
            dist, xtemp, ytemp, ztemp = run_klass.Gaussian_Beam(run_klass)
            self.x.append(xtemp)
            self.y.append(ytemp)
            self.z.append(ztemp)  
        for i in range(0, len(self.x)):
            print('size ', self.En[i].get(), ' = ', len(self.x[i]))

class Process():
    data = []
    MeanP = float
    Half_Max_Perc = float
    Peak_No_Sims = float
    target_layer = list
    srim_direc = str
    ion_Iden = 'H'
    atom_num = 1
    ion_Mass = 0.1134289259
    
    
    def __init__(self):
        self.Gaussian_Beam()
        self.Print_Vals()
    
    def Print_Vals(self):
        print('MeanP= ', self.MeanP, ', Half_Max_Perc= ', self.Half_Max_Perc, 
              ', Peak_No_Sims= ', self.Peak_No_Sims, ', target_layer= ', self.target_layer, 
              ', ion_Iden= ', self.ion_Iden, ', atom_num= ', self.atom_num, 'ion_Mass= ', 
              self.ion_Mass, 'srim_direc= ', self.srim_direc)
    
    def Gaussian_Beam(self):
        ##SETTING UP ENERGY BEAM
        #Full Width Half Maximum - Energy
        HMP = self.Half_Max_Perc/100
        HM = self.MeanP * HMP
        HM2 = HM/2
        #Sigma in Gaussian
        sig = HM2*np.sqrt(2*np.log(2))
        lowP = self.MeanP - 3*sig
        highP = self.MeanP + 3*sig
        div = (3*sig)/20
        ##Filling a list of energies that are 3 sigmas less than MeanE, up to 3 sigmas above meanE
        ##Using 20 energies either side of meanE, this can be change by increasing number in denominator of div 
        Moms = []
        x = lowP
        while x <= highP:
            Moms.append(x)
            # print(x)
            x+=div
        
        #Setting up a way of getting a number of runs at  given energy that fits the gaussian dist of energies 
        #from here we can work out a scaling factor for each energy in which we turn the y axis on the gaussian into the number of runs that would give a total number of runs we want. 
        Sums = 0
        Gvals= []
        for i in Moms:
            y = ((1)/(sig*np.sqrt(2*np.pi))) * np.exp(-(1/2) * pow((((i-self.MeanP)/(sig))), 2))
            Gvals.append(y)
            Sums += y 
        scale = self.Peak_No_Sims/Sums
        print("scale ", self.MeanP,  " = ", scale)
        num_runs = []
        for i in Gvals:
            num_runs.append(round(i*scale, 0))
        
        #this is the total number of runs that will be executed, because of the major approximations above, it will usually be less than the target, but not by enough to notice i.e 10input -> 9total, 1000input -> 997total
        area2 = 0
        for i in num_runs:
            area2 += i
        print("total = ", area2)
        
        Ens = []
        for i in Moms:
            E = np.sqrt(pow(i,2) + pow(105.6583755e6, 2)) - 105.6583755e6
            Ens.append(E)
        
        ##RUNNING TRIM CALCULATIONS
        #Setting up target layers
        target = Target(self.target_layer)
        #Initialising Depth Arrays
        x = []
        y = []
        z = []
        
        #Setting up trim.dat file
        #this is a file that cna be used as a trim input instead of running single simultions at different energies
        #this allows one ot control the intial energy, (x,y,z) positions an also offset angles
        intro = ['Ûßßßßßßßßßßßßßßßß  TRIM - Recoil Cascade Data File ßßßßßßßßßßßßßßßßßßßßßßßßßßßÛ', 
                'Û Top  10 lines are user comments,  with  line  #8 describing experiment.     Û', 
                'Û Line #8 will be written into all TRIM output files ( various files:  *.TXT).Û',
                'Û Data Table line consist of: EventName(5 char)+9 numbers separated by spaces.Û',
                'Û The Event Name consists of any 5  characters  to identify that line.        Û',
                'Û Cos(X) = 1 for normal incidence, and Cos(X) = -1  for backwards.            Û',
                'ßßßßßßßßßßßßßßßß Typical Data File is shown below  ßßßßßßßßßßßßßßßßßßßßßßßßßßßß',
                'ÉÍÍÍ  Depth of muons in Sample ÍÍÍÍÍÍÍÍÍÍÍ»',
                'Event  Atom  Energy  Depth   Lateral-Position   ----- Atom Direction ----',
                'Name   Numb   (eV)    _X_(A)   _Y_(A)  _Z_(A)   Cos(X)   Cos(Y)   Cos(Z)']
        rest = []
        with open(self.srim_direc + '\TRIM.dat', 'w') as tdat:
            for i in intro:
                tdat.write(i+'\n')
            j = 0 
            while j<len(num_runs):
                count = 0
                while count < num_runs[j]:
                    #Here we can use either a standard random distrubution of positions in the collimation space, a truncated normal distribtion, or a straight beam
                    #This is set up for the GPD collimation with some aditional angles input. 
                    line = self.ion_Iden + '      ' + '1'+ ' ' + str(Ens[j]) + ' ' + '0' + ' ' + str(np.random.normal(0, 2e7)) + ' ' + str(np.random.normal(0, 5e7)) + ' '+ '1.0' + ' '+ str(random.uniform(-5, 5)) + ' '+ str(random.uniform(-5, 5)) 
                    rest.append(line)
                    count+=1
                j+= 1
            for k in rest:
                tdat.write(k + '\n')
        #Now the trim.dat file is filled
        #Setting up all left over information needed for the simulation
        #As using trim.dat file (), can use energy = Ens[-1] and number_ions = 9999, since all this info is contained in trim.dat file
        #Calculation = 4 is for using trim.dat file
        ion = Ion(identifier= self.ion_Iden, mass = self.ion_Mass, energy = Ens[-1])
        trim = TRIM(target, ion, number_ions = 9999, calculation = 4, ranges = 1)
        srim_executable_directory = self.srim_direc
        results = trim.run(srim_executable_directory)
        with open(self.srim_direc + '\SRIM Outputs\RANGE_3D.txt') as temp:
            for line in temp: 
                l = line.split()
                # print(l)
                if line.startswith('00'):
                    ##Converting to mm
                    x.append(float(l[1]) * pow(10,-7))
                    y.append(float(l[2]) * pow(10,-7))
                    z.append(float(l[3]) * pow(10,-7))
        depth_list = results.range.depth
        return depth_list, x, y, z

overview = GUI()
overview.run()