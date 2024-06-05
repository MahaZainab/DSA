public class GridWays{

    // Function to count the number of ways using backtracking
    public static int countWays(int m, int n) {
        return countWaysUtil(0, 0, m, n);
    }

    // Utility function to perform backtracking
    private static int countWaysUtil(int i, int j, int m, int n) {
        // If the current position is the bottom-right corner, return 1 way
        if (i == m - 1 && j == n - 1) {
            return 1;
        }

        // If the current position is out of bounds, return 0 ways
        if (i >= m || j >= n) {
            return 0;
        }

        // Move right and down and sum the number of ways
        int moveRight = countWaysUtil(i, j + 1, m, n);
        int moveDown = countWaysUtil(i + 1, j, m, n);

        // Return the total number of ways from the current position
        return moveRight + moveDown;
    }

    public static void main(String[] args) {
        int m = 3, n = 3; // Example for a 3x3 grid
        System.out.println("Number of ways to reach the bottom-right corner: " + countWays(m, n));
    }
}
