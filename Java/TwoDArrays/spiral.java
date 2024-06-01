import java.util.*;
import java.util.Scanner;
public class spiral {

    public static void spiralPrint(int[][] mat){
        int startRow=0;
        int startCol=0;
        int endRow=mat.length-1;
        int endCol=mat[0].length-1;
        while(startRow<=endRow && startCol<=endCol){
            // top
            for(int i=startCol; i<=endCol; i++){
                System.out.print(mat[startRow][i] + " ");
            }
            // right
            for(int j=startRow+1; j<=endRow; j++){
                System.out.print(mat[j][endCol]+ " ");
            }
            // bottom
            
            for(int i=endCol-1; i>=startCol; i--){
                if(startRow==endRow){
                    break;
                }
                System.out.print(mat[endRow][i]+ " ");
            }
        // left
            for(int j=endRow-1; j>=startRow+1; j--){
                if(startCol==endCol){
                    break;
                }

                System.out.print(mat[j][startCol]+ " ");
            }
            
            startCol++;
            startRow++;
            endCol--;
            endRow--;
        }

        System.out.println();
    }


    public static int[][] matrixCreate(){
        System.out.println("Hello, Please enter the matrix data");
        int mat[][]= new int[3][4];
        int rows= mat.length;
        int column = mat[0].length;
        Scanner  sc= new Scanner(System.in);
        for(int i=0; i<rows; i++){
            for(int j=0; j<column; j++){
                mat[i][j]=sc.nextInt();
            }
        }
        return mat;

    }
    public static void matrixPrint(int mat[][]){
        int rows= mat.length;
        int column = mat[0].length;
        System.out.println("Here is your matrix");
        for(int i=0; i<rows; i++){
            for(int j=0; j<column; j++){
                System.out.print(mat[i][j] + " ");
            }
            System.out.println();
        }


    }
    public static void main(String args[]){
        int mat1[][]={
            {1,2,3,4},
            {5,6,7,8},
            {9,10,11,12}
        };
        //int mat[][]= matrixCreate();
        matrixPrint(mat1);
        spiralPrint(mat1);
                

    }
    
}
