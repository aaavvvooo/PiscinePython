from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    """Main function"""
    for elem in ft_tqdm(range(333)):
        sleep(0.05)
    for elem in tqdm(range(333)):
        sleep(0.05)


if __name__ == "__main__":
    main()
