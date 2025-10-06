clear all

x = randi([0,10], 1)

clc

if x > 5
    disp(['x est plus grand que 5, x=', num2str(x)])
elseif x == 5
    disp(['x est égal à 5, x=', num2str(x)])
else 
    disp(['x est inférieur à 5, x=', num2str(x)])
end