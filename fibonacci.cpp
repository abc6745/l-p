#include <iostream>
using namespace std;

int fib_recursive(int n) {
    if (n <= 1)
        return n;
    return fib_recursive(n - 1) + fib_recursive(n - 2);
}

void fib_nonrecursive(int n) {
    int a = 0, b = 1, c;
    cout << a << " " << b << " ";
    for (int i = 2; i < n; i++) {
        c = a + b;
        cout << c << " ";
        a = b;
        b = c;
    }
}

int main() {
    int n;
    cout << "Enter number of terms: ";
    cin >> n;

    cout << "\nFibonacci Series (Recursive): ";
    for (int i = 0; i < n; i++){
        cout << fib_recursive(i) << " ";}

    cout << "\nFibonacci Series (Non-Recursive): ";
    fib_nonrecursive(n);

    return 0;
}
