class Solution:
  def minTimeRequired(self,jobs: list[int],k:int)->int:
    jobs.sort(reverse=True)

    left=max(jobs)
    right=sum(jobs)

  def can_distribute(limit:int)->bool:
    workers=[0]*k

    def dfs(idx:int)->bool:
      if idx==len(jobs):
          return True

      curr_jobs=jobs[idx]
      for i in range(k):
        if workers[i]+curr_job<=limit:
          workers[i] += curr_job
          if dfs(idx+1):
            return True
          workers[i]-= curr_job

          if workers[i]==0:
            break
      return False
    return dfs(0)

  ans=right
  while left<=right:
    mid  =(left+right)>>1
    if can_distribute(mid):
      ans=mid
      right=mid-1
    else:
      left=mid+1
  return ans
  
