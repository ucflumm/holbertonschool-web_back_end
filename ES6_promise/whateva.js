/* I wish to capitalize the first letter of every sentence */
import { capitalizeThisLetter } from './0-main.js';

const newfunc = function capitalizeSentenceFirstLetter(sentence) {
  let parsedSentence = sentence.split('');
  let newSentence = [];
  for (let i in parsedSentence) {
    if (i == 0) {
      console.log("Capitalize first letter");
      newSentence.push(capitaliseThisLetter(parsedSentence[i]));
      // newSentence.push(parsedSentence[i].toUpperCase());
    } else {
      console.log("Do not capitalize");
      newSentence.push(parsedSentence[i]);
    }
  }
}