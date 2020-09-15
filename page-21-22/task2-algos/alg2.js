/* 
Пишу на джаваскрипте, ибо исходный на питоне,
Для нормальной работы нужен модуль readline, среда node.js
*/ 

const readline = require('readline')
    .createInterface({input: process.stdin, output: process.stdout});

const input = q => 
    new Promise( (resolve, reject) => readline.question(q||'', ans => resolve(ans) ) );

void async function main() {
    const a = await input();
    let k = 0, s = 1;
    while(k < a){
        k += 1;
        s += 1/k;
    }
    console.log(s);
}();
