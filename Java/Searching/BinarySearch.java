public class BinarySearch {
    public static int binSearch(int arr[], int target){
        int start=0;
        int end= arr.length-1;

        while (start<=end) {
            int mid=(start+end)/2;
            System.out.println(mid);
            if(arr[mid]==target){
                return mid;
            }
            else if(arr[mid]<target){
                start=mid+1;
            }
            else{
                end=mid-1;                
            }
        }
        return -1;
        
    }
    public static void printArray(int arr[]){
        for (int i : arr) {
            System.out.println(i);       
        }
    }
    public static void main(String args[]){
        System.out.println("In Binary Search, always remember the array will be sorted");
        int arr[]={47,55,62,84,87,92,93,94,95};
        int idx=binSearch(arr, 84);
        System.out.println("you key is found at index: "+ idx);
    }
    
}
