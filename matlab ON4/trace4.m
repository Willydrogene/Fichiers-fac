clear all;

% Générer le vecteur x (abscisses)
x = -pi : 2*pi/10 : pi;

% Générer les vecteurs y1, y2, y3, y4, y5, y6
y1 = cos(x);
y2 = cos(x).^2;
y3 = sin(x);
y4 = sin(x).^2;
y5 = x / 3;
y6 = x.^2 / 10;

% Tracer les figures
figure;

% Tracer y1 et y2 dans la 1e figure en haut à gauche
subplot(2, 2, 1);
plot(x, y1, 'b', x, y2, 'r');
xlabel('AXE X');
ylabel('AXE Y');
title('Y1 et Y2');

% Tracer y3 et y4 dans la 2e figure en haut à droite
subplot(2, 2, 2);
plot(x, y3, 'g', x, y4, 'y');
xlabel('AXE X');
ylabel('AXE Y');
title('Y3 et Y4');

% Tracer y5 dans la 3e figure en bas à gauche
subplot(2, 2, 3);
plot(x, y5, 'm');
xlabel('AXE X');
ylabel('AXE Y');
title('Y5');

% Tracer y6 dans la 4e figure en bas à droite
subplot(2, 2, 4);
plot(x, y6, 'c');
xlabel('AXE X');
ylabel('AXE Y');
title('Y6');
