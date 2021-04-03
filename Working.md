for partition in partitions
    current weight is reset to 0
    for i in partition:
        get the cow weight and add to current weight.
        if weight exceeds the condition then move on.

if all partitions meet the condition then check the length of partitions
if it is shorter then the best solution, then make this the new solution and save the list and length

for cow in cows:
    add cow weight to current weight
        if the weight is greater than limit then 
        append the current journey to journeys
        create a new journey
        set weight to 0
        add that cow & weight to it
        
        else add the cow to the current journey