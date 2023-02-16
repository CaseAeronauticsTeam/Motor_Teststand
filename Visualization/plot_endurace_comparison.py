import matplotlib.pyplot as plt
import numpy as np


def plt_endurance_comparison(files, labels, title):
    assert len(files) == len(labels)

    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    fig.set_dpi(500)

    for (file_name, label) in zip(files, labels):
        f = open(file_name, 'r')

        time = []
        voltage = []
        thrust = []

        lines = f.readlines()

        i = 1
        while i < len(lines):
            data = lines[i].split(',')
            if (len(data) >= 10):
                time.append(float(data[0]))
                thrust.append(float(data[9]))
                voltage.append(float(data[10]))
            # print(data[0], data[10])
            i += 1

        ax2.plot(time, thrust, color="#FF0000")

        ax.plot(time, voltage, color="#00FF00")
        annotation_coords = (time[len(time) - 1] + .04*(len(labels) / 2)*(max(time)-min(time)),
                             thrust[len(thrust) - 1] - 0.02*(max(thrust)-min(thrust)))

        print(annotation_coords)
        ax2.annotate(label, xy=(300, 5), xycoords='data',
                    xytext=annotation_coords, textcoords='data',
                    horizontalalignment='right', verticalalignment='top',
                    )

    ax.set_title(title)
    ax.set_xlabel('Time (s)', color="#FFFFFF")
    ax.set_ylabel('Battery Voltage (V)', color="#00FF00")
    ax2.set_ylabel('Thrust (lbf)', color="#FF0000")

    size = 64.
    fig.set_size_inches(size * (1 / 9), size * (1 / 16))
    plt.show()


if __name__ == "__main__":
    plt.style.use("dark_background")
    plt.rcParams["font.family"] = "Consolas"

    # Parse Args
    plt_endurance(args[0], args[1], args[2])
