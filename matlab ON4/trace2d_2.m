clear all;


% Définition des valeurs de x et y
[x, y] = meshgrid(-5:0.1:5, -5:0.1:5);

% Calcul de f(x, y)
f = (x - 2) .* (x + 3) .* (y - 3) .* (y + 2);

% Tracé de la courbe avec contourf et différentes palettes de couleurs
figure;

contourf(x, y, f, 'LineColor', 'none');
colorbar;
colormap(colorcube);
title('Palette de couleurs : Hot');
