%���� pr53_rec_gaus_uneq. ������ � ������ ���������� ������������� ��� � 
%���������� ��������� ����������
clear all; close all;
%1.������� �������� ������
n=3;M=2;%%����������� ������������ ������������ � ����� �������
K=1000;%���������� �������������� ���������
%��������� �����������, �������������� �������� � ������� ���������� �������
dm=2.0;%���������� ����� ��������������� ���������� ������� �� ������������ ����
C=zeros(n,n,M); C_=C;%������� ���������� ������� ��������� ��������� �������
pw=[0.6 0.4];
 
pw=pw/sum(pw);
D=3*eye(2);
m=[2 1 -1; 2 -1 2]';
C(:,:,1)=[2 -0.5 -0.3;-0.5 1 -0.5;-0.3 -0.5 1];
C(:,:,2)=[1 -0.3 -0.3;-0.3 1 -0.3;-0.3 -0.3 1];
for k=1:M,
    C_(:,:,k)=C(:,:,k)^-1; 
end;
np=sum(pw); pw=pw/np; %���������� ������������� ������� ��������� ������������
%2.������ ������ ������������ ������ �������������
PIJ=zeros(M); PIJB=zeros(M); mg=zeros(M); Dg=zeros(M); l0_=zeros(M);
for i=1:M,
    for j=i+1:M,
           dmij=m(:,i)-m(:,j); 
           l0_(i,j)=log(pw(j)/pw(i)); 
           dti=det(C(:,:,i)); dtj=det(C(:,:,j));
           trij=trace(C_(:,:,j)*C(:,:,i)-eye(n)); trji=trace(eye(n)-C_(:,:,i)*C(:,:,j));
           mg1=0.5*(trij+dmij'*C_(:,:,i)*dmij-log(dti/dtj)); 
           trij2=trace((C_(:,:,j)*C(:,:,i)-eye(n)) ^ 2); trji2=trace((eye(n)-C_(:,:,i)*C(:,:,j)) ^ 2);
           Dg1=0.5*trij2+dmij'*C_(:,:,j)*C(:,:,i)*C_(:,:,j)*dmij; 
           mg2=0.5*(trji-dmij'*C_(:,:,j)*dmij+log(dtj/dti)); 
           Dg2=0.5*trji2+dmij'*C_(:,:,i)*C(:,:,j)*C_(:,:,i)*dmij; 
           sD1=sqrt(Dg1); sD2=sqrt(Dg2);
           PIJ(i,j)=normcdf(l0_(i,j),mg1,sD1); PIJ(j,i)=1-normcdf(l0_(i,j),mg2,sD2);
           mu2=(1/8)*dmij'*((C(:,:,i)/2+C(:,:,j)/2)^-1)*dmij...
               +0.5*log((dti+dtj)/(2*sqrt(dti*dtj)));%���������� ����������
           PIJB(i,j)=sqrt(pw(j)/pw(i))*exp(-mu2);PIJB(j,i)=sqrt(pw(i)/pw(j))*exp(-mu2);%������� �������
    end;
    PIJB(i,i)=1-sum(PIJB(i,:));
    PIJ(i,i)=1-sum(PIJ(i,:));%������ ������� ����������� ����������� �������������
 end;
 
disp('������������� ������� ������������ ������');disp(PIJ);
err1 = PIJ(1, 2); % ������ ����� ������ ���
err2 = PIJ(2, 1); % ������ ����� ������ ���
errSum=pw(1)*PIJ(1,2)+pw(2)*PIJ(2,1);
 
disp('������ ������� ������ ������� ����');disp(err1);
disp('������ ������� ������ ������� ����');disp(err2);
disp('��������� ������');disp(errSum);
