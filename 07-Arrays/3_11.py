def bubble_sort(arr):
   n = len(arr)
   a = 0

   for i in range(n):
      for j in range(n-i-1):
         if  arr[j] > arr[j+1]:
             a = arr[j]
             arr[j] = arr[j+1]
             arr[j+1] = a
            

   return arr