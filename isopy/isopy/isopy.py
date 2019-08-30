import numpy as np
import xarray as xr
from scipy import interpolate

def compute_iso(data, iso, lev, d_or_t):

    """ compute the depth of some isopycnal/isotherm.
    
    Parameters:
    ----------------
    
    data: the input variable (Temperature, Density),
        array_like (3D), shape (N, M, L).
    iso: the objective isosurface layer,
        float.
    lev: the vertical depth,
        array_like (1D), shape (N).
    d_or_t: input d or t for density or temperature (lowercase)
        string
        
    Returns:
    ----------------
    
    var_iso: the output variable,
        array_like (2D), shape (M, L).
        
    """
    size = data.shape
    L = size[2]
    M = size[1]
    N = size[0] #this should be the same length as lev
    
    #check that the input data is in the for depth lat lon (or depth lon lat)
    if len(lev) != N:
        print('Error: either data input variable does not have depth as dimension 0, or lev variable is not same length as depth')
    else:
<<<<<<< HEAD
        if d_or_t in {'d','t'} :
=======
        if d_or_t in {'d', 't'}:
>>>>>>> de45a08845c975984e414208bcd1b15f38337a0a
            var_iso = np.zeros((M, L)) # define the output var
            var_iso[:, :] = np.nan # NaN fill to avoid any later computation errors with zeros

            for i in np.arange(L): #loop through dimension 1
                for j in np.arange(M): #loop through dimension 2

                    data_prof = data[:, j, i] #select one profile
                    if d_or_t == 'd':
                        id1 = np.where(data_prof < iso)
                        if np.size(id1) > 0 and np.size(id1) < len(z):
                            var1 = data_prof[id1[0][-1]]
                            var2 = data_prof[id1[0][-1] + 1]
                            if var1 < var2:
                                func = interpolate.interp1d([var1, var2], [lev[id1[0][-1]], lev[id1[0][-1] + 1]])
                                var_iso[j, i] = func(iso)

                    else:
                        id1 = np.where(data_prof > iso)

                        if np.size(id1) > 0 and np.size(id1) < len(z):

                            var1 = data_prof[id1[0][-1]]
                            var2 = data_prof[id1[0][-1] + 1]

                            if var1 > var2:
                                func = interpolate.interp1d([var1, var2], [lev[id1[0][-1]], lev[id1[0][-1] + 1]])
                                var_iso[j, i] = func(iso)

        else:
            print('Is this density or temperature?')
    return var_iso

def iso_val(density_data, ts_data, iso):

    """ compute temperature or salinity along some isopycnal/isotherm.
    
    Parameters:
    ----------------
    
    density_data: density input,
        array_like (3D), shape (N, M, L).
    ts_data: temp or salt input,
        array_like (3D), shape (N, M, L).
    iso: the objective isosurface layer,
        float.
        
    Returns:
    ----------------
    
    ts_iso: the output variable,
        array_like (2D), shape (M, L).
        
    """
    size = density_data.shape
    L = size[2]
    M = size[1]
    N = size[0]
    
    ts_iso = np.zeros((M, L)) # define the output var
    ts_iso[:, :] = np.nan # NaN fill to avoid any later computation errors with zeros
    
    dens = xr.DataArray(density_data)
    var = xr.DataArray(ts_data)
    a = dens.where(dens.min(axis=0)<iso)
    b = var.where(dens.min(axis=0)<iso) 

    for j in range(M):
        for k in range(L):
            x = a[:,j,k]
            y = b[:,j,k]
            f = interpolate.interp1d(x.values,y.values,'linear')
            ts_iso[j,k] = f(iso)
            
    return ts_iso

def iso_average(data, var_iso, lev):
    
    """ compute vertical average above the objective isopycnal layer
    
    Parameters:
    ----------------
    
    data: the input variable (temperature, salinity, U, V),
        array_like (3D), shape (N, M, L).   
    var_iso: the isopycnal layer,
        array_like (2D), shape (M, L).

    lev: the vertical depth,
        array_like (1D), shape (N).
        
    Returns:
    ----------------
    
    var_ave: the output variable,
        array_like (2D), shape (M, L).
    
    """
    
    size = data.shape
    L = size[2]
    M = size[1]
    N = size[0]
    
    data_new = (data[:-1, :, :] + data[1:, :, :]) / 2
    dz = lev[1:] - lev[:-1]

    var_out = np.zeros((M, L))
    var_out[:, :] = np.NaN
    
    for i in np.arange(L): #loop through dimension 1
        for j in np.arange(M): #loop through dimension 2
            
            var1 = data_new[:, j, i] * dz
            idx = find_nearest(lev, dep_iso[j, i])
        
            if idx > 0:
                var_out[j, i] = np.nansum(var1[:idx]) / np.sum(dz[:idx])
    return var_out
                
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

