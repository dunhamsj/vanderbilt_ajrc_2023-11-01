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

ax.text( 0.7, 0.9, r'$\mathcal{M}\cong\Sigma\times\mathbb{R}^{+}$', \
         fontsize = 16 )

x = np.linspace( xM[0]+0.01, xM[1]-0.01, 100 )

def y1( x ):
    return 0.15 + ( 0.07 * np.sin( 5.0 * 2.0 * np.pi * x ) \
                    + 0.07 * np.sin( 2.0 * 2.0 * np.pi * x ) )
ax.plot( x, y1(x), 'k-' )
x1 = x[5]
ax.text( 0.84, 0.05, r'$\Sigma_{t_{1}}$', fontsize = 16 )

def y2( x ):
    return 0.25 + y1( x )
ax.plot( x, y2(x), 'k-' )
x2 = x[10]
ax.text( 0.86, y2( 0.87 ) - 0.12, r'$\Sigma_{t_{2}}$', fontsize = 16 )

def y3( x ):
    return 0.65 + y1( x )
ax.plot( x, y3(x), 'k-' )
x3 = x[15]
ax.text( 0.88, 0.8, r'$\Sigma_{t_{3}}$', fontsize = 16 )

n12 = patches.FancyArrowPatch \
        ( ( x1, y1( x1 ) ), ( x1, y2( x1 ) ), \
          color = 'r' )
plt.gca().add_patch( n12 )
ax.text( x1 + 0.015, 0.5 * ( y1( x1 ) + y2( x2 ) ), \
         r'$\overline{n}$', fontsize = 16, color = 'r' )
n23 = patches.FancyArrowPatch \
        ( ( x1, y2( x1 ) ), ( x1, y3( x1 ) ), \
        color = 'r', **kw )
plt.gca().add_patch( n23 )

ind1 = 60
ind2 = 70
u12 = patches.FancyArrowPatch \
        ( ( x[ind1], y1( x[ind1] ) ), ( x[ind2], y2( x[ind2] ) ), \
          connectionstyle='arc3,rad=-.3', color = 'b' )
plt.gca().add_patch( u12 )
ax.text( 0.5 * ( x[ind1] + x[ind2] ) + 0.00, \
         0.5 * ( y1( x[ind1] ) + y2( x[ind2] ) ), \
         r'$\overline{u}$', fontsize = 16, color = 'b' )
ind1 = ind2
ind2 = 90
u23 = patches.FancyArrowPatch \
        ( ( x[ind1], y2( x[ind1] ) ), ( x[ind2], y3( x[ind2] ) ), \
        connectionstyle='arc3,rad=.2', color = 'b', **kw )
plt.gca().add_patch( u23 )

plt.show()
#plt.savefig( 'fig.1+1b.png', dpi = 300 )
