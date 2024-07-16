# This prints the list number in a set
smallest = None
print("before:", smallest)
for itervar in [3,41,12,9,74,15]:
    if smallest is None or itervar<smallest:
        smallest=itervar
        break
    print("Loop:",itervar,smallest)
print("smallest:",smallest)
