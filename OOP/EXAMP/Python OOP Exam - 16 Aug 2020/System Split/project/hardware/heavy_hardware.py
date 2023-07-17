from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    HARDWARE_TYPE = "Heavy"

    def __init__(self, name, capacity, memory):
        super().__init__(name, HeavyHardware.HARDWARE_TYPE, capacity * 2, int(memory * 0.75))
