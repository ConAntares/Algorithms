#### Coin

# Readme: https://www.zhihu.com/question/315108379?

function coin(tot)
    toc         = tot +1
    category    = [1, 5 , 10, 20, 50, 100] 
    dp          = zeros(toc)                # 0 from 1 to toc
    dp[1]       = 1
    for i in category
        for j in 1:tot
            if j >= i
                dp[j] = dp[j] + dp[j-i]
            end
        end 
    end
    return dp[tot]
end

println(coin(500))
 