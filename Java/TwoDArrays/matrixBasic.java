import java.util.Scanner;
import java.util.*;
public class matrixBasic {
    public static boolean search(int marks[][], int key){
        for(int i=0; i<marks.length; i++){
            for(int j=0; j< marks[0].length; j++){
                if(marks[i][j]==key){
                    System.out.println("Your value has been found in the matrix");
                    return true;
                }
            }
        }
        System.out.println("Marks wnot found");
        return false;

    }

    public static void main(String args[]){
        System.out.println("Hello, This tutorial contains all the basics of 2D Arrays");
        int marks[][]= new int[3][3];
        int rows=marks.length;
        // To store the length of the column
        int columns=marks[0].length;
        // To take input from user we need Scanner class object
        Scanner sc= new Scanner(System.in);
        // 2 loops will be used to take input from the user on each location
        
        for(int i=0; i< rows; i++){
            for(int j=0; j<columns; j++){
                marks[i][j]=sc.nextInt();
            }
        }

        // To print the matrix
        for(int i=0; i<rows; i++){
            for(int j=0; j<columns; j++){
                System.out.print(marks[i][j]+ " ");
            }
            System.out.println();
        }
        System.out.println("Enter the marks you want to search");
        int key= sc.nextInt();
        search(marks, key);



    }
    
}
