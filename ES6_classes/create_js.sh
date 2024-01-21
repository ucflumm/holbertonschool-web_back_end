#!/bin/bash

for i in {0..10}
do
  touch "${i}-main.js"
  chmod u+x "${i}-main.js"
done

