function solution(keymap, targets) {
    var answer = [];
    let keys = new Map()
    //keymap을 통해 Map을 하나 만든다 
    keymap.map((val)=> 
        {for(let i = 0; i < val.length  ; i++){
            if (!keys.has(val[i])){
                keys.set(val[i],i+1)    
            }else {
                if(keys.get(val[i]) > i){
                    keys.set(val[i], i+1)   
                }
            }
        }
    })
    //key값 targets찾기
    targets.map((val)=>{
        let cnt = 0;
        for(let i = 0; val.length > i; i++){
            const getKeyCnt = keys.get(val[i])
            if (getKeyCnt){
                cnt += getKeyCnt
            } else {
                cnt = -1
                break
            }
        }
      
        answer.push(cnt)
    })
    return answer;
}