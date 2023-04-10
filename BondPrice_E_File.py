
def getBondPrice_E(face,couponRate,yc):
  coupon=face*couponRate
  pvcf=0
  for i,Y in enumerate(yc):
    pv = (1+Y)**(-(i+1))
    pvcf += coupon*pv
  pvcftotal=face*pv+pvcf

  return pvcftotal
