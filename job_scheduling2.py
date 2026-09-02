def maxProfit(startTime: list[int],endTime: list[int],profit:list[int])->int:
  jobs=sorted(zip(startTime,endTime,profit), key = lambda x:x[1])
  end_times = [j[1] for j in jobs]
  n = len(jobs)

  dp=[0]*(n+1)

  for i in range(1,n+1):
    start,end,p = jobs[i-1]

    idx =bisect.bisect_right(end_times,start)
    dp[i] = max(dp[i-1],p+dp[idx])
  return dp[n]
