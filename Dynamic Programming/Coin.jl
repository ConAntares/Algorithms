#### Coin

# Readme: https://www.zhihu.com/question/315108379?

function coin(tot)
    toc      = tot + 1
    category = [1, 5 , 10, 20, 50, 100]
    count    = zeros(toc)
    count[1] = 1
    for i in category
        for j in 2:toc
            if j-1 >= i
                count[j] = count[j] + count[j-i]
            end
        end
    end
    return count[toc]
end

print(coin(500))