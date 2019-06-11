#### Linear Combination

function lincomb(coeff, vectors)
    n = length(vectors[1])
    a = zeros(n)
    for i = 1:length(vectors)
        a = a + coeff[i] * vectors[i]
    end
    return a
end

