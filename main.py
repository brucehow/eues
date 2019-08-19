from lib.process_data import process_csv

sample_data = "tests/cheetah_data.csv"

def main():
    cheetah = process_csv(sample_data)
    cheetah.plot_original_data()
    return

if __name__ == '__main__':
    main()