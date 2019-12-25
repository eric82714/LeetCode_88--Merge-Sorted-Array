void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int last = m + n - 1;     
    n--;
    m--;
        
    while(n >= 0 && m >= 0)
    {
        if(nums1[m] > nums2[n])
        {
            nums1[last] = nums1[m];
            m--;
        }
        else
        {
            nums1[last] = nums2[n];
            n--;
        }
        last--;
    }
        
    while(n >= 0)
    {
        nums1[last] = nums2[n];
        n--;
        last--;
    }
}
