public class SumOfNaturalNumbers {

    // Recursive method to find sum of first n natural numbers
    public static int sumOfNaturalNumbers(int n) {
        // Base case: sum of first 0 natural numbers is 0
        if (n == 0) {
            return 0;
        }
        // Recursive case: n + sum of (n-1) natural numbers
        return n + sumOfNaturalNumbers(n - 1);
    }

    // Main method to test the sumOfNaturalNumbers method
    public static void main(String[] args) {
        int n = 5; // You can change this value to test with other numbers
        int result = sumOfNaturalNumbers(n);
        System.out.println("Sum of first " + n + " natural numbers is: " + result);
    }
}
