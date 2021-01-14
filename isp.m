dg = 0.01;
gamma = 0.07;

t =  norminv((2 - gamma) / 2);
display(t)
K = ceil(t^2 / (4 * dg^2));
display(K)