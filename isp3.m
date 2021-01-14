p_e = 0.1;
p_c = 1-p_e; % ����������� ������
d_g = 0.1 * p_e; % ������������� ��������, ��� 25% �� ������
gamma = 0.07; % �����, ������� ����������
 
t_critical = norminv((2 - gamma) / 2);
K = ceil((t_critical * t_critical * p_c * (1 - p_c)) / (d_g * d_g));
 
disp(K);
