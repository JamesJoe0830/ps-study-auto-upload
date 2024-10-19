// https://school.programmers.co.kr/learn/courses/30/lessons/17682
// [1차] 다트 게임 : LEVEL 1
// [🎯 걸린 시간] : 40분 (풀이 참조 X) 
// [⏰ 시간복잡도] : O(n)
// [자료구조] : 큐(Queue)
// 
// [📚 풀이 방법]
// 앞에서 값을 뽑으면서 판단하기 위해 큐 자료구조를 사용함.
// 0. 10이라는 값이 있기 때문에 연속해서 뽑는 경우를 생각해야한다.
// 1. 제곱의 값은 결국 숫자 바로 다음에 온다. 0번에서 판별한 덕분에 nextValue는 무조건 제곱값이다.
// 2. 제곱값 까지 뽑았다면, 옵션을 판별한다. 옵션이 아니면 다시 넣어준다.
// ----------------------------------------------------------------------------------------

function solution(dartResult) {
    dartSquare = ["S","D","T"]
    var answer = 0;
    dartArray=Array.from(dartResult)
    let prevScore = 0 // 이전값 -> 옵션 *일 경우 때문에 이전값을 저장한다.
    while (dartArray.length > 0){
        let addScore = 0 //현재 제곱을 더해줄 number타입 Score
        let score = ""; // 10인지를 판단하기 위해 string을 더해줄 녀석
        let dartValue = dartArray.shift()
        
        // [10인경우 판단]
        // 숫자는 더하고 아니면 다시 앞으로 넣는다.        
        if(!isNaN(dartValue)){
            let tenValue = dartArray.shift()
            score += dartValue
            // 뽑았더니 숫자야
            if(!isNaN(tenValue)){
                score += tenValue
            } else {
                dartArray.unshift(tenValue)
            }
        }
        
        // [제곱과 옵션을 판단하는 로직]
        // nextDartValue : 무조건 square 값이온다.         
        let nextDartValue = dartArray && dartArray.shift()
        if (dartSquare.includes(nextDartValue)) {
              let squareValue = dartSquare.indexOf(nextDartValue) + 1
              addScore += Number(score) ** squareValue
              // option는 square값("S","D","T")바로 다음에 온다.
              // optionsValue가 아니면 다시 넣어주면된다.             
              let optionsValue = dartArray && dartArray.shift()
              if (optionsValue === "*"){
                  answer -= prevScore
                  addScore *= 2
                  prevScore *=2
                  answer = answer + prevScore +addScore
              } else if(optionsValue === "#"){
                  addScore *= -1
                  answer += addScore
              } else {
                  answer += addScore
                  dartArray.unshift(optionsValue)
              }
             
        }
        prevScore = addScore
    }
    return answer;
}

// ----------------------------------------------------------------------------------------