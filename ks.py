import numpy as np
import pandas as pd
from scipy.stats import ks_2samp
from scipy.stats import kstest

obsz=pd.read_csv('obsresult/z_repo.txt')
obs_sz=pd.read_csv('obsresult/sz_repo.txt')
constz=pd.read_csv('result/const/z_repo.txt')
gaussz=pd.read_csv('result/gauss/z_repo.txt')
bplz=pd.read_csv('result/bpl/z_repo.txt')

obseiso=pd.read_csv('obsresult/eiso_repo.txt')
consteiso=pd.read_csv('result/const/eiso_repo.txt')
gausseiso=pd.read_csv('result/gauss/eiso_repo.txt')
bpleiso=pd.read_csv('result/bpl/eiso_repo.txt')


obsz=np.array(obsz)
obs_sz=np.array(obs_sz)
constz=np.array(constz)
gaussz=np.array(gaussz)
bplz=np.array(bplz)
obseiso=np.array(obseiso)
consteiso=np.array(consteiso)
gausseiso=np.array(gausseiso)
bpleiso=np.array(bpleiso)


obs=[]
sz=[]
const=[]
gauss=[]
bpl=[]
obse=[]
conste=[]
gausse=[]
bple=[]
for i in range(len(obsz)):
    obs=np.append(obs,obsz[i][0])
    const=np.append(const,constz[i][0])
    gauss=np.append(gauss,gaussz[i][0])
    bpl=np.append(bpl,bplz[i][0])
    obse=np.append(obse,np.log10(obseiso[i][0]))
    conste=np.append(conste,np.log10(consteiso[i][0]))
    gausse=np.append(gausse,np.log10(gausseiso[i][0]))
    bple=np.append(bple,np.log10(bpleiso[i][0]))
for i in range(len(obs_sz)):
    sz=np.append(sz,obs_sz[i][0])

obs_const=ks_2samp(obs,const)
obs_gauss=ks_2samp(obs,gauss)
obs_bpl=ks_2samp(obs,bpl)
obs_const_sz=ks_2samp(sz,const)
obs_gauss_sz=ks_2samp(sz,gauss)
obs_bpl_sz=ks_2samp(sz,bpl)
obs_const_e=ks_2samp(obse,conste)
obs_gauss_e=ks_2samp(obse,gausse)
obs_bpl_e=ks_2samp(obse,bple)



#print(obs_const)
#print(obs_gauss)
#print(obs_bpl)
pvalue=['ks_pvalue']
pvalue=np.vstack((pvalue,obs_const[1]))
pvalue=np.vstack((pvalue,obs_const_sz[1]))
pvalue=np.vstack((pvalue,obs_const_e[1]))
pvalue=np.vstack((pvalue,obs_gauss[1]))
pvalue=np.vstack((pvalue,obs_gauss_sz[1]))
pvalue=np.vstack((pvalue,obs_gauss_e[1]))
pvalue=np.vstack((pvalue,obs_bpl[1]))
pvalue=np.vstack((pvalue,obs_bpl_sz[1]))
pvalue=np.vstack((pvalue,obs_bpl_e[1]))
pvalue=pd.DataFrame(pvalue)
pvalue.to_csv('result/kstest.txt',index=False,header=False)

