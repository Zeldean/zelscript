"""Pomodoro timer - configurable work/rest cycles for productivity"""
import time


def timer(work = 25, rest = 5, cycles = 4):
    timeing = {
        "work": work,
        "rest": rest,
        "cycles": cycles
    }

    print("Pomodoro timer started")
    for c in range(timeing['cycles']):
        print(f"Cycle {c+1} of {timeing['cycles']}")

        workStart = time.time()
        workingTime = timeing['work'] * 60
        print(f"Work for {timeing['work']} minutes")
        countDown(workingTime, workStart, timeing['work'])

        restStart = time.time()
        restingTime = timeing['rest'] * 60
        print(f"Rest for {timeing['rest']} minutes")
        countDown(restingTime, restStart, timeing['rest'])

       

def countDown(remainingTime, start, total):
    while remainingTime > 0:
        mins, secs = divmod(remainingTime, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"Time Remaining: {timer}", end="\r")
        time.sleep(1)
        remainingTime = total * 60 - int(time.time() - start)
    print("Time's up!")

