
x_100 = a + (b-a).*rand(1,100)

x_1000 = a + (b-a).*rand(1,1000)
x_10000 = a + (b-a).*rand(1,10000)
x_100000 = a + (b-a).*rand(1,100000)

liste_x = {x_100; x_1000; x_10000; x_100000}

disp(x_100(1))
disp(liste_x{1}(1))

disp(['on a: ', num2str(length(liste_x{1}))])