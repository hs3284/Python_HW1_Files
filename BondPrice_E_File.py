
import numpy as np
def getBondPrice(y, face, couponRate, m, ppy=1):
 if ppy==1: 
  coupon=face*couponRate/ppy
  n=m*ppy
  t=np.arange(1,n+1)
  pvcf=0

  pv = (1+y/ppy)**(-t/ppy)
  pvcf += coupon*pv
  lastyear = face*pv[-1]
  bond_price = pvcf.sum()+lastyear
  return bond_price
  
 elif ppy==2:
  coupon=face*couponRate/ppy
  n=m*ppy
  t=np.arange(1,n+1)
  pvcf=0
  
  pv = (1+y/ppy)**(-t)
  pvcf += coupon*pv
  lastyear = face*pv[-1]
  bond_price = pvcf.sum()+lastyear
  return bond_price
