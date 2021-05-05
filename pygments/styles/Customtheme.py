"""
    pygments.styles.material
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Mimic the Material theme color scheme.

    https://github.com/material-theme/vsc-material-theme

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Escape, \
    Error, Text, Number, Operator, Generic, Punctuation, Literal

class CustomthemeStyle(Style):
    """
    The style used in Lovelace interactive learning environment. Tries to avoid
    the "angry fruit salad" effect with desaturated and dim colours.
    """
    background_color = '#282828'
    default_style = "#ebdbb2"

    _KW_BLUE =       '#2838b0'
    _NAME_GREEN =    '#388038'
    _DOC_ORANGE =    '#b85820'
    _OW_PURPLE =     '#a848a8'
    _FUN_BROWN =     '#785840'
    _STR_RED =       '#b83838'
    _CLS_CYAN =      '#287088'
    _ESCAPE_LIME =   '#709030'
    _LABEL_CYAN =    '#289870'
    _EXCEPT_YELLOW = '#908828'
#GRUVBOX COLORS(Dark Mode, medium contrast) FROM https://github.com/morhetz/gruvbox
    background = '#282828'
    foreground = '#ebdbb2'

    darkgray = '#928374'
    lightgray = '#a89984'

    darkred = '#cc241d'
    lightred = '#fb4934'

    darkgreen = '#98971a'
    lightgreen = '#b8bb26'

    darkyellow = '#d79921'
    lightyellow = 'fabd2f'

    darkblue = '#458588'
    lightblue = '#83a598'

    darkpurple = '#b16286'
    lightpurple = '#d3869b'

    darkaqua = '#689d6a'
    lightaqua = '#8ec07c'


    bg0_h = '#1d2021'
    bg0 = '#282828'
    bg1 = '#3c3836'
    bg2 = '#504945'
    bg3 = '#665c54'
    bg4 = '#7c6f64'
    bg0_s = '#32302f'
    fg4 = '#a89984'
    fg3 = '#bdae93'
    fg2 = '#d5c4a1'
    fg1 = '#ebdbb2'
    fg0 = '#fbf1c7'

    mediumgray = '#928374'

    darkorange = '#d65d0e'
    lightorange = '#fe8019'




    default_style =  '#222222'

    styles = {
       
        Comment:             'italic #928374',
        Comment.Hashbang:    _CLS_CYAN,
        Comment.Multiline:   '#928374',
        Comment.Preproc:     'noitalic '+_LABEL_CYAN,

        Keyword:             darkred,
        Keyword.Constant:    'italic #444444',
        Keyword.Declaration: 'italic',
        Keyword.Type:        'italic',

        Operator:            '#666666',
        Operator.Word:       _OW_PURPLE,

     #   Punctuation:         '#888888',

        Name.Attribute:      _NAME_GREEN,
        Name.Builtin:        _NAME_GREEN,
        Name.Builtin.Pseudo: 'italic',
        Name.Class:          lightaqua,
        Name.Constant:       _DOC_ORANGE,
        Name.Decorator:      _CLS_CYAN,
        Name.Entity:         _ESCAPE_LIME,
        Name.Exception:      _EXCEPT_YELLOW,
        Name.Function:       _FUN_BROWN,
        Name.Function.Magic: _DOC_ORANGE,
        Name.Label:          _LABEL_CYAN,
        Name.Namespace:      _LABEL_CYAN,
        Name.Tag:            _KW_BLUE,
        Name.Variable:       fg1,
        Name.Variable.Global:_EXCEPT_YELLOW,
        Name.Variable.Magic: _DOC_ORANGE,

        String:             lightgreen,
        String.Affix:        '#444444',
        String.Char:         _OW_PURPLE,
        String.Delimiter:    _DOC_ORANGE,
        String.Doc:          'italic '+ lightgreen,
        String.Escape:       _ESCAPE_LIME,
        String.Interpol:     'underline',
        String.Other:        _OW_PURPLE,
        String.Regex:        _OW_PURPLE,

        Number:              lightpurple,

        Generic.Deleted:     '#c02828',
        Generic.Emph:        'italic',
        Generic.Error:       '#c02828',
        Generic.Heading:     '#666666',
        Generic.Subheading:  '#444444',
        Generic.Inserted:    _NAME_GREEN,
        Generic.Output:      '#666666',
        Generic.Prompt:      '#444444',
        Generic.Strong:      'bold',
        Generic.Traceback:   _KW_BLUE,

        Error:               'bg:'+_OW_PURPLE,
    }
