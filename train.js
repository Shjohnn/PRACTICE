//TASK F
// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!


function findDoublers(str) {
  let letters = [];

  for (let i = 0; i < str.length; i++) {
    if (letters.includes(str[i])) {
      return true;
    }

    letters.push(str[i]);
  }

  return false;
}

console.log(findDoublers("hello")); // true













// TASK E: 

// Shunday function tuzing, u bitta string argumentni 
// qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

// function teskariString(str) {
//     return str.split("").reverse().join("");
// };

// console.log(teskariString("hello")); // "olleh"