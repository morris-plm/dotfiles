# -*- coding: utf-8 -*-
# A customized config.py for Qtile window manager (http://www.qtile.org)
# Modified by LongerHV (http://www.gitlab.com/LongerHV)
# Based on Derek Taylor configuration (http://www.gitlab.com/dwt1)
#
# The following comments are the copyright and licensing information from the default
# qtile config. Copyright (c) 2010 Aldo Cortesi, 2010, 2014 dequis, 2012 Randall Ma,
# 2012-2014 Tycho Andersen, 2012 Craig Barnes, 2013 horsik, 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.

# IMPORTS
import os
import subprocess
from typing import List  # noqa: F401

from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.command import lazy
from libqtile.config import Click, Drag, DropDown, Group, Key, ScratchPad, Screen
# from mylib import BGroupBox

# DEFINING SOME VARIABLES
os.environ['QT_QPA_PLATFORMTHEME'] = 'qt5ct'
MOD = "mod4"  # Sets mod key to SUPER/WINDOWS
ALT = "mod1"
MYTERM = "alacritty"
MYFONT = "Ubuntu Nerd Font"

BLACK = '#29414f'
RED = '#ec5f67'
GREEN = '#99c794'
YELLOW = '#fac863'
BLUE = '#6699cc'
MAGENTA = '#c594c5'
CYAN = '#5fb3b3'
WHITE = '#ffffff'

# KEYBINDINGS
keys = [
    # The essentials
    Key([MOD], "Return",
        lazy.spawn(MYTERM),
        desc='Launches Terminal'),
    Key([MOD, "shift"], "Return",
        lazy.run_extension(extension.DmenuRun(
            dmenu_prompt=">",
            dmenu_font='-'.join([MYFONT, '18']),
            background=BLACK,
            foreground=GREEN,
            selected_background=GREEN,
            selected_foreground=WHITE))),
    Key([MOD], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'),
    Key([MOD, "shift"], "c",
        lazy.window.kill(),
        desc='Kill active window'),
    Key([MOD, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'),
    Key([MOD, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'),
    Key([MOD, "shift"], "l",
        lazy.spawn("light-locker-command -l"),
        desc='Lock screen'),
    # Switch focus to specific monitor (out of three)
    Key([MOD], "w",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 1'),
    Key([MOD], "e",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 2'),
    Key([MOD], "r",
        lazy.to_screen(2),
        desc='Keyboard focus to monitor 3'),
    # Switch focus of monitors
    Key([MOD], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'),
    Key([MOD], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'),
    Key([MOD], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'),
    Key([MOD], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'),
    Key([MOD, "shift"], "k",
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'),
    Key([MOD, "shift"], "j",
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'),
    Key([MOD], "h",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'),
    Key([MOD], "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'),
    Key([MOD], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'),
    Key([MOD], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'),
    Key([MOD, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'),
    # Stack controls
    Key([MOD, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'),
    Key([MOD, "shift"], "v",
        lazy.spawn("clipmenu"),
        desc='Clipboard menu'),
    #  Key([MOD], "space",
    #      lazy.layout.next(),
    #      desc='Switch window focus to other pane(s) of stack'),
    #  Key([MOD, "control"], "Return",
    #      lazy.layout.toggle_split(),
    #      desc='Toggle between split and unsplit sides of stack'),
    # My applications launched with SUPER + ALT + KEY
    Key([MOD, ALT], "b",
        lazy.spawn("brave-nightly"),
        desc='Brave browser'),
    Key([MOD, ALT], "i",
        lazy.spawn("brave-nightly --incognito"),
        desc='Incognito window for perverted stuff '),
    Key([MOD, ALT], "m",
        lazy.spawn("spotify"),
        desc='Spotify'),
    Key([MOD, ALT], "s",
        lazy.spawn("spicy"),
        desc='Spicy'),
    Key([MOD, ALT], "v",
        lazy.spawn("virt-manager"),
        desc='Virt Manager'),
    Key([MOD, ALT], "c",
        lazy.spawn("code"),
        desc='VSCode'),
    Key([MOD, ALT], "g",
        lazy.spawn("steam"),
        desc='Steam'),
    Key([MOD, ALT], "f",
        lazy.spawn("pcmanfm-qt"),
        desc='File manager'),
    Key([], "F12",
        lazy.group["scratchpad"].dropdown_toggle('term'),
        desc='Dropdown terminal'),

    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    #  Key([MOD, ALT], "Return",
    #      lazy.group["ScratchPad"].dropdown_toggle(MYTERM),
    #      desc='Dropdown terminal'),
    #  Key(
    #  [], "3270_PrintScreen",
    #  [MOD], "Insert",
    #  lazy.spawn("screengrab"),
    #  desc="Print Screen"
    #  ),
    #  Key(
    #      [MOD, ALT], "v",
    #      lazy.spawn(MYTERM+" -e vim"),
    #      desc='vim'
    #      ),
]

# GROUPS
groups = (
    Group('1', label='', layout='monadtall'),
    Group('2', label='', layout='monadtall'),
    Group('3', label='', layout='monadtall'),
    Group('4', label='', layout='monadtall'),
    Group('5', label='', layout='monadtall'),
    Group('6', label='', layout='monadtall'),
    Group('7', label='', layout='monadtall'),
    Group('8', label='', layout='monadtall'),
    ScratchPad('scratchpad', [DropDown(
        'term', MYTERM, width=0.9, height=0.9,
        x=0.05, y=0.05, opacity=1.0, on_focus_lost_hide=False
    )])
)

for i, group in enumerate(groups[:-1], 1):
    # Switch to another group
    keys.append(Key([MOD], str(i), lazy.group[group.name].toscreen()))
    # Send current window to another group
    keys.append(Key([MOD, "shift"], str(i), lazy.window.togroup(group.name)))

# DEFAULT THEME SETTINGS FOR LAYOUTS
layout_theme = {
    "border_width": 3,
    "margin": 8,
    "border_focus": GREEN,
    "border_normal": BLACK
}

# THE LAYOUTS
layouts = (
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    #  layout.Tile(shift_windows=True, **layout_theme),
    #  layout.Stack(num_stacks=2),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
    #  layout.Floating(**layout_theme)
)

# DEFAULT WIDGET SETTINGS
widget_defaults = dict(
    font=MYFONT,
    fontsize=18,
    padding=2,
    background=BLACK
)
extension_defaults = widget_defaults.copy()


# WIDGETS
def init_xmenu():
    return widget.TextBox(
        text="",
        foreground=WHITE,
        background=BLACK,
        fontsize=32,
        padding=8,
        mouse_callbacks={
            'Button1': lambda: qtile.cmd_spawn([
                '/bin/bash', os.path.expanduser(os.path.join(
                    '~', 'scripts', 'xmenu.sh'))
            ])
        }
    )


def init_group_box():
    return widget.GroupBox(
        fontsize=26,
        spacing=5,
        disable_drag=True,
        active=WHITE,
        inactive=WHITE,
        rounded=False,
        highlight_method="block",
        this_current_screen_border=GREEN,
        this_screen_border=CYAN,
        other_current_screen_border=BLACK,
        other_screen_border=BLACK,
        foreground=WHITE,
        background=BLACK,
        margin_x=6,
        margin_y=3,
        padding_x=4,
        padding_y=7,
    )


def init_check_updates():
    return widget.CheckUpdates(
        execute=' '.join([MYTERM, '-e', 'yay']),
        distro='Arch_yay',
        display_format=' Updates: {updates}',
        update_interval=1800,
        foreground=WHITE,
        background=CYAN,
        padding=5
    )


def init_bitcoin_ticker():
    return widget.BitcoinTicker(
        # currency='USD',
        fmt=" {}",
        foreground=WHITE,
        background=GREEN,
        padding=5
    )


def init_thermal_sensor():
    return widget.ThermalSensor(
        fmt=' {}',
        tag_sensor="Package id 0",
        foreground=WHITE,
        background=CYAN,
        padding=5
    )


def init_volume():
    return widget.Volume(
        fmt=" {}",
        foreground=WHITE,
        background=GREEN,
        padding=5
    )


def init_current_layout_icon():
    return widget.CurrentLayoutIcon(
        custom_icon_paths=[os.path.expanduser(
            "$HOME/.config/qtile/icons")],
        foreground=WHITE,
        background=CYAN,
        scale=0.6
    )


def init_curren_layout():
    return widget.CurrentLayout(
        foreground=WHITE,
        background=CYAN,
        padding=5
    )


def init_clock():
    return widget.Clock(
        fmt=" {}",
        foreground=WHITE,
        background=GREEN,
        padding=5,
        format="%A, %d %B [ %H:%M ]"
    )


def init_wide_bar(tray=True):
    return [
        init_xmenu(),
        init_group_box(),
        widget.TaskList(),
        widget.Systray(
            background=BLACK,
            padding=5
        ) if tray else widget.Sep(linewidth=0),
        widget.Sep(
            linewidth=0,
            padding=5,
            background=BLACK
        ),
        init_check_updates(),
        init_bitcoin_ticker(),
        init_thermal_sensor(),
        init_volume(),
        init_current_layout_icon(),
        init_curren_layout(),
        init_clock(),
        widget.Sep(
            linewidth=0,
            padding=5,
            background=GREEN
        )
    ]


def init_short_bar():
    return [
        init_group_box(),
        widget.TaskList(),
        init_current_layout_icon(),
        init_curren_layout(),
        init_clock(),
        widget.Sep(
            linewidth=0,
            padding=5,
            background=GREEN
        )
    ]


bar_list = (
    init_wide_bar(),
    init_wide_bar(tray=False),
    init_short_bar(),
)

# if __name__ in ["config", "__main__"]:
#     screens = [
#         Screen(top=bar.Bar(
#             widgets=widgets, opacity=1, size=30, margin=[8, 8, 0, 8],
#         )) for widgets in bar_list
#    ]

# DRAG FLOATING WINDOWS
mouse = (
    Drag([MOD], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], "Button2", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], "Button3", lazy.window.bring_to_front())
)

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

# FLOATING WINDOWS
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules
], **layout_theme)

auto_fullscreen = True
focus_on_window_activation = "smart"


# STARTUP APPLICATIONS
# @hook.subscribe.startup
# def runner():
#     subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    if qtile.core.name == 'x11':
        subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
