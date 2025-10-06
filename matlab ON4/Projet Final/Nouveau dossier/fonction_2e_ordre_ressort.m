%dx²/dt² + (k(x-x0))/m = g
function[dz_point_dt] = fonction_2e_ordre_ressort(k, z, z0, m, g, alpha, z_point)
  dz_point_dt = -g - (k/m)*(z-z0) - alpha*z_point;  % 3*pi*0.6*1.8*10^(-5)*z_point*5000
end
