def ft_tqdm(lst: range) -> None:
    """Prints a progress bar in defined range"""
    total = len(lst)
    length = 100
    for i in enumerate(lst):
        percent = round(float(("{0:.1f}").format(100 * ((i[0] + 1) / float(total)))))
        filledLength = int(length * (i[0] + 1) // total)
        bar = '█' * filledLength + ' ' * (length - filledLength)
        print(f'{percent}%|{bar}| {i[0] + 1}/{len(list((lst)))}', end='\r')
        yield i
    print("\n")
