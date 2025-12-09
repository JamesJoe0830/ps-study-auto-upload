function solution(s) {
    const numbers = new Map([
        ['zero', 0],
        ['one', 1],
        ['two', 2],
        ['three', 3],
        ['four', 4],
        ['five', 5],
        ['six', 6],
        ['seven', 7],
        ['eight', 8],
        ['nine', 9],
    ]);

    let answer = '';
    let strNumber = '';

    for (const char of s) {
        // 숫자인 경우 (0~9)
        if (!isNaN(char)) {
            answer += char;
            continue;
        }
        // 문자일 때 → 누적
        strNumber += char;
        // 완성된 단어인지 확인
        if (numbers.has(strNumber)) {
            answer += numbers.get(strNumber);
            strNumber = '';
        }
    }

    return Number(answer);
}