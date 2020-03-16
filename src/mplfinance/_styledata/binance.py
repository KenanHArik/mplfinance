style = dict(style_name    = 'binance',
             base_mpl_style= 'seaborn-darkgrid',
             marketcolors  = {'candle'  : {'up':'#70a800', 'down':'#ea0070'},
                              'edge'    : {'up':'#70a800', 'down':'#ea0070'},
                              'wick'    : {'up':'#70a800', 'down':'#ea0070'},
                              'ohlc'    : {'up':'#70a800', 'down':'#ea0070'},
                              'volume'  : {'up':'#70a800', 'down':'#ea0070'},
                              'vcedge'  : {'up':'#70a800', 'down':'#ea0070'},
                              'vcdopcod': False,
                              'alpha'   : 0.9,
                             },
             mavcolors     = ['#ffc201','#ff10ff','#cd0468','#1f77b4',
                              '#ff7f0e','#2ca02c','#40e0d0'],
             y_on_right    = False,
             gridcolor     = '#d0d0d0',
             gridstyle     = '--',
             facecolor     = '#ffffff',
             rc            = [ ('axes.edgecolor'  , '#e6e6e6' ),
                               ('axes.linewidth'  ,  1.5      ),
                               ('axes.labelsize'  , 'medium'  ),
                               ('axes.labelweight', 'semibold'),
                               ('lines.linewidth' ,  2.0      ),
                               ('font.weight'     , 'medium'  ),
                               ('font.size'       ,  12.0     ),
                             ],
             base_mpf_style= 'binance'
            )
