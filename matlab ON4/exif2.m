clear all

y = randi([-5,5], 1)

clc

if y <= -2
    disp(['y est plus petit ou égal à -2, y=', num2str(y)])
elseif y > -2 && y < 2
    disp(['y est compris entre -2 et 2, y=', num2str(y)])
else
    disp(['y est supérieur ou égal à 2, y=', num2str(y)])
end