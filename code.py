# keyboard
from kmk.kmk_keyboard import KMKKeyboard # type: ignore
from kmk.keys import KC, make_key # type: ignore
from keys import *

# board definition
import pins as p
from kmk.scanners import DiodeOrientation # type: ignore
keyboard = KMKKeyboard()

keyboard.col_pins = [p.C0, p.C1, p.C2, p.C3, p.C4, p.C5, p.C6, p.C7, p.C8, p.C9]
keyboard.row_pins = [p.R0, p.R1, p.R2, p.R3, p.R4, p.R5, p.R6, p.R7]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# media
from kmk.extensions.media_keys import MediaKeys # type: ignore
mediaKeys = MediaKeys()
keyboard.extensions.append(mediaKeys)

VLUP = KC.AUDIO_VOL_UP
VLDN = KC.AUDIO_VOL_DOWN

# layers
from kmk.modules.layers import Layers # type: ignore
layers = Layers()
keyboard.modules.append(layers)

# layer definitions
NUMB = KC.MO(1)
NAVI = KC.MO(2)
FUNC = KC.MO(3)
SYMB = KC.MO(4)
TRNS = KC.TRNS

# holdtap
from kmk.modules.holdtap import HoldTap, HoldTapRepeat # type: ignore
holdtap = HoldTap()
keyboard.modules.append(holdtap)

holdtap.tap_time = None
holdtap.prefer_hold = False
holdtap.repeat = HoldTapRepeat.NONE

# hold taps (HOME ROW MOD)
CTLA = KC.HT(KC.A, LCTL)
ALTR = KC.HT(KC.R, LALT)
CMDS = KC.HT(KC.S, LCMD)
SFTT = KC.HT(KC.T, LSFT)

SFTN = KC.HT(KC.N, RSFT)
CMDE = KC.HT(KC.E, RCMD)
ALTI = KC.HT(KC.I, RALT)
CTLO = KC.HT(KC.O, RCTL)

SPNV = KC.HT(SPAC, NAVI)
FUND = KC.HT(KC.D, FUNC)

# combos
from kmk.modules.combos import Combos, Chord # type: ignore
combos = Combos()
keyboard.modules.append(combos)

# combos
combos.combos = [
    # LEFT HAND
    # (INDEX, MAJOR)
    Chord((KC.P, KC.F), KC.PLUS),
    Chord((SFTT, CMDS), KC.HT(KC.EQUAL, KC.LCMD(KC.LSFT))),
    Chord((FUND, KC.C), KC.TAB),
    Chord((FUND, CMDS), KC.LEFT_PAREN),
    # (MAJOR, RING)
    Chord((KC.F, KC.W), KC.MINUS),
    Chord((CMDS, ALTR), KC.HT(KC.UNDS, KC.LALT(KC.LCMD))),
    Chord((KC.X, KC.C), KC.LABK),
    # (RING, MINOR)
    Chord((KC.W, KC.Q), KC.TILDE),
    Chord((CTLA, ALTR), KC.HT(KC.GRAVE, KC.LCTL(KC.LALT))),
    # (INDEX, RING)
    Chord((FUND, ALTR), KC.LCBR),
    # (INDEX, MINOR)
    Chord((FUND, CTLA), KC.LBRC),
    
    # RIGHT HAND
    # (INDEX, MAJOR)
    Chord((KC.L, KC.U), KC.DOUBLE_QUOTE),
    Chord((SFTN, CMDE), KC.HT(KC.QUOTE, KC.RCMD(KC.RSFT))),
    Chord((KC.H, CMDE), KC.RIGHT_PAREN),
    Chord((KC.H, KC.COMMA), KC.SPACE),
    Chord((NUM7, NUM8), KC.COMMA),
    Chord((NUM8, NUM9), KC.DOT),
    # (MAJOR, RING)
    Chord((KC.U, KC.Y), KC.BSLASH),
    Chord((CMDE, ALTI), KC.HT(KC.PIPE, KC.RCMD(KC.RALT))),
    Chord((KC.DOT, KC.COMMA), KC.RABK),
    # (INDEX, RING)
    Chord((KC.H, ALTI), KC.RCBR),
    # (INDEX, MINOR)
    Chord((KC.H, CTLO), KC.RBRC),
]

# mod morph
def MOD(names={'DUMMY_KEY'}, default_kc=NONE, morphed_kc=NONE, triggers={LSFT, RSFT}):
    mods_before_modmorph = set()  # Define the variable before using it as a nonlocal variable
    def _pressed(key, state, KC, *args, **kwargs):
        nonlocal mods_before_modmorph
        mods_before_modmorph = triggers & state.keys_pressed
        if mods_before_modmorph:
            state.keys_pressed -= mods_before_modmorph
            state.keys_pressed.add(morphed_kc)
        else:
            state.keys_pressed.add(default_kc)
        state.hid_pending = True

    def _released(key, state, KC, *args, **kwargs):
        nonlocal mods_before_modmorph
        if morphed_kc in state.keys_pressed:
            state.keys_pressed.remove(morphed_kc)
            state.keys_pressed |= mods_before_modmorph
        else:
            state.keys_pressed.discard(default_kc)
        state.hid_pending = True

    return make_key(names=names, on_press=_pressed, on_release=_released)

ERAS = MOD({'ERAS'}, BSPC, DELE)
MDUP = MOD({'MDUP'}, VLUP, KC.F15)
MDDN = MOD({'MDDN'}, VLDN, KC.F14)

keyboard.keymap = [
    # Alphas
    [
        #left hand
        KC.Q, KC.W, KC.F, KC.P, KC.B, NONE, NONE, NONE, NONE, NONE,
        CTLA, ALTR, CMDS, SFTT, KC.G, NONE, NONE, NONE, NONE, NONE,
        KC.Z, KC.X, KC.C, FUND, KC.V, NONE, NONE, NONE, NONE, NONE,
        NONE, NONE, NONE, NONE, NUMB, NONE, NONE, NONE, NONE, NONE,
        #right hand
        NONE, NONE, NONE, NONE, NONE, KC.J, KC.L, KC.U, KC.Y, SEMI,
        NONE, NONE, NONE, NONE, NONE, KC.M, SFTN, CMDE, ALTI, CTLO,
        NONE, NONE, NONE, NONE, NONE, KC.K, KC.H, COMM, PERI, SLAS,
        NONE, NONE, NONE, NONE, NONE, SPNV, NONE, NONE, NONE, NONE,
    ],
    # Numbers
    [
        #left hand
        ESCP, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
        LCTL, LALT, LCMD, LSFT, NONE, NONE, NONE, NONE, NONE, NONE,
        NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
        NONE, NONE, NONE, NONE, TRNS, NONE, NONE, NONE, NONE, NONE,
        #right hand
        NONE, NONE, NONE, NONE, NONE, NONE, NUM1, NUM2, NUM3, ERAS,
        NONE, NONE, NONE, NONE, NONE, NONE, NUM4, NUM5, NUM6, NUM0,
        NONE, NONE, NONE, NONE, NONE, NONE, NUM7, NUM8, NUM9, NONE,
        NONE, NONE, NONE, NONE, NONE, ENTR, NONE, NONE, NONE, NONE,
    ],
    # Navigation
    [
        #left hand
        ESCP, NONE, ARUP, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
        MDUP, ARLF, ARDN, ARRT, NONE, NONE, NONE, NONE, NONE, NONE,
        MDDN, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
        NONE, NONE, NONE, NONE, CAPS, NONE, NONE, NONE, NONE, NONE,
        #right hand
        NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
        NONE, NONE, NONE, NONE, NONE, NONE, RSFT, RCMD, RALT, RCTL,
        NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
        NONE, NONE, NONE, NONE, NONE, TRNS, NONE, NONE, NONE, NONE,
    ],
    # Function
    [
        #left hand
        NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
        NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
        NONE, NONE, NONE, TRNS, NONE, NONE, NONE, NONE, NONE, NONE,
        NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
        #right hand
        NONE, NONE, NONE, NONE, NONE, NONE, FN01, FN02, FN03, FN04,
        NONE, NONE, NONE, NONE, NONE, NONE, FN05, FN06, FN07, FN08,
        NONE, NONE, NONE, NONE, NONE, NONE, FN09, FN10, FN11, FN12,
        NONE, NONE, NONE, NONE, NONE, SPAC, NONE, NONE, NONE, NONE,
    ]
]

if __name__ == '__main__':
    keyboard.go()
