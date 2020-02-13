from Hopfield_Network import *
import numpy as np
import seaborn as sns

PERCENTAGES = np.linspace(start=0, stop=1, num=11)
ITERATIONS = 100
PATTERNS = True
ITERATIVE_WEIGHT = True


def random_patterns(size, columns=1):
    return np.array(np.random.choice([-1, 1], size=size * columns)).reshape(-1, size)


def iterative_patterns(w_mat):
    uniques = {}
    for i in range(w_mat.shape[0]):
        aux = ""
        for j in range(len(w_mat[i, :])):
            if j != len(w_mat[i, :]) - 1:
                aux += str(w_mat[i, j]) + " "
            else:
                aux += str(w_mat[i, j])
        if aux not in uniques:
            uniques[aux] = 0

    return w_mat.shape[0] - len(uniques)


def main():
    # Load data
    data = np.loadtxt('pict.dat', delimiter=",", dtype=int).reshape(-1, 1024)
    patterns = random_patterns(100, 300)

    if PATTERNS:
        if ITERATIVE_WEIGHT:
            uniques = list()
            for i in range(300):
                w = weights(patterns[:i+1, :].reshape(i+1, 100))
                uniques.append(iterative_patterns(w))
        else:
            w = weights(patterns)
        image = 0
        counter = np.zeros(len(PERCENTAGES))
        counter = noised_images(PERCENTAGES, patterns, image, counter, w, noised_iterations=100)
        plt.figure()
        # sns.set_style('darkgrid')
        counter_plot = sns.lineplot(x=PERCENTAGES, y=counter)
        counter_plot.set(xlabel='Noise level', ylabel='Accuracy')
        plt.show()
        input("Press enter to continue...")

    else:
        for pat in range(4, 8):
            print("Running network for image", pat)
            w = weights(data[:pat, :])
            image = 0
            counter = np.zeros(len(PERCENTAGES))
            counter = noised_images(PERCENTAGES, data, image, counter, w)
            plt.figure()
            # sns.set_style('darkgrid')
            counter_plot = sns.lineplot(x=PERCENTAGES, y=counter)
            counter_plot.set(xlabel='Noise level', ylabel='Accuracy')
            plt.show()
            input("Press enter to continue...")


if __name__ == "__main__":
    main()