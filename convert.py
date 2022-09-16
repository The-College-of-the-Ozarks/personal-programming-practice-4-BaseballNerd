# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s

#Defining Functions
def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

#Converting Inputs to Floats
mph = input("Input speed in mph: ")
mph = float(mph)
inputvalue = input('Would you like 1) Convert to kph, 2) Convert to m/s, 3) Convert to ft/s')
inputvalue = float(inputvalue)

#Creating If Statements


#Printing Answer
print("Speed in kph is", mph_to_kph(mph))

print("Speed in m/s is", mph_to_ms(mph))

print("Speed in ft/s is", mph_to_fts(mph))
