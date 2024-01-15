#!/bin/bash

for i in {0..2}
do
  echo "#!/usr/bin/env python3" > "${i}-main.py"
  chmod u+x "${i}-main.py"
done

