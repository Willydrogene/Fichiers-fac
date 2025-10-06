clear all
%carre =  [ -1 ≤x≤1 ; -1 ≤x≤1 ] 100, 1000, 10000, 100000 

a = -1;
b = 1;

x_100 = a + (b-a).*rand(1,100);
x_1000 = a + (b-a).*rand(1,1000);
x_10000 = a + (b-a).*rand(1,10000);
x_100000 = a + (b-a).*rand(1,100000);
x_1000000 = a + (b-a).*rand(1,1000000);

y_100 = a + (b-a).*rand(1,100);
y_1000 = a + (b-a).*rand(1,1000);
y_10000 = a + (b-a).*rand(1,10000);
y_100000 = a + (b-a).*rand(1,100000);
y_1000000 = a + (b-a).*rand(1,1000000);

liste_x = {x_100; x_1000; x_10000; x_100000; x_1000000};
liste_y = {y_100; y_1000; y_10000; y_100000; y_1000000};
clc
liste_points = [];

for p=1 : length(liste_x)
    points_int = 0;
    for n=1 : length(liste_x{p})
        if ((liste_x{p}(n))^2 + (liste_y{p}(n))^2) <= 1
            points_int = points_int + 1;
        end
    end
    liste_points = [liste_points, points_int];
end


for i = 1 : length(liste_points)
    disp(['pi_', num2str(length(liste_x{i})), ' = ', num2str(4 * liste_points(i)/length(liste_x{i}))]);
end
disp(['liste de points intérieur: ', num2str(liste_points)]);