import numpy as np

def dot_product_manual(A, B):
    result = 0
    for A_i, B_i in zip(A, B):
        result += A_i * B_i
    return result

def dot_product_np(A, B):
    return np.dot(A, B)

def euclidean_norm_manual(A):
    sum_of_squares = 0
    for element in A:
        sum_of_squares += element ** 2
    return sum_of_squares ** 0.5

def euclidean_norm_np(A):
    return np.linalg.norm(A)

def main():
    n = int(input("Enter number of dimensions: "))

    print("Enter elements of vector A :")
    A = list(map(float, input().split()))

    print("Enter elements of vector B :")
    B = list(map(float, input().split()))

    if len(A) != n or len(B) != n:
        print("Error: Number of elements must match the given dimension.")
        return

    manual_dot = dot_product_manual(A, B)
    numpy_dot = dot_product_np(A, B)

    print("\nResults of Dot Product:")
    print("Dot product manually :", manual_dot)
    print("Dot product using NumPy:", numpy_dot)

    manual_norm = euclidean_norm_manual(A)
    numpy_norm = euclidean_norm_np(A)

    print("\nResults of Euclidean Norm (Vector A):")
    print("Euclidean norm manually :", manual_norm)
    print("Euclidean norm using NumPy:", numpy_norm)

if __name__ == "__main__":
    main()
