clear all;

% Définition des valeurs de x et y
[x, y] = meshgrid(-10:0.1:10, -10:0.1:10);

% Calcul de r
r = sqrt(x.^2 + y.^2);

% Initialisation de f
f = zeros(size(r));

% Calcul de f en tenant compte du cas où r est égal à 0
indices_r_nul = (r == 0);
f(indices_r_nul) = 1; % Si r est égal à 0, f(x, y) = 1
indices_r_non_nul = ~indices_r_nul;
f(indices_r_non_nul) = sin(r(indices_r_non_nul)) ./ r(indices_r_non_nul);


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%CA%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Tracé de la surface
surf(x, y, f);
xlabel('X');
ylabel('Y');
zlabel('f(x, y)');
title('Surface de f(x, y)');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%OU CA%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Tracé des lignes de contour
%figure;
%contour(X, Y, f);
%xlabel('X');
%ylabel('Y');
%title('Lignes de contour de f(x, y)');

% Tracé des zones remplies entre les lignes de contour
%figure;
%contourf(X, Y, f);
%xlabel('X');
%ylabel('Y');
%title('Zones remplies entre les lignes de contour de f(x, y)');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%