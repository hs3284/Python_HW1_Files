

def getBondPrice_Z(face,couponRate,times,yc):
  coupon=face*couponRate
  pvcf=0
  for t,y in zip(times,yc):
    pv=(1+y)**(-t)
    pvcf+=coupon*pv
  
  pvcftotal2=face*(1+yc[-1])**(-times[-1])+pvcf

  return  pvcftotal2

face = 2000000
couponRate = 0.04
times = [1, 1.5, 3, 4, 7]
yc = [0.01, 0.015, 0.02, 0.025, 0.03]

bondPrice = getBondPrice_Z(face, couponRate, times, yc)
print(bondPrice)
