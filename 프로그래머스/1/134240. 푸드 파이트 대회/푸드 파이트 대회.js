function solution(food) {
    var answer = '';
    let strFood = '';
    const len = food.length
    
    for (let i = 1; i < len; i++) {
        if (food[i]%2 ==0){
            // 짝수인 경우
            strFood += `${i}`.repeat(food[i]/2)
        } else {
            // 홀수인 경우
            if (food[i]-1 > 0){
                strFood += `${i}`.repeat((food[i]-1)/2)
            }
        }
    }
    answer += strFood + "0" + strFood.split('').reverse().join("")

    
    
    return answer;
}