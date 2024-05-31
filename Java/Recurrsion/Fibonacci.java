public class Fibonacci {

    // Recursive method to find the nth Fibonacci number
    public static int fibonacci(int n) {
        // Base cases: F(0) = 0, F(1) = 1
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        // Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    // Main method to test the fibonacci method
    public static void main(String[] args) {
        int n = 5; // You can change this value to test with other numbers
        int result = fibonacci(n);
        System.out.println("The " + n + "th Fibonacci number is: " + result);
    }
}
