class Frequency_Stack:
    def __init__(self):
        self.cnt = {}
        self.maxcnt = 0
        self.stacks = {}

    def push(self, value: int) -> None:
        new_freq = 1 + self.cnt.get(value, 0)
        self.cnt[value] = new_freq
        # For Updating MaxCount
        if new_freq > self.maxcnt:
            self.maxcnt = new_freq
            self.stacks[self.maxcnt] = []

        self.stacks[new_freq].append(value)

    def pop(self) -> int:
        max_int = self.maxcnt
        self.cnt[max_int] -= 1
