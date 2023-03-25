#!/bin/bash

for i in {1..70}
do
cat permutation_test/$i/* > permutation_test/$i.csv
done
