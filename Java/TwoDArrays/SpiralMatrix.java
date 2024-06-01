public class SpiralMatrix {
    public static int[][] generateSpiralMatrix(int n) {
        int[][] spiralMatrix = new int[n][n];


        int value = 1; // Value to be filled in the cells

        int top = 0, bottom = n - 1, left = 0, right = n - 1;

        while (top <= bottom && left <= right) {
            // Move right
            for (int i = left; i <= right; i++) {
                spiralMatrix[top][i] = value++;
            }
            top++;

            // Move down
            for (int i = top; i <= bottom; i++) {
                spiralMatrix[i][right] = value++;
            }
            right--;

            // Move left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    spiralMatrix[bottom][i] = value++;
                }
                bottom--;
            }

            // Move up
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    spiralMatrix[i][left] = value++;
                }
                left++;
            }
        }

        return spiralMatrix;
    }

    public static void main(String[] args) {
        int n = 4; // Size of the matrix
        int[][] matrix = generateSpiralMatrix(n);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
