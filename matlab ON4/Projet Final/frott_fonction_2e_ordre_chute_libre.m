function[dz_point_dt] = frott_fonction_2e_ordre_chute_libre(g, Cx, rho, S, z_point)
  dz_point_dt = -g - (1/2)*Cx*rho*S*z_point^2;  % 3*pi*0.6*1.8*10^(-5)*z_point
end
