from give_bmi import give_bmi, apply_limit


def main():
    try:
        height = []
        weight = []

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as e:
        print("An error occurred while testing your code:", e)


if __name__ == "__main__":
    main()
