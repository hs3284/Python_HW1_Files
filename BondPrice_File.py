

def getBondPrice(y, face, couponRate, m, ppy=1):
  
  if ppy==1: 
    coupon=face*couponRate/ppy
    pvcf=0
    for i in range(1,m):
      pvcf+=coupon*((1+y/ppy)**(-i*ppy))

    lastyear=coupon*((1+y/ppy)**(-m*ppy))+face*((1+y/ppy)**(-m*ppy))

    bondPrice=pvcf+lastyear
  
  elif ppy==2:

    coupon=face*couponRate/ppy
    pvcf=0
    for i in range(1,m*ppy):
      pvcf+=coupon*(1+y/ppy)**(-i)

    lastyear=coupon*((1+(y/ppy))**(-m*ppy))+face*((1+(y/ppy))**(-m*ppy))

    bondPrice=pvcf+lastyear
  
  return bondPrice


y = 0.03  
face = 2000000  
couponRate = 0.04  
maturity = 10

bondPrice1 = getBondPrice(y, face, couponRate, maturity, ppy=1)
print(bondPrice1)
bondPrice2 = getBondPrice(y, face, couponRate, maturity, ppy=2)
print(bondPrice2)
