#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:54:21 2022

@author: phil
"""
from typing import List
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os, subprocess, json


mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "google-chrome-beta" # My browser of choice
myRun = "krunner" # My program runner

def htop():
    qtile.cmd_spawn('urxvtc -e htop')
def powermenu():
    qtile.cmd_spawn('powermenu')
def weather():
    qtile.cmd_spawn('xdg-open https://openweathermap.org/city/3333147')
def sound():
    qtile.cmd_spawn('outputmenu')
def calendar():
    qtile.cmd_spawn('urxvtc -e khal interactive')
def launcher():
    qtile.cmd_spawn('rofi -show drun -show-icons -location 7 -yoffset -22')
def timer():
    qtile.cmd_spawn('timermenu')
def quake():
    qtile.cmd_spawn('qtile cmd-obj -o group scratchpad  -f  dropdown_toggle -a term')
def metamenu():
    qtile.cmd_spawn('metamenu')
    
    
#Pywal Colors
colors = os.path.expanduser('~/.cache/wal/colors.json')
colordict = json.load(open(colors))
ColorZ=(colordict['colors']['color0'])
ColorA=(colordict['colors']['color1'])
ColorB=(colordict['colors']['color2'])
ColorC=(colordict['colors']['color3'])
ColorD=(colordict['colors']['color4'])
ColorE=(colordict['colors']['color5'])
ColorF=(colordict['colors']['color6'])
ColorG=(colordict['colors']['color7'])
ColorH=(colordict['colors']['color8'])
ColorI=(colordict['colors']['color9'])


keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod, "shift"], "Return",
             lazy.spawn(myRun),
             desc='Run Launcher'
             ),
         Key([mod], "b",
             lazy.spawn(myBrowser),
             desc='google-chrome-beta'
             ),
         # Key([mod], "/",
         #     lazy.spawn("dtos-help"),
         #     desc='DTOS Help'
         #     ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key(["control", "shift"], "e",
             lazy.spawn("emacsclient -c -a emacs"),
             desc='Doom Emacs'
             ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         Key([mod], "r",
             lazy.to_screen(2),
             desc='Keyboard focus to monitor 3'
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         # Emacs programs launched using the key chord CTRL+e followed by 'key'
         KeyChord([mod],"e", [
             Key([], "e",
                 lazy.spawn("emacsclient -c -a 'emacs'"),
                 desc='Emacsclient Dashboard'
                 ),
             Key([], "a",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(emms)' --eval '(emms-play-directory-tree \"~/Music/\")'"),
                 desc='Emacsclient EMMS (music)'
                 ),
             Key([], "b",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
                 desc='Emacsclient Ibuffer'
                 ),
             Key([], "d",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
                 desc='Emacsclient Dired'
                 ),
             Key([], "i",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
                 desc='Emacsclient ERC (IRC)'
                 ),
             Key([], "n",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
                 desc='Emacsclient Elfeed (RSS)'
                 ),
             Key([], "s",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
                 desc='Emacsclient Eshell'
                 ),
             Key([], "v",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
                 desc='Emacsclient Vterm'
                 ),
             Key([], "w",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(doom/window-maximize-buffer(eww \"distro.tube\"))'"),
                 desc='Emacsclient EWW Browser'
                 )
         ]),
         # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
         KeyChord([mod], "p", [
             Key([], "h",
                 lazy.spawn("dm-hub"),
                 desc='List all dmscripts'
                 ),
             Key([], "a",
                 lazy.spawn("dm-sounds"),
                 desc='Choose ambient sound'
                 ),
             Key([], "b",
                 lazy.spawn("dm-setbg"),
                 desc='Set background'
                 ),
             Key([], "c",
                 lazy.spawn("dtos-colorscheme"),
                 desc='Choose color scheme'
                 ),
             Key([], "e",
                 lazy.spawn("dm-confedit"),
                 desc='Choose a config file to edit'
                 ),
             Key([], "i",
                 lazy.spawn("dm-maim"),
                 desc='Take a screenshot'
                 ),
             Key([], "k",
                 lazy.spawn("dm-kill"),
                 desc='Kill processes '
                 ),
             Key([], "m",
                 lazy.spawn("dm-man"),
                 desc='View manpages'
                 ),
             Key([], "n",
                 lazy.spawn("dm-note"),
                 desc='Store and copy notes'
                 ),
             Key([], "o",
                 lazy.spawn("dm-bookman"),
                 desc='Browser bookmarks'
                 ),
             Key([], "p",
                 lazy.spawn("passmenu -p \"Pass: \""),
                 desc='Logout menu'
                 ),
             Key([], "q",
                 lazy.spawn("dm-logout"),
                 desc='Logout menu'
                 ),
             Key([], "r",
                 lazy.spawn("dm-radio"),
                 desc='Listen to online radio'
                 ),
             Key([], "s",
                 lazy.spawn("dm-websearch"),
                 desc='Search various engines'
                 ),
             Key([], "t",
                 lazy.spawn("dm-translate"),
                 desc='Translate text'
                 )
         ])
]


#Workspace Groups
group_names = [("I", {}),
               ("II", {}),
               ("III", {}),
               ("IV", {}),
               ("V", {}),]
groups = [Group(name, **kwargs) for name, kwargs in group_names]
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group
groups = [ScratchPad("scratchpad",[
          DropDown("term", "urxvt", opacity=0.95)]),
          Group("I", layout='monadtall', matches=[Match(wm_class=["qutebrowser",
                                                                  "Thunderbird",
                                                                  "akregator",])]),
          Group("II", layout='monadtall', matches=[Match(wm_class=["vlc",
                                                                   "gpodder"])]),
          Group("III", layout='bsp', matches=[Match(wm_class=["Steam",
                                                             "Lutris",
                                                             "RetroArch",
                                                              "dosbox"])]),
          Group("IV", layout='max', matches=[Match(wm_class=["VirtualBox Machine",
                                                             "virt-manager",
                                                             "VirtualBox Manager",
                                                             "VirtualBoxVM"])]),
          Group("V", layout='max', matches=[Match(wm_class=["gimp",
                                                            "Inkscape",
                                                            "krita",
                                                            "darktable",
                                                            "shotwell",
                                                            "scribus",
                                                            "Blender"])]),]

layouts = [
     layout.Bsp(margin=5,
                border_focus=ColorE,
                border_normal=ColorA),
     layout.MonadTall(margin=5,
                border_focus=ColorE,
                border_normal=ColorA),
     layout.Max(),
]

#Widget Defaults
widget_defaults = dict(
    font='Noto Sans',
    fontsize=13,
    padding=5,
    foreground=ColorG
)
extension_defaults = widget_defaults.copy()

#Screens
screens = [
    Screen(
        top=bar.Bar(
            [
             widget.GroupBox(highlight_method='line',
                             urgent_border=ColorF,
                             active=ColorG,
                             inactive=ColorB,
                             this_screen_border=ColorB,
                             this_current_screen_border=ColorC,),
             widget.Spacer(length = bar.STRETCH),
             widget.TextBox(text='',
                            mouse_callbacks = {'Button1':quake}),
             widget.Clock(format='%a %b %d',
                          font='Noto Sans Bold',
                          padding=0,
                          mouse_callbacks={'Button1':calendar}),
             widget.Clock(format='%I:%M %p',
                          font='Noto Sans Bold',
                          mouse_callbacks={'Button1':timer}),
             widget.Spacer(length = bar.STRETCH),
             widget.KhalCalendar(foreground="#282828",
                                 remindertime=1440,
                                 reminder_color=ColorG,
                                 mouse_callbacks={'Button1':calendar}),
             widget.OpenWeather(cityid=3333147,
                               metric=False,
                               format=' {main_temp}°{units_temperature}',
                               mouse_callbacks = {'Button1':weather}),
             widget.TextBox(text='',
                            mouse_callbacks = {'Button1':sound}),
             widget.PulseVolume(),
             widget.TextBox(mouse_callbacks = {'Button1':powermenu},
                            text='',),
             widget.Spacer(length=5)
           ],
            22,
            background ='#282828',
        ),
        bottom=bar.Bar(
        [
            widget.TextBox(text='',
                           foreground=ColorB,
                           mouse_callbacks = {'Button1':launcher}),
            widget.WindowName(font='Noto Sans Bold'),
            widget.Cmus(play_color=ColorG,
                        noplay_color=ColorB),
            widget.CPU(mouse_callbacks = {'Button1':htop}),
            widget.Memory(format='MEM{MemUsed: .0f}{mm}',
                          mouse_callbacks = {'Button1':htop}),
            widget.Systray(),
            widget.CurrentLayoutIcon(scale=.65),
            widget.TextBox(text='',
                           mouse_callbacks = {'Button1':metamenu})
        ],
            22,
            background='#282828',
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating( border_focus=ColorE,
                                   border_normal=ColorA,
    float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='ssh-askpass'),
    Match(title='branchdialog'),
    Match(title='pinentry'),
    Match(title='khal'),
    Match(title='Volume Control'),
    Match(title='Library'),
    Match(title='Unlock Login Keyring'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='lxpolkit'),
    Match(wm_class='error'),
    Match(wm_class='pamac-manager'),
    Match(wm_class='lxappearance'),
    Match(wm_class='kvantummanager'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='gcolor3'),
    Match(wm_class='qalculate-gtk'),
    Match(wm_class='qt5ct'),])


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wmname = "LG3D"
