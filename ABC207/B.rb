a, b, c, d = *gets.split(" ").map{|a| a.to_i}

if c * d <= b
    puts '-1'
    exit
end

div, mov = *a.divmod((c*d - b))
div += 1 if mov != 0
puts div
