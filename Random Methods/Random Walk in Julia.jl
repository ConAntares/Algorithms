#### Random Walk

using Random
using Plots; pyplot()

function Walk(tot)
    x_set = [0.0]; y_set = [0.0]
    x_direction = 0.0; y_direction = 0.0

    while length(x_set) <= tot
        x_direction = rand(Float64)*2 - 1
        x_distance  = Float64(rand(1:1:4))
        x_move      = x_direction * x_distance

        y_direction = rand(Float64)*2 - 1
        y_distance  = Float64(rand(1:1:4))
        y_move      = y_direction * y_distance

        x_refresh   = x_set[end] + x_move
        y_refresh   = y_set[end] + y_move

        append!(x_set, x_refresh)
        append!(y_set, y_refresh)
    end
    return x_set, y_set
end

X,Y = Walk(10000)

plot(fontfamily=("Serif"),dpi=512)
scatter!(X,Y,marker=(:circle,4,Plots.stroke(:white)))