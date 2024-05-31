public class eveodd {
    public static void calEvenOdd(int n){
        int bitMask=1;
        if((n & bitMask)==1){
            System.out.println("Number is Odd");
        } else{
            System.out.println("Number is even");
        }
    }
    public static void main(String[] args) {
        int n=13;
        calEvenOdd(n);
    }
    
}
