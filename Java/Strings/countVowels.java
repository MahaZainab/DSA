import java.util.*;
public class countVowels {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter a string and then hit enter: ");
        String str= sc.nextLine();
        int count=0;
        for(int i=0; i<str.length();i++){
            if(str.charAt(i)=='a' || str.charAt(i)=='e' || str.charAt(i)=='i' || str.charAt(i)=='o' || str.charAt(i)=='u'  ){
                System.out.println(str.charAt(i));
                count++;
            }
        }
        System.out.println(count);


    }
    
}
