%(a=10,b=20,c=30) , (a=4,b=12,c=9) , (a=1,b=16,c=4) , (a=0,b=1,c=-1)

a = input('? a=')
b = input('? b=')
c = input('? c=')

delta = b^2-4*a*c

if a == 0
    disp(['a = 0 donc on ne peut pas diviser par 0.' newline, 'En revanche la racine est x=-c/b soit x=', num2str(-c/b)])
elseif delta > 0
    x1 = (-b-(sqrt(delta)))/(2.*a)
    x2 = (-b+(sqrt(delta)))/(2.*a)
    disp(['Delta=', num2str(delta), ', Il y a deux racines x1=',num2str(x1), ' et x2=', num2str(x2)])
elseif delta == 0
    x = (-b)/(2*a)
    disp(['Delta=', num2str(delta), ', Il n''y a qu''une seule racine x=',num2str(x)])
else
    disp(['Il n''y a pas de racine réelle.'])
end

