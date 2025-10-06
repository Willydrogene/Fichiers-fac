clear all;

liste_nb_premiers = [];

for i=1 : 100
  test_nb_premier = true;
  for j=2  : i-1
    if mod(i,j)==0
      test_nb_premier = false;
      break;
    end
  end
  if test_nb_premier
    liste_nb_premiers = [liste_nb_premiers, i];
  end
end


disp(['Les nombres premiers entre 1 et 100 sont:', newline, num2str(liste_nb_premiers)])