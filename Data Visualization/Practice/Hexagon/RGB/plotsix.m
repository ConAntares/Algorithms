%function plotsix(x,y,r,clr)
%for i=1:6
%    xy(i,1)=x+1.15*r*cos(i/6*2*pi+pi/6);
%    xy(i,2)=y+r*sin(i/6*2*pi+pi/6);
%end
%fill(xy(:,1),xy(:,2),clr);
%end


function plotsix(x,y,r,clr)
for i=1:6
    xy(i,1)=x+1.15*r*cos(i/6*2*pi+pi/6);
    xy(i,2)=y+r*sin(i/6*2*pi+pi/6);
end
h=fill(xy(:,1),xy(:,2),clr);
set(h,{'LineStyle'},{'none'}); 
end