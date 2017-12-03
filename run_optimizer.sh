#!/usr/bin/env bash

# default parameters

MAX_BATCH_SIZE=1
ALGORITHM="single_match"
NUM_BITMAPS=10
NUM_LEAFS_PER_BITMAP=3
REDUNDANCY_PER_BITMAP=2
NUM_RULES_PER_LEAF=1000
PROBABILITY_DIVIDEND=2
PROBABILITY_DIVISOR=3
DATA_FILE_PREFIX="/mnt/sdb1/baseerat/numerical-evals/12-2-2017/output-1M-random/cloud.*"
DUMP_FILE_PREFIX="/mnt/sdb1/baseerat/numerical-evals/12-2-2017/output-1M-random/optimizer"

PYTHON=pypy3  # options: pypy3 or python or python3

# running parameters

for file in ${DATA_FILE_PREFIX}
do
    for num_rules_per_leaf in 10000
    do
        for num_bitmaps in 30
        do
            for num_leafs_per_bitmap in 4
            do
                ${PYTHON} run_optimizer.py  ${MAX_BATCH_SIZE} \
                                            "exact-match" \
                                            ${num_bitmaps} \
                                            ${num_leafs_per_bitmap} \
                                            0 \
                                            ${num_rules_per_leaf} \
                                            ${PROBABILITY_DIVIDEND} \
                                            ${PROBABILITY_DIVISOR} \
                                            ${file} \
                                            ${DUMP_FILE_PREFIX} &

                for redundancy_per_bitmap in 0 6
                do
                    ${PYTHON} run_optimizer.py  ${MAX_BATCH_SIZE} \
                                                "random-fuzzy-match" \
                                                ${num_bitmaps} \
                                                ${num_leafs_per_bitmap} \
                                                ${redundancy_per_bitmap} \
                                                ${num_rules_per_leaf} \
                                                ${PROBABILITY_DIVIDEND} \
                                                ${PROBABILITY_DIVISOR} \
                                                ${file} \
                                                ${DUMP_FILE_PREFIX} &
                done
                wait
            done
        done
    done
done
wait
