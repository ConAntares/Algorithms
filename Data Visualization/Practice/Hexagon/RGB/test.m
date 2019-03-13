clc;
xyh = load('test4.dat');
close all;
f   = figure;
hold on;
black = [0,0,0];
red   = [1,0,0];
green = [0,1,0];
blue  = [0,0,1];
white = [0,0,0];
maxv  = max(xyh(:,3));
maxv  = 0.048;
minv  = min(xyh(:,3));
minv  = 0.001;
pcls  = [1,1,1; 0,0.2,0.5; 0.5,0,0.5];
pvals = [0.001; 0.01; 0.048];
for i = 1:size(xyh,1.2)
    plotsix(xyh(i,1),xyh(i,2),2.8,val2cls(xyh(i,3),pcls,pvals));
end
caxis([minv,maxv]);
axis equal
axis off
cls   = [];
cpcls = val2cls(minv:0.001:maxv,pcls,pvals);
%set(H_F1,{'LineStyle'},{'none'}) 
colormap(cpcls)
colorbar; 

