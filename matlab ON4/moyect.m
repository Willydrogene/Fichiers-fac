function[moyenne, ecartype] = moyect(tableau)
    plus = 0;
    for i = 1 : length(tableau)
        plus = plus + tableau(i);
    end

    moyenne = plus / length(tableau);


    liste_ecart_type = [];
    somme = 0;
    for i=1 : length(tableau)
        valeur = (tableau(i)-moyenne)^2;
        somme = somme + valeur;
    end

    ecartype = sqrt(somme / (length(tableau)-1));
end



