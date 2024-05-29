public class Factorial {

    // Recursive method to find factorial of n
    public static int factorial(int n) {
        // Base case: factorial of 0 is 1
        if (n == 0) {
            return 1;
        }
        // Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1);
    }

    // Main method to test the factorial method
    public static void main(String[] args) {
        int n = 5; // You can change this value to test with other numbers
        int result = factorial(n);
        System.out.println("Factorial of " + n + " is: " + result);
    }
}
