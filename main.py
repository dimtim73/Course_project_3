from utils import get_data
from utils import get_filtered_data
from utils import get_sorted_data
from utils import get_formatted_data


def main():
    print("Курсовая работа №3")

    data = get_data()

    filtered_data = get_filtered_data(data)

    sorted_data = get_sorted_data(filtered_data)

    get_formatted_data(sorted_data)


main()

