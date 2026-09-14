

// TASK G:

// Yagona parametrga ega function tuzing.
// Va bu function parametr orqalik integer ma'lumot turlariga ega bo'lgan bir arrayni qabul qilsin.
// Ushbu function bizga arrayning tarkibidagi birinchi eng katta qiymatning indeksini qaytarsin.

// MASALAN: getHighestIndex([5, 21, 12, 21 ,8]); return qiladi 1 sonini
// Yuqoridagi misolda, birinchi indeksda 21 joylashgan.
// Va bu 21 soni arrayning tarkibidagi birinchi eng katta son hisobladi va bizga uning indeksi 1 qaytadi.



function getHighestIndex(arr) {
  let katta = arr[0];
  let kattaIndex = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > katta) {
      katta = arr[i];
      kattaIndex = i;
    }
  }

  return kattaIndex;
}

console.log(getHighestIndex([5, 1, 12, 21, 8])); // 3


















//TASK F
// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!






// function findDoublers(str) {
//   let letters = [];

//   for (let i = 0; i < str.length; i++) {
//     if (letters.includes(str[i])) {
//       return true;
//     }
//     str=str.toLowerCase();
//     letters.push(str[i]);
//   }

//   return false;
// }

// console.log(findDoublers("heLaAlo")); // true













// TASK E: 

// Shunday function tuzing, u bitta string argumentni 
// qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

// function teskariString(str) {
//     return str.split("").reverse().join("");
// };

// console.log(teskariString("hello")); // "olleh"