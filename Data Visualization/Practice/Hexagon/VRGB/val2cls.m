function cls=val2cls(vals,pvalcls,type)
cls=[];
for i=1:length(vals)
    if vals(i)< pvalcls(1,1);vals(i)= pvalcls(1,1);end
    if vals(i)> pvalcls(end,1);vals(i)= pvalcls(end,1);end
    for j=1:size(pvalcls,1)-1
        if vals(i) <= pvalcls(j+1,1)
            break;
        end
    end
    if type==1
        u=(vals(i)-pvalcls(j,1))/(pvalcls(j+1,1)-pvalcls(j,1));
        cls=[cls;u*pvalcls(j+1,2:end)+(1-u)*pvalcls(j,2:end)];
    else
        cls=[cls;(pvalcls(j,2:end)+pvalcls(j+1,2:end))./2.0];
    end
end
end