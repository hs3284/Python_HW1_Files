def getBondDuration(y,face,couponRate,m,ppy=1):
    
  coupon = face * couponRate / ppy
  pvcf = 0
  pvcft = 0
  for i in range(1,m+1):
    pvcf += coupon * ((1+y/ppy)**(-i*ppy))
    pvcft+=i * coupon * ((1+y/ppy)**(-i*ppy))

  lastyear = face * ((1+y/ppy)**(-m*ppy))
  pvcftotal =pvcft+ m * face * ((1+y/ppy)**(-m*ppy))
  bondPrice = pvcf + lastyear


  bondDuration = pvcftotal / bondPrice

  return bondDuration

