import pandas as pd
import numpy as np

class noisy_or():
    def __init__(self,states):
        self.states = states
        
    def fit(self,variables,inhibition_probability):
        if type(variables) != list:
            raise ValueError(f"Variables Names should be in the list. Eg [\"x1\",\"x2\",\"x3\"]. You provided {variables}")
            
        if type(inhibition_probability) != list:
            raise ValueError(f"Inhibition Probability should be list. Eg [0.3,0.2,0.1]. You provided {inhibition_probability}")
            
        if len(variables) != len(inhibition_probability):
            raise ValueError(f"Length of variable names and inhbition probability mismatch. {len(variables)}!={len(inhibition_probability)} ")
        
        if all(x <=1  for x in inhibition_probability) == False:
            raise ValueError(f"Inhibition Probablilities should be less than 1. You provided {inhibition_probability}")
        self.variables = variables
        self.inhibition_probability= inhibition_probability
    
    def predict(self,values):
         if all(x <self.states  for x in values) == False:
             raise ValueError(f"Values  should be less than give state {self.states}. States start from Zero. You provided {values}")
            
         self.values = values
         return (1 - np.prod(np.power(self.inhibition_probability,self.values)))
