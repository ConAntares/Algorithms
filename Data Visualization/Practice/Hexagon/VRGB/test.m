clc;
xyh=load('test1.dat');
close all;
f=figure;
hold on;
black   = [0,0,0];
red     = [1,0,0];
green   = [0,1,0];
blue    = [0,0,1];
white   = [0,0,0];
maxv    = max(xyh(:,3));
maxv    = 0.048;
minv    = min(xyh(:,3));
minv    = 0.001;
pvalcls = [ 0.001,0,0,1;
            0.002,0,1,0;
            0.010,0,1,1;
            0.020,1,1,1;
            0.048,1,0,0];
for i=1:size(xyh,1)
    plotsix(xyh(i,1),xyh(i,2),2.8,val2cls(xyh(i,3),pvalcls,1));
end
caxis([minv,maxv]);
axis equal
axis off
cls=[];
cpcls=val2cls(minv:0.0001:maxv,pvalcls,1);
colormap(cpcls)
colorbar; 
