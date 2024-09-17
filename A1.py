# Mean and Median calculator functions

def meanavg(arr): # Definition of the mean function
    lArr = len(arr) # We retrieve the size of the list, aka how many items.
    tmpSum = 0.0 # We then create a temporary variable to store the sum
    for i in arr: tmpSum += i # Now we are in a loop. This loop runs exactly as much as the amount of items in the list
    # For each iteration in the loop, we add the designated element to the tmpSum variable

    # Now that we have the sum, we need to perform this formula for mean:
    # Sum of all elements divided by number of items...
    return float(tmpSum/lArr) # Thus, the calculation is performed, converted to a decimal, and returned.

def medianavg(arr): # Definition of the median function
    # The way the median works is we don't calculate the average,
    # but rather the middle position of all the elements sorted in
    # ascending order...

    # So we create our own array to modify so it's not volatile:
    medianArr = arr

    # And now we sort it...
    medianArr = medianArr.sort()

    # How big is the list of items?
    arrSize = len(arr)

    

    # Now we want to find the middle element, but there's an issue...
    # See, what if it's an even number of items? Now there's two
    # middle elements... That's why we check it first

    if arrSize%2==0: # Is the list size even?
        # If it is, then we need to get the two middle items and mean average them...

        result = medianArr[arrSize/2] # Let's save the left middle one
        result += medianArr[arrSize/2+1] # Now let's add the right middle one
        result = result/2 # Let's divide by two to complete the mean

    else: # but what if it's odd?
        # There's no work needed :)
        result = medianArr[
            arrSize//2 # See we floor divide the length by two so we don't have a decimal.
        ]

    # And the function is complete!

myNumbers = [
    1, 7, 4, 5, 5, 7, 8, 2
]

print("List:", myNumbers)
print("Mean:", meanavg(myNumbers))
print("Mean:", medianavg(myNumbers))

