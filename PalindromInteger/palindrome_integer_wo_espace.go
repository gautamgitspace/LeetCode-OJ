package main
import (
  "fmt"
)

func main(){
  fmt.Println(checkPalindrome(121))
}

func checkPalindrome(x int) bool {
  if x < 0{
    return false
  }
  div := 1
  for (x / div >= 10){
			div *= 10
	}
  for (x != 0){
    left := x / div
    right := x % 10

    if (left != right){
      return false
    }
    x = (x % div) / 10
    div /= 100
	}
 return true
}
