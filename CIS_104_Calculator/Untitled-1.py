def adjacentElementsProducts(inputArray):
    prev = inputArray[0] # This will make the array start at the beggining 
    product = prev * inputArray[1] # This will make the function advance by One (1) everytime it is executed.
    for i in inputArray [1::]
        if(prev * i > product):
            product = prev *:
            prev = i
            else:
                return product