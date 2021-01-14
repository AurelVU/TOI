P_err = 0.1;
gamma = 0.07;
K = 1000;
t = norminv((2 - gamma) / 2);
display(t);
dg = t * sqrt(((1 - P_err) * P_err) / K);
display(dg);