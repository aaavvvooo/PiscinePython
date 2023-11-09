from give_bmi import give_bmi, apply_limit


def main():
    try:
        height = [1.71, 1.65, 1.73, 1.95, 1.63]
        weight = [65.3, 58.4, 63.4, 94.5, 72.9]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as e:
        print("An error occurred while testing your code:", e)


if __name__ == "__main__":
    main()
