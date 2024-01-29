// BEGIN: Test cases for getListStudents function
import getListStudents from '/home/uwe/git/holbertonschool-web_back_end/ES6_data_manipulation/0-get_list_students.js';

// Test case 1: Check if the returned value is an array
const students = getListStudents();
console.log(Array.isArray(students)); // Expected output: true

// Test case 2: Check if the returned array has the correct length
console.log(students.length); // Expected output: 3

// Test case 3: Check if the returned array contains the expected objects
console.log(students[0]); // Expected output: { id: 1, firstName: 'Guillaume', location: 'San Francisco' }
console.log(students[1]); // Expected output: { id: 2, firstName: 'James', location: 'Columbia' }
console.log(students[2]); // Expected output: { id: 5, firstName: 'Serena', location: 'San Francisco' }
// END: Test cases for getListStudents function