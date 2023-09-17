from src.utils.dataset import open_dataset
from src.evolution_strategy.individual import generate_individual


def main():
    dataset = open_dataset()
    vpl = 0
    i = 0
    while i < 10:
        individual = generate_individual(dataset)
        print(individual['vpl'].values[0])
        i += 1


if __name__ == '__main__':
    main()

