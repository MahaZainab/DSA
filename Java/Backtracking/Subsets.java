public class Subsets{
    public static void findSubsets(String str, String ans, int i){

        //base case
        if(i== str.length()){
            System.out.println(ans);
            return;
        }
        // yes choice
        findSubsets(str, ans+str.charAt(i), i+1);
        // no choice
        findSubsets(str, ans, i+1);
    }

    public static void main(String[] args) {
        System.out.println("This program will print all the subsets of a string");
        String str = "abc";
        findSubsets(str, "", 0);
    }
}