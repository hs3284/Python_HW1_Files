
def getBondPrice_Z(face,couponRate,times,yc):
  coupon=face*couponRate
  pvcf=0
  for t,y in zip(times,yc):
    pv=(1+y)**(-t)
    pvcf+=coupon*pv
  
  pvcftotal2=face*(1+yc[-1])**(-times[-1])+pvcf

  return  pvcftotal2
