n, k = *gets.split(" ")
n = n.to_i
k = k.to_i

aaa = gets.split(" ").map{|a| a.to_i}
base, bonus = *k.divmod(n)

sorted_aaa = aaa.sort
th = bonus == 0 ? -1 : sorted_aaa[bonus-1].to_i

for a in aaa do
  if a.to_i <= th
    puts base + 1
  else
    puts base
  end
end
