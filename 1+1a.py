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

fig, ax = plt.subplots( 1, 1 )
ax.axis( 'off' )

xM = [ 0.0, 1.0 ]
yM = [ 0.0, 1.0 ]
ax.plot( [ xM[0], xM[1] ], [ yM[0], yM[0] ], 'k-' )
ax.plot( [ xM[1], xM[1] ], [ yM[0], yM[1] ], 'k-' )
ax.plot( [ xM[1], xM[0] ], [ yM[1], yM[1] ], 'k-' )
ax.plot( [ xM[0], xM[0] ], [ yM[1], yM[0] ], 'k-' )

ax.text( 0.65, 0.9, r'$\mathcal{M}\cong\Sigma\times\mathbb{R}^{+}$', \
         fontsize = 16 )

x = np.linspace( xM[0]+0.01, xM[1]-0.01, 100 )

def y1( x ):
    return 0.15 + ( 0.07 * np.sin( 5.0 * 2.0 * np.pi * x ) \
                    + 0.07 * np.sin( 2.0 * 2.0 * np.pi * x ) )
ax.plot( x, y1(x), 'k-' )
x1 = x[5]
#ax.plot( x1, y1( x1 ), 'ko', ms = 8 )
ax.text( 0.8, 0.05, r'$\Sigma_{t}$', fontsize = 16 )

def y2( x ):
    return 0.75 + ( 0.07 * np.sin( 3.0 * 2.0 * np.pi * x ) \
                      - 0.03 * np.sin( 5.0 * 2.0 * np.pi * x ) )
    #return y1( x ) + 0.5
ax.plot( x, y2(x), 'k-' )
x2 = x[5]
#ax.plot( x2, y2( x2 ), 'ko', ms = 8 )
ax.text( 0.8, y2( 0.85 ) - 0.1, r'$\Sigma_{t+dt}$', fontsize = 16 )

n12 = patches.FancyArrowPatch \
        ( ( x1, y1( x1 ) ), ( x2, y2( x2 ) ), \
          color = 'r', **kw )
plt.gca().add_patch( n12 )
ax.text( 0.5 * ( x1 + x2 ) + 0.02, 0.5 * ( y1( x1 ) + y2( x2 ) ), \
         r'$\alpha\,\overline{n}$', fontsize = 16, color = 'r' )

#ind1 = 60
#ind2 = 70
#u12 = patches.FancyArrowPatch \
#        ( ( x[ind1], y1( x[ind1] ) ), ( x[ind2], y2( x[ind2] ) ), \
#          color = 'b', **kw )
#plt.gca().add_patch( u12 )
#ax.text( 0.5 * ( x[ind1] + x[ind2] ) + 0.02, \
#         0.5 * ( y1( x[ind1] ) + y2( x[ind2] ) ) - 0.01, \
#         r'$\overline{u}$', fontsize = 16, color = 'b' )

#plt.show()
plt.savefig( 'fig.1+1a.png', dpi = 300 )
