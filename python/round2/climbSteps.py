def steps1(stepsLeft):
        if stepsLeft == 0:
                return 1
        if stepsLeft < 0:
                return 0
        return steps(stepsLeft -1) + steps(stepsLeft -2) + steps(stepsLeft -3)

def steps2(stepsLeft):
        stepCount = {0: 1}
        def build(steps):
                if steps < 0:
                        return 0
                if steps not in stepCount:
                        stepCount[steps] = build(steps-1) + build(steps-2) + build(steps-3)
                return stepCount[steps]
        return build(stepsLeft)


TEST = 5
print(steps2(TEST))
