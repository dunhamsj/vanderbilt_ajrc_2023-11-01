#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
plt.style.use( 'publication.sty' )
plt.rcParams.update \
  ( { 'text.latex.preamble': r'\usepackage{amsfonts}' \
                               + r'\usepackage{amsmath}' } )

style = 'Simple, tail_width = 0.5, head_width = 4, head_length = 8'
kw = dict( arrowstyle = style )
fs = 14

fig, ax = plt.subplots( 1, 1 )
ax.axis( 'off' )

xM = [ 0.0, 1.5 ]
yM = [ 0.0, 1.5 ]
ax.plot( [ xM[0], xM[1] ], [ yM[0], yM[0] ], 'k-' )
ax.plot( [ xM[1], xM[1] ], [ yM[0], yM[1] ], 'k-' )
ax.plot( [ xM[1], xM[0] ], [ yM[1], yM[1] ], 'k-' )
ax.plot( [ xM[0], xM[0] ], [ yM[1], yM[0] ], 'k-' )

r = np.array( [ 0.5, 0.4 ], np.float64 )

def y( x1, x0, m ):
    return m * ( x1 - x0 ) + 0.4

# v
dx = np.array( [ 0.3, 0.6 ], np.float64 )
mv = 1.15
xp = r + dx
v  = np.array( [ y( xp[0], xp[0], mv ), \
                 y( xp[1], xp[0], mv ) ], np.float64 )
vt = v + r
vv = patches.FancyArrowPatch \
       ( ( r[0], r[1] ), ( vt[0], vt[1] ), \
         color = 'b', **kw )
plt.gca().add_patch( vv )
magv = np.sqrt( v[0]**2 + v[1]**2 )
ax.text( vt[0], vt[1], r'$\overline{v}$', fontsize = fs, color = 'b' )

# n
dx = np.array( [ 0.3, 0.2 ], np.float64 )
mn = 0.9
xp = r + dx
n = np.array( [ y( xp[0], xp[0], mn ), \
                y( xp[1], xp[0], mn ) ], np.float64 )
magn = np.sqrt( n[0]**2 + n[1]**2 )
n /= magn
nt = n + r
nn = patches.FancyArrowPatch \
       ( ( r[0], r[1] ), ( nt[0], nt[1] ), \
          color = 'r', **kw )
plt.gca().add_patch( nn )
magn = np.sqrt( n[0]**2 + n[1]**2 )
ax.text( nt[0], nt[1], r'$\overline{n}$', fontsize = fs, color = 'r' )

# (v . n )n
vdns = v[0] * n[0] + v[1] * n[1]
vdn = r + vdns * n
vdnn = patches.FancyArrowPatch \
         ( ( r[0], r[1] ), \
           ( vdn[0], \
             vdn[1] ), \
           color = 'm', **kw )
plt.gca().add_patch( vdnn )
ax.text( 0.6 * vdn[0], 0.55 * vdn[1], \
         r'$\left(-\overline{n}\otimes\underline{n}\right)\overline{v}$', \
         fontsize = fs, color = 'm' )

# delta + ( v . n )n
vcn = r + np.array( [ vt[0] - ( r[0] + vdns * n[0] ), \
                      vt[1] - ( r[1] + vdns * n[1] ) ], np.float64 )

vcnn = patches.FancyArrowPatch \
         ( ( r[0], r[1] ), \
           ( vcn[0], \
             vcn[1] ), \
           color = 'm', **kw )
plt.gca().add_patch( vcnn )
ax.text( 0.3 * vcn[0], 1.05 * vcn[1] + 0.15, \
         r'$\overline{\underline{\gamma}}\,\overline{v}$', \
         fontsize = fs, color = 'm' )
ax.text( 0.3 * vcn[0], 1.05 * vcn[1], \
         r'$=\left(\overline{\underline{\delta}}+\overline{n}\otimes\underline{n}\right)\overline{v}$', \
         fontsize = fs, color = 'm' )

ax.set_aspect( 'equal' )

#plt.show()
plt.savefig( 'fig.decomp.png', dpi = 300 )
