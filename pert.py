#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.style.use( 'publication.sty' )

from UtilitiesModule import GetData, MapCenterToCorners, GetNorm

#### ========== User Input ==========

rootDirectory \
  = '/lump/data/accretionShockStudy/newData/2D/'
rootDirectory \
  = '/Users/dunhamsj/Desktop/SASI_Data/'

ID = 'GR2D_M2.8_Rpns020_Rs6.00e1'

field = 'AF_P'

saveFigAs = 'fig.pert.png'

verbose = True

#### ====== End of User Input =======

plotfileBaseName = ID + '.plt'

dataDirectory = rootDirectory + ID + '/'

data0, dataUnits, \
X1, X2, X3, dX1, dX2, dX3, xL, xH, nX \
  = GetData( dataDirectory, plotfileBaseName, field, \
             'spherical', True, argv = ['a','99999999'], \
             ReturnTime = False, ReturnMesh = True )

data, dataUnits, \
  = GetData( dataDirectory, plotfileBaseName, field, \
             'spherical', True, argv = ['a','0'], \
             ReturnTime = False, ReturnMesh = False )

data = data / data0 - 1.0

Rs   = 6.00e1
Rpns = 2.00e1

X1_C = np.copy( ( X1  [:,:,0] - Rpns ) / ( Rs - Rpns ) )
X2_C = np.copy( X2  [:,:,0] )
dX1  = np.copy( dX1 [:,:,0] / ( Rs - Rpns ) )
dX2  = np.copy( dX2 [:,:,0] )
data = np.copy( data[:,:,0] )

shape = ( X2_C.shape[0], 2*X2_C.shape[1] )

X22_C = np.empty( shape, np.float64 )
dX22  = np.empty( shape, np.float64 )
X11_C = np.empty( shape, np.float64 )
dX11  = np.empty( shape, np.float64 )
dataa = np.empty( shape, np.float64 )

for iX1 in range( shape[0] ):

    X22_C[iX1,0 :64] = np.copy( X2_C[iX1]       )
    X22_C[iX1,64:  ] = np.copy( X2_C[iX1] + np.pi )
    dX22 [iX1,0 :64] = np.copy( dX2 [iX1]       )
    dX22 [iX1,64:  ] = np.copy( dX2 [iX1][::-1] )

    X11_C[iX1,0 :64] = np.copy( X1_C[iX1] )
    X11_C[iX1,64:  ] = np.copy( X1_C[iX1] )
    dX11 [iX1,0 :64] = np.copy( dX1 [iX1] )
    dX11 [iX1,64:  ] = np.copy( dX1 [iX1] )

    dataa[iX1,0 :64] = np.copy( data[iX1]       )
    dataa[iX1,64:  ] = np.copy( data[iX1][::-1] )

X2_C = np.copy( X22_C )
dX2  = np.copy( dX22 )

X1_C = np.copy( X11_C )
dX1  = np.copy( dX11 )

X1c, X2c = MapCenterToCorners( X1_C, X2_C, dX1, dX2 )

X1c = np.copy( X1c[:,0] )
X2c = np.copy( X2c[0,:] )

X2c, X1c = np.meshgrid( X2c, X1c )

data = np.copy( dataa )

### Plotting

fig = plt.figure()
ax  = fig.add_subplot( 111, polar = True )
ax.grid(False)

vmin = data.min()
vmax = data.max()
vmin = -1.0e-6
vmax = +1.0e-6

Norm = GetNorm( 'None', data, vmin = vmin, vmax = vmax )

im = ax.pcolormesh( X2c, X1c, data, \
                    cmap = 'RdBu', \
                    shading = 'flat', \
                    norm = Norm )

theta = np.linspace( 0.0, 2.0 * np.pi, 1000 )
rpns  = np.zeros( theta.shape[0], np.float64 )
rsh   = np.ones ( theta.shape[0], np.float64 )
ax.plot( theta, rpns, 'k-' )
ax.plot( theta, rsh , 'k-' )

r0 = -2.0e1 / ( 6.0e1 - 2.0e1 )
ax.text( 1.33 * np.pi, -0.32, \
         r'$M_{\mathrm{PNS}},$' + '\n' + r'$R_{\mathrm{PNS}}$' )
ax.text( 0.0, 1.1, r'$R_{\mathrm{Sh}}$' )

yticks = np.linspace( 0.0, 1.5, 7 )
yticklabels = [ '{:.2f}'.format( yt ) for yt in yticks ]
ax.set_yticks( yticks )
ax.set_yticklabels( yticklabels )

ax.set_thetamin( 0.0  )
ax.set_thetamax( 360.0)
ax.set_rmin( r0 )
ax.set_rmax( 1.5 )
ax.set_theta_direction( -1 )
ax.set_theta_zero_location( 'N' )
#ax.set_yticklabels( [] )

cbar = fig.colorbar( im )
cbar.set_label( r'$\delta p/p-1$' )

plt.savefig( saveFigAs, dpi = 300 )
#plt.show()
plt.close()

import os
os.system( 'rm -rf __pycache__ ' )
