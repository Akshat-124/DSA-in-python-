def merge(nums1,nums2):
    n=len(nums1)
    m=len(nums2)
    result=[]
    i=0
    j=0
    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
                i+=1
        else:
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
                j+=1
        while i<n :
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1  
        while j<n :
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1
        return result
nums1=[1,1,1,2,3,6,9]
nums2=[1,1,4,5,6,7,10]
print(merge(nums1,nums2))


 