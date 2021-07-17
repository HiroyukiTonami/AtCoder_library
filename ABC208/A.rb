a, b = *gets.split(" ")
a = a.to_i
b = b.to_i

if a <= b && b <= 6*a
    puts 'Yes'
else
    puts 'No'
end