function[z, z_point, ep_euler, ec_euler, em_euler] = euler_method(z, z_point, dt, Nt, k, z0, m, g, ep_euler, ec_euler, em_euler)
  temps_vitesse_nulle = [];
  % Compteur de pourcentage
  progress = 0; % Initialisation du pourcentage
  for n=1 : Nt-1
    if z(n)>0.30000
      z(n+1) = z(n) + dt*z_point(n);
      z_point(n+1) = z_point(n) + dt*fonction_2e_ordre_chute_libre(g);
    elseif (z(n)<=0.3) && (z(n)>0)
      z(n+1) = z(n) + dt*z_point(n);
      z_point(n+1) = z_point(n) + dt*fonction_2e_ordre_ressort(k, z(n), z0, m, g);
    elseif z(n)<(5*dt) && z(n)>(-5*dt)
      z(n+1) = dt*z_point(n);
      z_point(n+1) = z_point(n) + dt*fonction_2e_ordre_ressort(k, z(n), z0, m, g);
    end

    % Calcul de l'énergie à chaque instant t
    ep_euler(n) = m * g * z(n);
    ec_euler(n) = 0.5 * m * z_point(n)^2;
    em_euler(n) = ep_euler(n) + ec_euler(n);

    % Calcul du pourcentage d'avancement
    new_progress = floor((n / Nt) * 100);
    % Si le pourcentage a changé, on l'affiche
    if new_progress ~= progress
      if mod(new_progress,5)==0
        disp(['Avancement Euler: ', num2str(new_progress), '%']);
      end
        progress = new_progress;
    end
    
    if z_point(n)<(5*dt) && z_point(n)>(-5*dt)
      temps_vitesse_nulle = [temps_vitesse_nulle, dt*n];
    end
    
  end
  disp(['vitesse nulle en t = ', num2str(temps_vitesse_nulle)]);
end
