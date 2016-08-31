var number = process.argv[2];


var fizzbuzz = function (num){
    str = ""
    if(num % 3 === 0){
        str += "Fizz";
    };
    if (num % 5 === 0){
        str += "Buzz";
    };
    if (!str){
        str = num;
    }
    return str;
};
console.log(fizzbuzz(number));

