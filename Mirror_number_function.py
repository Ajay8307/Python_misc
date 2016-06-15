#! python3
# Mirror_number_function.py - Function determines if a number is a mirror number

def mirror(num):
    """ Function to determine if a number is a mirror number or not"""
    li=list(str(num))
    length = len(li)
    for i in range(length//2):
        if li[i]!=li[length-i-1]:
            print("Not a mirror number")
            return
    print("Mirror number!")
    
    
