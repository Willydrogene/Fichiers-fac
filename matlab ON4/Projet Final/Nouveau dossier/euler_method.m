function[z, z_point, ep_euler, ec_euler, em_euler] = euler_method(z, z_point, dt, Nt, k, z0, m, g, Cx, rho, S, alpha, ep_euler, ec_euler, em_euler)
  % Compteur de pourcentage
  progress = 0; % Initialisation du pourcentage
  for i=1 : Nt-1
    if z(i)>0.30000
      z(i+1) = z(i) + dt*z_point(i);
      z_point(i+1) = z_point(i) + dt*fonction_2e_ordre_chute_libre(g, Cx, rho, S, z_point(i));
    elseif z(i)<=0.3 && z(i)>0
      z(i+1) = z(i) + dt*z_point(i);
      z_point(i+1) = z_point(i) + dt*fonction_2e_ordre_ressort(k, z(i), z0, m, g, alpha, z_point(i));
    elseif z(i)==0
      z(i+1) = dt*z_point(i);
      z_point(i+1) = z_point(i) + dt*fonction_2e_ordre_ressort(k, z(i), z0, m, g, alpha, z_point(i));
    end
    
    % Calcul de l'énergie à chaque instant t
    ep_euler(i) = m * g * z(i);
    ec_euler(i) = 0.5 * m * z_point(i)^2;
    em_euler(i) = ep_euler(i) + ec_euler(i);

    % Calcul du pourcentage d'avancement
    new_progress = floor((i / Nt) * 100);
    % Si le pourcentage a changé, on l'affiche
    if new_progress ~= progress
        disp(['Avancement : ', num2str(new_progress), '%']);
        progress = new_progress;
    end

  end
end
