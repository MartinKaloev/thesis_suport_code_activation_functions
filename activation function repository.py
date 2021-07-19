#start
#this is example for activation function in neural networks
#Martin Kaloev 2021
#Notes for thesis work part 1: activation functions

#!!!!!!!!!!!!!!!!!!
#please be mindfull that this is example lib and not working file, so modifie it into corect extension for Notepad jupiter lab 

#example use Import [name class] exmp; import linear
#example use Import sigmoid.set_input(your imput) ; exmp: import sigmoid \n sigmoid s \n s.set_input(9)
#!!!!!!!!!!!!!!!!

#linear
#sigmoid forward and deriv
#relu
#relu paramateric
#elu
#tanh
#softmax


import math

class linear:

 def __init__(self):
   self.__input_signal = 1

 def act_output(self):
   print('activation output: {}'.format(self.__input_signal))

 def set_input(self, input_):
   self.__input_signal = input_

class sigmoid:

 def __init__(self):
   self.__input_signal = 1

 def act_output(self):
   print('activation output: {}'.format(self.__input_signal))

 def set_input(self, input_):
   self.__input_signal = input_

 def sigmoid_for(self):
    self.__input_signal= 1 / (1 + math.exp(self.__input_signal))
    return self.__input_signal
 
 def sigmoid_der(self):
    der=sigmoid.sigmoid_for()
    dervite=der*(1-der)
    return dervite


class relu:

 def __init__(self):
   self.__input_signal = 1

 def act_output(self):
   print('activation output: {}'.format(self.__input_signal))

 def set_input(self, input_):
   self.__input_signal = input_

 def relu_der(self):
    return max(0.0,self.__input_signal)

class parametric_relu_and_leaky_relu:

 def __init__(self):
   self.__input_signal = 1
   self.__paramet = 0.1

 def coment(self):
    print('default parametris is 0.1')

 def act_output(self):
   print('activation output: {}'.format(self.__input_signal))

 def set_input(self, input_):
   self.__input_signal = input_

 def set_parameter(self , parameter):
    self.__paramet = parameter

 def parametric_relu_der(self):
    if self.__input_signal > 0:
        return self.__input_signal
    else:
        return self.__paramet*self.__input_signal

class Elu:

 def __init__(self):
   self.__input_signal = 1
   self.__a_parameter = 1.0

 def act_output(self):
   print('activation output: {}'.format(self.__input_signal))

 def set_input(self, input_):
   self.__input_signal = input_

 def Elu_for(self):
    if self.__input_signal >=0:
        return self.__input_signal
    else:
        return self.__a_parameter*(math.e^self.__input_signal-1)

 def Elu_der(self):
    if self.__input_signal >0:
        return 1
    else:
        self.__a_parameter*math.exp(self.__input_signal)


class tanh:

 def __init__(self):
   self.__input_signal = 1
   

 def act_output(self):
   print('activation output: {}'.format(self.__input_signal))

 def set_input(self, input_):
   self.__input_signal = input_

#########
#(e^x-e^(-x))/(e^x+e^(-x))
###########
 def tanh_for(self):
    return math.tanh(self.__input_signal)
 
 def tanh_der(self):
    return 1- tanh.tanh_for*tanh.tanh_for



class softmax:

 def __init__(self):
   self.__input_vector = []
   self.__pobability_vector=[]
   self.exp_sumury=1.0
   


 def set_input(self, input_):
   self.__input_vector.append(input_)

 def expos_sumury(self):
    self.exp_sumury=0
    for i in self.__input_vector:
        self.exp_sumury=self.exp_sumury+math.exp(i)
    return self.exp_sumury

 def probability(self):
    for i in self.__input_vector:
        self.__pobability_vector.append(i/self.exp_sumury)
    
