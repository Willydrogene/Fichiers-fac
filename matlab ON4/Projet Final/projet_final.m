% P=mg jusqu'à >=30cm Donc -mg=ma => -g=a, <30cm on a P=mg et Fr = -k(l-l0) Donc P+Fr=ma => -mg-k(x-x0)=m(d²z/dt²) => dx²/dt² + (k(x-x0))/m = -g
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% delta=-4
clear all
close all
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Conditions de l'expérience %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%% Conditions initiales %%%%%%%%%%%%%%%%%%%%%%%%
tmin = 0;                                    % début de l'expérience  en s
tmax = 6;                                    % fin de l'expérience    en s
dt = 0.0001;                                 % temps infinitésimal pour la précision
m = 1;                                       % masse                  en  kg
g = 9.81;                                    % pesanteur              en  m/s²
z0 = 0.3;                                    % longueur du ressort à l'équilibre (rayon ballon)
k = 5000;                                    % constante de raideur du ressort
alpha = 10*m;                                % frottements inélastiques
Cx = 0.45;                                   % coefficient de résistance « aérodynamique »
rho = 1.22;                                  % masse volumique de l'air en kg/m³
S = 2*pi*z0^2;                               % maître-couple, section droite perpendiculaire au mouvement

hauteur_initiale = 30;                        % on lache le ballon à 3m de haut
vitesse_initiale = 0;                        % on peut lancer le ballon vers le bas pour voir ce qu'il se passe

%%%%%%%%%%%%%%%%%%%%%%%% Création de tableaux %%%%%%%%%%%%%%%%%%%%%%%%
Nt = floor((tmax - tmin) / dt) + 1;          % Calcul du nombre total d'échantillons
t = linspace(tmin, tmax, Nt);                % Générer un vecteur de temps linéairement espacé

%%%%%%%%%% Méthode d'Euler %%%%%%%%%%
z = zeros(1, Nt);                            % Créer un vecteur x de taille Nt avec des zéros
z_point = zeros(1, Nt);                      % Créer un vecteur x_point de taille Nt avec des zéros
ep_euler = zeros(1, Nt);
ec_euler = zeros(1, Nt);
em_euler = zeros(1, Nt);
%%%%%%%% Méthode de Verlet %%%%%%%%%%
z_verlet = zeros(1, Nt);                            % Créer un vecteur x de taille Nt avec des zéros
z_point_verlet = zeros(1, Nt);                      % Créer un vecteur x_point de taille Nt avec des zéros
ep_verlet = zeros(1, Nt);
ec_verlet = zeros(1, Nt); 
em_verlet = zeros(1, Nt);


z(1) = hauteur_initiale;         z_point(1) = vitesse_initiale;
z_verlet(1) = hauteur_initiale;  z_point_verlet(1) = vitesse_initiale;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Appel de la fonction %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%% SANS FROTTEMENTS %%%%%%%%
%[z, z_point, ep_euler, ec_euler, em_euler] = euler_method(z, z_point, dt, Nt, k, z0, m, g, ep_euler, ec_euler, em_euler);
%[z_verlet, z_point_verlet, ep_verlet, ec_verlet, em_verlet] = verlet_method(z_verlet, z_point_verlet, dt, Nt, k, z0, m, g, ep_verlet, ec_verlet, em_verlet);

%z_point = abs(z_point);
%z_point_verlet = abs(z_point_verlet);

%fonction_plot(t, z, z_point, ep_euler, ec_euler, em_euler, 'Euler')
%fonction_plot(t, z_verlet, z_point_verlet, ep_verlet, ec_verlet, em_verlet, 'Verlet')
%%%%%%%% AVEC FROTTEMENTS %%%%%%%%
[f_z, f_z_point, f_ep_euler, f_ec_euler, f_em_euler] = frott_euler_method(z, z_point, dt, Nt, k, z0, m, g, Cx, rho, S, alpha, ep_euler, ec_euler, em_euler);
[f_z_verlet, f_z_point_verlet, f_ep_verlet, f_ec_verlet, f_em_verlet] = frott_verlet_method(z_verlet, z_point_verlet, dt, Nt, k, z0, m, g, Cx, rho, S, alpha, ep_verlet, ec_verlet, em_verlet);

f_z_point = abs(f_z_point);
f_z_point_verlet = abs(f_z_point_verlet);

fonction_plot(t, f_z, f_z_point, f_ep_euler, f_ec_euler, f_em_euler, 'Euler frott')
fonction_plot(t, f_z_verlet, f_z_point_verlet, f_ep_verlet, f_ec_verlet, f_em_verlet, 'Verlet frott')

%disp(['z= ', num2str(z_verlet)])
%disp(['z_point = ', num2str(z_point)])
%disp(f_z_point_verlet(1:100))

disp(['Avancement : ', num2str(100), '%']);
