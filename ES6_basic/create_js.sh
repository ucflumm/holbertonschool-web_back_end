#!/bin/bash

for i in {1..12}
do
  touch "${i}-main.js"
  chmod u+x "${i}-main.js"
done

