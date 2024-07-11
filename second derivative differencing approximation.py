#Let a equation of fourth order (10x^4+4x^3-12x^2-5x-6)
import numpy as np
poly = np.array([10, 4, -12, -5, -6])
poly_der = np.polyder(poly)
poly_val = np.polyval(poly, 0)
poly_val_der = np.polyval(poly_der, 0)
poly_der_der = np.polyder(poly_der)
poly_der_der_val = np.polyval(poly_der_der, 0)

print("The actual value: ", poly_der_der_val)

#grid spacing 
h=0.125

#central differencing method 

poly_central_der_value = (np.polyval(poly, h)-2*poly_val+np.polyval(poly, -h))/(h**2)
error_central_der_value = np.abs((poly_central_der_value-poly_der_der_val)/poly_der_der_val)

print("The aprroximated value using central differencing method and the error: ", poly_central_der_value, error_central_der_value)

#forward differencing method

poly_forward_der_value = (np.polyval(poly,2*h)-2*np.polyval(poly, h)+poly_val)/(h**2)
error_forward_der_value = np.abs((poly_forward_der_value-poly_der_der_val)/poly_der_der_val)

print("The approximated value using forward differencing method and the error: ", poly_forward_der_value, error_forward_der_value)

#backward differencing method

poly_backward_der_value = (poly_val-2*np.polyval(poly, -h)+np.polyval(poly, 2*h))/(2**h)
error_backward_der_value = np.abs((poly_backward_der_value-poly_der_der_val)/poly_der_der_val)

print("The approximated value using backward differencing method and the error: ", poly_backward_der_value, error_backward_der_value)
