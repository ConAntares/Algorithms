function cls=val2cls(vals,pcls,pvals)
cls=[];
if size(pcls,2)~=size(pvals,1)
    return;
end
for i=1:length(vals)
    if vals(i)< pvals(1);vals(i)= pvals(1);end
    if vals(i)> pvals(end);vals(i)= pvals(end);end
    for j=1:length(pvals)-1
        if vals(i) >= pvals(j) && vals(i)<= pvals(j+1)
            break;
        end
    end
    u=(vals(i)-pvals(j))/(pvals(j+1)-pvals(j));
    cls=[cls;u*pcls(j+1,:)+(1-u)*pcls(j,:)];
end
end