public class RotatedSortedArr {
    public static int search(int arr[], int target, int si, int ei){
        if(si>ei){
            return -1;
        }
        //Calculated mid
        int mid=si+(ei-si)/2;
        // If target found
        if(arr[mid]==target){
            return mid;
        }
        if(arr[si]<= target && target<=arr[mid]){
            return search(arr, target, si, mid-1);
        }
        else{
            return search(arr, target, mid+1, ei);
        }

        /* 
        if(arr[si]<=arr[mid]){
            if(arr[si]<= target && target<=arr[mid]){
                return search(arr, target, si, mid-1);
            }
            else{
                return search(arr, target, mid+1, ei);
            }
            
        }
        else{
            if(arr[mid]<=target && target<=arr[ei]){
                return search(arr, target, mid+1, ei);
            }
            else{
                return search(arr, target, si, mid-1);
            }
        }
        */



    }
    public static void main(String[] args) {
        System.out.println("Hello");
        int arr[]={4,5,6,7,0,1,2};
        int idx=search(arr, 5, 0, arr.length-1);
        System.err.println(idx);
    }
    
}
