#### Linear Combination

function lincomb(coeff, vectors)
    n = length(vectors[1])
    r = zeros(n)
    for i = 1:length(vectors)
        r = r + coeff[i] * vectors[i]
    end
    return r
end

re = lincomb(([-0.5, 1.5]),([1, 2], [3, 4]))

println(re)
    # [4.0, 5.0]