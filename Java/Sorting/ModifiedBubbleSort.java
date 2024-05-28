public class ModifiedBubbleSort {
    public static void printArray(int arr[]){
        for (int i : arr) {
            System.out.println(i);
            
        }

    }
    public static void MBSort(int arr[]){
        for(int i=0; i<arr.length-1; i++){
            Boolean swap= false;
            for(int j=0; j<arr.length-1-i; j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                    swap=true;
                }
            }
            if(swap==false){
                break;
            }


        }

    }
    public static void main(String args[]){
        System.out.println("This code has been written to give better time complexity in average cases while implementing bubble sort ");
        int arr[]={4,7,11,3,4,12};
        MBSort(arr);
        printArray(arr);
    }
    
}
