import matplotlib.pyplot as plt
import numpy as np


def plt_stress_test(file_name, title_prefix, save):
    f = open(file_name, 'r')
    fig, ax = plt.subplots(2)
    ax2 = ax[0].twinx()
    ax21 = ax[1].twinx()
    fig.set_dpi(500)

    # time = []
    throttle = []
    voltage = []
    thrust = []
    torque = []
    current = []

    lines = f.readlines()

    i = 1
    # while i < len(lines):
    while i < len(lines):
        data = lines[i].split(',')
        if (len(data) >= 11):
            # time.append(float(data[0]))
            throttle.append((float(data[1]) - 1000.) / 10.)
            thrust.append(float(data[9]))
            voltage.append(float(data[10]))
            current.append(float(data[11]))
            torque.append(float(data[8]))
        # print(data[0], data[10])
        i += 1

    ax[0].plot(throttle, thrust, color="#00FF00")
    ax2.plot(throttle, torque, color="#FF0000")
    # plt.xticks(np.arange(start=0, stop=40, step=5))
    ax[0].set_title(title_prefix + " Stress Test: Mechanical Performance")
    ax[0].set_xlabel('% Throttle', color="#FFFFFF")
    ax[0].set_ylabel('Thrust (lbf)', color="#00FF00")
    ax2.set_ylabel('Torque (lb·ft)', color="#FF0000")


    ax[1].plot(throttle, voltage, color="#00FF00")
    ax21.plot(throttle, current, color="#FF0000")
    # plt.xticks(np.arange(start=0, stop=40, step=5))
    ax[1].set_title(title_prefix + " Stress Test: Electrical Performance")
    ax[1].set_xlabel('% Throttle', color="#FFFFFF")
    ax[1].set_ylabel('Battery Voltage (V)', color="#00FF00")
    ax21.set_ylabel('Battery Current (A)', color="#FF0000")


    size = 64.*1.5

    fig.set_size_inches(size * (1 / 9), size * (1 / 16))
    plt.show()
    if save:
        fig.savefig("StressTest_Mechanical-Electrical.png", dpi=500)


if __name__ == "__main__":
    plt.style.use("dark_background")
    plt.rcParams["font.family"] = "Consolas"

    # Parse Args
    plt_stress_test(args[0], args[1], args[2])
