clear;
clc;
r=-5.61:0.00001:-5.6000;
x= 0.5*r;
for i =1:5000000
    x=0.5*x.*x+0.5*r;
end
figure;
hold on;
for i =1:10000
    x=0.5*x.*x+0.5*r;
    plot(r,x,'k.','markersize',1);
end
