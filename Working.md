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


1b)

create variable for egg weight in basket (set to 0)
avail_weight = target_weight
total_eggs = {}

loop:
    for egg in egg weights:
        num_eggs = avail_weight//egg
        total_eggs[egg] = num_eggs
        remaining_weight = avail_weight % egg
        avail_weight = remaining_weight

check egg weight in basket
if possible to add egg at largest quantity then add that egg
else if not then try again with the next largest egg
repeat until total weight is 99

