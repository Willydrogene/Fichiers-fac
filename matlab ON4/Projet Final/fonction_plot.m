function[] = fonction_plot(t, z, z_point, ep, ec, em, titre2)
  graphics_toolkit gnuplot
  % Créer une nouvelle figure avec une taille personnalisée
  figure('Position', [100, 100, 800, 600]); % [left, bottom, width, height]

  % Tracer la fonction
  subplot(2,2,1);
  plot(t, z, color='r');
  xlabel('Temps');
  ylabel('Position');
  legend('Balle');
  titre = ['Balle qui rebondit : ', titre2];
  title(titre);

  subplot(2,2,2);
  plot(t, z_point, color='b');
  xlabel('Temps');
  ylabel('Vitesse');
  legend('Vitesse Balle');
  title(titre);

  subplot(2,2,[3,4]);
  plot(t, ep, 'g', 'DisplayName', 'Énergie potentielle');
  hold on; % Permet de garder le même graphique ouvert pour ajouter les autres courbes
  plot(t, ec, 'b', 'DisplayName', 'Énergie cinétique');
  plot(t, em, 'r', 'DisplayName', 'Énergie mécanique');
  xlabel('Temps [s]');
  ylabel('Énergie [J]');
  titre = ['Énergies Balle : ', titre2];
  title(titre);
  legend('Ec', 'Ep', 'Em'); % Légende
end
