import board # type: ignore

# keyboard
from kmk.kmk_keyboard import KMKKeyboard # type: ignore
from kmk.keys import KC, make_key # type: ignore
from kmk.scanners import DiodeOrientation # type: ignore
keyboard = KMKKeyboard()

# mcu
C0 = board.GP7
C1 = board.GP6
C2 = board.GP5
C3 = board.GP4
C4 = board.GP3
C5 = board.GP28
C6 = board.GP27
C7 = board.GP26
C8 = board.GP22
C9 = board.GP20

R0 = board.GP2
R1 = board.GP8
R2 = board.GP9
R3 = board.GP12
R4 = board.GP29
R5 = board.GP23
R6 = board.GP21
R7 = board.GP16

RED_LED = board.GP17

# board definition
keyboard.col_pins = [C0, C1, C2, C3, C4, C5, C6, C7, C8, C9]
keyboard.row_pins = [R0, R1, R2, R3, R4, R5, R6, R7]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# layers
from kmk.modules.layers import Layers # type: ignore
layers = Layers()
keyboard.modules.append(layers)

# led
from kmk.extensions.LED import LED # type: ignore
from kmk.extensions.lock_status import LockStatus # type: ignore
led = LED(led_pin=RED_LED)
keyboard.extensions.append(led)

class LEDLockStatus(LockStatus):
    def set_lock_leds(self):
        if self.get_caps_lock():
            led.set_brightness(100)
        else:
            led.set_brightness(0)

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)  # Critically important. Do not forget
        if self.report_updated:
            self.set_lock_leds()

keyboard.extensions.append(LEDLockStatus())

# combos
from kmk.modules.combos import Combos, Chord # type: ignore
combos = Combos()
keyboard.modules.append(combos)

combos.combo_term = 500

# holdtap
from kmk.modules.holdtap import HoldTap, HoldTapRepeat # type: ignore
holdtap = HoldTap()
keyboard.modules.append(holdtap)

holdtap.tap_time = None
holdtap.prefer_hold = False
holdtap.repeat = HoldTapRepeat.NONE

# media
from kmk.extensions.media_keys import MediaKeys # type: ignore
mediaKeys = MediaKeys()
keyboard.extensions.append(mediaKeys)

# keycode abbreviations
# mods
LSFT = KC.LSFT
RSFT = KC.RSFT
LCMD = KC.LCMD
RCMD = KC.RCMD
LALT = KC.LALT
RALT = KC.RALT
LCTL = KC.LCTL
RCTL = KC.RCTL
# misc
ENTR = KC.ENT
SPAC = KC.SPACE
COMM = KC.COMMA
SEMI = KC.SCOLON
SLAS = KC.SLASH
PERI = KC.DOT
BSPC = KC.BSPC
DELE = KC.DEL
CAPS = KC.CAPS
ESCP = KC.ESCAPE
NONE = KC.NO
# numbers
NUM1 = KC.N1
NUM2 = KC.N2
NUM3 = KC.N3
NUM4 = KC.N4
NUM5 = KC.N5
NUM6 = KC.N6
NUM7 = KC.N7
NUM8 = KC.N8
NUM9 = KC.N9
NUM0 = KC.N0
# symbols
BANG = KC.EXLM
ROBA = KC.AT
HASH = KC.HASH
BUCK = KC.DLR
PERC = KC.PERC
CIRC = KC.CIRC
AMPR = KC.AMPR
STAR = KC.ASTR
# navigation
ARUP = KC.UP
ARLF = KC.LEFT
ARRT = KC.RIGHT
ARDN = KC.DOWN
# function
FN01 = KC.F1
FN02 = KC.F2
FN03 = KC.F3
FN04 = KC.F4
FN05 = KC.F5
FN06 = KC.F6
FN07 = KC.F7
FN08 = KC.F8
FN09 = KC.F9
FN10 = KC.F10
FN11 = KC.F11
FN12 = KC.F12
# media
VLUP = KC.AUDIO_VOL_UP
VLDN = KC.AUDIO_VOL_DOWN

# layer definitions
NUMB = KC.MO(1)
NAVI = KC.MO(2)
FUNC = KC.MO(3)
SYMB = KC.MO(4)
TRNS = KC.TRNS

# hold taps (HOME ROW MOD)
ACTL = KC.HT(KC.A, LCTL)
RALT = KC.HT(KC.R, LALT)
SCMD = KC.HT(KC.S, LCMD)
TSFT = KC.HT(KC.T, LSFT)

NSFT = KC.HT(KC.N, RSFT)
ECMD = KC.HT(KC.E, RCMD)
IALT = KC.HT(KC.I, RALT)
OCTL = KC.HT(KC.O, RCTL)

SPCN = KC.HT(SPAC, NAVI)
FUND = KC.HT(KC.D, FUNC)

# combos
combos.combos = [
    # LEFT HAND
    # (INDEX, MAJOR)
    Chord((KC.P, KC.F), KC.PLUS),
    Chord((TSFT, SCMD), KC.HT(KC.EQUAL, KC.LCMD(KC.LSFT))),
    Chord((FUND, KC.C), KC.TAB),
    Chord((FUND, SCMD), KC.LEFT_PAREN),
    # (MAJOR, RING)
    Chord((KC.F, KC.W), KC.MINUS),
    Chord((SCMD, RALT), KC.HT(KC.UNDS, KC.LALT(KC.LSFT))),
    Chord((KC.X, KC.C), KC.LABK),
    # (RING, MINOR)
    Chord((KC.W, KC.Q), KC.TILDE),
    Chord((ACTL, RALT), KC.HT(KC.GRAVE, KC.LCTL(KC.LALT))),
    # (INDEX, RING)
    Chord((FUND, RALT), KC.LCBR),
    # (INDEX, MINOR)
    Chord((FUND, ACTL), KC.LBRC),
    
    # RIGHT HAND
    # (INDEX, MAJOR)
    Chord((KC.L, KC.U), KC.DOUBLE_QUOTE),
    Chord((NSFT, ECMD), KC.HT(KC.QUOTE, KC.RCMD(KC.RSFT))),
    Chord((KC.H, ECMD), KC.RIGHT_PAREN),
    Chord((KC.H, KC.COMMA), KC.SPACE),
    # (MAJOR, RING)
    Chord((KC.U, KC.Y), KC.BSLASH),
    Chord((ECMD, IALT), KC.HT(KC.PIPE, KC.RCMD(KC.RALT))),
    Chord((KC.DOT, KC.COMMA), KC.RABK),
    # (INDEX, RING)
    Chord((KC.H, IALT), KC.RCBR),
    # (INDEX, MINOR)
    Chord((KC.H, OCTL), KC.RBRC),
]

mods_before_modmorph = set()
def MOD(names = {'DUMMY_KEY',}, default_kc = NONE, morphed_kc = NONE, triggers = {LSFT, RSFT}):
    def _pressed(key, state, KC, *args, **kwargs):
        global mods_before_modmorph
        mods_before_modmorph = triggers.intersection(state.keys_pressed)
        # if a trigger is held, morph key
        if mods_before_modmorph:
            state._send_hid()
            for mod_kc in mods_before_modmorph:
                # discard triggering mods so morphed key is unaffected by them
                state.keys_pressed.discard(mod_kc)
            state.keys_pressed.add(morphed_kc)
            state.hid_pending = True
            return state
        # else return default keycode
        state.keys_pressed.add(default_kc)
        state.hid_pending = True
        return state
    def _released(key, state, KC, *args, **kwargs):
        if {morphed_kc,}.intersection(state.keys_pressed):
            state.keys_pressed.discard(morphed_kc)
            for mod_kc in mods_before_modmorph:
                # re-add previously discarded shift so normal typing isn't impacted
                state.keys_pressed.add(mod_kc)
        else:
            state.keys_pressed.discard(default_kc)
        state.hid_pending = True
        return state
    modmorph_key = make_key(names=names, on_press=_pressed,
                            on_release=_released)
    return modmorph_key

MOD({'ERAS'}, BSPC, DELE)
ERAS = KC.ERAS

keyboard.keymap = [
    # Alphas
    [
        #left hand
        KC.Q, KC.W, KC.F, KC.P, KC.B, NONE, NONE, NONE, NONE, NONE,
        ACTL, RALT, SCMD, TSFT, KC.G, NONE, NONE, NONE, NONE, NONE,
        KC.Z, KC.X, KC.C, FUND, KC.V, NONE, NONE, NONE, NONE, NONE,
        NONE, NONE, NONE, NONE, NUMB, NONE, NONE, NONE, NONE, NONE,
        #right hand
        NONE, NONE, NONE, NONE, NONE, KC.J, KC.L, KC.U, KC.Y, SEMI,
        NONE, NONE, NONE, NONE, NONE, KC.M, NSFT, ECMD, IALT, OCTL,
        NONE, NONE, NONE, NONE, NONE, KC.K, KC.H, COMM, PERI, SLAS,
        NONE, NONE, NONE, NONE, NONE, SPCN, NONE, NONE, NONE, NONE,
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
        VLUP, ARLF, ARDN, ARRT, NONE, NONE, NONE, NONE, NONE, NONE,
        VLDN, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
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
