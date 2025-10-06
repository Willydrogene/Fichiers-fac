clc
n = [10,100,1000,10000]; %
for i = 1 : length(n)
    elem = n(i);
    tableau = (rand(1,elem) * 10);
    [moyenne, ecartype] = moyect(tableau);
    disp(['L''élément ', num2str(i), ' : ', num2str(tableau), newline]);
    disp(['La moyenne des ', num2str(n(i)), ' éléments est: ', num2str(moyenne)])
    disp(['L''écartype des ', num2str(n(i)), ' éléments est: ', num2str(ecartype), newline newline])
end

