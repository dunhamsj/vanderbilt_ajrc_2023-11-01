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
fs = 16

fig, ax = plt.subplots( 1, 1 )
ax.axis( 'off' )

xlim = [ 0.0, 1.0 ]
ylim = [ 0.0, 1.0 ]
ax.plot( [ xlim[0], xlim[1] ], [ ylim[0], ylim[0] ], 'k-' )
ax.plot( [ xlim[1], xlim[1] ], [ ylim[0], ylim[1] ], 'k-' )
ax.plot( [ xlim[1], xlim[0] ], [ ylim[1], ylim[1] ], 'k-' )
ax.plot( [ xlim[0], xlim[0] ], [ ylim[1], ylim[0] ], 'k-' )

def y( x, y0 = 0.1 ):
    return np.sqrt( 1.0 - x**2 ) - y0
x = np.linspace( 0.4, 0.9, 100 )
ax.plot( x - 0.1, y( x ), 'k-' )
ax.text( x[-1] - 0.1, y( x[-1] ) - 0.05, r'$R_{\mathrm{Sh}}$', fontsize = fs )
ax.text( x[50] - 0.1, y( x[50] ) + 0.05, \
r'$\boldsymbol{U}_{1},\boldsymbol{F}^{r}\left(\boldsymbol{U}_{1}\right)$', \
         fontsize = fs )
ax.text( x[15] - 0.1, y( x[20] ) - 0.25, \
r'$\boldsymbol{U}_{2},\boldsymbol{F}^{r}\left(\boldsymbol{U}_{2}\right)$', \
         fontsize = fs )

v1 = patches.FancyArrowPatch \
       ( ( 0.47, 0.98 ), ( 0.4, 0.8 ), \
         color = 'k', **kw )
plt.gca().add_patch( v1 )
ax.text( 0.37, 0.9, r'$v^{r}_{1}$', fontsize = fs )
v2 = patches.FancyArrowPatch \
       ( ( 0.36, 0.7 ), ( 0.32, 0.6 ), \
         color = 'k', **kw )
plt.gca().add_patch( v2 )
ax.text( 0.27, 0.67, r'$v^{r}_{2}$', fontsize = fs )
#plt.show()
plt.savefig( 'fig.jump.png', dpi = 300 )
