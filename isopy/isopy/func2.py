{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}
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
        if d_or_t is ('d' or 't'):
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