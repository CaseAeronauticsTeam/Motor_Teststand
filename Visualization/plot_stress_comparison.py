import matplotlib.pyplot as plt
import numpy as np


def plt_stress_comparison(file_names, labels, title_prefix):
    assert len(file_names) == len(labels)

    fig, ax = plt.subplots(2)
    fig.set_dpi(500)

    for (file_name, label, prop_num) in zip(file_names, labels, range(len(file_names))):
        f = open(file_name, 'r')
        throttle = []
        thrust = []
        current = []

        lines = f.readlines()

        i = 1
        while i < len(lines):
            data = lines[i].split(',')
            if (len(data) >= 11):
                throttle.append((float(data[1]) - 1000.) / 10.)
                thrust.append(float(data[9]))
                current.append(float(data[11]))
            i += 1

        prop_color = "#" + hex(0xFF0000 + (int((prop_num/len(file_names))*255) << 8))[2:]
        ax[0].plot(throttle, thrust, color=prop_color, label=label)
        ax[0].set_title(title_prefix + " Stress Test Comparison: Mechanical Performance")
        ax[0].set_xlabel('% Throttle', color="#FFFFFF")
        ax[0].set_ylabel('Thrust (lbf)', color="#00FF00")

        ax[1].plot(throttle, current, color=prop_color, label=label)
        ax[1].set_title(title_prefix + " Stress Test Comparison: Electrical Performance")
        ax[1].set_xlabel('% Throttle', color="#FFFFFF")
        ax[1].set_ylabel('Battery Current (A)', color="#FF0000")

    ax[0].legend(loc='upper right', bbox_to_anchor=(1.13, 1.03))
    size = 64. * 1.5
    fig.set_size_inches(size * (1 / 9), size * (1 / 16))
    ax[0].grid(color='w', linestyle=':', linewidth=.5)
    ax[1].grid(color='w', linestyle=':', linewidth=.5)
    plt.show()


if __name__ == "__main__":
    plt.style.use("dark_background")
    plt.rcParams["font.family"] = "Consolas"

    # Parse Args
    plt_stress_comparison(args[0], args[1], args[2])
