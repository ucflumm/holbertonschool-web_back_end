#!/bin/bash

for i in {8..12}
do
  echo "#!/usr/bin/env python3" > "${i}-main.py"
  chmod u+x "${i}-main.py"
done

