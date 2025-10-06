x = 0:1:30;
s1 = 1;
sn = [s1];

for i=2 : length(x)
  sn = [sn, 2 * sn(i-1) +1]
end


plot(x, sn)