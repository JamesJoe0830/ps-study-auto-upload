// https://school.programmers.co.kr/learn/courses/30/lessons/178871
// 달리기 경주 : LEVEL 1
// [🎯 걸린 시간] : 1시간 (풀이 참조) 
// [⏰ 시간복잡도] : O(n)
// [자료구조] : Map(key-value)
// 
// [📚 풀이 방법]
// 0. key와 value를 가진 Map을 만든다.
// 1. 계속 업데이트를 하는 것은 원본 배열인 players와 만든 Map을 업데이트한다.
// 2. 현재 인덱스, 이전 사람을 기록하면서 calling의 배열만큼 순회한다.
// 
// 
// -------------------------------------------------------------
function solution(players, callings) {
    let newPlayersMap = {};
    
    for (let i = 0;  i<players.length;i++ ){
        newPlayersMap[players[i]] = i
    }
    
    for (let i = 0;  i<callings.length;i++ ){
        // 현재 인덱스 및 이전사람을 기록
        const currentIdx = newPlayersMap[callings[i]];
        const frontPlayers = players[currentIdx - 1] ;

        // players의 순서를 바꿔준다.
        players[currentIdx-1] = callings[i]
        players[currentIdx] =  frontPlayers
        
        //newPlayersMap도 업데이트
        newPlayersMap[callings[i]] -= 1
        newPlayersMap[frontPlayers] += 1
        
        
    }
    

    return players;
}
// -------------------------------------------------------------