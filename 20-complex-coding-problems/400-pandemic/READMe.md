# Covid Pandemic

We have an array of n homes in a town (1 to n). It is found on a given day that some of these houses {i,j,k... index} are 
infected with the covid virus. It is guranted that on the next day the nearest neighbour houses will also get infected i.e.{i+1 and i-1}.
You have to find out in how many ways can the whole town be infected.

## example:

lets say 6 houses    {1,2,3,4,5,6}

infected house num {3,5}

on the fist day of infection = {2,4,6} Total ways = 6  
Infection can be spread in 6 different ways
i.e. 

{2,4,6} => first 1 then 4 then 6  
{2,6,4} => first 1 then 2 then 4  
{4,2,6} => first 4 then 1 then 6  
{4,6,1}  
{6,2,4}  
{6,4,1}  

on the second day : {1} total ways = 1

Now all houses are infected total ways = 6*1 = 6 different ways
