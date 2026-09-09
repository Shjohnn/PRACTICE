// TASK E: 

// Shunday function tuzing, u bitta string argumentni 
// qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

function teskariString(str) {
    return str.split("").reverse().join("");
};

console.log(teskariString("hello")); // "olleh"