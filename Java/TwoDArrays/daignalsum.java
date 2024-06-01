public class daignalsum {
    public static int dSum(int mat[][]){
        int sum=0;
        for(int i=0; i<=mat.length-1; i++){
            sum+=mat[i][i];
            if(i != mat.length-1-i){
                sum+=mat[i][mat.length-1-i];
            }

        }
        return sum;
    }
    public static void main(String args[]){
        //int mat[][]= new int[4][4];
        int mat[][]={{12, 4, 5, 11},{34, 14, 55, 89},{7,8,7,9},{9,12,55,13}};
        int sum=dSum(mat);
        System.out.println(sum);
    }
    
}
