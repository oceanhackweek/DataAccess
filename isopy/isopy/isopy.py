import numpy as np
import xarray as xr
from scipy import interpolate

def compute_iso(data, iso, lev,var):

    """ compute the var along isopycnal layers.
    
    Parameters:
    ----------------
    
    data: the input variable (Temperature, Salinity, Density ...),
        array_like (3D), shape (N, M, L).
    iso: the objective isopycnal layer,
        float.
    lev: the vertical depth,
        array_like (1D), shape (N)
        
    Returns:
    ----------------
    
    var_iso: the output variable,
        array_like (2D), shape (M, L).
        
    """
    if var = 'temp':
    
    if var = 'salinity':
    
    if var = 'density':
        
    size = data.shape
    L = size[2]
    M = size[1]
    N = size[0]
    
    var_iso = np.zeros((M, L)) # define the output var
    var_iso[:, :] = np.nan
    
    for i in np.arange(L):
        for j in np.arange(M):

            data_tmp = data[:, j, i]

            id1 = np.where(data_tmp < iso)

            if np.size(id1) > 0 and np.size(id1) < len(z):
                
                den1 = data_tmp[id1[0][-1]]
                den2 = data_tmp[id1[0][-1] + 1]

                if den1 < den2:
                    fun2 = interpolate.interp1d([den1, den2], [lev[id1[0][-1]], lev[id1[0][-1] + 1]])
                    var_iso[j, i] = fun2(iso)

    return var_iso


def iso_average(data, iso, lev):
    
    """ compute vertical average above the objective isopycnal layer
    
    Parameters:
    ----------------
    
    data: the input variable (Temperature, Salinity, Density ...),
        array_like (3D), shape (N, M, L).
    iso: the objective isopycnal layer,
        float.
    lev: the vertical depth,
        array_like (1D), shape (N)
        
    Returns:
    ----------------
    
    var_ave: the output variable,
        array_like (2D), shape (M, L).
    
    """
    
    return var_ave