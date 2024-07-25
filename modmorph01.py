from kmk.keys import make_argumented_key
from kmk.modules import Module

class ConditionalKeyMeta:
    def __init__(self, mods, keyThen, keyElse):
        self.mods = set(mods)
        self.keyThen = keyThen
        self.keyElse = keyElse

class ConditionalKey(Module):
    def __init__(self):
        make_argumented_key(
            names=('CK',),
            validator=ConditionalKeyMeta,
        )

    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def process_key(self, keyboard, key, is_pressed, int_coord):
        if not isinstance(key.meta, ConditionalKeyMeta):
            return key

        if key.meta.mods.issubset(keyboard.keys_pressed):
            return key.meta.keyThen

        return key.meta.keyElse

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return