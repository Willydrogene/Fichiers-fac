clear all;
clf;
% Définition du tableau x
x = -20:0.1:20;
n = length(x); % Longueur du tableau x

% Initialisation du tableau y
y = zeros(1, n);

% Calcul des valeurs de y en utilisant une boucle for
for k = 1:n
    if x(k) == 0
        y(k) = 1;
    else
        y(k) = sin(x(k)) / x(k);
    end
end

% Tracer la fonction
plot(x, y);
xlabel('Valeurs de x');
ylabel('Valeurs de y');
title('Graphique de sin(x)/x');
legend('On est là')