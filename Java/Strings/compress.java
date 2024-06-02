public class compress {
    public static String compressString1(String str){
        StringBuilder newStr=new StringBuilder();
        for(int i=0; i<str.length();i++){
            Integer count=1;
            while(i<str.length()-1 && str.charAt(i)== str.charAt(i+1)){
                count++;
                i++;
            }
            newStr.append(str.charAt(i));
            if(count>1){
                newStr.append(count.toString());
            }
        }
        return newStr.toString();
    }

    public static String compressString(String str){
        String newStr="";
        for(int i=0; i<str.length();i++){
            Integer count=1;
            while(i<str.length()-1 && str.charAt(i)== str.charAt(i+1)){
                count++;
                i++;
            }
            newStr+=str.charAt(i);
            if(count>1){
                newStr+=count.toString();
            }
        }
        return newStr;
    }
    public static void main(String[] args) {
        String str="aaabbcddddd";
        String str2= compressString1(str);
        System.out.println(str2);
    }
    
}
