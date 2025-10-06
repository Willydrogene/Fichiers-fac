clear all;

% Définition des valeurs de x et y
x0 = 15;
y0 = 25;
[x, y] = meshgrid(-10:1:10, 0:0.1:20);

% Calcul du champ scalaire f(x, y)
f = 10 * sin(2 * pi * x / x0) .* sin(2 * pi * y / y0);

% Calcul du gradient de f
[dfx, dfy] = gradient(f);

% Tracé des isocontours non remplis en bleu
figure;
contour(x, y, f, 'b');

hold on; % Garder la figure active pour le tracé suivant

% Tracé des vecteurs gradient en rouge
quiver(x, y, dfx, dfy, 'r');
hold off;

xlabel('x');
ylabel('y');
title('Isocontours non remplis et vecteurs gradient');
legend('Isocontours (bleu)', 'Vecteurs gradient (rouge)');
