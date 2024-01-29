#!/bin/bash

for i in {2..9}
do
  touch "${i}-main.js"
  chmod u+x "${i}-main.js"
done

