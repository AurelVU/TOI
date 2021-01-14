p_e = 0.1;
p_c = 1-p_e; % вероятность ошибки
d_g = 0.1 * p_e; % доверительный интервал, тут 25% от ошибки
gamma = 0.07; % гамма, уровень значимости
 
t_critical = norminv((2 - gamma) / 2);
K = ceil((t_critical * t_critical * p_c * (1 - p_c)) / (d_g * d_g));
 
disp(K);
