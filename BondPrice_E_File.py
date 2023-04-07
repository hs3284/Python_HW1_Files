
def getBondPrice_E(face,couponRate,m,yc):
  coupon=face*couponRate
  pvcf=0
  for i,Y in enumerate(yc):
    pv = (1+Y)**(-(i+1))
    pvcf += coupon*pv
  pvcftotal=face*(1+yc[-1])**(-m)+pvcf

  return pvcftotal



yc = [.010,.015,.020,.025,.030]
face = 2000000
couponRate = .04
m = 5

bondPrice = getBondPrice_E(face, couponRate, m, yc)
print(bondPrice)
