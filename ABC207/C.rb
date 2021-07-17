N = gets.to_i
tlrs = N.times.map{gets.split.map(&:to_i)}

# 準備。'より大きい'と'未満'を消して全部'以上'と'以下'の条件にする。
N.times do |i|
  # 0.5を取り扱うのが面倒なので2倍する
  tlrs[i][1] *= 2
  tlrs[i][2] *= 2
  if tlrs[i][0] == 2
    tlrs[i][2] -= 1
  elsif tlrs[i][0] == 3
    tlrs[i][1] += 1
  elsif tlrs[i][0] == 4
    tlrs[i][1] += 1    
    tlrs[i][2] -= 1
  end
end

count = 0
tlrs.each_with_index do |tlr, i|
  for tlrr in tlrs[i+1, N] do
    if tlrr[1] <= tlr[1] && tlr[1] <= tlrr[2] || tlr[1] <= tlrr[1] && tlrr[1] <= tlr[2]
      count += 1
    end
  end
end

puts count
