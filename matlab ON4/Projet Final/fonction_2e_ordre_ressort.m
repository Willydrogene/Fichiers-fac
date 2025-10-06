%dx²/dt² + (k(x-x0))/m = g
function[dz_point_dt] = fonction_2e_ordre_ressort(k, z, z0, m, g)
  dz_point_dt = -g - (k/m)*(z-z0);
end
