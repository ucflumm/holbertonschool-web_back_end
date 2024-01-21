#!/bin/bash

for i in {0..10}
do
  touch "${i}-main.js"
  chmod u+x "${i}-main.js"
done

touch "0-classroom.js"
touch "1-make_classrooms.js"
touch "2-hbtn_course.js"
touch "3-currency.js"
touch "4-pricing.js"
touch "5-building.js"
touch "6-sky_high.js"
touch "7-airport.js"
touch "8-hbtn_field.js"
touch "9-hoisting.js"
touch "10-car.js"

ls -la