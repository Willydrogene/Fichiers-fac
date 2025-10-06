# J'utilise Verlet pour plus de précision avec un gros pas de temps dt
function[z_verlet, z_point_verlet, ep_verlet, ec_verlet, em_verlet] = frott_verlet_method(z_verlet, z_point_verlet, dt, Nt, k, z0, m, g, Cx, rho, S, alpha, ep_verlet, ec_verlet, em_verlet)
  temps_vitesse_nulle = [dt]; variable = 0;
  % Compteur de pourcentage
  progress = 0; % Initialisation du pourcentage
  for n = 2 : Nt
    if z_verlet(n-1)>0.30000
      z_half = z_verlet(n - 1) + z_point_verlet(n - 1) * dt / 2;
      temp_z_point_verlet = z_point_verlet(n - 1) + frott_fonction_2e_ordre_chute_libre(g, Cx, rho, S, z_point_verlet(n-1)) * dt;
      z_verlet(n) = z_half + temp_z_point_verlet * dt / 2;
      z_point_verlet(n) = temp_z_point_verlet;
    elseif (z_verlet(n-1)<=0.3) && (z_verlet(n-1)>0.000)
      z_half = z_verlet(n - 1) + z_point_verlet(n - 1) * dt / 2;
      temp_z_point_verlet = z_point_verlet(n - 1) + frott_fonction_2e_ordre_ressort(k, z_half, z0, m, g, alpha, z_point_verlet(n-1)) * dt;
      z_verlet(n) = z_half + temp_z_point_verlet * dt / 2;
      z_point_verlet(n) = temp_z_point_verlet;
      %disp(['entre'])
      %disp(['z = ', num2str(z_verlet(n-1))])
      %disp(['z_point = ', num2str(z_point_verlet(n-1))])
    elseif z_verlet(n-1) == 0.000
      z_half = z_point_verlet(n - 1) * dt / 2;
      temp_z_point_verlet = z_point_verlet(n - 1) + frott_fonction_2e_ordre_ressort(k, z_half, z0, m, g, alpha, z_point_verlet(n-1)) * dt;
      z_verlet(n) = z_half + temp_z_point_verlet * dt / 2;
      z_point_verlet(n) = temp_z_point_verlet;
      disp(['Zeros'])
    end

    % Calcul de l'énergie à chaque instant t
    ep_verlet(n) = m * g * z_verlet(n);
    ec_verlet(n) = 0.5 * m * z_point_verlet(n)^2;
    em_verlet(n) = ep_verlet(n) + ec_verlet(n);

    % Calcul du pourcentage d'avancement
    new_progress = floor((n / Nt) * 100);
    % Si le pourcentage a changé, on l'affiche
    if new_progress ~= progress
        if mod(new_progress, 5)==0
          disp(['Avancement Verlet : ', num2str(new_progress), '%']);
        end
        progress = new_progress;
    end
    
    if z_point_verlet(n)<(5*dt) && z_point_verlet(n)>(-5*dt)
      if temps_vitesse_nulle(end) == (dt*n)-dt
        variable = 1;
      end
      if variable == 0
        temps_vitesse_nulle = [temps_vitesse_nulle, dt*n];
      end
    end
    
  end
  
  if length(temps_vitesse_nulle(2:end)) >= 4
    if (temps_vitesse_nulle(3)-temps_vitesse_nulle(2)) == (temps_vitesse_nulle(end)-temps_vitesse_nulle(end-1))
      periode = ['La période est de T = ', num2str(temps_vitesse_nulle(3)-temps_vitesse_nulle(2))];
    else
      periode = ['La période commence à T = ', num2str(temps_vitesse_nulle(3)-temps_vitesse_nulle(2)), ' et diminue.'];
    end
  end
  disp(['vitesse nulle en t = ', num2str(temps_vitesse_nulle(2:end)), newline, periode]);
  
end
