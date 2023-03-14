import time
class SignalController:
    def __init__(self, gotime):
        self.all_signals = []
        total_time = sum(gotime)

        for i, gt in enumerate(gotime):
            red_time = total_time - gt
            curr = sum(gotime[0:i])
            self.all_signals.append(Signal(gt, red_time, curr))

    def play(self):
        while True:
            time.sleep(1) #delay
            print('-----------------------')
            for sig in self.all_signals:
                sig.transit()
                print(sig.get_state())
            print('-----------------------')


class Signal:
    all_state = {0: ['RED', 'Stop!'], 1: ['GREEN', 'Go!'], 2: ['ORANGE', 'Slow Down, Don\'t Cross The Line!'] }

    def __init__(self, go_time, red_time, curr):
        self.state = 0
        self.curr = curr
        self.time = [red_time, go_time - (go_time*10//100), go_time * 10 // 100]

    def transit(self):
        if self.curr == 0:
            self.state = (self.state + 1) % len(Signal.all_state)
            self.curr = self.time[self.state]

        self.curr-=1

    def get_state(self):
        return Signal.all_state[self.state], self.curr

def main():
    controller = SignalController((30,40, 25, 40))
    controller.play()

main()