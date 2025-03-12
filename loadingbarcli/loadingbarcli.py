import sys
import time
from colorama import Fore, Style

class LoadingBar:
    def __init__(self, total, length=50, fill='█', color=Fore.GREEN):
        self.total = total
        self.length = length
        self.fill = fill
        self.color = color
        self.progress = 0

    def update(self, progress):
        self.progress = progress
        percent = f"{100 * (self.progress / self.total):.1f}%"
        filled_length = int(self.length * self.progress // self.total)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        sys.stdout.write(f'\r{self.color}|{bar}| {percent}{Style.RESET_ALL}')
        sys.stdout.flush()

    def finish(self):
        self.update(self.total)
        print()

# Example usage
if __name__ == "__main__":
    bar = LoadingBar(total=100, color=Fore.BLUE)
    for i in range(101):
        time.sleep(0.05)
        bar.update(i)
    bar.finish()