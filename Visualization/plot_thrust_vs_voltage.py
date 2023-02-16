import matplotlib.pyplot as plt
import numpy as np


def plt_thrust_vs_voltage(file_name, save):
    TITLE = "Motor Endurance Test: Thrust vs Battery Voltage"

    f = open(file_name, 'r')
    fig, ax = plt.subplots()
    # ax2 = ax.twinx()
    fig.set_dpi(500)

    time = []
    voltage = []
    thrust = []
    current = []

    lines = f.readlines()

    i = 1
    while i < len(lines):
        data = lines[i].split(',')
        if (len(data) >= 10):
            time.append(float(data[0]))
            thrust.append(float(data[9]))
            voltage.append(float(data[10]))
            current.append(float(data[11]))
        # print(data[0], data[10])
        i += 1

    # ax2.plot(time, thrust, color="#FF0000")
    # print(sorted(current))
    paired = []
    for i in range(len(voltage)):
        paired.append([voltage[i], thrust[i]])
    paired.sort()
    # for i in range(len(paired)):
    #     print(i, *paired[i])


    # Remove outliers via eyeballed best-fit line
    x = np.arange(0, paired[len(paired) - 1][0], paired[len(paired) - 1][0] / len(paired))
    y = []
    for c in x:
        y.append(1.3 * c**.525)
    paired_pruned = []
    for i in range(len(paired)):
        if abs(paired[i][1] - 1.3 * paired[i][0]**.525) < 3:
            paired_pruned.append(paired[i])

    paired = np.array(paired_pruned)
    ax.plot(paired[:, 0], paired[:, 1], color="#00FF00")

    ax.set_title(TITLE)
    ax.set_xlabel('Battery Voltage (V)', color="#FFFFFF")
    ax.set_ylabel('Thrust (lbf)', color="#FFFFFF")

    size = 64.
    fig.set_size_inches(size * (1 / 9), size * (1 / 16))
    plt.show()
    if save:
        fig.savefig("StressTest_ThrustVsVoltage.png", dpi=500)


if __name__ == "__main__":
    plt.style.use("dark_background")
    plt.rcParams["font.family"] = "Consolas"

    # Parse Args
    plt_thrust_vs_voltage(args[0], args[1], args[2])
