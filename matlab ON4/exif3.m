clear all
% 24, 35, 49 et 60
z = input('z nombre entier =?')
clc

disp(mod(z,2))
disp(mod(z,3))
disp(mod(z,5))

%if (mod(z,2) == mod(z,3)) && (mod(z,3) == mod(z,5))
%    disp([num2str(z), ' est divisible par 2, 3 et 5'])
%end

if (mod(z,2) == 0 && mod(z,3) == 0 && mod(z,5) == 0)
    disp([num2str(z), ' est divisible par 2, 3 et 5'])
elseif (mod(z,2) ~= 0 && mod(z,3) ~= 0 && mod(z,5) ~= 0)
    disp([num2str(z), ' n''est  pas divisible par 2, 3 et 5'])
elseif mod(z,2)==0 | mod(z,3) == 0 | mod(z,5) == 0
    if mod(z,2)==0
        disp([num2str(z), ' est divisible par 2'])
    end
    if mod(z,3)==0
        disp([num2str(z), ' est divisible par 3'])
    end
    if mod(z,5)==0
        disp([num2str(z), ' est divisible par 5'])
    end
end