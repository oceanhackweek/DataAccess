import numpy as np
import xarray as xr
from scipy import interpolate

def compute_iso(data, iso, lev):

    """ compute the var along isopycnal layers.
    
    Parameters:
    ----------------
    
    data: the input variable (Temp, Salinity, Density ...)
        array_like (3D), shape (N, M, L).
    iso: the objective isopycnal layer
        float.
    lev: the vertical depth
        array_like (1D), shape (N)
        
    Returns
        
    """
    
    
    dep_iso = np.zeros((den.shape[1], den.shape[2]))
    dep_iso[:, :] = np.nan
    for i in np.arange(0, den.shape[2], 1):
        for j in np.arange(0, den.shape[1], 1):

            den_tmp = den[:, j, i]

            id1 = np.where(den_tmp < iso)

            if np.size(id1) > 0 and np.size(id1) < len(z):
                
                den1 = den_tmp[id1[0][-1]]
                den2 = den_tmp[id1[0][-1] + 1]

                if den1 < den2:
                    fun2 = interpolate.interp1d([den1, den2], [z[id1[0][-1]], z[id1[0][-1] + 1]])
                    dep_iso[j, i] = fun2(iso)
                    print(str(i) + '  ' + str(j))
                    print('success')

    return var_iso


def iso_average(data, iso, lev):
    
    
    return var_ave