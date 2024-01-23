function solution(seq) {
    var bad=0
    for(var i=1;i<seq.length;i++) {
      if(seq[i]<=seq[i-1]) {
        bad++
        if(bad>1) {
          console.log("bad is > 1 so i return false")
          console.log("false")
          return false
        }
        if(seq[i]<=seq[i-2]&&seq[i+1]<=seq[i-1]) {
         
          console.log("false")
          return false
      }
      }  
      }
      console.log("i dont execute nested if")
    console.log("True")
    return true
  }
  arr = [3]
  solution(arr)
