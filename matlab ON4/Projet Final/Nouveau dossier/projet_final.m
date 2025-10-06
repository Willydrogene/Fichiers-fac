% P=mg jusqu'à >=30cm Donc -mg=ma => -g=a, <30cm on a P=mg et Fr = -k(l-l0) Donc P+Fr=ma => -mg-k(x-x0)=m(d²z/dt²) => dx²/dt² + (k(x-x0))/m = -g
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% delta=-4
clear all

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Conditions de l'expérience %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%% Conditions initiales %%%%%%%%%%%%%%%%%%%%%%%%
tmin = 0;                                    % début de l'expérience  en s
tmax = 6;                                    % fin de l'expérience    en s
dt = 0.0001;                                 % temps infinitésimal pour la précision
m = 1;                                       % masse                  en  kg
g = 9.81;                                    % pesanteur              en  m/s²
z0 = 0.3;                                    % longueur du ressort à l'équilibre (rayon ballon)
k = 5000;                                    % constante de raideur du ressort
alpha = 10*m                                 % frottements inélastiques
Cx = 0.45;                                   % coefficient de résistance « aérodynamique » 
rho = 1.22;                                  % masse volumique de l'air en kg/m³  
S = 2*pi*z0^2;                               % maître-couple, section droite perpendiculaire au mouvement

hauteur_initiale = 30;                        % on lache le ballon à 3m de haut
vitesse_initiale = 0;                        % on peut lancer le ballon vers le bas pour voir ce qu'il se passe

%%%%%%%%%%%%%%%%%%%%%%%% Création de tableaux %%%%%%%%%%%%%%%%%%%%%%%%
Nt = floor((tmax - tmin) / dt) + 1;          % Calcul du nombre total d'échantillons
t = linspace(tmin, tmax, Nt);                % Générer un vecteur de temps linéairement espacé

z = zeros(1, Nt);                            % Créer un vecteur x de taille Nt avec des zéros
z_point = zeros(1, Nt);                      % Créer un vecteur x_point de taille Nt avec des zéros
ep_euler = zeros(1, Nt);
ec_euler = zeros(1, Nt);
em_euler = zeros(1, Nt);

z(1) = hauteur_initiale;
z_point(1) = vitesse_initiale;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Appel de la fonction %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[z, z_point, ep_euler, ec_euler, em_euler] = euler_method(z, z_point, dt, Nt, k, z0, m, g, Cx, rho, S, alpha, ep_euler, ec_euler, em_euler);
%disp(['z= ', num2str(z)])
%disp(['z_point = ', num2str(z_point)])

z_point = abs(z_point);

graphics_toolkit gnuplot


% Créer une nouvelle figure avec une taille personnalisée
figure('Position', [100, 100, 800, 600]); % [left, bottom, width, height]


% Tracer la fonction
subplot(2,2,1)
plot(t, z, color='r');
xlabel('Temps');
ylabel('Position');
legend('Balle')
title('Balle qui rebondit');

subplot(2,2,2)
plot(t, z_point, color='b');
xlabel('Temps');
ylabel('Vitesse');
legend('Vitesse Balle')
title('Balle qui rebondit');

subplot(2,2,[3,4]);
plot(t, ep_euler, 'g', 'DisplayName', 'Énergie potentielle');
hold on; % Permet de garder le même graphique ouvert pour ajouter les autres courbes
plot(t, ec_euler, 'b', 'DisplayName', 'Énergie cinétique');
plot(t, em_euler, 'r', 'DisplayName', 'Énergie mécanique');
xlabel('Temps [s]');
ylabel('Énergie [J]');
title('Énergies Balle (Euler)');
legend('Ec', 'Ep', 'Em'); % Légende


disp(['Avancement : ', num2str(100), '%']);
