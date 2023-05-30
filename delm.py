import pywavelets as pywlt
import elm

class Delm():

    def __init__(self,x,y,elm_type,C,hidden_units) -> None:
        self.x = x
        self.y = y 
        self.elm_type = elm_type
        self.C = C
        self.activate_function = "sigmoid"
        self.hidden_units = hidden_units

    def dwt(data) :
        cA, cD = pywlt.dwt(data,mode="sym")
        return cA, cD

    def train(x,y,activation_function,elm_type,C,hidden_units):

        ELM = elm(hidden_units,activation_function,x,y,C,elm_type,on_hot=True,random_type="normal")
        
        return
    