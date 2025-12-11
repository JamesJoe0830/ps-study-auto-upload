function solution(array, commands) {
    var answer = [];
    const len = commands.length;
    //commands의 length만큼 반복한다. 
    for (let n = 0; n < len ; n++){
        let i = commands[n][0]-1
        let j = commands[n][1]-1
        let k = commands[n][2]-1
        let targetNumber = array.slice(i,j+1).sort((a,b)=>a-b)[k]
        answer.push(targetNumber)
    }
    return answer;
}