import matplotlib.pyplot as plt
import numpy as np


def plt_thrust_vs_power_comparison(file_names, labels, title):
    assert len(file_names) == len(labels)


    fig, ax = plt.subplots()
    # ax2 = ax.twinx()
    fig.set_dpi(500)

    for (file_name, label, prop_num) in zip(file_names, labels, range(len(file_names))):
        f = open(file_name, 'r')
        time = []
        voltage = []
        thrust = []
        power = []

        lines = f.readlines()

        i = 1
        while i < len(lines):
            data = lines[i].split(',')
            if (len(data) >= 10):
                time.append(float(data[0]))
                thrust.append(float(data[9]))
                voltage.append(float(data[10]))
                power.append(float(data[14]))
            # print(data[0], data[10])
            i += 1

        prop_color = "#" + hex(0xFF0000 + (int((prop_num/len(file_names))*255) << 8))[2:]
        paired = []
        for i in range(len(power)):
            paired.append([power[i], thrust[i]])
        paired.sort()
        # for i in range(len(paired)):
        #     print(i, *paired[i])

        # Remove outliers via eyeballed best-fit line
        x = np.arange(0, paired[len(paired) - 1][0], paired[len(paired) - 1][0] / len(paired))
        y = []
        for c in x:
            y.append(1.3 * c ** .525)
        paired_pruned = []
        for i in range(len(paired)):
            # if abs(paired[i][1] - 1.3 * paired[i][0] ** .525) < 3:
            if True:
                paired_pruned.append(paired[i])

        paired = np.array(paired_pruned)
        ax.plot(paired[:, 0], paired[:, 1], color=prop_color, label=label)
        # plt.xticks(np.arange(start=0, stop=280, step=30))
        # plt.yticks(np.arange(start=0, stop=30,  step=5))

        ax.set_title(title)
        ax.set_xlabel('Battery Current (A)', color="#FFFFFF")
        ax.set_ylabel('Thrust (lbf)', color="#FFFFFF")
        # ax2.set_ylabel('Thrust (lbf)', color="#FF0000")

    plt.legend()
    ax.grid(color='w', linestyle=':', linewidth=.5)
    size = 64.
    fig.set_size_inches(size * (1 / 9), size * (1 / 16))
    plt.show()


if __name__ == "__main__":
    plt.style.use("dark_background")
    plt.rcParams["font.family"] = "Consolas"

    # Parse Args
    plt_thrust_vs_power_comparison(args[0], args[1], args[2])
