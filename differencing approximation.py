import numpy as np

p = np.array ([-4, 7, 3, -9])
p_fder = np.polyder(p)
p_fder_value = np.polyval(p_fder, 0)
print ("The value of polynomial at x=0 after differentiation: ", p_fder_value)
#grid spacing 
h = 0.25
P_value = np. polyval(p,0)
#Forward differencing method
p_for_der_value = (np.polyval(p,0.25)-P_value)/0.25
print("Approximation using forward differencing method: ",p_for_der_value)
#Backward differencing method
p_back_der_value = (P_value-np.polyval(p,-0.25))/0.25
print("Approximation using backward differencing method: ", p_back_der_value)
#Central differencing method
p_central_der_value = (np.polyval(p,0.25)-np.polyval(p,-0.25))/(2*h)
print("Approximation using central differencing method: ", p_central_der_value)
#Error calculation
for_forward = np.abs(p_fder_value-p_for_der_value)/p_fder_value
for_backward = np.abs(p_fder_value-p_back_der_value)/p_fder_value
for_central = np.abs(p_fder_value-p_central_der_value)/p_fder_value

print ("The error for forward, backward, and central differencing approximation is respectively: ", for_forward, for_backward, for_central)