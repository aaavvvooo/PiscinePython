class calculator():
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product of two vectors"""
        prod = 0
        count = min(len(V1), len(V2))
        for i in range(count):
            prod += V1[i] * V2[i]
        print(f"Dot product is: {prod}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds two vectors"""
        ret = []
        count = min(len(V1), len(V2))
        for i in range(count):
            ret.append(float(V1[i] + V2[i]))
        print(f"Sum of vectors is: {ret}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts two vectors"""
        ret = []
        count = min(len(V1), len(V2))
        for i in range(count):
            ret.append(float(V1[i] - V2[i]))
        print(f"Difference of vectors is: {ret}")
